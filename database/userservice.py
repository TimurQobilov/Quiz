from database import get_db
from database.models import *

# функция добавления юзера
def add_user_db(name, phone_number):
    # создаем сессию (первый вариант, устаревший)
    db = next(get_db())
    # создать объект нового пользователя
    new_user = User(username=name, phone_number=phone_number)
    # добавляем объект в бд
    db.add(new_user)
    # сохраняем изменения
    db.commit()
    return True
# получение всех юзеров
def get_all_user_db():
    # второй вариант создания сессии (актуальный)
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users
# получение информации об конкретном юзере
def get_exact_user_db(id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=id).one()
        # если мы смогли поместить информацию в переменную
        if exact_user:
            # мы передаем её
            return exact_user
        return "Юзер не найден"
# функция сохранения ответа
def user_answer_db(user_id, q_id, level, user_answer=0):
    with next(get_db()) as db:
        exact_question = db.query(Question).filter_by(id=q_id).one()
        if exact_question.correct_answer == user_answer:
            new_answer = UserAnswer(user_id=user_id, question_id=q_id,
                                    user_answer=user_answer, correctness=True,
                                    level=level)
            db.add(new_answer)
            db.commit()
            user_rating = db.query(Rating).filter_by(user_id=user_id, level=level).filter_by().one()
            if user_rating:
                user_rating.correct_answers += 1
                db.commit()
            elif not user_rating:
                new_rating = Rating(user_id=user_id, level=level,
                                    correct_answers=1)
                db.add(new_rating)
                db.commit()
            return True
        else:
            new_answer = UserAnswer(user_id=user_id, question_id=q_id,
                                    user_answer=user_answer, correctness=False,
                                    level=level)
            db.add(new_answer)
            db.commit()
            return False