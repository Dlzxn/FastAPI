from fastapi import APIRouter
from starlette.requests import Request
from fastapi.responses import FileResponse
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

from admin.token import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, User, Token
from models.db import insert_project, insert_post

admin_rout = APIRouter(prefix="/admin", tags=["admin"])

@admin_rout.get("/")
async def admin_panel():
    return FileResponse("templates/registration.html")
#
# @admin_rout.post("/registration")
# async def registration():
#     return {"message": "Registration successful"}


@admin_rout.post("/registration", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print("[INDO] FORM:", form_data.username,form_data.password)
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        print("PAISE in str: 28 module adm_rout")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    print(f"[INFO] TOKEN READY: {access_token}")
    return {"access_token": access_token, "token_type": "bearer"}

class ProjectCreate(BaseModel):
    title: str
    description: str
    link: str
    download: str

class NewsCreate(BaseModel):
    title: str
    description: str
    link: str

@admin_rout.get("/adm_panel")
async def admin_panel(request: Request):
    print("[INDO] ADM PANEL")
    token = request.query_params.get("token")
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing")

    try:
        user_k = get_current_user(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    return FileResponse("templates/admin_panel.html")

@admin_rout.post("/projects")
async def add_project(
    project: ProjectCreate,
    current_user: User = Depends(get_current_user)  # Проверка авторизации
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    project_data = project.dict()
    insert_project(project_data["title"], project_data["description"], project_data["link"], project_data["download"])
    return {"message": "Project added successfully", "data": project_data}

@admin_rout.post("/news")
async def add_news(
    project: NewsCreate,
    current_user: User = Depends(get_current_user)  # Проверка авторизации
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    project_data = project.dict()
    print(f"[INDO] ADM PROJECT {project_data}")
    insert_post(project_data["title"],  project_data["link"], project_data["description"])
    return {"message": "Project added successfully", "data": project_data}

