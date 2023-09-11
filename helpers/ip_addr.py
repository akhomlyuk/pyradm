from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
import logging
import requests
import json

router: Router = Router()


@router.message(Command("ip"))
async def cmd_ipaddr(message: Message):
    try:
        url = "http://ip-api.com/json/?fields=country,region,regionName,city,lat,lon,query"
        request = requests.get(url)
        request_map = json.loads(request.text)
        location_info = (f'<b>IP address:</b> {request_map["query"]}\n<b>City</b>: {request_map["city"]}\n'
                         f'<b>Region:</b> {request_map["region"]}\n<b>Country:</b> {request_map["country"]}\n'
                         f'<b>Coordinates:</b> <code>{str(request_map["lat"])}, {str(request_map["lon"])}</code>')

        await message.answer_location(request_map["lat"], request_map["lon"])
        await message.answer(f"{location_info}")
    except Exception as e:
        logging.error(e)
