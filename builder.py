import suffix
from functools import *
from immdict import ImmDict
NONWORD = '/n'


def line_gen(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line


def pairs_gen(file_name, line_gen_fn):
    """
    Takes a file name and a line generating function (such as line_gen) as parameters. It
    calls the line generating function to get the lines of text. It returns a generator that
    produces tuples. Each of these tuples contains a prefix (itself a tuple) and the following
    word in the text. At the start, it creates the starting prefix contains (NONWORD ,
    NONWORD) and pairs it with the first word in the first line. It then shifts that word in to
    the next prefix, and so on. In processing the lines of text, it must keep track of the last
    two words in a line as that will be the ‘sliding’ prefix for the next line. Note that the last
    tuple returned will include the last prefix and NONWORD. A loop is allowed here as it is
    fully encapsulated
    """
    def pairs_from_line(word_list):
        for i in range(0, len(word_list) - 2):
            yield (word_list[i], word_list[i + 1]), word_list[i + 2]
    line_gen = line_gen_fn(file_name)
    words = [NONWORD, NONWORD] + next(line_gen).split(' ')
    for x in pairs_from_line(words):
        yield x
    for line in line_gen:
        words = line.split(' ')
        for x in pairs_from_line(words):
            yield x
    for x in pairs_from_line([words[len(words)-2], words[len(words)-1]] + [NONWORD]):
        yield x


def add_to_chain(chain, pair):
    if chain.get(pair[0]) is None:
        return chain.put(pair[0], suffix.add_word(ImmDict(), pair[1]))
    else:
        value = chain.get(pair[0])
        return chain.put(pair[0], suffix.add_word(value, pair[1]))


def build_chain(add_fn, pair_gen, immdict_obj):
    return reduce(lambda d, p: add_fn(d, p), pair_gen, immdict_obj)


def build(file_name):
    gen = pairs_gen(file_name, line_gen)
    return build_chain(add_to_chain, gen, ImmDict())
