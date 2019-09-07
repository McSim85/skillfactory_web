import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указываюзая на способ соединения с базой
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = "user"
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():
    """
    Устанавливает соединение с базой данных, создает таблицы, если их еще нет и возвращает обьект сессии
    """
    # создаем соединение с базой данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессий
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # запрашиваем данные
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    email = input("Адрес электронной почты: ")
    gender = input("Пол (Male/Female): ")
    birthdate = input("Дата рождения (YYYY-MM-DD): ")
    height = float(input("Рост (м): "))

    # создаем нового пользователя
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        birthdate=birthdate,
        height=height,
    )
    # возвращаем созданного пользователя
    return user


def main():
    """
    Осуществляет взаимодействие с пользователем и обрабатывает пользовательский ввод
    """
    session = connect_db()
    # запрашиваем данные пользователя
    user = request_data()
    # добавляем нового пользователя в сессию
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")

if __name__ == "__main__":
    main()

