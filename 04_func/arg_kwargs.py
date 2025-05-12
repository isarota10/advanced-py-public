from rich.console import Console
from enum import Enum, auto


class ClientType(Enum):
    CORPORATE = auto()
    NON_PROFIT = auto()
    INTERNATIONAL = auto()
    OTHER = auto()


class InvoiceFormatter:
    def __init__(self, client_type: ClientType):
        self.client_type = client_type
        self._console = Console()

    def print(self, amount, **kwargs):
        # TODO: Check kwargs sanity

        if any([k not in ["color","italic"] for k in kwargs]):
            self._console.print(f"[red]WARNING:[/red] Unknown parameters in optional parameters: {kwargs}")

        # color = kwargs["color"]
        color = kwargs.get("color", "black")
        is_italic = kwargs.get("italic", False)

        match self.client_type:
            case ClientType.CORPORATE:
                tax = 0.2
                footer = "Thanks for your business :briefcase:"
            case ClientType.NON_PROFIT:
                tax = 0.0
                footer = "Thanks for your support :pray:"
            case ClientType.INTERNATIONAL:
                tax = 0.15
                footer = "Subject to international tax fees :airplane:"
            case _:
                tax = 0.18
                footer = "Standard terms applied."

        total = f"${amount * (1 + tax)}"

        if is_italic:
            header = "[i]Total[/i]"
        else:
            header = "Total"

        header = f"[{color}]{header}[/{color}]"

        self._console.print(header, total)
        self._console.print(footer)


if __name__ == "__main__":
    formatter = InvoiceFormatter(ClientType.INTERNATIONAL)

    formatter.print(10_000)
    formatter.print(10_000, color="blue", italic=True, have_you_seen_this_movie="dune")
    formatter.print(10_000, color="red")
    formatter.print(10_000, italic=True)
