from aiogram import Router
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from aiogram.types import Message
import logging
import os
from sys import platform
import pyperclip
from PIL import ImageGrab

router: Router = Router()


@router.message(Command("clip"))
async def cmd_sc(message: Message):
    try:
        text_clipboard = pyperclip.paste()
        if platform == "win32":
            path = os.path.expanduser('~') + r'\clip.jpg'
        else:
            path = os.path.expanduser('~') + r'/clip.jpg'

        if len(text_clipboard) == 0:
            img = ImageGrab.grabclipboard()
            img.save(path, 'PNG')
            img_clipboard = FSInputFile(path)
            await message.answer_photo(img_clipboard, caption='Thumbnail')
            await message.answer_document(img_clipboard)
            os.remove(path)
        else:
            await message.answer(text_clipboard)
    except Exception as e:
        logging.error(e)
