from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#тип и насвания базы
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
#движок базы
engine = create_engine(SQLALCHEMY_DATABASE_URI)
#функция для создания сессий
SessionLocal = sessionmaker(bind=engine)
#суперкласс для моделей
Base = declarative_base()

#функции-генератора сессий
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
