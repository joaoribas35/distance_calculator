from app import create_app
import json


def app_client():
    app = create_app()
    return app.test_client()


def test_status_when_inside_MKAD():
    client = app_client()
    data = {
        "address": "Prospekt Mira, 119, Moscow, Rússia, 129223"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 201


def test_response_when_inside_MKAD():
    client = app_client()
    data = {
        "address": "Prospekt Mira, 119, Moscow, Rússia, 129223"
    }

    expected = {
        "address": "Moscow, MS, Russia",
        "distance": "null",
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    actual = response.get_json()
    del actual['id']

    assert actual == expected


def test_status_when_outside_MKAD():
    client = app_client()
    data = {
        "address": "Khimki, Moscow Oblast, Russia, 141400"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 201


def test_response_when_outside_MKAD():
    client = app_client()
    data = {
        "address": "Khimki, Moscow Oblast, Russia, 141400"
    }

    expected = {
        "address": "Khimki, MS, Russia",
        "distance": "19.57 km",
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    actual = response.get_json()
    del actual['id']

    assert actual == expected


def test_status_invalid_key():
    client = app_client()
    data = {
        "invalid": "Khimki, Moscow Oblast, Russia, 141400"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400


def test_response_invalid_key():
    client = app_client()
    data = {
        "invalid": "Khimki, Moscow Oblast, Russia, 141400"
    }

    expected = {
        "error": "invalid key"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    actual = response.get_json()

    assert actual == expected


def test_status_short_address():
    client = app_client()
    data = {
        "address": "aa"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400


def test_response_short_address():
    client = app_client()
    data = {
        "address": "aa"
    }

    expected = {
        "error": {
            "code": "validation_error",
            "context": {
                "query": {
                    "message": "query must have at 3 character's",
                    "type": "invalid_query"
                }
            },
            "message": "Request failed with validation error"
        }
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    actual = response.get_json()

    assert actual == expected


def test_status_invalid_address():
    client = app_client()
    data = {
        "address": "aa12354bga"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400


def test_response_invalid_address():
    client = app_client()
    data = {
        "address": "aa12354bga"
    }

    expected = {
        "error": "invalid or inexistent address"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    actual = response.get_json()

    assert actual == expected


def test_status_invalid_address_type():
    client = app_client()
    data = {
        "address": 1234
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400


def test_response_invalid_address_type():
    client = app_client()
    data = {
        "address": 1234
    }

    expected = {
        "error": "address must be a string"
    }

    response = client.post(
        "/api/distances/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    actual = response.get_json()

    assert actual == expected
