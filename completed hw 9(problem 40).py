import functools    # долго считает зато в одну строку!
print('Project Euler problem 40 solution:', functools.reduce(lambda a, b: a * b,
[int(functools.reduce(lambda a, b: str(a) + str(b), [x for x in range(1, 200000)], '')[10 ** a - 1]) for a in range(7)]))

