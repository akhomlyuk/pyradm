from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
from cfg import bot
import logging

router: Router = Router()


@router.message(Command("download"))
async def cmd_download(message: Message):
    try:
        msg = message.text
        args = msg.split(' ')
        file_path = args[1]
        file = FSInputFile(file_path)
        await bot.send_document(message.chat.id, file)
    except Exception as e:
        logging.error(e)


@router.message(F.document)
async def cmd_upload(message: Message):
    try:
        file = await bot.get_file(message.document.file_id)
        file_path = file.file_path
        await bot.download_file(file_path, message.document.file_name)
    except Exception as e:
        logging.error(e)
