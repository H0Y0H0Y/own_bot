from bs4 import BeautifulSoup

from functions.ph_stocks.utils import (get_page_content_from_investagram,
                                       get_text_by_id, get_stock_name,
                                       check_if_stock_exists)


def handle_get_addtl_info(bot, query):
    action = query.data.split('_')[0]
    stock = query.data.split('_')[1]
    content = get_page_content_from_investagram(stock)
    soup = BeautifulSoup(content, 'html.parser')
    stock_exists = check_if_stock_exists(soup)
    if stock_exists:
        soup = BeautifulSoup(content, 'html.parser')
        name = get_stock_name(soup)
        if action == "more":
            volume = get_text_by_id(soup, 'lblStockLatestVolume')
            value = get_text_by_id(soup, 'lblStockLatestValue')
            market_cap = get_text_by_id(soup, 'lblStockLatestMarketCap')
            prev_close = get_text_by_id(soup, 'lblStockLatestClose')
            net_foreign = get_text_by_id(soup, 'lblStockLatestNetForeign')

            send_text = f"{name}\n" \
                        f"Volume: {volume}\n" \
                        f"Value: {value}\n" \
                        f"Market Cap: {market_cap}\n" \
                        f"Previous Closing Price: {prev_close}\n" \
                        f"Net foreign buying: {net_foreign}"

            bot.send_message(query.message.chat.id, send_text)

        if action == "fundamental":
            fundamental = soup.find('div', id='FundamentalAnalysisContent')
            fundamental_info = fundamental.find_all('td')
            high_52_week = fundamental_info[1].get_text()
            eps = fundamental_info[3].get_text()
            price_to_book = fundamental_info[5].get_text()
            low_52_week = fundamental_info[7].get_text()
            price_earning = fundamental_info[9].get_text()
            return_on_equity = fundamental_info[11].get_text()
            fair_value = fundamental_info[13].get_text()
            div_per_share = fundamental_info[15].get_text()

            send_text = f"{name}\n" \
                        f"52-week High: {high_52_week}\n" \
                        f"52-week Low: {low_52_week}\n" \
                        f"Earnings Per Share: {eps}\n" \
                        f"Price to Book Value (P/BV): {price_to_book}\n" \
                        f"Price-Earnings Ratio (P/E): {price_earning}\n" \
                        f"Return on Equity (ROE): {return_on_equity}\n" \
                        f"Fair Value: {fair_value}\n" \
                        f"Dividends Per Share (DPS): {div_per_share}"

            bot.send_message(query.message.chat.id, send_text)

        if action == "technical":
            technical = soup.find('div', id='TechnicalAnalysisContent')
            technical_info = technical.find_all('td')
            supports = technical_info[1].get_text() + ", " + \
                technical_info[7].get_text()
            resistances = technical_info[3].get_text() + ", " + \
                technical_info[9].get_text()
            short_term = technical_info[5].get_text()
            medium_term = technical_info[11].get_text()

            send_text = f"{name}\n" \
                        f"Support: {supports}\n" \
                        f"Resistance: {resistances}\n" \
                        f"Short-term Trend: {short_term}\n" \
                        f"Medium-term Trend: {medium_term}"

            bot.send_message(query.message.chat.id, send_text)

    else:
        bot.send_message(query.message.chat.id, "No data found.")
