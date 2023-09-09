import asyncio
import logging
import os
from aiogram import Dispatcher, types, Bot
import handlers
import sys_info
import screenshot
import ip_addr
import up_down
import shell
import ps
from cfg import bot as bot
from icecream import ic

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


@dp.errors()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f'Error: {update}: {exception}')


async def main():
    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit) as e:
        logging.info("Bot stopped")
        ic(e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='logs/bot.log',
                        format="%(filename)s:%(lineno)d #%(levelname)-8s" "[%(asctime)s] - %(name)s - %(message)s")
    logging.info('Bot starting...')
    asyncio.run(main())
