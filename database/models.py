from database import Base
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

#модель юзера
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    phone_number = Column(String(20), nullable=True)
    reg_date = Column(DateTime, default=datetime.now())

#модели вопросов
class Question():
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_question = Column(String(200), nullable=False)
    v1 = Column(String(200), nullable=False)
    v2 = Column(String(200), nullable=False)
    v3 = Column(String(200), nullable=True)
    v4 = Column(String(200), nullable=True)
    correct_answer = Column(Integer)
    level = Column(String(200), default='Beginner')
    timer = Column(Integer, default=45)

#ответ юзера
class UserAnswer():
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    user_answer = Column(Integer, nullable=True)
    correctness = Column(Boolean, nullable=False)
    level = Column(String)
    #создания связи
    user_fk = relationship(User, lazy='subquery')
    question_fk = relationship(Question, lazy='subquery')


#рейтинг юзера
class Rating():
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    correct_answer = Column(Integer)
    level = Column(String)




