import os

import pytest
from flask import current_app, g
import isitdown.index as flaskr

def get_db():
    if 'db' not in g:
        g.db = flaskr.init_db(current_app)
    return g.db


@pytest.fixture
def client():
    DATABASE_URI = os.environ["DATABASE_URI"]
    app = flaskr.create_app(DATABASE_URI)
    app.app_context().push()
    client = app.test_client()
    db = None

    with app.app_context():
        db = flaskr.init_db(app)
    yield client
    get_db().drop_all()


def test_json_api(client):
    resp = client.get('/api/google.it')
    json_data = resp.get_json()
    assert json_data is not None
    assert json_data['isitdown'] is False


def test_working_index(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert rv.status_code == 200