"""Index literal artifact stems, retaining inventory-change checks."""
from pathlib import Path


class ArtifactDirectoryIndex:
    def __init__(self, ignored_suffixes=()):
        self.directories = {}
        self.watched = {}
        self.ignored_suffixes = tuple(ignored_suffixes)

    def inventory(self, paths):
        return frozenset(p.name for p in paths if not p.name.endswith(self.ignored_suffixes))

    @staticmethod
    def literal(stem):
        return not any(c in stem for c in '.*?[')

    @staticmethod
    def read(directory):
        result = {}
        try:
            entries = list(directory.iterdir())
        except FileNotFoundError:
            return result
        for path in entries:
            stem, separator, _ = path.name.partition('.')
            if separator:
                result.setdefault(stem, []).append(path)
        return result

    def matches(self, path):
        path = Path(path)
        if self.literal(path.name):
            if path.parent not in self.directories:
                self.directories[path.parent] = self.read(path.parent)
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
        current = {directory: self.read(directory) for directory in self.directories}
        for path, expected in self.watched.items():
            found = (current[path.parent].get(path.name, []) if self.literal(path.name)
                     else path.parent.glob(path.name + '.*'))
            if self.inventory(found) != expected:
                raise ValueError('Artifact inventory changed: ' + str(path))
