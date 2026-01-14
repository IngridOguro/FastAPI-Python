from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []
class Item(BaseModel):
    text: str = None
    is_done: bool = False

# POST
@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return items

# GET ALL ITEMS
@app.get("/items")
def get_all():
    return items

# GET ITEM BY ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id:int) -> list[Item]:
    if item_id < len(items):
        items.pop(item_id)
        return items
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

#UPDATE
@app.put("/items/{item_id}")
def change_status(item_id:int):
    if item_id < len(items):
        items[item_id].is_done = True
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    