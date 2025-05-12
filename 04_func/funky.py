def build_chain(fns: list[callable]) -> callable:
    def inner(input):
        first_fn, *tail = fns

        output = first_fn(input)

        for fn in tail:
            output = fn(output)

        return output

    return inner


def x2(x: float) -> float:
    return 2 * x


def add1(x: float) -> float:
    return x + 1


if __name__ == "__main__":
    chain = build_chain([x2, add1, add1])

    y = add1(x2(5))
    y = chain(5)

    print(f"2x5 + 1 = {y}")
