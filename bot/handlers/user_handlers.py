from aiogram.filters import Command
from aiogram import Router, types
from bot.config import BotConfig
from random import choice

user_router = Router()


@user_router.message(Command(commands=['start']))
async def start_command(message: types.Message , config: BotConfig) -> None:
    '''
    This handler will be called when user sends `/start` command
    '''
    emo = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]
    react = types.ReactionTypeEmoji(emoji=choice(emo))
    await message.react([react])
    await message.answer(config.welcome_message)


@user_router.message(Command('reply'))
async def cmd_reply(message: types.Message):
    await message.reply('I am replying to you')


@user_router.message(Command('admin_info'))
async def cmd_admin_info(message: types.Message, config: BotConfig):
    if message.from_user.id in config.admin_ids:
        await message.answer(f'You can use this bot {message.from_user.full_name}')
    else:
        await message.answer('You are not allowed to use this bot {message.from_user.full_name}')


@user_router.message(Command('dice'))
async def cmd_dice(message: types.Message) -> None:
    await message.answer_dice(emoji='🎲')