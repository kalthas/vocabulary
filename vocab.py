"""
Manages vocabulary
"""

vocab = set()

with open('known_words.txt', 'r') as f:
    for l in f.readlines():
        vocab.add(l.strip())
