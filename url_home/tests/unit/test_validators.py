import pytest

from url_home.validators import validate_url


def test_validate_url_valid():

    validate_url("https://google.com")


def test_validate_url_invalid():

    with pytest.raises(ValueError):

        validate_url("google.com")
