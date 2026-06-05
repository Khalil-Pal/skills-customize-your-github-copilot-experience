from fastapi import FastAPI, HTTPException, Depends, Header
from typing import List, Optional
from .models import Item, ItemCreate, ItemUpdate
from .store import get_store

app = FastAPI(title="FastAPI REST API Assignment")

store = get_store()


def require_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    return store.create_item(item)


@app.get("/items/", response_model=List[Item])
def list_items():
    return store.list_items()


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = store.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    updated = store.update_item(item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, api_key: None = Depends(require_api_key)):
    deleted = store.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
