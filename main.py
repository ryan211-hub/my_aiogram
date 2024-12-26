import asyncio

from aiogram import Dispatcher
from bot_instance import bot
from bot.handlers.user_handlers import user_router
from bot.config import *
from datetime import datetime


def register_routers(dp: Dispatcher)->None:
  '''Registers routers'''
  dp.include_router(user_router)


async def main()->None:
  '''The main funcion which will execute our event loop and start polling.'''
  print(f'Program started at {datetime.now()}')
  config = BotConfig(
    admin_ids=[1275751314],
    welcome_message=f'Hello, <b>world</b>!\nI am <i>Bot</i>  in lesson_5 😀'
  )
  dp = Dispatcher()
  dp['config'] = config
  register_routers(dp)
  await dp.start_polling(bot)



if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print (f'Program stopped manually at {datetime.now()}')