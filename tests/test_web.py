import pytest

from src.web import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    assert client.get("/health").get_json() == {"status": "ok"}


def test_languages(client):
    assert client.get("/languages").get_json() == {"languages": ["ar", "en"]}


def test_greet_en(client):
    r = client.get("/greet?name=abood")
    assert r.status_code == 200
    assert r.get_json()["message"] == "Hello from PACT, abood!"


def test_greet_ar(client):
    r = client.get("/greet", query_string={"name": "abood", "lang": "ar"})
    assert r.get_json()["message"] == "مرحباً من PACT، abood!"


@pytest.mark.parametrize("qs", [{}, {"name": ""}, {"name": "x" * 65}, {"name": "a", "lang": "fr"}])
def test_greet_bad_input(client, qs):
    assert client.get("/greet", query_string=qs).status_code == 400


def test_security_headers(client):
    h = client.get("/health").headers
    assert h["X-Content-Type-Options"] == "nosniff"
    assert h["Content-Security-Policy"] == "default-src 'none'"
