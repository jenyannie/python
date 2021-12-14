import random
def random_line(f):
    lines = open(f).read().splitlines()
    return random.choice(lines)
print(random_line("c:/jeny/python/lab3/q15/test.txt"))