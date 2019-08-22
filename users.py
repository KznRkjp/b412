import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



DB_PATH = "sqlite:///sochi_athletes.sqlite3"


Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """
    # указываем имя таблицы
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("А теперь пол: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    bdate = input("Дата рождения (дд.мм.гг):")
    height = input("Длина туловища (в метрах):")
    # генерируем идентификатор пользователя и сохраняем его строковое представление

    # создаем нового пользователя
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender = gender.capitalize(),
        email = email,
        birthdate = datetime.strptime(bdate, "%d.%m.%y"),
        height = height,
    )
    # возвращаем созданного пользователя
    return user



def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()

    # запрашиваем данные пользоватлея
    user = request_data()
    # добавляем нового пользователя в сессию
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")

if __name__ == "__main__":
    main()
