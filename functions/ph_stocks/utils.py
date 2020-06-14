import requests


def get_page_content_from_investagram(stock):
    page = requests.get(f"https://www.investagrams.com/Stock/{stock}")

    if page.ok:
        return page.content
    return None


def get_text_by_id(soup, id):
    return soup.find(id=id).get_text()


def get_stock_name(soup):
    return soup.find('h4', class_="mb-0").find('small').get_text()


def check_if_stock_exists(soup):
    s = soup.find_all(id='lblStockLatestLastPrice')
    if s:
        return True
    return False
