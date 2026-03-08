import logging

from .repository import URLRepository
from .utils import generate_short_id
from .validators import validate_url


logger = logging.getLogger(__name__)


class URLService:

    BASE_URL = "http://localhost:8000"

    @staticmethod
    def create_short_url(original_url, expiration_date=None, custom_alias=None):

        validate_url(original_url)

        if custom_alias:

            if URLRepository.exists(custom_alias):
                raise ValueError("Alias já existe")

            short_id = custom_alias

        else:

            while True:

                short_id = generate_short_id()

                if not URLRepository.exists(short_id):
                    break

        data = {
            "id": short_id,
            "original_url": original_url,
            "expiration_date": expiration_date
        }

        url = URLRepository.create(data)

        logger.info(f"Short URL created: {short_id}")

        return {
            "id": url.id,
            "shortUrl": f"{URLService.BASE_URL}/{url.id}",
            "originalUrl": url.original_url,
            "createdAt": url.created_at,
            "expirationDate": url.expiration_date
        }

    @staticmethod
    def get_url(url_id):

        url = URLRepository.get_by_id(url_id)

        if not url:

            logger.warning(f"id not found: {url_id}")

            return None

        if url.is_expired():

            raise ValueError("URL expirada")

        URLRepository.increment_click(url)

        return url
