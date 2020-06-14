import configparser

import telebot

from utils import can_reply_to_chat_id
from functions.covid_ph.processor import (process_get_cases,
                                          process_update_csv_id)
from functions.covid_ph.callback_handler import handle_get_cases_by_city
from functions.ph_stocks.processor import process_get_stock_update
from functions.ph_stocks.callback_handler import handle_get_addtl_info

config = configparser.ConfigParser()
config.read('config.ini')
token = config.get('DEFAULT', 'token')
bot = telebot.TeleBot(token)


@bot.message_handler(func=can_reply_to_chat_id, commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! Welcome!")


# functions: covid_ph - Covid-19 stats in Metro Cebu commands
#
# Updates CSV file containing latest data
@bot.message_handler(func=can_reply_to_chat_id, commands=['updateCsvId'])
def update_csv_id(message):
    process_update_csv_id(bot, message)


# Returns an InlineKeyboard buttons one of each city. On click show the
# stats of each selected city
@bot.message_handler(func=can_reply_to_chat_id, commands=['getCases'])
def get_cases(message):
    process_get_cases(bot, message)


# Handles selected InlineKeyboardButton of /getCases
@bot.callback_query_handler(func=lambda query: query.data in
                            ["cc", "mc", "llc"])
def get_cases_by_city(query):
    handle_get_cases_by_city(bot, query)


# functions: ph_stocks - send price update of specific PH stocks
#
# /stock {SYMBOL} - gets details of given stock
@bot.message_handler(func=can_reply_to_chat_id, commands=['stock'])
def get_stock_update(message):
    process_get_stock_update(bot, message)


# Handles selected InlineKeyboardButton of /stock
@bot.callback_query_handler(func=lambda query:
                            query.data.split('_')[0]
                            in ['more', 'fundamental', 'technical'])
def get_addtl_info(query):
    handle_get_addtl_info(bot, query)


if __name__ == '__main__':
    bot.polling()
