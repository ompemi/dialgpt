from fastapi import FastAPI
from main import server

app = FastAPI()

@app.post("/")
async def vocode_proxy(request: dict):
    return await server.app.post("/")(request)