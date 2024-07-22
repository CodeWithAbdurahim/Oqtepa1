from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.menu import Example
from keyboards.reply.button import phone_number
from geopy.geocoders import Photon
 


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}. Botimizga xush kelibsiz.\nIltimos raqamingizni kiriting", reply_markup=phone_number)

@dp.message_handler(state=Example.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_handler(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await state.finish()


@dp.message_handler(content_types = types.ContentType.LOCATION)
async def location_handler(message: types.Message):
    user_location = message.location
    user_latitude = user_location.latitude
    user_longitude = user_location.longitude
    
    geolocator = Photon(user_agent='userapp')
    location = geolocator.reverse(f"{user_latitude},{user_longitude}")
    city = location.raw['properties']['city']
    street = location.raw['properties']['street']
    house_number = location.raw['properties']['housenumber']
    district = location.raw['properties']['district']
    print(location.raw)

    
    await message.answer(f"Manzilingiz: {city}, {district},{street}, {house_number}")
