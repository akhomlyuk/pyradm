from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
import logging
from icecream import ic
import requests


router: Router = Router()


@router.message(Command("ip"))
async def cmd_ipaddr(message: Message):
    try:
        ip = requests.get('http://ipinfo.io/ip')
        await message.answer(f"IP address is: {ip.content.decode('utf-8')}")
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
