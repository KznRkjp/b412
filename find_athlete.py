import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
import users
#
#
Base = declarative_base()
#
class Athlete(Base):
    """
    Описывает структуру таблицы athelete
    """
    # указываем имя таблицы
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.FLOAT)
    country = sa.Column(sa.FLOAT)




def find(id, session):
    """
    Производит поиск пользователя в таблице user по заданному имени name
    """
    # находим все записи в таблице User, у которых поле User.id совпадает с параметром id
    query = session.query(users.User).filter(users.User.id == id)
    # подсчитываем количество таких записей в таблице с помощью метода .count()
    if query.count() == 1:

    # составляем список идентификаторов всех найденных пользователей
        user = query.first()
        return user.birthdate, user.height
    else:
        print("пользователя с таким Id не найдено")
        return -1, -1


def find_athlete_height(height,session):
    for i in range(20000):

        query = session.query(Athlete).filter(Athlete.height == height + i*0.01)
        if query.count() > 0:
            athelete = query.first()
            print("Ближайшее совпадение по росту (",i,"см.):")
            print (athelete.name,", рост:", athelete.height)
            break
        else:
            query = session.query(Athlete).filter(Athlete.height == height-i*0.01)
            if query.count() > 0:
                athelete = query.first()
                print("Ближайшее совпадение по росту (",i,"см.):")
                print (athelete.name,", рост:", athelete.height)
                break


def find_athlete_db(db,session):
    init_date = datetime.strptime(db, "%Y-%m-%d %H:%M:%S")
    for i in range(200000):
        search_date = init_date + timedelta(days=1*i)
        search_str=(str(search_date).split(" ")[0])
        query = session.query(Athlete).filter(Athlete.birthdate == search_str)
        if query.count() > 0:
            athelete = query.first()
            print("Ближайшее совпадение по дате рождения (",i,"дн.):")
            print (athelete.name, ", дата рождения:", athelete.birthdate)
            break
        else:
            search_date = init_date + timedelta(days=-1*i)
            search_str=(str(search_date).split(" ")[0])
            query = session.query(Athlete).filter(Athlete.birthdate == search_str)
            if query.count() > 0:
                athelete = query.first()
                print("Ближайшее совпадение по дате рождения, (",i,"дн.):")
                print (athelete.name, ", дата рождения:", athelete.birthdate)
                break


def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = users.connect_db()
    id = input("Введи id пользователя для поиска (1,2,..,201..,1003): ")
    user_db, user_height = find(id, session)
    if user_db != -1 and user_height != -1:
        find_athlete_height(user_height, session)
        find_athlete_db(user_db, session)


if __name__ == "__main__":
    main()
