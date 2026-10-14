from src.pact_app import greet


def test_greet():
    assert greet("abood") == "Hello from PACT, abood!"
