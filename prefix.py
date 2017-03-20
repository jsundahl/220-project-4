

class Prefix:

    def new_prefix(self, first, second):
        return first, second

    def shift_in(self, tuple, word):
        return tuple[1], word