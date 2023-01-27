import json
import requests

from app.db import Statistic


def test_create_statistic():

    data = {
        "clicks": 100,
        "views": 1000,
        "cost": 50.5,
        "date": "2022-01-01"
    }

    response = requests.post("http://localhost:8000/statistics/create/", json=data)

    assert response.status_code == 200
    assert response.json() == {"message": "Succesfully created!"}

def test_create_wrong_statistic():
    data = {
        "clicks": 100,
        "views": 1000,
        "cost": -50.5,
        "date": "2022-01-01"
    }

    response = requests.post("http://localhost:8000/statistics/create/", json=data)
    
    assert response.status_code == 422

def test_statistic_reset():
    data = {
        "clicks": 100,
        "views": 1000,
        "cost": 50.5,
        "date": "2022-01-01"
    }
    requests.post("http://localhost:8000/statistics/create/", json=data)

    response = requests.delete("http://localhost:8000/statistics/reset/")

    assert response.status_code == 200
    assert "Succesfully deleted 2 statistic objects" in response.json()

def test_statistic_reset_not_enough():

    response = requests.delete("http://localhost:8000/statistics/reset/")

    assert response.status_code == 200
    assert "Sorry, we do not have enough stastic to delete" in response.json()