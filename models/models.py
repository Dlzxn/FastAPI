from pydantic import BaseModel

class Project(BaseModel):
    id: int

class SuperUser(BaseModel):
    name: str
    password: str