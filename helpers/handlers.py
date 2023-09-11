from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
import logging

router: Router = Router()

commands = '''
/start - start pyradm
/help - help
/shell - shell commands
/sc - screenshot
/download - download (abs. path)
/info - system info
/ip - public ip address and geolocation
/ps - process list
/webcam 5 - record video (secs)
/webcam - screenshot from camera
Send any file as file for upload to target'''


@router.message(Command("start"))
async def cmd_start(message: Message):
    try:
        await message.answer(f'Hello @{message.from_user.username}')
        await message.answer(f'{commands}')
        await message.answer(f'Author: @pt_soft')
    except Exception as e:
        logging.error(e)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(f'{commands}')
    await message.answer(f'Author: @pt_soft')
