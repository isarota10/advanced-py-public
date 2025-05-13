from collections.abc import Iterator, Iterable
from random import choice, randint
from typing import Literal
import gzip
import json
from pathlib import Path
from itertools import tee, islice


def synetic_passengers(n: int = 1_000_000) -> Iterator[dict]:
    for i in range(n):
        yield dict(
            status=choice(["cheked-in", "boarding", "not-checked-in"]),
            baggage=choice([0, 1, 2]),
            trip_id=f"UFCG-{i}",
        )


"""
Partitioning strategies
 - Random       --> Input ? i n
 - Round robin  --> Input ? i n
 - By a key     --> Input ? which column i  n 
"""


class Random:
    def __init__(self):
        pass

    def __call__(self, i: int, data: dict, n: int) -> int:
        return randint(0, n - 1)


class RoundRobin:
    def __init__(self):
        pass

    def __call__(self, i: int, data: dict, n: int) -> int:
        return i % n


class KeyBased:
    def __init__(self, *keys):
        self.keys = keys

    def __call__(self, i: int, data: dict, n: int) -> int:
        value = tuple([data[k] for k in self.keys])

        return hash(value) % n


class partitioned:
    def __init__(self, n: int = 8, strategy=Random()):
        self.partition_count = n
        self.partitioner = strategy

    def __call__(self, fn_writer):
        def wrapper(
            path_like: Path | str,
            data: Iterable[dict],
            *,
            batch_size: int | None = None,
            sort_key: tuple[str] | None = None,
            compression: CompressionType | None = None,
        ):
            total_bytes, n_io_request = 0, 0

            partitions = [[] for _ in range(self.partition_count)]

            for i, e in enumerate(data):
                partitions[self.partitioner(i, e, self.partition_count)].append(e)

            if isinstance(path_like, str):
                directory = Path(path_like)
            else:
                directory = path_like

            directory.mkdir(exist_ok=False, parents=True)

            for i in range(self.partition_count):
                part_bytes, part_io_request = fn_writer(
                    directory / f"{i}.jsonl",
                    partitions[i],
                    batch_size=batch_size,
                    sort_key=sort_key,
                    compression=compression,
                )
                total_bytes += part_bytes
                n_io_request += part_io_request

            with (directory / "SUCCESS").open("w") as wp:
                print("Done", file=wp)

            return total_bytes, n_io_request

        return wrapper


CompressionType = Literal["gzip", "zstd", "snappy", "bz2"]


# @partitioned(n=4, strategy=KeyBased("baggage","status"))
# @partitioned(n=4, strategy=Random())
@partitioned(n=4, strategy=KeyBased("trip_id"))
def clever_write(
    path_like: Path | str,
    data: Iterable[dict],
    *,
    batch_size: int | None = None,
    sort_key: tuple[str] | None = None,
    compression: CompressionType | None = None,
) -> tuple[int, int]:
    def smart_open(path: Path, compression: CompressionType):
        if compression == "gzip":
            return gzip.open(path, "wb",compresslevel=4)
        else:
            return path.open("wb")

    total_bytes, n_io_request = 0, 0
    if isinstance(path_like, str):
        path = Path(path_like)
    else:
        path = path_like

    if sort_key:
        processed = sorted(data, key=lambda e: tuple((e[k] for k in sort_key)))
    else:
        processed = data

    with smart_open(path, compression) as wp:
        if batch_size:
            batch = []
            for d in processed:
                line = json.dumps(d)

                batch.append(line)
                total_bytes += len(line)

                if len(batch) == batch_size:
                    #print("\n".join(batch), file=wp)
                    wp.write("\n".join(batch).encode())
                    n_io_request += 1
                    batch = []

            if len(batch) > 0:
                wp.write("\n".join(batch).encode())
                n_io_request += 1
        else:
            for d in data:
                line = json.dumps(d)
                wp.write(line.encode())

                total_bytes += len(line)
                n_io_request += 1

    return total_bytes, n_io_request


if __name__ == "__main__":
    """
        - [x] Create a output directory
        - [x] Write a json file
        - [x] Write a json line file
        - [x] Batching
        - [x] Write a segmented/partitioned json line file
        - [x] Random partitioning
        - [x] Key parittioning
        - [x] Write a segment/partitioned sorted json line file
        - [x] Compresssion        
        - [] Memory efficient version of same code
    """

    base_dir = Path("data")

    output_dir = base_dir / "output"

    output_dir.mkdir(parents=True, exist_ok=True)

    data_s = list(synetic_passengers(n=10))

    with (output_dir / "passenger.json").open("w") as wp:
        json.dump(data_s, wp, indent=2)

    data_m = synetic_passengers(n=100_000)

    data_m_1, data_m_2 = tee(data_m)

    # print(f"Total number of records {sum((1 for _ in data_m_1))}")
    # print(f"Total number of records {sum((1 for _ in data_m_2))}")

    # byte_count, n_io_request = clever_write(
    #     output_dir / "passenger.m.jsonl", data_m_1, batch_size=None
    # )

    # print(f"Total of {byte_count} written in {n_io_request} requests")

    # byte_count, n_io_request = clever_write(
    #     output_dir / "passenger.m.jsonl", data_m_2, batch_size=100
    # )

    # print(f"Total of {byte_count} written in {n_io_request} requests")

    byte_count, n_io_request = clever_write(
        output_dir / "passenger.m.jsonl", data_m_1, batch_size=100, compression="gzip"
    )

    print(f"Total of {byte_count} written in {n_io_request} requests")

    byte_count, n_io_request = clever_write(
        output_dir / "passenger.m.sorted.jsonl",
        data_m_2,
        batch_size=100,
        sort_key=("trip_id",),
        compression="gzip",
    )

    print(f"Total of {byte_count} written in {n_io_request} requests")
