import pytest
from django.test import Client
from django.conf import settings


@pytest.mark.django_db
def test_create_url_endpoint():

    client = Client()

    response = client.post(
        "/v1/urls",
        data={
            "originalUrl": "https://google.com"
        },
        content_type="application/json",
        HTTP_X_API_KEY=settings.API_KEY
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_redirect_url():

    client = Client()

    response = client.post(
        "/v1/urls",
        data={
            "originalUrl": "https://google.com"
        },
        content_type="application/json",
        HTTP_X_API_KEY=settings.API_KEY
    )

    data = response.json()

    short_id = data["id"]

    redirect_response = client.get(f"/{short_id}")

    assert redirect_response.status_code == 302
