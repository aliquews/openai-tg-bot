from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message


router = Router()


@router.message(Text(startswith='!д'))
async def dalle_handler(message: Message):
    pass