from aiogram.dispatcher.filters.state import State, StatesGroup


class Example(StatesGroup):
    phone_number = State()