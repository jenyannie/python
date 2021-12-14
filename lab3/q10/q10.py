from collections import Counter
def word_count(fname):
   with open(fname) as f:
    return Counter(f.read().split())

print(word_count("c:/jeny/python/lab3/q10/test.txt"))