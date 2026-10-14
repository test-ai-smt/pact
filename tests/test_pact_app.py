import pytest

from src.pact_app import greet


def test_greet():
    assert greet("abood") == "Hello from PACT, abood!"


def test_greet_arabic():
    assert greet("abood", "ar") == "مرحباً من PACT، abood!"


def test_greet_unsupported_language():
    with pytest.raises(ValueError):
        greet("abood", "fr")
