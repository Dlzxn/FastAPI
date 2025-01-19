from sqlalchemy import Table, Column, Integer, String
from db import metadata

# Пример модели
users = Table(
    "news",
    metadata,
    Column("title", String),
    Column("link", String, unique=True, nullable=False),
    Column("descriptions", String, nullable=True),
)
