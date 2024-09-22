from datetime import datetime

from src import *
from src import db_utils

from flask import request, jsonify


def check_inscription_data(inscription_data):
    assert 'user' in inscription_data
    check_user_data(inscription_data['user'])
    assert 'tripId' in inscription_data
    assert 'people' in inscription_data
    assert 'allergies' in inscription_data
    assert 'questions' in inscription_data


def check_user_data(user_data):
    assert 'name' in user_data
    assert 'surnames' in user_data
    assert 'dob' in user_data
    assert 'passportId' in user_data
    assert 'phoneNumber' in user_data
    assert 'email' in user_data
    assert 'country' in user_data
    assert 'city' in user_data
    assert 'address' in user_data


def process_str_2_date(date_str):
    datetime_object = datetime.strptime(date_str, '%d-%m-%Y')
    return datetime_object


def check_trip_data(trip_data):
    assert 'name' in trip_data
    assert 'start_date' in trip_data
    assert 'end_date' in trip_data
    assert 'country' in trip_data
    assert 'age_range' in trip_data
    assert 'price' in trip_data
    assert 'description' in trip_data
    assert 'num_people' in trip_data

    trip_data['start_date'] = process_str_2_date(trip_data['start_date'])
    trip_data['end_date'] = process_str_2_date(trip_data['end_date'])


def make_trip(trip_db):
    return {
        'id': trip_db.id,
        'name': trip_db.name,
        'start_date': trip_db.start_date,
        'end_date': trip_db.end_date,
        'country': trip_db.country,
        'age_range': trip_db.age_range,
        'price': trip_db.price,
        'description': trip_db.description,
        'num_people': trip_db.num_people
    }


def make_user(user_data_db):
    return {
        'id': user_data_db.id,
        'name': user_data_db.name,
        'surname_1': user_data_db.surname_1,
        'email': user_data_db.email,
        'age': user_data_db.age,
        'country': user_data_db.country,
        'city': user_data_db.city,
        'address': user_data_db.address,
        'phone': user_data_db.phone
    }


# Trips information
@app.get('/trip')
def get_trips():
    trips = [make_trip(trip_db) for trip_db in db_utils.get_trips_db()]
    response = jsonify(trips)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.get('/trip/<int:trip_id>')
def get_trip(trip_id):
    trip = db_utils.get_trip_db(trip_id)
    response = jsonify(make_trip(trip))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.get('/trip/<int:trip_id>/summary')
def get_trip_summary(trip_id):
    return 'Endpoint not implemented yet'


@app.post('/trip/')
def insert_trip():
    trip_data = request.get_json()
    check_trip_data(trip_data)
    db_utils.insert_trip_db(trip_data)
    return 'Trip added'


# Users information
@app.get('/user')
def get_users():
    users_db = db_utils.get_all_users()
    users = [make_user(user_db) for user_db in users_db]
    response = jsonify(users)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.get('/user/<int:user_id>')
def get_user(user_id):
    user = db_utils.get_user(user_id)
    return make_user(user)


@app.post('/user')
def insert_user():
    user_data = request.get_json()
    check_user_data(user_data)
    db_utils.insert_user_db(user_data)
    return 'User has been inserted into database'


# Users information
@app.post('/inscription')
def insert_inscription():
    inscription_data = request.get_json()
    check_inscription_data(inscription_data)
    check_inscription_data(inscription_data)
    db_utils.insert_inscription_db(inscription_data)
    return 'User has been inserted into database'

