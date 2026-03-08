import json

from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .services import URLService
from .repository import URLRepository
from .auth import validate_api_key


@csrf_exempt
def create_url(request):

    if request.method != "POST":
        return JsonResponse({"error": "method not allowed"}, status=405)

    try:

        validate_api_key(request)

    except PermissionError as e:

        return JsonResponse({"error": str(e)}, status=403)

    data = json.loads(request.body)

    original_url = data.get("originalUrl")
    expiration_date = data.get("expirationDate")
    custom_alias = data.get("customAlias")

    try:

        result = URLService.create_short_url(
            original_url,
            expiration_date,
            custom_alias
        )

        return JsonResponse(result, status=201)

    except ValueError as e:

        return JsonResponse({"error": str(e)}, status=400)


def redirect_url(request, url_id):

    try:

        url = URLService.get_url(url_id)

        if not url:
            return JsonResponse({"error": "URL not found"}, status=404)

        return HttpResponseRedirect(url.original_url)

    except ValueError as e:

        return JsonResponse({"error": str(e)}, status=410)


def get_url_details(request, url_id):

    url = URLRepository.get_by_id(url_id)

    if not url:

        return JsonResponse({"error": "URL not found"}, status=404)

    return JsonResponse({

        "id": url.id,
        "shortUrl": f"http://localhost:8000/{url.id}",
        "originalUrl": url.original_url,
        "createdAt": url.created_at,
        "expirationDate": url.expiration_date,
        "clickCount": url.click_count
    })
