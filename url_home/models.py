from django.db import models
from django.utils import timezone


class ShortURL(models.Model):

    id = models.CharField(primary_key=True, max_length=20)

    original_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    expiration_date = models.DateTimeField(null=True, blank=True)

    click_count = models.IntegerField(default=0)

    def is_expired(self):

        if not self.expiration_date:
            return False

        return timezone.now() > self.expiration_date
