from db import engine, metadata

# Создание таблиц
def init_db():
    metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
