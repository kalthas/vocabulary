import re
import sys
import nltk

from vocab import vocab as known

if len(sys.argv) < 2:
    print('Need a file from while to extract')
    sys.exit(1)
infn = sys.argv[1]

reWord = re.compile("^[a-zA-Z']+$")
all_vocab = set()
known_vocab = set()
invalid_vocab = set()
target_vocab = set()

with open(infn, 'r') as inf:
    words = [w.lower() for w in nltk.wordpunct_tokenize(inf.read())]
    all_vocab = sorted(set(words))
    for w in all_vocab:
        if w in known:
            known_vocab.add(w)
        elif reWord.match(w) is None:
            invalid_vocab.add(w)
        else:
            target_vocab.add(w)

def print_set(tag, vocabset):
    print("======= %s(%d) ======="%(tag, len(vocabset)))
    for word in vocabset:
        print(word)
    print()
    
print_set("Invalid", invalid_vocab)
print_set("Known", known_vocab)
print_set("Target", target_vocab)
