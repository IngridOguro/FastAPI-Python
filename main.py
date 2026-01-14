from fastapi import FastAPI

app = FastAPI()

items = []

# POST
@app.post("/items")
def create_item(item:str):
    items.append(item)
    return items

# GET ITEM BY ID
@app.get("/items/{item_id}")
def get_item(item_id:int) -> str:
    item = items[item_id]
    return item