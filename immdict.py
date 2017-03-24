import copy

class ImmDict:

    def __init__(self, d=None):
        if d is None:
            self.d = {}
        else:
            self.d = d

    def put(self, key, value):
        return ImmDict({**{key: value}, **self.d})

    def get(self, key):
        try:
            return self.d[key]
        except KeyError:
            return None

    def keys(self):
        return copy.copy(self.d.keys())

    def values(self):
        return copy.copy(self.d.values())

    def get_dict(self):
        return copy.deepcopy(self.d)
