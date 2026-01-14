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
def get_item_or_404(item_id: int):
    try:
        return items[item_id]
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found"
        )

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int) -> Item:
    return get_item_or_404(item_id)

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id:int) -> list[Item]:
    items.remove(get_item_or_404(item_id))
    return items


#UPDATE
@app.put("/items/{item_id}")
def change_status(item_id:int):
    item = get_item_or_404(item_id)
    item.is_done = True
    return item
    