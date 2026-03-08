import pytest
from django.conf import settings


@pytest.mark.django_db
def test_create_short_url(client):

    payload = {
        "originalUrl": "https://google.com"
    }

    response = client.post(
        "/v1/urls",
        payload,
        content_type="application/json",
        HTTP_X_API_KEY=settings.API_KEY
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert "shortUrl" in data
    assert data["originalUrl"] == "https://google.com"
