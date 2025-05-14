from fastapi import FastAPI, HTTPException, status

from service.model.data import Item, Category
from service.model.data import (
    get_all_items,
    get_item,
    search_items,
    store_item,
    update_item,
)
from service.model.exception import ItemNotFound, DataAccessError, DuplicateItem


app = FastAPI()


@app.get("/")
def index() -> dict[str, str]:
    """Main page of my application"""
    return {"Hello": "World"}


@app.get("/items/")
def all_items() -> list[Item]:
    """Fetch all items in inventory"""
    return get_all_items()


@app.get("/item/{item_id}")
def get_item_by_id(item_id: int) -> Item:
    """Fetch a specific Item"""

    try:
        return get_item(item_id)
    except ItemNotFound:
        raise HTTPException(404, detail=f"Item {item_id} not found in inventory")


@app.get("/item/")
def search_item(
    name: str | None = None,
    price: float | None = None,
    amount: int | None = None,
    category: Category | None = None,
) -> dict[int, Item]:
    """Search items with matching attributes

    * You can use any of following fields to filter out
      * **name**: Name of the item
      * price: _cost_ parameter of item

    """

    try:
        items = search_items(name, price, amount, category)

        return items
    except DataAccessError:
        raise HTTPException(403, detail="API access violation")


@app.post("/item/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> Item:
    try:
        store_item(item)

        return item
    except DuplicateItem:
        raise HTTPException(400, detail=f"Item {item.id} already exists")


@app.put("/item/{item_id}", status_code=status.HTTP_201_CREATED)
def update_item_by_id(item_id: int, item: Item) -> Item:
    try:
        update_item(item_id, item)

        return item
    except ItemNotFound:
        raise HTTPException(404, detail=f"Item {item_id} not found in inventory")
