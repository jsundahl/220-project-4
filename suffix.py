from immdict import ImmDict
import copy


class Suffix:

    def empty_suffix(self):
        return ImmDict()

    def add_word(self, suffix, word):
        if suffix.get(word) is None:
            return suffix.put(word, 1)
        else:
            d = copy.deepcopy(suffix)
            d.pop(word)
            return d

    def choose_word(self, chain, prefix, randomizer):
        return NotImplemented
