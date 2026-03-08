from urllib.parse import urlparse


def validate_url(url):

    if not url:
        raise ValueError("originalUrl é obrigatório")

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("URL inválida")
