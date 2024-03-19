from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
import logging
import psutil

router: Router = Router()


procs = ''.join(
    f"{process.name()} : {str(process.pid)}\n"
    for process in psutil.process_iter()
)


@router.message(Command("ps"))
async def cmd_process_list(message: Message):
    try:
        part_size = 3900
        message_parts = [procs[i:i + part_size] for i in range(0, len(procs), part_size)]
        for part in message_parts:
            await message.answer(f'<b>Process name</b> : <b>PID</b>\n{part}')
    except Exception as e:
        logging.error(e)
