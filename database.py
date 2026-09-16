from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


from sqlalchemy import text

def check_db_health():
    """Проверяет соединение с БД. Возвращает True, если всё ок, иначе False."""
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
    finally:
        db.close()

# ВАЖНО: Укажи правильное имя файла твоей базы данных!
# Если в DBeaver подключение называется "bd ver1", то сам файл, скорее всего, называется "bd ver1.db" или "bd_ver1.db".
# Проверь в проводнике Windows, как точно называется файл, и вставь его имя сюда.
# Если файл лежит не в папке проекта, укажи полный путь (но лучше скопируй его в папку проекта).
SQLALCHEMY_DATABASE_URL = "sqlite:///./music_store.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
