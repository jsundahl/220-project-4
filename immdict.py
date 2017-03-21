import copy

class ImmDict:

    def __init__(self):
        self.d = {}

    def put(self, key, value):
        return {**{key: value}, **self.d}

    def get(self, key):
        try:
            return self.d[key]
        except KeyError:
            return None

    def keys(self):
        return copy.copy(self.d.keys())

    def values(self):
        return copy.copy(self.d.values())
