
#
# Setup example from 
# https://flask.palletsprojects.com/en/stable/testing/
#

import pytest
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
# Tests down from here
#


def test_request_example(client):
    response = client.get("/")
    assert b"Hello, World!" in response.data