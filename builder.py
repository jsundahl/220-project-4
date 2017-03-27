import suffix
from functools import *
from immdict import ImmDict
NONWORD = '/n'


def line_gen(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line


def pairs_gen(file_name, line_gen_fn):
    def pairs_from_line(word_list):
        for i in range(0, len(word_list) - 2):
            yield (word_list[i], word_list[i + 1]), word_list[i + 2]
    line_gen = line_gen_fn(file_name)
    words = [NONWORD, NONWORD] + next(line_gen).split()
    for x in pairs_from_line(words):
        yield x
    last_two = [words[-2], words[-1]]
    for line in line_gen:
        words = last_two + line.split()
        for x in pairs_from_line(words):
            yield x
        last_two = [words[-2], words[-1]]
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
