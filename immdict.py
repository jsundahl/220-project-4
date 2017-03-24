import copy
from functools import *

class ImmDict:

    def __init__(self, d=None):
        if d is None:
            self.d = {}
        else:
            self.d = d

    def put(self, key, value):
        return ImmDict({**self.d, **{key: value}})

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

    def __str__(self):
        list = []
        for k, v in self.d.items():
            value = None
            if isinstance(v, ImmDict):
                value = str(v.d)
            else:
                value = str(v)
            list.append("{}: {}".format(str(k), value))
        return '\n'.join(list)
