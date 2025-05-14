from pathlib import Path
from itertools import tee

from collections.abc import Iterator


def diy_line_reader(path):
    # TODO: Incomplete !!!
    with path.open() as fp:
        while True:
            buffer = fp.read()

            if buffer:
                lines = buffer.split("\n")

                yield from lines
            else:
                break


def list_reader(path):
    with path.open() as fp:
        print("I am in function")
        return [line for line in fp]


def list_reader(path):
    with path.open() as fp:
        print("I am in function")
        return [line for line in fp]


def gen_reader1(path):
    with path.open() as fp:
        for line in fp:
            print("I am in function")
            yield line


def gen_reader2(path) -> Iterator[str]:
    with path.open() as fp:
        yield from fp


def gen_block_reader(path, block_target_size: int = 100) -> Iterator[list[str]]:
    block = []
    with path.open() as fp:
        for line in fp:
            print("I am in function")

            block.append(line)

            if len(block) == block_target_size:
                yield block

                block = []

        yield block


def my_enumerator(generator):
    i = 0

    for e in generator:
        yield i, e
        i += 1


if __name__ == "__main__":

    it1 = list_reader(Path("data/output/passenger.m.sorted.jsonl/0.jsonl"))

    print("Output of list iteration")

    for i, e in enumerate(it1):
        print("I am in Main")

        if i > 5:
            break

    it2 = gen_reader1(Path("data/output/passenger.m.sorted.jsonl/0.jsonl"))

    r_one, r_two = tee(it2, 2)

    print("Output of generator iteration")
    for i, e in my_enumerator(r_one):
        print("I am in Main")

        if i > 5:
            break
