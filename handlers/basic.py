from aiogram import Bot
import asyncio
from aiogram.types import Message, update, InputMediaPhoto, FSInputFile
from core.keyboards.buttons import my_keyboard, get_keyboard, sto_keyboard
from core.filters.filters import BuyDetailFilter
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from core.commands.commands import set_commands


async def command_start(message: Message, bot: Bot):
    photo = FSInputFile(r'core/imeges/bot2.jpg')
    await bot.send_photo(message.chat.id, photo)
    await bot.send_message(message.from_user.id, f'<b>\U0001F468\U0000200D\U0001F527Привет {message.from_user.username},'
                         f' я бот-помошник.\nЯ помогу тебе найти где купить необходимую запчасть,'
                         f'\nи где отремонтировать твой автомобиль.</b>\n\U0001F697 \U0001F527 \U0001F697 \U0001F527'
                         f'\U0001F697 \U0001F527 \U0001F697 \U0001F527 \U0001F697 \U0001F527 \U0001F697 \U0001F527\n'
                         f'Давай скорее приступим!!!\nЧто будем искать?(жми кнопку ниже)', reply_markup=my_keyboard)
    await message.delete()


async def get_help(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "\U0001F697 \U0001F527<b>Я создан для того чтобы помочь тебе!</b>"
                                                 "\U0001F527\U0001F697\n\U0001F539С помощью кнопок расположенных в "
                                                 "нижней части экрана я предоставляю нужную информацию;\n"
                                                 "\U0001F539Я могу дать контакт менеджера или проложить маршрут к "
                                                 "магазину запчастей;\n\U0001F539а еще я могу предоставить контакты "
                                                 "мастеров для ремонта твоего авто;")


async def get_exit(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Благодарю. Обращайтесь еще!")


#развитие диалога в случае выбора юзером "Запчасть"
async def buy_detail(message: Message, bot: Bot):
    print(message.chat.id)
    photo = FSInputFile(r'core/imeges/mexanik.jpg')
    await bot.send_photo(message.chat.id, photo)
    await bot.send_message(message.from_user.id, f"<b><u>Огромный выбор запчастей в магазине 'МЕХАНИК'\U0001F468\U0000200D\U0001F527</u></b>\n"
                         "\U0001F539Узнать адрес магазина жми 'Адрес'\n\U0001F539Для связи с менеджером жми 'Менеджер'\n"
                         "\U0001F539'МЕХАНИК' в соц.сетях жми 'Instagram'", reply_markup=get_keyboard(), parse_mode="HTML")

async def adress(message: Message, bot: Bot):
    chat_id = message.from_user.id
    # задаем координаты геолокации (широту и долготу)
    latitude = 51.681360
    longitude = 33.924419
    # отправляем геолокацию пользователю
    await bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)
    await bot.send_message(message.from_user.id, '\U0001F4CDНаш адрес: г.Глухов, ул.Ковпака 2А\n\U0001F539Режим работы:\n'
                                                 '      Пн-Пт с 9:00 до 17:00\n'
                                                 '      Сб-Вс с 9:00 до 12:00\n'
                                                 'Для построения маршрута нажми на картинку(карту)')

async def manager(message: Message, bot: Bot):
    chat_id = message.from_user.id
    first_name = "Алексей"
    last_name = "Юрьевич"
    phone_number = "+380684212616"
    # отправляем контакт пользователю
    await bot.send_contact(chat_id=chat_id, first_name=first_name, last_name=last_name, phone_number=phone_number)


async def instagram(message: Message, bot: Bot):
    text = '<a href= "https://www.instagram.com/automechanicgl/?hl=ru">\u27a1\ufe0f Жми на эту ссылочку!!!</a>'
    await bot.send_message(message.from_user.id, text=text, parse_mode="HTML")

async def start_page(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Ты на главной странице', reply_markup=my_keyboard)


#развитие диалога в случае выбора юзером "СТО"
async def remont_avto(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Хорошо {message.from_user.username},\nукажи что именно в твоем авто\n'
                                                 f'нужно отремонтировать', reply_markup=sto_keyboard())
    await message.delete()

async def kuzovnya(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Этот мастер специализируется:\nПокраска, \nрихтовка, '
                                                 '\nвостановление после ДТП')
    chat_id = message.from_user.id
    first_name = "Александр"
    last_name = "Сытник"
    phone_number = "+380660062989"
    await bot.send_contact(chat_id=chat_id, first_name=first_name, last_name=last_name, phone_number=phone_number)

async def hodovka(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Этот мастер специализируется:\nПокраска, \nрихтовка, '
                                                 '\nвостановление после ДТП')
    chat_id = message.from_user.id
    first_name = "Юра"
    phone_number = "+380662165553"
    await bot.send_contact(chat_id=chat_id, first_name=first_name, phone_number=phone_number)

    await bot.send_message(message.from_user.id, 'Этот мастер специализируется:\nСход-развал')
    chat_id = message.from_user.id
    first_name = "Александр"
    phone_number = "+380669759306"
    await bot.send_contact(chat_id=chat_id, first_name=first_name, phone_number=phone_number)

async def dvigok(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Этот мастер специализируется:\nремонт двигателей')
    chat_id = message.from_user.id
    first_name = "Дядя"
    last_name = "Вася"
    phone_number = "+380952235306"
    await bot.send_contact(chat_id=chat_id, first_name=first_name, last_name=last_name, phone_number=phone_number)

async def electrica(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Этот мастер специализируется:\nэлектроника')
    chat_id = message.from_user.id
    first_name = "Дядя"
    last_name = "Вася"
    phone_number = "+380952235306"
    await bot.send_contact(chat_id=chat_id, first_name=first_name, last_name=last_name, phone_number=phone_number)
