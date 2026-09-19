import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps Task Manager" in response.data


def test_add_task(client):
    response = client.post(
        "/add",
        data={"task": "Learn Docker"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Learn Docker" in response.data


def test_delete_task(client):
    client.post(
        "/add",
        data={"task": "Temporary Task"},
        follow_redirects=True
    )

    response = client.post(
        "/delete/0",
        follow_redirects=True
    )

    assert response.status_code == 200