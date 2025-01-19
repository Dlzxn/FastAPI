from fastapi import FastAPI
from fastapi.responses import FileResponse

import admin
from API import api
from projects import project
from admin import adm_rout


app = FastAPI()
app.include_router(api.api)
app.include_router(project.project)
app.include_router(adm_rout.admin_rout)

@app.get("/")
async def main():
    return FileResponse("templates/main.html")
