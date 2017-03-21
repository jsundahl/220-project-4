from immdict import ImmDict
import copy


class Suffix:

    def empty_suffix(self):
        return ImmDict()

    def add_word(self, suffix, word):
        if suffix.get(word) is None:
            return suffix.put(word, 1)
        else:
            old_pair = suffix.get(word)
            return suffix.put({old_pair[0]: old_pair[1] + 1})

    def choose_word(self, chain, prefix, randomizer):
        return NotImplemented
