from converter import sync_converter
from fastapi import APIRouter

router = APIRouter()

@router.get("/converter/{from_currency}")
async def converter(from_currency: str, to_currency: str, price: float):
    to_currencies = to_currency.split(',')
    converted_prices = []
    
    for to_currency in to_currencies:
        converted_price = sync_converter(from_currency, to_currency, price)
        converted_prices.append(converted_price)
        
    return converted_prices