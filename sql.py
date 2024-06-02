from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    passport = Column("Passport", String, primary_key=True)
    photo = Column("photo", String)
    firstname = Column("firstname", String)
    name = Column("name", String)
    gender = Column("gender", CHAR)
    phone_number = Column("phone_number", String)
    date_of_birthday = Column("Day of birthday", DateTime)
    notes = Column("Notes", String)
    age = Column("age", Integer)

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.date_of_birth.year
        return age

    def __init__(self, passport, photo, firstname, lastname, gender, phone_number, day_of_birthday, notes):
        self.passport = passport
        self.photo = photo
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birthday = day_of_birthday
        self.notes = notes

    def __repr__(self):
        age = self.calculate_age()
        return f"({self.passport} {self.photo} {self.firstname} {self.lastname} {self.gender} {self.phone_number} {self.day_of_birthday} {self.notes})"


engine = create_engine("sqlite:///C:/projects/PersonDB/Users.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#person = Person("AB1232", "C:\\Users\\path", "Alen", "Wolf", "M", "+375298068085",
                #datetime(1986, 1, 1), "Był zauważen w okolicach")
#session.add(person)
session.commit()
