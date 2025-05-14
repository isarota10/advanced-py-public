from pydantic import BaseModel
from enum import Enum
from service.model.exception import ItemNotFound, DataAccessError, DuplicateItem


class Category(str, Enum):
    """Categories for good available in inventory"""

    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    """Detailed information about our products"""

    id: int
    name: str
    price: float
    amount: int
    category: Category


items = {
    0: Item(name="Hammer", price=9.99, amount=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, amount=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, amount=100, id=2, category=Category.CONSUMABLES),
}


def get_all_items() -> list[Item]:
    return list(items.values())


def get_item(item_id: int) -> Item:
    # walrus operator
    if (item := items.get(item_id)) is None:
        raise ItemNotFound(item_id)

    return item

    # try:
    #     item = items[item_id]

    #     return item
    # except KeyError:
    #     raise ItemNotFound(item_id)


def search_items(
    name: str | None, price: float | None, amount: int | None, category: Category | None
) -> dict[int, Item]:
    # Create an audit log with timestamp, client_ip, token, search conditions...
    def match(it):
        return all(
            (
                name is None or name == it.name,
                price is None or price == it.price,
                amount is None or amount == it.amount,
                category is None or category == it.category,
            )
        )

    if all(
        (
            name is None,
            price is None,
            amount is None,
            category is None,
        )
    ):
        raise DataAccessError()

    return {i: it for i, it in items.items() if match(it)}


def store_item(item: Item):
    if item.id in items:
        raise DuplicateItem(item.id)

    items[item.id] = item


def update_item(item_id: int, item: Item):
    get_item(item_id)

    items[item_id] = item
