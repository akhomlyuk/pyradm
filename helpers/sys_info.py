from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
import logging
from datetime import datetime
import psutil
import platform

router: Router = Router()


@router.message(Command("info"))
async def cmd_sysinfo(message: Message):
    try:
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        svmem = psutil.virtual_memory()
        await message.answer(f'''
<b>System:</b> <code>{uname.system}</code>
<b>Host name:</b> <code>{uname.node}</code>
<b>Release:</b> <code>{uname.release}</code>
<b>Version:</b> <code>{uname.version}</code>
<b>Machine:</b> <code>{uname.machine}</code>
<b>Processor:</b> <code>{uname.processor}</code>
<b>Physical cores:</b> <code>{psutil.cpu_count(logical=False)}</code>
<b>Total cores:</b> <code>{psutil.cpu_count(logical=True)}</code>
<b>Total RAM:</b> <code>{svmem.total // 1024 // 1024} Mb</code>
<b>Available:</b> <code>{svmem.available // 1024 // 1024} Mb</code>
<b>Boot Time:</b> <code>{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}</code>''')
    except Exception as e:
        logging.error(e)
