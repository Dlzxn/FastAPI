from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI()


@app.get("/")
async def main():
    return FileResponse("base.html")