from database import Base
from sqlalchemy import (Column, Integer, String,
                        BigInteger, DateTime, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime

# создаем модель юзеров
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    reg_date = Column(DateTime, default=datetime.now())
# модель вопросов
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_question = Column(String, nullable=False) # на самом деле nullable итак по умолчанию Flase
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)
    correct_answer = Column(Integer)
    level = Column(String, default="Beginner")
    # timer = Column(Integer, default=45)
# создаем модель Ответов юзера
class UserAnswer(Base):
    __tablename__ = "useranswer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(Integer, nullable=True)
    correctness = Column(Boolean, default=False)
    level = Column(String)
    # создание связей
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")
# на дз создать модель Rating (id, user_id, correct_answers, level)
class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    level = Column(String, ForeignKey("questions.level"))
    correct_answers = Column(Integer, default=0)
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")




