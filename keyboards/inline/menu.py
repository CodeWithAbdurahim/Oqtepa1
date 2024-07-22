from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('🛒Buyurtma berish', callback_data='Buyurtma berish')],
        [InlineKeyboardButton("🔔 Biz haqimizda", callback_data='biz haqimizda'),
         InlineKeyboardButton("🛍 Buyurtmalarim", callback_data='Buyurtmalarim')],
        [InlineKeyboardButton("🏚FILIALAR", callback_data='filialar')],
        [InlineKeyboardButton("📝 Fikir qoldirish",url='https://oqtepalavash.uz/'),
         InlineKeyboardButton("⚙️ Sozlamalar", callback_data='Sozlamalar')],
    ]
)
Asosiy=InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton('⬅️ Ortga',callback_data='⬅️ Ortga')]
  ],

)

sozlamalar=InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton("Muloqot tili",callback_data="Muloqot tili"),
    InlineKeyboardButton("Telefon",callback_data="Telefon"),
    InlineKeyboardButton("Shahar",callback_data="Shahar")],
    [InlineKeyboardButton("Asosiy",callback_data='Asosiy')]
  ]
)

