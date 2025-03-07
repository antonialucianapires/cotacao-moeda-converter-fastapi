from converter import sync_converter, async_converter
from fastapi import APIRouter, Path, Query
from asyncio import gather

router = APIRouter(prefix="/converter")

@router.get("/{from_currency}")
async def converter(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"), 
    to_currency: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"), 
    price: float = Query(gt=0)):
    
    to_currencies = to_currency.split(',')
    converted_prices = []
    
    for to_currency in to_currencies:
        converted_price = sync_converter(from_currency, to_currency, price)
        converted_prices.append(converted_price)
        
    return converted_prices

@router.get("/async/{from_currency}")
async def async_converter_router(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"), 
    to_currency: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"), 
    price: float = Query(gt=0)):
    to_currencies = to_currency.split(',')
    coroutines = []
    
    for curr in to_currencies:
        coroutine = async_converter(from_currency, curr, price)
        coroutines.append(coroutine)
        
    result = await gather(*coroutines)
    return result