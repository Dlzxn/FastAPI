from fastapi import APIRouter

from models.db import insert_project, insert_post, read_project, read_posts

api = APIRouter(prefix="/api")


@api.get("/news")
async def news():
    news_data = read_posts()
    return news_data

@api.get("/projects")
async def projects():
    projects_all = read_project()
    return projects_all