from sqlalchemy import Table, Column, Integer, String
from db import metadata

# Пример модели
users = Table(
    "projects",
    metadata,
Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String, nullable=False),
    Column("link", String, nullable=False),
    Column("download", String, nullable=False),
)
