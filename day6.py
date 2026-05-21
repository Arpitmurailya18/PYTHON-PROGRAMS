from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/fast")
async def faster():
    return "hello"

@app.get("/slow")
async def slower():
    await asyncio.sleep(5)
    return "hello"