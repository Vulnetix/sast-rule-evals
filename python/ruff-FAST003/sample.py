from fastapi import FastAPI

app = FastAPI()


@app.get("/things/{thing_id}")
async def read_thing(query: str): ...

