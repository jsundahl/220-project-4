
NONWORD = '/n'

def build(file_name):
    return NotImplemented

def line_gen(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line

# todo: test this as well
def pairs_gen(file_name, line_gen_fn):
    def pairs_from_line(words):
        for i in range(0, len(words) - 2):
            yield (words[i], words[i+1]), words[i+2]
    line_gen = line_gen_fn(file_name)
    word_array = line_gen.next().split(' ')
    yield (NONWORD, NONWORD), word_array[0]
    pairs_from_line(word_array[1:])
    for line in line_gen:
        words = line.split(' ')
        pairs_from_line(words)


def add_to_chain(chain, pair):
    return NotImplemented