from .models import ShortURL


class URLRepository:

    @staticmethod
    def create(data):

        return ShortURL.objects.create(**data)

    @staticmethod
    def get_by_id(url_id):

        try:
            return ShortURL.objects.get(id=url_id)

        except ShortURL.DoesNotExist:
            return None

    @staticmethod
    def exists(url_id):

        return ShortURL.objects.filter(id=url_id).exists()

    @staticmethod
    def increment_click(url):

        url.click_count += 1
        url.save()
