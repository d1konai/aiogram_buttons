from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Аниме", reply_markup=menu)

@dp.message_handler(Text(equals=["Томоэ", "Нанами", "Карусоно","Бездомный бог"]))
async def get_food(message: Message):
    await message.answer(f" {message.text}. Chosen", reply_markup=ReplyKeyboardRemove())