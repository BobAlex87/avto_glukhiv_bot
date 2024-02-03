from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Написать боту'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='exit',
            description='Выход'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())