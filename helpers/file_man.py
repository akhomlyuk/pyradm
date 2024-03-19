from aiogram import Router, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging
import os
from pathlib import Path

router: Router = Router()


def file_man(folder=None):
    markup = InlineKeyboardBuilder()
    markup.button(text="⬆️", callback_data=f"{folder}*dir*")
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            if len(os.path.join(folder, file)) >= 50:
                markup.button(text=f"📃 {file}", callback_data=os.path.join(folder, file)[:44])
            else:
                markup.button(text=f"📃 {file}", callback_data=os.path.join(folder, file))
        elif len(os.path.join(folder, file)) >= 50:
            markup.button(text=f"📁 {file}", callback_data=os.path.join(folder, file)[:44])
        else:
            markup.button(text=f"📁 {file}", callback_data=os.path.join(folder, file))
    markup.adjust(1, 2)
    return markup


@router.message(Command("fm"))
async def cmd_fm(message: Message):
    try:
        args = message.text.split()
        if len(args) == 1:
            keyboard = file_man(os.getcwd())
            await message.answer(f'📚 Files:\n{os.getcwd()}', reply_markup=keyboard.as_markup())
        else:
            keyboard = file_man(os.path.join(args[1]))
            await message.answer(f'📚 Files:\n{os.path.abspath(args[1])}', reply_markup=keyboard.as_markup())
    except Exception as e:
        logging.error(e)


@router.callback_query(F.data)
async def file_action(callback: CallbackQuery):
    try:
        file_name = callback.data
        if os.path.isfile(file_name):
            file = FSInputFile(file_name)
            await callback.message.answer_document(file)
        elif file_name.endswith("*dir*"):
            parent_dir = os.path.join(Path(file_name).parent)
            keyboard = file_man(parent_dir)
            await callback.message.answer(f'📚 Files:\n{parent_dir}', reply_markup=keyboard.as_markup())
        else:
            folder = os.path.join(Path(file_name))
            keyboard = file_man(folder)
            await callback.message.answer(f'📚 Files:\n{folder}', reply_markup=keyboard.as_markup())
        await callback.answer()
    except WindowsError:
        await callback.message.answer(f'Problem with long name\nTry to download from /shell or /download command')
    except Exception as e:
        print(e)
        logging.error(e)
