from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from models.models import Project
from models.db import insert_project, insert_post, read_project, read_posts

templates = Jinja2Templates(directory="templates")

project = APIRouter(prefix="/projects")

@project.get("/{id}")
async def get_project(request: Request, id: int):
    print(id)
    projects_all = read_project()
    project_html = next((p for p in projects_all if p["id"] == id), None)
    if not project_html:
        raise HTTPException(status_code=404, detail="Project not found")
    return templates.TemplateResponse("project.html", {"request": request, "project": project_html})

