import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app  # noqa: E402


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    flask_app.config["DATABASE"] = ":memory:"
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()