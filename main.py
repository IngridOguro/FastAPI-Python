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

# GET ITEM BY ID
@app.get("/items/{item_id}")
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
