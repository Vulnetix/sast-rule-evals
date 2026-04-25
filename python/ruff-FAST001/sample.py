# Sample for Ruff rule FAST001: fast-api-redundant-response-model
# This file is designed to trigger the FAST001 rule.
# Run: ruff check --select FAST001 <this_file>

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return item
