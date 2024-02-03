from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from aiogram import types

my_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='\U0001F697 Запчасть'
        ),
        KeyboardButton(
            text="\U0001F527 СТО"
        ),
    ],
], resize_keyboard=True)


def get_keyboard():
    button_build = ReplyKeyboardBuilder()

    button_build.button(text='Адрес')
    button_build.button(text='Менеджер')
    button_build.button(text='Instagram')
    button_build.button(text='На_главную')

    button_build.adjust(3, 1)
    return button_build.as_markup(resize_keyboard=True)

def sto_keyboard():
    button_build = ReplyKeyboardBuilder()

    button_build.button(text='Ходовка')
    button_build.button(text='/Кузовщина')
    button_build.button(text='Двигатель')
    button_build.button(text='Электрика')
    button_build.button(text='На_главную')

    button_build.adjust(2, 2, 1)
    return button_build.as_markup(resize_keyboard=True, one_time_keyboard=True)

# def sto_keyboard():
#     button_build = InlineKeyboardMarkup(inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text='Ходовка',
#                 callback_data="Ходовка"
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text='Кузовщина',
#                 callback_data="Кузовщина"
#             )
#         ],
#         ])
#
#     return button_build


# detail_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(
#             text='/Адрес'
#         ),
#         KeyboardButton(
#             text='/Менеджер'
#         ),
#         KeyboardButton(
#             text='/Instagram'
#         ),
#         KeyboardButton(
#             text='/На_главную'
#         ),
#     ],
# ], resize_keyboard=True)
