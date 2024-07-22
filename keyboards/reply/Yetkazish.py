
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yetkazish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" 🛵 Eltib berish"),
         KeyboardButton(text="🏃🏽‍♂️ Borib olish")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


olibborish = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📍 Geolokatsiyani yuboring", request_location=True)],
        [KeyboardButton(text='⬅️ Ortga')]])

boribolish=ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📍 Geolokatsiyani yuboring", request_location=True)],
        [KeyboardButton(text='⬅️ Ortga')]])