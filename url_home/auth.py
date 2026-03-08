from django.conf import settings


def validate_api_key(request):

    api_key = request.META.get("HTTP_X_API_KEY")

    if not api_key:
        raise PermissionError("API key missing")

    if api_key != settings.API_KEY:
        raise PermissionError("Invalid API key")
