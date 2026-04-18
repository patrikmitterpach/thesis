#
# Setup example from 
# https://flask.palletsprojects.com/en/stable/testing/
#

import pytest
import json

from main import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app
@pytest.fixture()
def client(app):
    return app.test_client()
@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


#
# Variables used in tests
#
empty_json = json.dumps({})
valid_json = json.dumps({"source": "https://example.com", "status": 401, "data": {"message": "Unauthorized"}})

#
# Tests down from here
#

def test_post_empty_json(client):
    response = client.post("/", data=empty_json)
    assert response.status == '400 BAD REQUEST'


def test_post_full_json_no_content_type(client):
    response = client.post("/", data=valid_json,  content_type="application/json")
    assert response.status == '400 BAD REQUEST'

def test_post_full_json_valid(client):
    response = client.post("/", data=valid_json,  content_type="text/json")
    assert response.status == '200 OK'

def test_post_full_json_valid_wrong_content_type(client):
    response = client.post("/", data=valid_json,  content_type="text/xml")
    assert response.status == '400 BAD REQUEST'
