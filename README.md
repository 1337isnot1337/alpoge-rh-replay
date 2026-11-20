# Independent replay of Alpöge’s RH release

Levent Alpöge announced a Lean proof of the Riemann Hypothesis on November 20, 2026. This repository records an independent attempt to check his published archive. Credit for the claimed proof belongs to Alpöge and his collaborators. [Original announcement](https://alpo.ge/remark.pdf)

## Current status

**Full replay in progress.** No full RH verification receipt has been produced by this project. The [two-worker pilot](evidence/pilot-receipt.json) transferred 150 previously unbuilt modules; the primary reused them and kernel-checked one downstream module.

Current cloud progress is recorded in the [worker status report](STATUS.md).

## Contributors

Choose any of **175,187 module tasks** or one of **2,858 work packets**. Each module has a source digest, direct dependencies, import depth, and a coordinator snapshot state. Use the [contributor guide](CONTRIBUTING.md) to find an available packet, claim it, build it, and return evidence. Browse the [packet index](tracker/packets.tsv), [snapshot totals](tracker/summary.json), or [open volunteer claims](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue%20is%3Aopen%20in%3Atitle%20Claim).

Start with the [agent instructions](auto-research.md) to claim work and submit replay evidence. Start your evidence comment with `Replay submission` to be credited automatically. Maintainers review the evidence before marking a task complete.

[Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

<!-- active-volunteers-start -->

| Contributor | Task | Status |
|---|---|---|
| [@dgahelper](https://github.com/dgahelper) | [P0826](https://github.com/rohanarun/alpoge-rh-replay/issues/160) | Claimed |
| [@Paulee314](https://github.com/Paulee314) | [M004105](https://github.com/rohanarun/alpoge-rh-replay/issues/174) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1340](https://github.com/rohanarun/alpoge-rh-replay/issues/181) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1274](https://github.com/rohanarun/alpoge-rh-replay/issues/186) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1219](https://github.com/rohanarun/alpoge-rh-replay/issues/187) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P0945](https://github.com/rohanarun/alpoge-rh-replay/issues/189) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1467](https://github.com/rohanarun/alpoge-rh-replay/issues/195) | Claimed |
| [@roonastgames](https://github.com/roonastgames) | [M164707](https://github.com/rohanarun/alpoge-rh-replay/issues/196) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1261](https://github.com/rohanarun/alpoge-rh-replay/issues/202) | Claimed |
| [@Lv-00-ANI](https://github.com/Lv-00-ANI) | [M170889](https://github.com/rohanarun/alpoge-rh-replay/issues/204) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1030](https://github.com/rohanarun/alpoge-rh-replay/issues/206) | Claimed |
| [@Lv-00-ANI](https://github.com/Lv-00-ANI) | [M175186](https://github.com/rohanarun/alpoge-rh-replay/issues/208) | Claimed |
| [@Lv-00-ANI](https://github.com/Lv-00-ANI) | [M175187](https://github.com/rohanarun/alpoge-rh-replay/issues/211) | Claimed |
| [@Lv-00-ANI](https://github.com/Lv-00-ANI) | [M175185](https://github.com/rohanarun/alpoge-rh-replay/issues/213) | Claimed |
| [@Lv-00-ANI](https://github.com/Lv-00-ANI) | [M108233](https://github.com/rohanarun/alpoge-rh-replay/issues/214) | Claimed |
| [@Lv-00-ANI](https://github.com/Lv-00-ANI) | [M109322](https://github.com/rohanarun/alpoge-rh-replay/issues/215) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M116516](https://github.com/rohanarun/alpoge-rh-replay/issues/217) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M100842](https://github.com/rohanarun/alpoge-rh-replay/issues/219) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M119679](https://github.com/rohanarun/alpoge-rh-replay/issues/220) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M100838](https://github.com/rohanarun/alpoge-rh-replay/issues/221) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M101080](https://github.com/rohanarun/alpoge-rh-replay/issues/222) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M002650](https://github.com/rohanarun/alpoge-rh-replay/issues/223) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M108181](https://github.com/rohanarun/alpoge-rh-replay/issues/224) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M004039](https://github.com/rohanarun/alpoge-rh-replay/issues/225) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M101079](https://github.com/rohanarun/alpoge-rh-replay/issues/226) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M004742](https://github.com/rohanarun/alpoge-rh-replay/issues/227) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M169429](https://github.com/rohanarun/alpoge-rh-replay/issues/228) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M037677](https://github.com/rohanarun/alpoge-rh-replay/issues/229) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M119836](https://github.com/rohanarun/alpoge-rh-replay/issues/230) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M149216](https://github.com/rohanarun/alpoge-rh-replay/issues/231) | Claimed |
| [@SeriousRising](https://github.com/SeriousRising) | [P0866](https://github.com/rohanarun/alpoge-rh-replay/issues/235) | Claimed |
| [@user42245](https://github.com/user42245) | [M102943](https://github.com/rohanarun/alpoge-rh-replay/issues/239) | Claimed |
| [@TVSuchty](https://github.com/TVSuchty) | [M141625](https://github.com/rohanarun/alpoge-rh-replay/issues/243) | Claimed |
| [@TVSuchty](https://github.com/TVSuchty) | [M119659](https://github.com/rohanarun/alpoge-rh-replay/issues/244) | Claimed |
| [@surfyhou](https://github.com/surfyhou) | [P1099](https://github.com/rohanarun/alpoge-rh-replay/issues/245) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M004402](https://github.com/rohanarun/alpoge-rh-replay/issues/247) | Claimed |
| [@surfyhou](https://github.com/surfyhou) | [P1279](https://github.com/rohanarun/alpoge-rh-replay/issues/248) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M049826](https://github.com/rohanarun/alpoge-rh-replay/issues/249) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M051308](https://github.com/rohanarun/alpoge-rh-replay/issues/250) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M157546](https://github.com/rohanarun/alpoge-rh-replay/issues/251) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M109400](https://github.com/rohanarun/alpoge-rh-replay/issues/252) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M131581](https://github.com/rohanarun/alpoge-rh-replay/issues/253) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M137272](https://github.com/rohanarun/alpoge-rh-replay/issues/254) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M168909](https://github.com/rohanarun/alpoge-rh-replay/issues/255) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M106334](https://github.com/rohanarun/alpoge-rh-replay/issues/256) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M051482](https://github.com/rohanarun/alpoge-rh-replay/issues/257) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M131798](https://github.com/rohanarun/alpoge-rh-replay/issues/258) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M007110](https://github.com/rohanarun/alpoge-rh-replay/issues/259) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M027152](https://github.com/rohanarun/alpoge-rh-replay/issues/260) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M138276](https://github.com/rohanarun/alpoge-rh-replay/issues/261) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M012733](https://github.com/rohanarun/alpoge-rh-replay/issues/262) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M161227](https://github.com/rohanarun/alpoge-rh-replay/issues/263) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M127561](https://github.com/rohanarun/alpoge-rh-replay/issues/264) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M100540](https://github.com/rohanarun/alpoge-rh-replay/issues/265) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M108607](https://github.com/rohanarun/alpoge-rh-replay/issues/266) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M110476](https://github.com/rohanarun/alpoge-rh-replay/issues/267) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M018347](https://github.com/rohanarun/alpoge-rh-replay/issues/268) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M120149](https://github.com/rohanarun/alpoge-rh-replay/issues/269) | Claimed |
| [@dga471](https://github.com/dga471) | [M113396](https://github.com/rohanarun/alpoge-rh-replay/issues/271) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P0975](https://github.com/rohanarun/alpoge-rh-replay/issues/272) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1385](https://github.com/rohanarun/alpoge-rh-replay/issues/273) | Claimed |
| [@Wronskode](https://github.com/Wronskode) | [M101325](https://github.com/rohanarun/alpoge-rh-replay/issues/274) | Claimed |
| [@Amahane-Hikari](https://github.com/Amahane-Hikari) | [M150069](https://github.com/rohanarun/alpoge-rh-replay/issues/275) | Claimed |
| [@shardmods](https://github.com/shardmods) | [P1409](https://github.com/rohanarun/alpoge-rh-replay/issues/278) | Claimed |
| [@rohanarun](https://github.com/rohanarun) | [M109467](https://github.com/rohanarun/alpoge-rh-replay/issues/279) | Claimed |
| [@gniax](https://github.com/gniax) | [M161831](https://github.com/rohanarun/alpoge-rh-replay/issues/280) | Claimed |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P1069](https://github.com/rohanarun/alpoge-rh-replay/issues/281) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M037368](https://github.com/rohanarun/alpoge-rh-replay/issues/282) | Claimed |

<!-- active-volunteers-end -->

### Submitted for review

<!-- pending-volunteers-start -->

| Contributor | Task | Review |
|---|---|---|
| [@MLTQ](https://github.com/MLTQ) | [P0123](https://github.com/rohanarun/alpoge-rh-replay/issues/87#issuecomment-7046017638) | Pending review |
| [@shardmods](https://github.com/shardmods) | [P0757](https://github.com/rohanarun/alpoge-rh-replay/issues/120#issuecomment-7046963832) | Pending review |
| [@shardmods](https://github.com/shardmods) | [P1016](https://github.com/rohanarun/alpoge-rh-replay/issues/122#issuecomment-7046960866) | Pending review |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0659](https://github.com/rohanarun/alpoge-rh-replay/issues/134#issuecomment-7047082940) | Pending review |
| [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng) | [P1230](https://github.com/rohanarun/alpoge-rh-replay/issues/158#issuecomment-7047054079) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M119671](https://github.com/rohanarun/alpoge-rh-replay/issues/185#issuecomment-7047062317) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M125803](https://github.com/rohanarun/alpoge-rh-replay/issues/197#issuecomment-7047062342) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M002164](https://github.com/rohanarun/alpoge-rh-replay/issues/198#issuecomment-7047062219) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M149215](https://github.com/rohanarun/alpoge-rh-replay/issues/216#issuecomment-7047090981) | Pending review |
| [@BenCaunt](https://github.com/BenCaunt) | [M106654](https://github.com/rohanarun/alpoge-rh-replay/issues/218#issuecomment-7047090799) | Pending review |
| [@gabeldev](https://github.com/gabeldev) | [M038888](https://github.com/rohanarun/alpoge-rh-replay/issues/277#issuecomment-7047066157) | Pending review |
| [@gabeldev](https://github.com/gabeldev) | [M149422](https://github.com/rohanarun/alpoge-rh-replay/issues/283#issuecomment-7047082284) | Pending review |

<!-- pending-volunteers-end -->

### Reviewed builds

<!-- volunteers-start -->

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@dgahelper](https://github.com/dgahelper) | [M000028](https://github.com/rohanarun/alpoge-rh-replay/issues/136#issuecomment-7046171466) | 1 | [Build evidence verified](evidence/volunteers/M000028.json) |
| [@varo6](https://github.com/varo6) | [M000756](https://github.com/rohanarun/alpoge-rh-replay/issues/157#issuecomment-7046169778) | 1 | [Build evidence verified](evidence/volunteers/M000756.json) |
| [@varo6](https://github.com/varo6) | [M000757](https://github.com/rohanarun/alpoge-rh-replay/issues/139#issuecomment-7046108657) | 1 | [Build evidence verified](evidence/volunteers/M000757.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [M002998](https://github.com/rohanarun/alpoge-rh-replay/issues/124#issuecomment-7045969982) | 1 | [Build evidence verified](evidence/volunteers/M002998.json) |
| [@varo6](https://github.com/varo6) | [M003369](https://github.com/rohanarun/alpoge-rh-replay/issues/164#issuecomment-7046219921) | 1 | [Build evidence verified](evidence/volunteers/M003369.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M003371](https://github.com/rohanarun/alpoge-rh-replay/issues/144#issuecomment-7046484735) | 1 | [Build evidence verified](evidence/volunteers/M003371.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M004133](https://github.com/rohanarun/alpoge-rh-replay/issues/146#issuecomment-7046485806) | 1 | [Build evidence verified](evidence/volunteers/M004133.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M004876](https://github.com/rohanarun/alpoge-rh-replay/issues/151#issuecomment-7046491574) | 1 | [Build evidence verified](evidence/volunteers/M004876.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M016897](https://github.com/rohanarun/alpoge-rh-replay/issues/10#issuecomment-7045920937) | 1 | [Build evidence verified](evidence/volunteers/M016897.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M062129](https://github.com/rohanarun/alpoge-rh-replay/issues/147#issuecomment-7046486614) | 1 | [Build evidence verified](evidence/volunteers/M062129.json) |
| [@TVSuchty](https://github.com/TVSuchty) | [M080008](https://github.com/rohanarun/alpoge-rh-replay/issues/86#issuecomment-7045864795) | 1 | [Build evidence verified](evidence/volunteers/M080008.json) |
| [@TVSuchty](https://github.com/TVSuchty) | [M080009](https://github.com/rohanarun/alpoge-rh-replay/issues/138#issuecomment-7046218293) | 1 | [Build evidence verified](evidence/volunteers/M080009.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M101624](https://github.com/rohanarun/alpoge-rh-replay/issues/159#issuecomment-7046492175) | 1 | [Build evidence verified](evidence/volunteers/M101624.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M103332](https://github.com/rohanarun/alpoge-rh-replay/issues/143#issuecomment-7046484168) | 1 | [Build evidence verified](evidence/volunteers/M103332.json) |
| [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng) | [M103506](https://github.com/rohanarun/alpoge-rh-replay/issues/126#issuecomment-7045987064) | 1 | [Build evidence verified](evidence/volunteers/M103506.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M108533](https://github.com/rohanarun/alpoge-rh-replay/issues/149#issuecomment-7046487953) | 1 | [Build evidence verified](evidence/volunteers/M108533.json) |
| [@gabeldev](https://github.com/gabeldev) | [M117317](https://github.com/rohanarun/alpoge-rh-replay/issues/156#issuecomment-7046204159) | 1 | [Build evidence verified](evidence/volunteers/M117317.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M141426](https://github.com/rohanarun/alpoge-rh-replay/issues/148#issuecomment-7046487357) | 1 | [Build evidence verified](evidence/volunteers/M141426.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M163942](https://github.com/rohanarun/alpoge-rh-replay/issues/145#issuecomment-7046485257) | 1 | [Build evidence verified](evidence/volunteers/M163942.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [M164962](https://github.com/rohanarun/alpoge-rh-replay/issues/150#issuecomment-7046491107) | 1 | [Build evidence verified](evidence/volunteers/M164962.json) |
| [@surfyhou](https://github.com/surfyhou) | [M170887](https://github.com/rohanarun/alpoge-rh-replay/issues/5#issuecomment-7044980759) | 1 | [Build evidence verified](evidence/volunteers/M170887.json) |
| [@arxhr007](https://github.com/arxhr007) | [M171103](https://github.com/rohanarun/alpoge-rh-replay/issues/141#issuecomment-7046656867) | 1 | [Build evidence verified](evidence/volunteers/M171103.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0012](https://github.com/rohanarun/alpoge-rh-replay/issues/1#issuecomment-7044609913) | 64 | [Build evidence verified](evidence/volunteers/P0012.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0020](https://github.com/rohanarun/alpoge-rh-replay/issues/2#issuecomment-7044751121) | 64 | [Build evidence verified](evidence/volunteers/P0020.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0021](https://github.com/rohanarun/alpoge-rh-replay/issues/3#issuecomment-7044905860) | 64 | [Build evidence verified](evidence/volunteers/P0021.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0041](https://github.com/rohanarun/alpoge-rh-replay/issues/6#issuecomment-7045037425) | 64 | [Build evidence verified](evidence/volunteers/P0041.json) |
| [@krisyotam](https://github.com/krisyotam) | [P0060](https://github.com/rohanarun/alpoge-rh-replay/issues/7#issuecomment-7045297630) | 64 | [Build evidence verified](evidence/volunteers/P0060.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0061](https://github.com/rohanarun/alpoge-rh-replay/issues/8#issuecomment-7045174078) | 64 | [Build evidence verified](evidence/volunteers/P0061.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0064](https://github.com/rohanarun/alpoge-rh-replay/issues/9#issuecomment-7045329594) | 64 | [Build evidence verified](evidence/volunteers/P0064.json) |
| [@DanieleCorso](https://github.com/DanieleCorso) | [P0103](https://github.com/rohanarun/alpoge-rh-replay/issues/11#issuecomment-7046400741) | 64 | [Build evidence verified](evidence/volunteers/P0103.json) |
| [@juanfers1](https://github.com/juanfers1) | [P0104](https://github.com/rohanarun/alpoge-rh-replay/issues/12#issuecomment-7045481960) | 64 | [Build evidence verified](evidence/volunteers/P0104.json) |
| [@gabeldev](https://github.com/gabeldev) | [P0108](https://github.com/rohanarun/alpoge-rh-replay/issues/14#issuecomment-7045548766) | 64 | [Build evidence verified](evidence/volunteers/P0108.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0111](https://github.com/rohanarun/alpoge-rh-replay/issues/15#issuecomment-7045474203) | 64 | [Build evidence verified](evidence/volunteers/P0111.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0113](https://github.com/rohanarun/alpoge-rh-replay/issues/18#issuecomment-7045681101) | 64 | [Build evidence verified](evidence/volunteers/P0113.json) |
| [@gabeldev](https://github.com/gabeldev) | [P0114](https://github.com/rohanarun/alpoge-rh-replay/issues/20#issuecomment-7045695171) | 64 | [Build evidence verified](evidence/volunteers/P0114.json) |
| [@krisyotam](https://github.com/krisyotam) | [P0125](https://github.com/rohanarun/alpoge-rh-replay/issues/88#issuecomment-7045913737) | 64 | [Build evidence verified](evidence/volunteers/P0125.json) |
| [@juanfers1](https://github.com/juanfers1) | [P0129](https://github.com/rohanarun/alpoge-rh-replay/issues/89#issuecomment-7045795333) | 64 | [Build evidence verified](evidence/volunteers/P0129.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [P0145](https://github.com/rohanarun/alpoge-rh-replay/issues/16#issuecomment-7045833885) | 64 | [Build evidence verified](evidence/volunteers/P0145.json) |
| [@dgahelper](https://github.com/dgahelper) | [P0172](https://github.com/rohanarun/alpoge-rh-replay/issues/91#issuecomment-7045992035) | 64 | [Build evidence verified](evidence/volunteers/P0172.json) |
| [@gabeldev](https://github.com/gabeldev) | [P0178](https://github.com/rohanarun/alpoge-rh-replay/issues/96#issuecomment-7046079755) | 64 | [Build evidence verified](evidence/volunteers/P0178.json) |
| [@gabeldev](https://github.com/gabeldev) | [P0182](https://github.com/rohanarun/alpoge-rh-replay/issues/97#issuecomment-7046142068) | 64 | [Build evidence verified](evidence/volunteers/P0182.json) |
| [@shardmods](https://github.com/shardmods) | [P0191](https://github.com/rohanarun/alpoge-rh-replay/issues/100#issuecomment-7046158317) | 64 | [Build evidence verified](evidence/volunteers/P0191.json) |
| [@shardmods](https://github.com/shardmods) | [P0199](https://github.com/rohanarun/alpoge-rh-replay/issues/98#issuecomment-7046154029) | 64 | [Build evidence verified](evidence/volunteers/P0199.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0209](https://github.com/rohanarun/alpoge-rh-replay/issues/95#issuecomment-7045938029) | 64 | [Build evidence verified](evidence/volunteers/P0209.json) |
| [@shardmods](https://github.com/shardmods) | [P0237](https://github.com/rohanarun/alpoge-rh-replay/issues/99#issuecomment-7046156582) | 64 | [Build evidence verified](evidence/volunteers/P0237.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0254](https://github.com/rohanarun/alpoge-rh-replay/issues/94#issuecomment-7045929752) | 64 | [Build evidence verified](evidence/volunteers/P0254.json) |
| [@shardmods](https://github.com/shardmods) | [P0255](https://github.com/rohanarun/alpoge-rh-replay/issues/104#issuecomment-7046166397) | 64 | [Build evidence verified](evidence/volunteers/P0255.json) |
| [@shardmods](https://github.com/shardmods) | [P0256](https://github.com/rohanarun/alpoge-rh-replay/issues/103#issuecomment-7046164400) | 64 | [Build evidence verified](evidence/volunteers/P0256.json) |
| [@shardmods](https://github.com/shardmods) | [P0261](https://github.com/rohanarun/alpoge-rh-replay/issues/101#issuecomment-7046160215) | 64 | [Build evidence verified](evidence/volunteers/P0261.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0287](https://github.com/rohanarun/alpoge-rh-replay/issues/92#issuecomment-7045860836) | 64 | [Build evidence verified](evidence/volunteers/P0287.json) |
| [@shardmods](https://github.com/shardmods) | [P0293](https://github.com/rohanarun/alpoge-rh-replay/issues/102#issuecomment-7046162412) | 64 | [Build evidence verified](evidence/volunteers/P0293.json) |
| [@shardmods](https://github.com/shardmods) | [P0300](https://github.com/rohanarun/alpoge-rh-replay/issues/113#issuecomment-7046252794) | 64 | [Build evidence verified](evidence/volunteers/P0300.json) |
| [@shardmods](https://github.com/shardmods) | [P0309](https://github.com/rohanarun/alpoge-rh-replay/issues/109#issuecomment-7046176449) | 64 | [Build evidence verified](evidence/volunteers/P0309.json) |
| [@shardmods](https://github.com/shardmods) | [P0311](https://github.com/rohanarun/alpoge-rh-replay/issues/105#issuecomment-7046168327) | 64 | [Build evidence verified](evidence/volunteers/P0311.json) |
| [@shardmods](https://github.com/shardmods) | [P0346](https://github.com/rohanarun/alpoge-rh-replay/issues/106#issuecomment-7046170429) | 64 | [Build evidence verified](evidence/volunteers/P0346.json) |
| [@shardmods](https://github.com/shardmods) | [P0392](https://github.com/rohanarun/alpoge-rh-replay/issues/108#issuecomment-7046174698) | 64 | [Build evidence verified](evidence/volunteers/P0392.json) |
| [@shardmods](https://github.com/shardmods) | [P0408](https://github.com/rohanarun/alpoge-rh-replay/issues/111#issuecomment-7046181111) | 64 | [Build evidence verified](evidence/volunteers/P0408.json) |
| [@shardmods](https://github.com/shardmods) | [P0419](https://github.com/rohanarun/alpoge-rh-replay/issues/118#issuecomment-7046257251) | 64 | [Build evidence verified](evidence/volunteers/P0419.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0452](https://github.com/rohanarun/alpoge-rh-replay/issues/93#issuecomment-7045926387) | 64 | [Build evidence verified](evidence/volunteers/P0452.json) |
| [@juanfers1](https://github.com/juanfers1) | [P0476](https://github.com/rohanarun/alpoge-rh-replay/issues/127#issuecomment-7046093484) | 64 | [Build evidence verified](evidence/volunteers/P0476.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0485](https://github.com/rohanarun/alpoge-rh-replay/issues/125#issuecomment-7046689906) | 64 | [Build evidence verified](evidence/volunteers/P0485.json) |
| [@shardmods](https://github.com/shardmods) | [P0494](https://github.com/rohanarun/alpoge-rh-replay/issues/112#issuecomment-7046182894) | 64 | [Build evidence verified](evidence/volunteers/P0494.json) |
| [@shardmods](https://github.com/shardmods) | [P0539](https://github.com/rohanarun/alpoge-rh-replay/issues/110#issuecomment-7046178996) | 64 | [Build evidence verified](evidence/volunteers/P0539.json) |
| [@shardmods](https://github.com/shardmods) | [P0558](https://github.com/rohanarun/alpoge-rh-replay/issues/114#issuecomment-7046255154) | 64 | [Build evidence verified](evidence/volunteers/P0558.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0562](https://github.com/rohanarun/alpoge-rh-replay/issues/130#issuecomment-7046694327) | 64 | [Build evidence verified](evidence/volunteers/P0562.json) |
| [@shardmods](https://github.com/shardmods) | [P0595](https://github.com/rohanarun/alpoge-rh-replay/issues/107#issuecomment-7046172719) | 64 | [Build evidence verified](evidence/volunteers/P0595.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0596](https://github.com/rohanarun/alpoge-rh-replay/issues/128#issuecomment-7046566514) | 64 | [Build evidence verified](evidence/volunteers/P0596.json) |
| [@shardmods](https://github.com/shardmods) | [P0628](https://github.com/rohanarun/alpoge-rh-replay/issues/115#issuecomment-7046297848) | 64 | [Build evidence verified](evidence/volunteers/P0628.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0630](https://github.com/rohanarun/alpoge-rh-replay/issues/135#issuecomment-7046723994) | 64 | [Build evidence verified](evidence/volunteers/P0630.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0661](https://github.com/rohanarun/alpoge-rh-replay/issues/132#issuecomment-7046674165) | 64 | [Build evidence verified](evidence/volunteers/P0661.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0744](https://github.com/rohanarun/alpoge-rh-replay/issues/133#issuecomment-7046804107) | 64 | [Build evidence verified](evidence/volunteers/P0744.json) |
| [@shardmods](https://github.com/shardmods) | [P0766](https://github.com/rohanarun/alpoge-rh-replay/issues/121#issuecomment-7046260012) | 64 | [Build evidence verified](evidence/volunteers/P0766.json) |
| [@JanSimeonMetzger](https://github.com/JanSimeonMetzger) | [P0783](https://github.com/rohanarun/alpoge-rh-replay/issues/129#issuecomment-7046740555) | 64 | [Build evidence verified](evidence/volunteers/P0783.json) |
| [@shardmods](https://github.com/shardmods) | [P0794](https://github.com/rohanarun/alpoge-rh-replay/issues/116#issuecomment-7046403491) | 64 | [Build evidence verified](evidence/volunteers/P0794.json) |
| [@juanfers1](https://github.com/juanfers1) | [P0799](https://github.com/rohanarun/alpoge-rh-replay/issues/153#issuecomment-7046623779) | 64 | [Build evidence verified](evidence/volunteers/P0799.json) |
| [@shardmods](https://github.com/shardmods) | [P0820](https://github.com/rohanarun/alpoge-rh-replay/issues/119#issuecomment-7046299655) | 64 | [Build evidence verified](evidence/volunteers/P0820.json) |
| [@shardmods](https://github.com/shardmods) | [P0849](https://github.com/rohanarun/alpoge-rh-replay/issues/117#issuecomment-7046376924) | 64 | [Build evidence verified](evidence/volunteers/P0849.json) |
| [@SeriousRising](https://github.com/SeriousRising) | [P1058](https://github.com/rohanarun/alpoge-rh-replay/issues/140#issuecomment-7046460455) | 64 | [Build evidence verified](evidence/volunteers/P1058.json) |

<!-- volunteers-end -->

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 4,230 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 14,699 |
| Volunteer build evidence reviewed | 3,606 |
| **Total with recorded module evidence** | **22,686 / 175,187** |

[See each completed part and its evidence](completed/README.md) · [Machine-readable ledger](tracker/completed.tsv)

<!-- completed-end -->

## Give this prompt to an agent

> Help independently replay the claimed RH proof using https://github.com/rohanarun/alpoge-rh-replay. Read auto-research.md and fast-forward to the latest main commit. Run `python3 tracker/tasks.py next` and inspect an open packet. Claim exactly one open packet or module. Wait for the claim-granted label and matching bot comment before starting. Reproduce the pinned inputs, build the assigned targets and their required imports, and attach the receipt, log, and artifact hashes to your issue. If you stop, release the claim. Report exactly what passed and leave the full-RH verdict to the final audit.

[Full instructions for agents](auto-research.md) · [Claims and conflicts](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+in%3Atitle+Claim)

## Reproduce the check

On Linux, install the elan launcher and ensure its `lean` and `lake` commands are on your PATH. The script also requires Bash, Git, curl, GNU tar, sha256sum, a C toolchain, network access, and a large writable build volume. Run from this repository with a fresh output directory.

```bash
./verify.sh /path/to/empty/replay-directory
```

The script compares every archive part with its SHA-256 digest, checks the toolchain and mathlib revision, builds the final module from source, and writes the transcript to `replay.log` in the output directory. The pinned Lean compiler is 4.33.1 and the mathlib commit is `0df444a360eaa60ab8c11dca51a86af692955474`.

## Read the evidence

1. `REPLAY_SOURCE_BUILD_PASSED` means Lake built the module containing the final theorem.
2. `REPLAY_AXIOM_AUDIT_PASSED` means the five public theorems in `Main` type-checked against their statements, which `Audit.lean` writes out with Mathlib definitions only. The audit rejects any reported axiom beyond propositional extensionality, classical choice, and quotient soundness.
3. `REPLAY_FRESH_KERNEL_PASSED` means Lean’s checker replayed the declarations imported by `Main` in a fresh environment. It uses the same Lean kernel implementation.

A completed report should include the exit status, all three outputs, the printed theorem and axioms, and a checksum for the archived transcript. A machine or storage failure leaves the mathematical claim unresolved.

## Volunteer activity

![Cumulative chart of volunteers, granted claims, and replay submissions](tracker/activity.svg)

[How the chart is counted](ACTIVITY.md) · [Event data](tracker/activity.tsv)

## License

The original replay tooling and documentation in this repository are available under the [MIT License](LICENSE). Upstream Lean source, Mathlib, and third-party artifacts retain their respective licenses.
