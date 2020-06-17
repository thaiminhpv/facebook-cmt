# TODO: create yield function take a string as its input and returns each word between each invoke


def getWords(message):
    words = message.split(" ")
    for word in words:
        yield word


def test(message):
    words = message.split(" ")
    for word in words:
        yield word
