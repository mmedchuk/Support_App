import json

from django.conf import settings


def create_url(request, from_currency="USD", to_currency="UAH") -> str:
    if request.method == "POST":
        request_to_json = json.loads(request.body)
        from_currency = request_to_json["from"]
        to_currency = request_to_json["to"]
    url = (
        f"{settings.ALPHA_VANTAGE_BASE_URL}/"
        f"query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={from_currency}&to_currency={to_currency}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    )
    return url
