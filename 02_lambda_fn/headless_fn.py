from rich.console import Console

from typing import Any

from collections.abc import Iterable, Callable

console = Console()

passengers = [
    {"name": "Alice", "seat": "12A", "status": "checked-in", "baggage": 2},
    {"name": "Bob", "seat": "14F", "status": "boarding", "baggage": 1},
    {"name": "Charlie", "seat": "15B", "status": "not-checked-in", "baggage": 0},
    {"name": "Dana", "seat": "16C", "status": "checked-in", "baggage": 1},
]


def ticket_label(p: dict) -> str:
    return f"{p['name']} ({p['seat']})"


if __name__ == "__main__":
    console.print("Ticket Labels", [ticket_label(p) for p in passengers])

    ticket_label_fn = lambda p: f"{p['name']} ({p['seat']})"  # noqa: E731 I am aware that this is no good

    console.print("Ticket Labels", [ticket_label_fn(p) for p in passengers])

    # First use of built-in map

    tickets = list(map(lambda p: f"{p['name']} ({p['seat']})", passengers))

    console.print("Name (Seat) using map", tickets)

    def lmap(fn: Callable, it: Iterable) -> list[Any]:
        return [fn(e) for e in it]

    tickets = lmap(lambda p: f"{p['name']} ({p['seat']})", passengers)

    console.print("Name (Seat) using lmap", tickets)

    only_carry_on = list(filter(lambda p: p["baggage"] == 0, passengers))

    console.print("Filter only carry on (using built-in)", only_carry_on)

    def lfilter(fn: Callable, it: Iterable) -> list:
        return [e for e in it if fn(e)]

    only_carry_on = lfilter(lambda p: p["baggage"] == 0, passengers)

    console.print("Filter only carry on (using lfilter)", only_carry_on)

    def lsuper(map_fn: Callable, filter_fn: Callable, it: Iterable) -> list:
        return [map_fn(e) for e in it if filter_fn(e)]

    only_carry_on = lsuper(
        lambda p: f"{p['name']} ({p['seat']})", lambda p: p["baggage"] == 0, passengers
    )

    console.print("Format only_carry_on (using Super Mapper)", only_carry_on)

    # Top problems for TGS
    console.print("Many baggages", sorted(passengers, key=lambda p: p["baggage"],reverse=True))

    # Sort by seat
    console.print("Seat ordered", sorted(passengers, key=lambda p: p["seat"]))

    # Boarding status and name
    console.print("Seat ordered", sorted(passengers, key=lambda p: (p["status"], p["name"])))
