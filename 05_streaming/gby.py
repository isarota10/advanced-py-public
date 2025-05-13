from collections.abc import Iterable

passengers = [
    {"name": "Alice", "seat": "12A", "status": "checked-in", "baggage": 2},
    {"name": "Bob", "seat": "14F", "status": "boarding", "baggage": 1},
    {"name": "Charlie", "seat": "15B", "status": "not-checked-in", "baggage": 0},
    {"name": "Dana", "seat": "16C", "status": "checked-in", "baggage": 1},
]


def hash_gby(data: Iterable[dict], column: str, metric="count"):
    bucket = {}

    for p in passengers:
        bucket[p[column]] = bucket.get(p[column], 0) + 1

    return bucket


def pipeline_gby(data: Iterable[dict], column: str, metric="count"):
    previous_key = None
    counter = 0

    for p in data:
        key = p[column]

        if previous_key != key and previous_key is not None:
            yield previous_key, counter

            counter = 0
        previous_key = key

        counter += 1

    yield previous_key, counter


if __name__ == "__main__":
    result = hash_gby(passengers, "status", "count")

    print("\nOutput HGBY 1")

    for k, v in result.items():
        print(k, v)

    result = hash_gby(sorted(passengers, key=lambda x: x["status"]), "status", "count")

    print("\nOutput HGBY 2")
    for k, v in result.items():
        print(k, v)

    result = pipeline_gby(sorted(passengers, key=lambda x: x["status"]), "status", "count")

    print("\nOutput PGBY 1")
    for k, v in result:
        print(k, v)
