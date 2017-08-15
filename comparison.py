import timeit
from functools import reduce

ELEMENTS = [i for i in range(10_000)]


def test_for():
    arr = []
    for e in ELEMENTS:
        arr.append(e ** 2)


def test_while():
    arr = []
    i = 0
    while i < len(ELEMENTS):
        arr.append(ELEMENTS[i] ** 2)
        i += 1


def test_map():
    a = list(map(lambda e: e**2, ELEMENTS))
    return a


def test_filter():
    a = list(filter(lambda x: x > 10, ELEMENTS))
    return a


def test_reduce():
    a = reduce((lambda x, y: x ** 2), ELEMENTS)
    return a


def test_generator():
    tuple(e ** 2 for e in ELEMENTS)


def test_list_generator():
    a = [x**2 for x in ELEMENTS]
    return a


def test_dict_generator():
    a = {x: x**2 for x in ELEMENTS}
    return a


def test_set_generator():
    a = {x**2 for x in ELEMENTS}
    return a

for test_part in (
    'for',
    'for',
    'while',
    'map',
    'filter',
    'reduce',
    'generator',
    'list_generator',
    'dict_generator',
    'set_generator'
):
    print(f'test {test_part:10}', timeit.timeit(f'test_{test_part}()',
                                                f'from __main__ import test_{test_part}', number=100) / 100)