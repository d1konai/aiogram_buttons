#keyboard.defalt
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Томоэ"),
            KeyboardButton(text="Нанами")
        ],
        [
            KeyboardButton(text="Карусоно"),
            KeyboardButton(text="Бездомный бог")
        ],
    ],
    resize_keyboard=True
)