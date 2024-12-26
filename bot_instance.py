from aiogram import Bot
from token_api import TOKEN_API
from aiogram.client.default import DefaultBotProperties

bot = Bot(
  token = TOKEN_API,
  default=DefaultBotProperties(parse_mode='HTML') # HTML mode 用html解析
)