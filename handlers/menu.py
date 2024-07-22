from aiogram import types
from loader import dp, bot
from keyboards.inline.menu import menu
from keyboards.inline.menu import Asosiy
from keyboards.reply.Yetkazish import yetkazish
from keyboards.reply.Yetkazish import olibborish
from keyboards.reply.Yetkazish import boribolish
from keyboards.inline.Manzil import manzil
from keyboards.inline.Manzil import manzil2
from keyboards.inline.menu import sozlamalar




@dp.message_handler(text='Share phone number')
async def manzil_handler(message: types.Message):
    text = """Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await message.answer(text, reply_markup=menu)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact_handler(message: types.Message):
    contact = message.contact
    phone_number = contact.phone_number
    await message.answer(f"https://telegra.ph/Taomnoma-09-30", reply_markup=menu)

@dp.callback_query_handler(lambda c: c.data == 'Buyurtma berish')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = "Buyurtmani birga joylashtiramizmi? 🤗\nBuyurtma turini tanlang"
    await bot.send_message(callback_query.from_user.id, text, reply_markup=yetkazish)
    await bot.answer_callback_query(callback_query.id)


@dp.message_handler(text='Ortga')
async def manzil_handler(message: types.Message):
    text = """Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await message.answer(" Ortga qaytdingiz")
    await message.answer(text, reply_markup=menu)



@dp.message_handler(text='🛵 Eltib berish')
async def manzil_handler(message: types.Message):
    text = """Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang"""
    await message.answer(text, reply_markup=olibborish)



@dp.message_handler(text='⬅️ Ortga')
async def manzil_handler(message: types.Message):
    text = """Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await message.answer("Ortga qaytdingiz menu tanlang")
    await message.answer(text, reply_markup=menu)



@dp.message_handler(text='🏃🏽‍♂️ Borib olish')
async def manzil_handler(message: types.Message):
    text = """Borib olish uchun geo-joylashuvni jo'nating, sizga yaqin bo'lgan filialni aniqlaymiz"""
    await message.answer(text, reply_markup=boribolish)


@dp.message_handler(text='⬅️ Ortga')
async def manzil_handler(message: types.Message):
    text = """Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await message.answer("Ortga qaytdingiz, menu tanlang")
    await message.answer(text, reply_markup=menu)


@dp.callback_query_handler(lambda c: c.data == 'biz haqimizda')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.

Qaynoqqina va mazali lavashlarimiz, shaurmayu donerlarimiz, gamburger va pitsalarimizdan albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!

Yetkazib berish xizmati:  +998781500030
Sayt (https://oqtepalavash.uz/) | Facebook (http://fb.me/oqtepalavash.official) | Instagram (https://www.instagram.com/oqtepalavash.official)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=Asosiy)
    await bot.answer_callback_query(callback_query.id)

@dp.callback_query_handler(lambda c: c.data == '⬅️ Ortga')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=menu)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Buyurtmalarim')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = "Siz hali hanuz birorta ham buyurtma bermagansiz"
    await bot.send_message(callback_query.from_user.id, text,reply_markup=menu)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'filialar')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = "Bizning filiallarimiz : 84 (1-10)"
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'Beruniy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Beruniy

📍 Ташкент, улица Беруни, 47  (http://maps.yandex.ru/?text=41.344468,69.205111)

🕑 10:00-22:00

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Algoritm')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Algoritm

📍 Ташкент, Чиланзарский район, махалля Бахористон махалля Бахористон (http://maps.yandex.ru/?text=41.262952,69.161994)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Andijon1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Andijon 1

📍 Андижан, улица Машраба, 62  (http://maps.yandex.ru/?text=40.751609,72.363240)

🕑 10:00-02:45

Bizning filiallarimiz : 84 (1-10)

Яндекс Карты (http://maps.yandex.ru/?text=40.751609,72.363240)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Andijon2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Andijon 2

📍 ул Машраб 22д (http://maps.yandex.ru/?text=40.751686,72.358418)

🕑 10:00-02:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Aviasozlar bozori')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Aviasozlar bozori

📍 Ташкент, 6-й проезд Бирлашган  (http://maps.yandex.ru/?text=41.286193,69.350026)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Bodomzor')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Bodomzor

📍 Ташкент, проспект Амира Темура, 98  (http://maps.yandex.ru/?text=41.337487,69.285620)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Bodomzor2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Bodomzor 2 

📍 Ташкент, проспект Амира Темура, 106  (http://maps.yandex.ru/?text=41.339567,69.285893)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Boka')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 BO'KA

📍 Ташкентская область, Букинский район, ул. Марказий, дом 6а (http://maps.yandex.ru/?text=40.812992,69.204796)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Chigatoy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Chigatoy

📍 Ташкент, улица Фараби  (http://maps.yandex.ru/?text=41.339299,69.220892)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'Chilonzor')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Chilonzor

📍 Ташкент, Чиланзарский район, массив Чиланзор, 16-й квартал, 18  (http://maps.yandex.ru/?text=41.272545,69.202428)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'ortga')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """Bizning filiallarimiz : 84 (1-10)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'kengisi')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """Bizning filiallarimiz : 84 (11-20)"""
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Chilonzor-19')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ Chilonzor-19

📍 Ташкент, улица Аль-Хорезми, 66/1  (http://maps.yandex.ru/?text=41.269353,69.191065)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Chinoz')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Chinoz

📍 Ташкентская область, Чиназ  (http://maps.yandex.ru/?text=40.940227,68.758729)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Chirchiq')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Chirchiq

📍 Ташкентская область, Чирчик  (http://maps.yandex.ru/?text=41.478039,69.590430)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Chopon ota')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """🏠 Cho'pon ota

📍 Ташкент, Чиланзарский район, махалля Лутфий махалля Лутфий (http://maps.yandex.ru/?text=41.293441,69.194863)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=text, reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)




@dp.callback_query_handler(lambda c: c.data == 'Chorsu')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Chorsu

📍 Ташкент, Шайхантахурский район, махалля Коратош махалля Коратош (http://maps.yandex.ru/?text=41.319572,69.233851)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)




@dp.callback_query_handler(lambda c: c.data == 'Compass Mall')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Compass Mall

📍 Ташкент, Ташкентская кольцевая автомобильная дорога, 17  (http://maps.yandex.ru/?text=41.239219,69.328495)

🕑 10:00-22:00

Bizning filiallarimiz : 84 (11-20)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)




@dp.callback_query_handler(lambda c: c.data == 'Depo Mall')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Depo Mall

📍 Ташкент, кладбище при мечети Абдуллаха ибн-Масуда кладбище при мечети Абдуллаха ибн-Масуда (http://maps.yandex.ru/?text=41.272888,69.170522)

🕑 10:00-22:00

Bizning filiallarimiz : 84 (11-20)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'Dombirabod')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Do'mbirobod

📍 Ташкент, улица Наккашлык, 1  (http://maps.yandex.ru/?text=41.254446,69.203177)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'Erkin')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Erkin

📍 Ташкент, улица Катта халка йули  (http://maps.yandex.ru/?text=41.230335%20,69.172604)

🕑 10:00-04:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'Fargona1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """ 🏠 Farg'ona 1

📍 Фергана, улица Сайилгох, 42  (http://maps.yandex.ru/?text=40.385422,71.785506)

🕑 10:00-02:45

Bizning filiallarimiz : 84 (11-20)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=manzil2)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'ortga')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await bot.send_message(callback_query.from_user.id, text,reply_markup=menu)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'Sozlamalar')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = """Muloqot tili: 🇺🇿 O'zbekcha
Telefon: +998994400070
Shahar: Tashkent

Quyidagilardan birini tanlang"""
    await bot.send_message(callback_query.from_user.id, text, reply_markup=sozlamalar)
    await bot.answer_callback_query(callback_query.id)



@dp.callback_query_handler(lambda c: c.data == 'Asosiy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text="""Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)"""
    await bot.send_message(callback_query.from_user.id,text,reply_markup=menu)
    await bot.answer_callback_query(callback_query.id)

