from random import randint

from rich.console import Console
from collections.abc import Iterator
from math import sqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for d in range(2, int(sqrt(n))):
            if n % d == 0:
                return False

        return True


def prime_generator():
    before, now = 2, 3

    # yield before, now

    while True:
        if is_prime(now):
            yield before, now

            before = now

        now += 2



def mean(x: list[int]) -> float:
    total = sum(x)

    return total / len(x)


def variance(x: list[int]) -> float:
    n = len(x)
    ex2 = sum((e**2 for e in x)) / n

    return ex2 - mean(x) ** 2


def get_batch_data(n: int) -> list[int]:
    return [randint(3, 6) for _ in range(n)]


def streaming_stats(
    stream: Iterator[float], stats_per_n: int = 10_0000
) -> Iterator[tuple[float, float, int]]:
    total = 0.0
    total2 = 0.0
    counter = 0

    for x in stream:
        total += x
        total2 += x**2

        counter += 1

        if counter % stats_per_n == 0:
            yield (
                total / counter,
                total2 / counter - (total / counter) ** 2,
                counter,
            )


if __name__ == "__main__":
    # v = get_batch_data(100_000)

    console = Console()

    # console.print(f"Mean", mean(v), "Variance", variance(v))


    if False:
        for ratio, now, before in (
            (now / before, now, before) for before, now in prime_generator()
        ):
            console.print(f"Current", now, "Previous", before, "Ration", ratio)

    for m, v, count in streaming_stats(
        (now / before for before, now in prime_generator()), stats_per_n=1000
    ):
        console.print(f"Mean", m, "Variance", v)
