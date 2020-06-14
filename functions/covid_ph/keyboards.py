from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_cases_markup():
    markup = InlineKeyboardMarkup()
    cebu_city = InlineKeyboardButton("Cebu City",
                                     callback_data="cc")
    mandaue_city = InlineKeyboardButton("Mandaue City",
                                        callback_data="mc")
    lapu_lapu_city = InlineKeyboardButton("Lapu-lapu City",
                                          callback_data="llc")
    markup.add(cebu_city, mandaue_city, lapu_lapu_city)
    return markup
