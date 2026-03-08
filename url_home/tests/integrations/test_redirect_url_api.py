import pytest
from django.conf import settings


@pytest.mark.django_db
def test_redirect_short_url(client):

    payload = {
        "originalUrl": "https://google.com"
    }

    create_response = client.post(
        "/v1/urls",
        payload,
        content_type="application/json",
        HTTP_X_API_KEY=settings.API_KEY
    )

    short_id = create_response.json()["id"]

    response = client.get(f"/{short_id}")

    assert response.status_code == 302
