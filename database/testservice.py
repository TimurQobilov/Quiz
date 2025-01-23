from database import get_db
from database.models import *

# функция добавления вопроса

def add_question_db(main_question, v1,v2, correct_answer, level,
                    v3=None, v4=None):
    with next(get_db()) as db:
        new_question = Question(main_question=main_question,
                                v1=v1, v2=v2, v3=v3, v4=v4,
                                correct_answer=correct_answer,
                                level=level)
        db.add(new_question)
        db.commit()
        return True
# функция получения топ 5 юзеров по баллам
def get_top5_db(level):
    with next(get_db()) as db:
        top5 = db.query(Rating).filter_by(level=level).order_by(Rating.correct_answers.desc()).all()
        return top5[:5]

# функция получения 20 вопросов
def get_20_questions_db(level):
    with next(get_db()) as db:
        questions = db.query(Question).filter_by(level=level).all()
        questions2 = list(set(questions))
        return questions2[:20]