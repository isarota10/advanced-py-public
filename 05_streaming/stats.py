from random import randint

from rich.console import Console
from collections.abc import Iterator
from collections import defaultdict

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
    fn_gen: list[callable], stats_per_n: int = 10_0000
) -> Iterator[tuple[float, float, int]]:
    total = defaultdict(int)
    total2 = defaultdict(int)
    counter = defaultdict(int)

    while True:
        segment = randint(0,1)
        x = fn_gen[segment]()

        total[segment] += x
        total2[segment] += x**2

        counter[segment] += 1

        if (counter[0] + counter[1])  % stats_per_n == 0:
            for i in [0,1]:
                yield i, total[i] / counter[i], total2[i] / counter[i] - (total[i] / counter[i]) ** 2, counter[i]

if __name__ == "__main__":
    #v = get_batch_data(100_000)

    console = Console()

    #console.print(f"Mean", mean(v), "Variance", variance(v))

    for segment, m, v, count in streaming_stats([lambda: randint(3, 6),lambda: randint(4, 8)], stats_per_n=1_000_000):
        console.print("Customer Segment", segment,"Mean", m, "Variance", v, "at", count, "elements")
