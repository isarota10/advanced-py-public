from rich.console import Console

console = Console()
passengers = [
    {"name": "Alice", "seat": "12A", "status": "checked-in", "baggage": 2},
    {"name": "Bob", "seat": "14F", "status": "boarding", "baggage": 1},
    {"name": "Charlie", "seat": "15B", "status": "not-checked-in", "baggage": 0},
    {"name": "Dana", "seat": "16C", "status": "checked-in", "baggage": 1},
]

if __name__ == "__main__":
    console.print("All passengers")

    console.print(passengers)

    # checked_in = []

    # for p in passengers:
    #     if p["status"] == "checked-in":
    #         checked_in.append(p)

    console.print("Checked-in", [p for p in passengers if p["status"] == "checked-in"])

    console.print(
        "Boarded (Seat Number)",
        [p["seat"] for p in passengers if p["status"] == "boarding"],
    )

    console.print(
        "Dict(Username -> Baggage Count)", {p["name"]: p["baggage"] for p in passengers}
    )

    console.print(
        "Dict(Username -> Status)",
        {p["name"]: p["status"] for p in passengers if p["baggage"] > 1},
    )
