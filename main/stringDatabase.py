# TODO: create yield function take a string as its input and returns each word between each invoke
from itertools import *
from functools import reduce


def get_words(message):
    words = message.split(" ")
    for word in words:
        yield word


def get_combination(message):
    return reduce(lambda i, w: i + w, [[i for i in permutations(get_words(message), j)] for j in range(1, len(message.split(" ")))])
