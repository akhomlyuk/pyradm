import asyncio
import logging
import os
from aiogram import Dispatcher, types
from helpers import ip_addr, ps, screenshot, shell, sys_info, up_down, webcam, handlers
from cfg import bot as bot

# Author : Exited3n
# https://t.me/pt_soft

os.makedirs('logs', exist_ok=True)

dp = Dispatcher()

# Append routers
dp.include_router(handlers.router)
dp.include_router(sys_info.router)
dp.include_router(screenshot.router)
dp.include_router(ip_addr.router)
dp.include_router(up_down.router)
dp.include_router(shell.router)
dp.include_router(ps.router)
dp.include_router(webcam.router)


@dp.errors()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f'Error: {update}: {exception}')


async def main():
    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='logs/bot.log',
                        format="%(filename)s:%(lineno)d #%(levelname)-8s" "[%(asctime)s] - %(name)s - %(message)s")
    logging.info('Bot starting...')
    asyncio.run(main())
