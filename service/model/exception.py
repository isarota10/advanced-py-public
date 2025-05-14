class ItemNotFound(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id
        self.resolve = "Please try with an item id that is available in inventory. Try /items first if you have permission"
        super().__init__(f"Item {self.item_id} not found in inventory")


class DataAccessError(Exception):
    def __init__(self, *args):
        super().__init__("Unauthorized API access")


class DuplicateItem(Exception):
    def __init__(self, item_id):
        self.item_id = item_id
        super().__init__(f"Duplicate item with id {item_id}")
