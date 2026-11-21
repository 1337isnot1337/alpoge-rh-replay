"""Check and measure shared lemmas against source-hashed declarations from the archive."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from scan import DECL, ROOT, indexed_sources, declarations, alpha_header, statement_header, statement_prefix
import hashlib

HERE = Path(__file__).resolve().parent
LEAN_COMMIT = '819816b2e0a3bf405af45ae5c7af2491d8f5bee6'
LIBRARIES = {
    'ReplayTopology': (
        'continuous_unitsHom',
        'totallyDisconnected_quotient',
        'continuous_charpoly_coeff',
    ),
    'ReplayAlgebra': (
        'specMap_ofHom_comp',
        'cardQuot_under_eq_pow_inertiaDeg',
        'not_isTotallyReal_and_isTotallyComplex',
        'padicAlgCl_isIntegral_iff_norm_le_one',
        'isLocalHom_of_isIntegral',
    ),
}
# For each new shared lemma, inference fills the parameters appearing in
# the conclusion; the other arguments come from the source hypotheses.
STRUCTURAL_LIBRARIES = {
    'ReplayAnalysis': {
        'polish_of_lcsc': ' _',
        'norm_le_one_of_isIntegral': ' (by assumption)',
        'poly_mul_gaussian_bounded': '',
    },
    'ReplayCommutativeAlgebra': {
        'exists_nat_mul_isIntegral': ' _',
        'span_insert_image_erase_eq_top': ' _ _ (by assumption)',
        'isLocalRing_quotient_span_singleton': ' (by assumption)',
        'maximalIdeal_eq_bot_of_le_sq': ' _ (by assumption)',
        'exists_mem_maximalIdeal_notMem_sq_notMem_minimalPrimes': ' _ (by assumption) (by assumption)',
        'exists_repr_ne_zero': ' _ (by assumption)',
        'spanFinrank_maximalIdeal_quotient_succ_le': ' _ (by assumption) (by assumption)',
    },
}
WRAPPER_TASKS = {'M144183', 'M172691'}
# The cotangent-space calculation and prime avoidance use earlier proofs
# from the same file. Compile those exact siblings in separate namespaces.
COTANGENT_HELPERS = {'spanFinrank_span_finset_le', 'exists_repr_ne_zero', 'span_insert_image_erase_eq_top'}
SIBLINGS = {
    'M156476': COTANGENT_HELPERS | {'isPrime_of_mem_minimalPrimes'},
    'M171687': COTANGENT_HELPERS | {'isPrime_of_mem_minimalPrimes'},
    'M171690': COTANGENT_HELPERS | {'isPrime_of_mem_minimalPrimes'},
    'M136424': {'isPrime_of_mem_minimalPrimes'},
    'M087333': {'norm_finset_sum_lt_of_forall_lt'},
}

# Each entry identifies the exact text (statement and proof), the shared lemma group,
# the replacement proof term, whether the consumer statement mentions an archive abbreviation
# (`spMap` or `normV`), and the source modules found by scan.py --match.
CASES = {
    '34271c25953e82f6977370f84a264df5bc8ad183a5f95a8e230f21bc4be9f670': (
        'specMap_ofHom_comp', 'ReplayAlgebra.specMap_ofHom_comp f g', True,
        'M002912 M012786 M013117 M014298 M024847 M025845 M029787 M032194 M037630 M040488 '
        'M046038 M050016 M050017 M052056 M052533 M052563 M052565 M054760 M069696 M075703 '
        'M077426 M077638 M082053 M084760 M085259 M085303 M085610 M085741 M091233 M110308 '
        'M110319 M130333 M140422'),
    'fd75d6b9f2b9fc3699439fa3b3ea292f90f8885409ca497911de151ebb610149': (
        'specMap_ofHom_comp', '(ReplayAlgebra.specMap_ofHom_comp f g).symm', True,
        'M003372 M006593 M006945 M013265 M013611 M015851 M015855 M015969 M017847 M028894 '
        'M040341 M047824 M052573 M053220 M054185 M082736 M099865 M110231 M130257 M130301 '
        'M131923'),
    'eda0620c639c59e3f6e40925c97726c03a73c86684782e725f94ac5ac40264db': (
        'specMap_ofHom_comp', '(ReplayAlgebra.specMap_ofHom_comp f g).symm', True,
        'M017805 M025167 M028730 M029749 M077946 M081605 M100087 M110080 M110086 M110121 '
        'M173382'),
    '29905a26a348ec0d7c5c03d9db696235bf12097f17db7dd9edcbbda543795a2d': (
        'specMap_ofHom_comp', 'ReplayAlgebra.specMap_ofHom_comp f g', True,
        'M003622 M033540 M033569 M039944 M044540 M052029 M078943 M099657 M132269 M150382'),
    'd393a9b9374acc508ece03d7fee06b9bd2356c732fed8e72eda34761128230d2': (
        'specMap_ofHom_comp', 'ReplayAlgebra.specMap_ofHom_comp g f', True,
        'M006583 M006779 M007140 M007333 M051963 M060797 M064360 M083656 M099536'),
    'a11d5d73353c0057599dcc0479a75be33f17535b6bbe102a0e5c60562ca6cbc0': (
        'cardQuot_under_eq_pow_inertiaDeg', 'ReplayAlgebra.cardQuot_under_eq_pow_inertiaDeg K w', True,
        'M062774 M101975 M102029 M102068 M102069 M102265 M102273 M102379 M103380 M103381 '
        'M103391 M103403 M103420 M104178 M104974 M105067 M105069 M105081 M106614 M106661 '
        'M106684 M106824 M106995 M107068 M111777 M171275 M171321'),
    'b22f16de291d4844b697b2d4d3658ff78484851da81860c87effa4c28ff8a877': (
        'continuous_unitsHom', 'ReplayTopology.continuous_unitsHom f h', False,
        'M061176 M102348 M103013 M104155 M104175 M104194 M104195 M104350 M104351 M104984 '
        'M105041 M105077 M105078 M105715 M105987 M106690 M106694 M108432 M171108'),
    '3a85de910ca7ee70763c329e104f0e728010b921be90cf8d76a4e2541280444a': (
        'not_isTotallyReal_and_isTotallyComplex',
        "ReplayAlgebra.not_isTotallyReal_and_isTotallyComplex h h'", False,
        'M101968 M103446 M105061 M105067 M105075 M106651 M106661 M110968 M111468 M111473 '
        'M111587 M113132 M137230 M170999 M171003'),
    '6908455f17486d5184e88449ae58304e52d0bf55948f9ee9989a1bbf7e3a8f6a': (
        'totallyDisconnected_quotient', 'ReplayTopology.totallyDisconnected_quotient N hN', False,
        'M103041 M105902 M105903 M105904 M106665 M106666 M106667 M106913 M107059 '
        'M108306 M108608 M108635 M108656 M109071'),
    'dcfcbb1cc29edfb0b14f225589fa578d39fa77a23fa928dfafc0e6ae356f520c': (
        'continuous_charpoly_coeff', 'ReplayTopology.continuous_charpoly_coeff i', False,
        'M018532 M018573 M071680 M087066 M094014 M101722 M101992 M103922 M104974 M105067 '
        'M106661 M106954 M141687 M171293'),
    '69cf43c3647f8beb153fe01e3cfe355b6bfea9baed22ab22fa8e0dffc74ce72c': (
        'padicAlgCl_isIntegral_iff_norm_le_one',
        'ReplayAlgebra.padicAlgCl_isIntegral_iff_norm_le_one x', False,
        'M101497 M103902 M103989 M104010 M106930 M107631 M107632 M108269 M108336 M108691 '
        'M108890 M109256'),
    'bbf7ecd88deb2e088d7d122bc93d909378befff9ce5a554dc7b5e733ab8315bf': (
        'isLocalHom_of_isIntegral', 'ReplayAlgebra.isLocalHom_of_isIntegral f', False,
        'M103047 M105900 M105905 M105982 M105989 M106573 M106668 M108438 M108453'),
}


# Alpha-mode header hash -> shared lemma and independently source-hashed module IDs.
# Different original scripts under a shared header are elaborated separately.
STRUCTURAL_CASES = {
    '02d415b1b8debf2c8a5a3fea8ef694d8bbb065c627b71100dbebce6bbaea98bd': (
        'ReplayCommutativeAlgebra.exists_mem_maximalIdeal_notMem_sq_notMem_minimalPrimes',
        'M136424 M156476 M171687 M171690'),
    '4535c173a159a5857a71822353aec5d3bc9430aa09a8e6dee6ce341ee12a13f1': (
        'ReplayCommutativeAlgebra.exists_nat_mul_isIntegral',
        'M027663'),
    '460d927bee576408ba560afe13d45358fc36cb25a37b6762f96c67efbd3bbb08': (
        'ReplayCommutativeAlgebra.exists_nat_mul_isIntegral',
        'M005501 M020865 M066009 M078091 M170829 M170870'),
    '9580b5ab017ece565133ca6c28faf911e27917e60f11694abdeef37fa7a153f0': (
        'ReplayCommutativeAlgebra.exists_nat_mul_isIntegral',
        'M005660 M033194 M064547 M088039'),
    'd04db0041130596941db243067f90badeaae79099c02dc1daa2bab2ea726006b': (
        'ReplayCommutativeAlgebra.exists_nat_mul_isIntegral',
        'M154557'),
    '3527a03acab575afc97f9a1c4f8f0449a8ed4333a800d21a4f33ace4b2c0037b': (
        'ReplayCommutativeAlgebra.exists_repr_ne_zero',
        'M136424 M156476 M171687 M171690'),
    '92844b50e834267c01e0a260068f449d90f900ac0f83e199d5462554d0f3e342': (
        'ReplayCommutativeAlgebra.isLocalRing_quotient_span_singleton',
        'M136424 M156476 M171687 M171690'),
    'fc8b0ce19200e1ccfd134c578b3ea8a1b89bd3c6847cc0a3d2219d7eeac27a6a': (
        'ReplayCommutativeAlgebra.maximalIdeal_eq_bot_of_le_sq',
        'M136424 M156476 M171687 M171690'),
    '4868cfc186709455ec79ea9ee7980fce7a92a09c46724df5abb61e9087706392': (
        'ReplayAnalysis.norm_le_one_of_isIntegral',
        'M086544 M087517 M088415 M088889 M120564 M140237'),
    '5be3539a02ef7c28ea31e5e97ee2be8456b05629ebc6da988dba172c4c19f873': (
        'ReplayAnalysis.norm_le_one_of_isIntegral',
        'M036261 M040345 M041696 M046355 M060240 M061253 M064135 M074060 M080622 '
        'M087349 M087532 M087818 M088895 M103317 M120061 M148413 M148663'),
    'd19a26562542734531a134d143644e120b6e05e4391462dc2282d72ba2255cd7': (
        'ReplayAnalysis.norm_le_one_of_isIntegral',
        'M023564 M044544 M055535 M061289 M083736 M087333 M149709'),
    '5b58389799cc78ac4c27a04211e833e1113acd180d76df2cfb41405a1cfd5ac5': (
        'ReplayAnalysis.polish_of_lcsc',
        'M154353 M156866 M157029 M157505 M157679'),
    '81fed670a1119ca1de770a14420ef1410afc4c927c5c0204679d4a28bdbe1da1': (
        'ReplayAnalysis.poly_mul_gaussian_bounded',
        'M046154 M115171 M115172'),
    'd482f2424df64ca2725edf1a298e5875d6ba8c76bfa0f44d931ea8c2f66b0a72': (
        'ReplayCommutativeAlgebra.span_insert_image_erase_eq_top',
        'M136424 M156476 M171687 M171690'),
    '458da6534cd8327ff26601d50301452cae6fde069a4cbd80ce8ae0daba7f093b': (
        'ReplayCommutativeAlgebra.spanFinrank_maximalIdeal_quotient_succ_le',
        'M156476 M171687 M171690'),
}


def source_cases(project):
    expected = {(task, key) for key, (_, _, _, tasks) in CASES.items() for task in tasks.split()}
    structural = {(task, key): lemma for key, (lemma, tasks) in STRUCTURAL_CASES.items()
                  for task in tasks.split()}
    cases = []
    seen_names = Counter()
    for row, data in indexed_sources(project, {task for task, _ in expected | structural.keys()}):
        for key, match, block in declarations(data):
            ident = (row['id'], key.hex())
            if ident in expected:
                expected.remove(ident)
                lemma, term, batch, _ = CASES[ident[1]]
                batch = 'Wrapped' if batch else 'Pure'
            else:
                header = statement_header(block)
                if header is None:
                    continue
                key = hashlib.sha256(alpha_header(header).encode()).hexdigest()
                full = structural.pop((row['id'], key), None)
                if full is None:
                    continue
                library, lemma = full.split('.')
                term = full + STRUCTURAL_LIBRARIES[library][lemma]
                batch = 'Structural'
            base_name = f"{ident[0]}.{match[1].decode()}"
            seen_names[base_name] += 1
            decl_name = base_name if seen_names[base_name] == 1 else f"{base_name}_{seen_names[base_name]}"
            cases.append((lemma, term, batch, decl_name, block.decode('utf-8')))
    if expected or structural:
        raise ValueError(f'Missing pinned declarations: {sorted(expected | structural.keys())}')
    return sorted(cases)


def compiler_environment(project, work):
    summary = json.loads((ROOT / 'tracker/summary.json').read_text(encoding='utf-8'))
    toolchain = (project / 'lean-toolchain').read_text(encoding='utf-8').strip()
    version = subprocess.check_output(['lean', '--version'], text=True).strip()
    if (toolchain != 'leanprover/lean4:v' + summary['lean'] or LEAN_COMMIT not in version
            or f"version {summary['lean']}," not in version):
        raise ValueError(f'Unexpected compiler: {version} ({toolchain})')
    manifest = json.loads((project / 'lake-manifest.json').read_text(encoding='utf-8'))
    packages = project / manifest['packagesDir']
    pins = [p['rev'] for p in manifest['packages'] if p['name'] == 'mathlib']
    actual = subprocess.check_output(['git', '-C', packages / 'mathlib', 'rev-parse', 'HEAD'],
                                     text=True).strip()
    if pins != [actual] or actual != summary['mathlib_commit']:
        raise ValueError(f'Unexpected Mathlib revision: {actual}')
    libraries = [packages / p['name'] / '.lake/build/lib/lean' for p in manifest['packages']]
    return version, actual, {**os.environ, 'LEAN_PATH': os.pathsep.join(map(str, [work, *libraries]))}


def compile_file(work, env, rel_stem, save=False, warning_as_error=True):
    cmd = ['lean', '-j1', '-DElab.async=false', '-DautoImplicit=false',
           '-DrelaxedAutoImplicit=false', '-DmaxSynthPendingDepth=3', '-DmaxHeartbeats=4000000',
           f'-DwarningAsError={"true" if warning_as_error else "false"}', '--tstack=400000']
    if save:
        cmd.extend(['-o', rel_stem + '.olean'])
    run = subprocess.run([*cmd, rel_stem + '.lean'], env=env, cwd=work, text=True, encoding='utf-8',
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if run.returncode:
        raise RuntimeError(f"{rel_stem} failed:\n{run.stdout}")
    return [int(n) for n in re.findall(r'\bUsed (\d+) heartbeats,', run.stdout)]


def replay(work, env, module):
    run = subprocess.run(['leanchecker', '-v', module], cwd=work, env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
    if run.returncode or f'replaying {module}' not in run.stdout.splitlines():
        raise RuntimeError(f'Kernel replay of {module} failed:\n{run.stdout}')
    print(run.stdout.rstrip(), file=sys.stderr, flush=True)
    return module


def audit(names):
    constants = ', '.join('`' + name for name in names)
    return f'''
open Lean in
run_cmd do
  let allowed := #[`propext, `Classical.choice, `Quot.sound]
  for decl in #[{constants}] do
    for ax in ← collectAxioms decl do
      unless allowed.contains ax do throwError m!"Unexpected axiom {{ax}} in {{decl}}"
'''


def prepare_wrappers(project, work, env, tasks):
    wrapper_modules = []
    for row, data in indexed_sources(project, tasks):
        rel_stem = row['module'].replace('.', '/')
        dest = work / (rel_stem + '.lean')
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        compile_file(work, env, rel_stem, save=True, warning_as_error=False)
        wrapper_modules.append(row['module'])
    if len(wrapper_modules) != len(tasks):
        raise ValueError('Missing wrapper modules')
    return sorted(wrapper_modules)


def prepare_siblings(project, work, env):
    # M087333's sum-bound helper calls this depth-0 archive module.
    modules = prepare_wrappers(project, work, env, {'M088903'})
    lines = [f'import {module}' for module in modules] + ['open IsLocalRing']
    for row, data in indexed_sources(project, set(SIBLINGS)):
        task = row['id']
        missing = set(SIBLINGS[task])
        lines.append(f'namespace ArchiveSiblings.{task}')
        for match in DECL.finditer(data):
            name = match[1].decode()
            if name in missing:
                missing.remove(name)
                lines.append(f'theorem {name} {match[2].strip().decode()}')
        if missing:
            raise ValueError(f'Missing {task} sibling declarations: {sorted(missing)}')
        lines.append(f'end ArchiveSiblings.{task}')
    (work / 'ArchiveSiblings.lean').write_text('\n\n'.join(lines), encoding='utf-8')
    compile_file(work, env, 'ArchiveSiblings', save=True, warning_as_error=False)


def check(project, work):
    cases = source_cases(project)
    version, pin, env = compiler_environment(project, work)

    kernel_replayed = []
    library_costs = {}
    for lib_name, decl_names in (LIBRARIES | STRUCTURAL_LIBRARIES).items():
        library = HERE / f'{lib_name}.lean'
        shutil.copyfile(library, work / library.name)
        compile_file(work, env, lib_name, save=True)
        kernel_replayed.append(replay(work, env, lib_name))
        source = library.read_text(encoding='utf-8')
        source = 'import Mathlib.Util.CountHeartbeats\n' + source.replace('\n/--', '\n#count_heartbeats in\n/--')
        cost_stem = f'{lib_name}Cost'
        (work / (cost_stem + '.lean')).write_text(source, encoding='utf-8')
        costs = compile_file(work, env, cost_stem)
        if len(costs) != len(decl_names):
            raise ValueError(f'Missing {lib_name} heartbeat measurements ({len(costs)} != {len(decl_names)})')
        for dname, cost in zip(decl_names, costs):
            library_costs[dname] = cost

    wrapper_modules = prepare_wrappers(project, work, env, WRAPPER_TASKS)
    prepare_siblings(project, work, env)

    measurements = {'Original': Counter(), 'Shared': Counter()}
    for mode in ('Original', 'Shared'):
        for batch_label in ('Pure', 'Wrapped', 'Structural'):
            batch_cases = [c for c in cases if c[2] == batch_label]
            use_wrappers = batch_label == 'Wrapped'
            libraries = STRUCTURAL_LIBRARIES if batch_label == 'Structural' else LIBRARIES
            lines = [f'import {lib}' for lib in libraries]
            if use_wrappers:
                for wmod in wrapper_modules:
                    lines.append(f'import {wmod}')
            lines.extend([
                'import Mathlib.Util.CountHeartbeats',
                'import Lean.Util.CollectAxioms',
                'open NumberField Polynomial',
                'open scoped Padic',
            ])
            if batch_label == 'Structural':
                lines.insert(0, 'import ArchiveSiblings')
                lines.extend(['open IsLocalRing Topology TopologicalSpace Set Filter', 'open scoped ENNReal NNReal'])
            if use_wrappers:
                lines.extend([
                    'open AlgebraicGeometry CategoryTheory IsDedekindDomain',
                    'open Formalism.ConjugateSelfDual (normV)',
                    'open ReciprocityTheory.ChartRestriction.G.Geo.Tor (spMap)',
                ])
            names = []
            for lemma, term, _, name, block in batch_cases:
                if mode == 'Shared':
                    statement = statement_prefix(block.encode('utf-8'))
                    if statement is None:
                        raise ValueError(f'Cannot locate proof for {name}')
                    block = f'{statement.decode("utf-8")}:= {term}'
                task = name.split('.')[0]
                if batch_label == 'Structural' and task in SIBLINGS:
                    lines.append(f'open ArchiveSiblings.{task} in')
                lines.extend(['#count_heartbeats in', f'theorem {name} {block}'])
                names.append(name)
            lines.append(audit(names + [f'{lib}.{name}' for lib, decls in libraries.items() for name in decls]))
            stem = f'{mode}{batch_label}'
            (work / (stem + '.lean')).write_text('\n\n'.join(lines), encoding='utf-8')
            beats = compile_file(work, env, stem, save=True, warning_as_error=(mode == 'Shared' and not use_wrappers))
            kernel_replayed.append(replay(work, env, stem))
            if len(beats) != len(batch_cases):
                raise ValueError(f'Missing {stem} heartbeat measurements ({len(beats)} != {len(batch_cases)})')
            for (lemma, _, _, _, _), n in zip(batch_cases, beats):
                measurements[mode][lemma] += n

    return dict(
        compiler=version,
        mathlib=pin,
        kernel_replayed=kernel_replayed,
        checked=dict(Counter(c[0] for c in cases)),
        heartbeats={k: dict(v) for k, v in measurements.items()},
        library_heartbeats_by_lemma=library_costs,
        library_heartbeats=sum(library_costs.values()),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path, help='prepared lean/ directory')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='rh-proof-reuse-') as temp:
        print(json.dumps(check(args.project.resolve(), Path(temp)), indent=2))


if __name__ == '__main__':
    main()
