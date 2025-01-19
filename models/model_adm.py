from xmlrpc.client import Boolean

from sqlalchemy import Table, Column, Integer, String
from db import metadata

# Пример модели
users = Table(
    "users",
    metadata,
    Column("username", Integer, primary_key=True),
    Column("hashed_password", String, unique=True, nullable=False),
    Column("is_admin", Boolean, nullable=False),
)

