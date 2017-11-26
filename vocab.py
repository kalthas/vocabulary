"""
Manages vocabulary
"""
import sys

vocab = set()

def read_as_set(fn):
    result = set()
    with open(fn, 'r') as f:
        for l in f.readlines():
            result.add(l.strip())
    return result

vocab = read_as_set('known_words.txt')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        new = read_as_set(sys.argv[1])
        vocab.update(new)
        with open('known_words.new.txt', 'w+') as fo:
            for w in sorted(vocab):
                fo.write(w)
                fo.write('\n')
