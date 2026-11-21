"""Index literal artifact stems, retaining inventory-change checks."""
from pathlib import Path


class ArtifactDirectoryIndex:
    def __init__(self, paths, ignored_suffixes=()):
        self.requested = set(map(Path, paths))
        self.selected = {}
        for path in self.requested:
            if self.literal(path.name):
                self.selected.setdefault(path.parent, set()).add(path.name)
        self.directories = {}
        self.watched = {}
        self.ignored_suffixes = tuple(ignored_suffixes)

    def inventory(self, paths):
        return frozenset(p.name for p in paths if not p.name.endswith(self.ignored_suffixes))

    @staticmethod
    def literal(stem):
        return not any(c in stem for c in '.*?[')

    @staticmethod
    def read(directory, stems):
        result = {}
        try:
            for path in directory.iterdir():
                stem, separator, _ = path.name.partition('.')
                if separator and stem in stems:
                    result.setdefault(stem, []).append(path)
        except FileNotFoundError:
            return result
        return result

    def matches(self, path):
        path = Path(path)
        if path not in self.requested:
            raise ValueError('Artifact stem was not selected: ' + str(path))
        if self.literal(path.name):
            if path.parent not in self.directories:
                self.directories[path.parent] = self.read(path.parent, self.selected[path.parent])
            found = list(self.directories[path.parent].get(path.name, []))
        else:
            # Preserve pathlib's pattern semantics for unusual stems.
            found = list(path.parent.glob(path.name + '.*'))
        names = self.inventory(found)
        if path in self.watched and self.watched[path] != names:
            raise ValueError('Artifact inventory changed: ' + str(path))
        self.watched[path] = names
        return found

    def verify(self):
        watched = {}
        for path, expected in self.watched.items():
            watched.setdefault(path.parent, {})[path] = expected
        for directory, paths in watched.items():
            stems = {path.name for path in paths if self.literal(path.name)}
            current = self.read(directory, stems) if stems else {}
            for path, expected in paths.items():
                found = (current.get(path.name, []) if self.literal(path.name)
                         else path.parent.glob(path.name + '.*'))
                if self.inventory(found) != expected:
                    raise ValueError('Artifact inventory changed: ' + str(path))
            del current
