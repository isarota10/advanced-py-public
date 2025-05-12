from rich.console import Console
from rich.table import Table
import json


def tablify(fn):
    def wrapper(*args, **kwargs):
        table = Table()

        first_row, *tail = fn(*args, **kwargs)

        for k in first_row:
            table.add_column(k)

        table.add_row(*[str(v) for _, v in first_row.items()])

        for row in tail:
            table.add_row(*[str(v) for _, v in row.items()])

        return table

    return wrapper


def csvify(fn):
    def wrapper(*args, **kwargs):
        lines = []
        first_row, *tail = fn(*args, **kwargs)

        lines.append(",".join([k for k in first_row]))

        lines.append(",".join([str(v) for _, v in first_row.items()]))

        for row in tail:
            lines.append(",".join([str(v) for _, v in row.items()]))

        return "\n".join(lines)

    return wrapper


def jsonify(fn):
    def wrapper(*args, **kwargs):
        lines = []

        for record in fn(*args, **kwargs):
            lines.append(json.dumps(record))

        return "\n".join(lines)

    return wrapper


def storage_size(fn):
    def wrapper(*arg, **kwargs):
        result = fn(*arg, **kwargs)

        print(f"Amout of storage u need {len(result)}")

        return result

    return wrapper


@storage_size
@jsonify
def get_data():
    return [
        {"name": "Alice", "seat": "12A", "status": "checked-in", "baggage": 2},
        {"name": "Bob", "seat": "14F", "status": "boarding", "baggage": 1},
        {"name": "Charlie", "seat": "15B", "status": "not-checked-in", "baggage": 0},
        {"name": "Dana", "seat": "16C", "status": "checked-in", "baggage": 1},
    ]


if __name__ == "__main__":
    console = Console()

    console.print(get_data())
