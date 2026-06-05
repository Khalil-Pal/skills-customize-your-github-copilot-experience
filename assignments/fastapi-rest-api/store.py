from typing import Dict, List, Optional
from .models import Item, ItemCreate, ItemUpdate


class Store:
    def __init__(self):
        self._items: Dict[int, Item] = {}
        self._next = 1

    def create_item(self, data: ItemCreate) -> Item:
        item = Item(id=self._next, **data.dict())
        self._items[self._next] = item
        self._next += 1
        return item

    def list_items(self) -> List[Item]:
        return list(self._items.values())

    def get_item(self, item_id: int) -> Optional[Item]:
        return self._items.get(item_id)

    def update_item(self, item_id: int, data: ItemUpdate) -> Optional[Item]:
        item = self._items.get(item_id)
        if not item:
            return None
        updated = item.dict()
        for k, v in data.dict(exclude_unset=True).items():
            updated[k] = v
        item = Item(**updated)
        self._items[item_id] = item
        return item

    def delete_item(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None


_store = Store()


def get_store() -> Store:
    return _store
