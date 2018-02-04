import brainfuck_generator as bfgen
from tests import brainfuck as bf


def test1():
    text = 'Hello world.'
    assert bf.evaluate(bfgen.string_to_bf(text, False)) == text

def test2():
    text = 'Hello world.'
    assert bf.evaluate(bfgen.string_to_bf(text, True)) == text
