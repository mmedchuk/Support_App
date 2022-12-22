import requests
from django.http import JsonResponse
from pydantic import BaseModel, Field

from exchange_rates.services import create_url


class ExchangeRatesResults(BaseModel):
    exchange_rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


def convert(request):
    response = requests.get(create_url(request))
    alphavantage_response = AlphavantageResponse(**response.json())
    return JsonResponse(alphavantage_response.dict())
