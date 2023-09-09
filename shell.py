from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
import logging
from icecream import ic
import subprocess

router: Router = Router()


class Shell(StatesGroup):
    ShellOn = State()


@router.message(Command("shell"))
async def shell_state(message: Message, state: FSMContext):
    try:
        await state.set_state(Shell.ShellOn)
        await message.answer('<b>Shell mode ON</b>\nSend <code>exit</code> for exit')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)


@router.message(Shell.ShellOn)
async def cmd_shell(message: Message, state: FSMContext):
    try:
        await state.update_data(shell_cmd=message.text.strip())

        command = message.text.strip()
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stdout:
            output = stdout.decode('utf-8', errors='ignore')
            part_size = 3900
            message_parts = [output[i:i + part_size] for i in range(0, len(output), part_size)]
            for part in message_parts:
                await message.answer(f"{part}")

        if command.lower() == 'exit':
            await state.clear()
            await message.answer(f"Exiting from shell...\n<b>Shell mode OFF</b>")
        else:
            await state.set_state(Shell.ShellOn)
    except Exception as e:
        ic()
        ic(e)
        await message.answer(str(e))
