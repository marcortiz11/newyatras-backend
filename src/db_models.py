from datetime import datetime
from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so

from src import db


class User(db.Model):
    __table_args__ = {'extend_existing': True}

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    surnames: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), nullable=False)
    dob: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    country: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    city: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    address: so.Mapped[str] = so.mapped_column(sa.String(200), nullable=False)
    phone: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    passport: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)

    def __repr__(self):
        return (f'User: {self.name} \n'
                f'Surname: {self.surnames} \n'
                f'Email: {self.email} \n'
                f'DOB: {self.dob} \n'
                f'Country: {self.country} \n'
                f'City: {self.city} \n'
                f'Address: {self.address} \n'
                f'Phone: {self.phone} \n' 
                f'Passport: {self.passport} \n')


class Trip(db.Model):
    __table_args__ = {'extend_existing': True}

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    country: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    start_date: so.Mapped[datetime] = so.mapped_column(sa.DateTime, nullable=False)
    end_date: so.Mapped[datetime] = so.mapped_column(sa.DateTime, nullable=False)
    description: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    age_range: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    price: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    num_people: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)

    def __repr__(self):
        return (f'Trip name: {self.name} \n'
                f'start date: {self.start_date} \n',
                f'end date: {self.end_date} \n',
                f'description: {self.description} \n',
                f'age range: {self.age_range} \n',
                f'price: {self.price} \n',
                f'num_people: {self.num_people} \n')


class Inscription(db.Model):
    __table_args__ = {'extend_existing': True}

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    trip_id: so.Mapped[int] = so.mapped_column(sa.String(64), nullable=False)
    user_id: so.Mapped[int] = so.mapped_column(sa.String(64), nullable=False)
    people: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    allergies: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    questions: so.Mapped[str] = so.mapped_column(sa.String(200), nullable=False)

    def __repr__(self):
        return (f'Trip id: {self.trip_id} \n'
                f'User id: {self.user_id} \n',
                f'people: {self.people} \n',
                f'allergies: {self.allergies} \n',
                f'questions: {self.questions} \n')