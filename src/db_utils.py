from src.db_models import User, Trip, Inscription
from src import db

import sqlalchemy as sa


def insert_trip_db(trip_data):
    db_trip = Trip(name=trip_data['name'],
                   start_date=trip_data['start_date'],
                   end_date=trip_data['end_date'],
                   country=trip_data['country'],
                   description=trip_data['description'],
                   age_range=trip_data['age_range'],
                   price=trip_data['price'],
                   num_people=trip_data['num_people'])
    db.session.add(db_trip)
    db.session.commit()
    pass


def get_trips_db():
    query = sa.select(Trip)
    trips = db.session.scalars(query).all()
    return trips


def get_trip_db(trip_id):
    return db.session.get(Trip, trip_id)


def insert_user_db(user_data):
    db_user = User(name=user_data['name'],
                    surname_1=user_data['surname_1'],
                    email=user_data['email'],
                    country=user_data['country'],
                    city=user_data['city'],
                    phone=user_data['phone'],
                    age=user_data['age'],
                    address=user_data['address'])

    db.session.add(db_user)
    db.session.commit()


def get_all_users():
    query = sa.select(User)
    users = db.session.scalars(query).all()
    return users


def get_user(user_id):
    return db.session.get(User, user_id)


def insert_inscription_db(inscription_data):
    db_user = User(name=inscription_data['user']['name'],
                   surnames=inscription_data['user']['surnames'],
                   dob=inscription_data['user']['dob'],
                   email=inscription_data['user']['email'],
                   country=inscription_data['user']['country'],
                   city=inscription_data['user']['city'],
                   address=inscription_data['user']['address'],
                   phone=inscription_data['user']['phoneNumber'],
                   passport=inscription_data['user']['passportId'])
    db.session.add(db_user)
    db.session.flush()

    db_inscription = Inscription(user_id=db_user.id,
                                 trip_id=inscription_data['tripId'],
                                 people=inscription_data['people'],
                                 allergies=inscription_data['allergies'],
                                 questions=inscription_data['questions'])
    db.session.add(db_inscription)

    db.session.commit()
