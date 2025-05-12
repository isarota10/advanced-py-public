from dataclasses import dataclass, field
from enum import Enum, auto

from rich.console import Console
from rich.table import Table

## pydantic
## spacy -> NLP


class Status(str, Enum):
    TODO = "todo"
    COMPLETED = "completed"
    SNOOZED = "snoozed"
    CANCELED = "canceled"

    def priority(self) -> int:
        if self == Status.TODO:
            return 4
        elif self == Status.COMPLETED:
            return 0
        else:
            return 3
        

@dataclass
class Task:
    name: str
    priority: int
    notes: list[str] = field(default_factory=list)
    status: Status = Status.TODO
    assignee: str = None

    def add_note(self, note: str):
        self.notes.append(note)

    def cancel(self):
        self.status = Status.CANCELED


class Workbench:
    def __init__(self):
        self.tasks = []
        self._console = Console()

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_done(self):
        self.tasks = [t for t in self.tasks if t.status != Status.COMPLETED]

    def show(self, high_priority_first: bool = False):
        table = Table(title="Getting Things Done")

        table.add_column("Name")
        table.add_column("Priority")
        table.add_column("Status")
        table.add_column("Notes", no_wrap=False)

        if not high_priority_first:
            for t in self.tasks:
                table.add_row(t.name, str(t.priority), t.status, ", ".join(t.notes))
        else:
            for t in sorted(self.tasks, key=lambda t: t.status, reverse=True):
                table.add_row(t.name, str(t.priority), str(t.status), ", ".join(t.notes))

        self._console.print(table)


if __name__ == "__main__":
    t1 = Task("Buy some stuff from TEMU", 2)
    t2 = Task("Cleanup home", 1)
    t3 = Task("Get prepared for BBVA training", 1)

    t3.add_note("Dont't forget precommit hooks")
    t3.add_note("Ruff and uv section for tooling")

    w = Workbench()
    w.add_task(t2)
    w.add_task(t3)
    w.add_task(t1)

    w.show()

    t1.cancel()

    w.show(True)
