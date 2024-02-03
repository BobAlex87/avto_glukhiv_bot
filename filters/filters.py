from aiogram.filters import BaseFilter
from aiogram.types import Message, ContentType

class BuyDetailFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.content_type == ContentType.TEXT
