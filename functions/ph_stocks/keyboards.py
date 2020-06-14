from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_addtl_info_markup(stock):
    markup = InlineKeyboardMarkup(row_width=1)
    more_info = InlineKeyboardButton("More Info",
                                     callback_data=f"more_{stock}")
    fundamental = InlineKeyboardButton("Fundamental",
                                       callback_data=f"fundamental_{stock}")
    technical = InlineKeyboardButton("Technical",
                                     callback_data=f"technical_{stock}")
    markup.add(more_info, fundamental, technical)
    return markup
