from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
import logging
import os
from PIL import ImageGrab
from sys import platform

router: Router = Router()


@router.message(Command("sc"))
async def cmd_sc(message: Message):
    try:
        if platform == "win32":
            path = os.path.expanduser('~') + r'\sc.jpg'
        else:
            path = os.path.expanduser('~') + r'/sc.jpg'
        sc = ImageGrab.grab(bbox=None)  # Fullscreen
        sc.save(path)
        screen = FSInputFile(path)
        await message.answer_photo(screen, caption='Thumbnail')
        await message.answer_document(screen)
        os.remove(path)
    except Exception as e:
        logging.error(e)
