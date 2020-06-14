from bs4 import BeautifulSoup

from utils import extract_message
from functions.ph_stocks.keyboards import get_addtl_info_markup
from functions.ph_stocks.utils import (get_page_content_from_investagram,
                                       get_text_by_id, get_stock_name,
                                       check_if_stock_exists)


def process_get_stock_update(bot, message):
    stock = extract_message(message.text)
    # investagrams url
    # page = requests.get(f"https://www.investagrams.com/Stock/{stock}")
    content = get_page_content_from_investagram(stock)
    soup = BeautifulSoup(content, 'html.parser')
    stock_exists = check_if_stock_exists(soup)

    if stock_exists:
        name = get_stock_name(soup)
        last_price = get_text_by_id(soup, 'lblStockLatestLastPrice')
        open_price = get_text_by_id(soup, 'lblStockLatestOpen')
        low_price = get_text_by_id(soup, 'lblStockLatestLow')
        high_price = get_text_by_id(soup, 'lblStockLatestHigh')
        ave_price = get_text_by_id(soup, 'lblStockLatestAverage')
        send_text = f"{name}\n" \
                    f"Price: {last_price}\n" \
                    f"Open Price: {open_price}\n" \
                    f"Low Price: {low_price}\n" \
                    f"High Price: {high_price}\n" \
                    f"Average Price: {ave_price}\n"
        bot.send_message(message.chat.id, send_text,
                         reply_markup=get_addtl_info_markup(stock))
    else:
        bot.send_message(message.chat.id, "Stock symbol invalid.")
