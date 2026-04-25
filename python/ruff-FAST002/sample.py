# Sample for Ruff rule FAST002: fast-api-non-annotated-dependency
# This file is designed to trigger the FAST002 rule.
# Run: ruff check --select FAST002 <this_file>

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
