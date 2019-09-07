import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

class Athelete(Base):
    """
    Описывает структуру таблицы athelete для хранения данных атлетов
    """
    __tablename__ = "athelete"

    id = sa.Column(sa.Integer, primary_key=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)

class User(Base):
    """
    Описывает структуру таблицы user для хранения данных пользователей
    """
    __tablename__ = "user"

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
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def find(user_id, session):
    """
    Производит поиск пользователя в таблице user по заданному user_id и 
    выводит на экран имена двух атлетов: ближайшего по дате рождения к
    данному пользователю и ближайшего по росту
    """
    # находим запись в таблице User, у которой поле User.id совпадает с параметром user_id
    user_check = session.query(User).get(user_id)
    if user_check is not None:
    
        user_bd_str = session.query(User).get(user_id).birthdate
        user_bd = datetime.date.fromisoformat(user_bd_str)  # конвертируем дату рождения пользователя в date
        user_height = float(session.query(User).get(user_id).height)   # float

        # строим два словаря с разностями роста и двты рождения
        ht_diff = {}    # dict athlet_id: height_difference
        bd_diff = {}    # dict athlet_id: birhdate_difference in timedelta
            
        for atlet in session.query(Athelete).all():
            if atlet.height is None:    # в базе есть атлеты с пустым полем height
                atlet.height = '0'
            ht_diff[atlet.id] = abs(float(atlet.height) - user_height)
            atlet_bd = datetime.date.fromisoformat(atlet.birthdate)
            bd_diff[atlet.id] = abs(atlet_bd - user_bd)
            
        # находим минимальные значения в словарях
        closest_height_id = min(ht_diff, key=ht_diff.get) # вариант min(ht_diff, key=lambda k: ht_diff[k])
        closest_birthdate_id = min(bd_diff, key=bd_diff.get)
            
        print("Ближайший по росту к пользователю атлет - "
            f"{session.query(Athelete).get(closest_height_id).name}"
            ", его рост - "
            f"{session.query(Athelete).get(closest_height_id).height}"
            " метра. Рост пользователя - "
            f"{session.query(User).get(user_id).height} метра.")
            
        print("Ближайший по дате рождения к пользователю атлет -",
            f"{session.query(Athelete).get(closest_birthdate_id).name}"
            ", дата рождения - "
            f"{session.query(Athelete).get(closest_birthdate_id).birthdate}"
            ". Дата рождения пользователя - "
            f"{session.query(User).get(user_id).birthdate}.")

    else:
        print("Пользователей с таким id нет.")

def main():
    """
    Осуществляет взаимодействие с пользователем и обрабатывает пользовательский ввод
    """
    session = connect_db()
    user_id = int(input("Введите id пользователя для поиска: "))
    
    # вызываем функцию поиска по id пользователя
    find(user_id, session)
    
    
if __name__ == "__main__":
    main()
