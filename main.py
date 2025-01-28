from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import admin
from API import api
from projects import project
from admin import adm_rout


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="main.ico")
app.include_router(api.api)
app.include_router(project.project)
app.include_router(adm_rout.admin_rout)

@app.get("/")
async def main():
    return FileResponse("templates/main.html")

@app.get("/image/github.png")
async def github():
    return FileResponse("image/github.png")

@app.get("/image/telegram.png")
async def telegram():
    return FileResponse("image/telegram.png")