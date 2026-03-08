import pytest

from url_home.services import URLService
from url_home.models import ShortURL


@pytest.mark.django_db
def test_create_short_url():

    result = URLService.create_short_url("https://google.com")

    assert result["originalUrl"] == "https://google.com"

    assert "id" in result


@pytest.mark.django_db
def test_create_custom_alias():

    result = URLService.create_short_url(
        "https://google.com",
        custom_alias="google"
    )

    assert result["id"] == "google"


@pytest.mark.django_db
def test_alias_collision():

    URLService.create_short_url(
        "https://google.com",
        custom_alias="google"
    )

    with pytest.raises(ValueError):

        URLService.create_short_url(
            "https://example.com",
            custom_alias="google"
        )
