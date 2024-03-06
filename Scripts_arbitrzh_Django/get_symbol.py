# import requests
# from bs4 import BeautifulSoup
#
#
# # def test (coins):
# # result = {}
# # html_resp = requests.get("https://coinmarketcap.com/ru/")
# # block = BeautifulSoup(html_resp, "lxml")
# # # block = {}
# # rows = block.findAll("head", "title")
# # print(rows)
# #
# # print(rows)
#
#     # for i in  rows:
#     #     test = i.find("div", class_="sc-feda9013-2 dxcftz")
#     #     print(test)
#
# # html_resp = requests.get("https://cryptomint.top/strategy/inside").text
# # block = BeautifulSoup(html_resp, "lxml")
# # # block = {}
# # rows = block.findAll("div", class_="page_nav")
# # print(rows)
#
#
#
# html_resp = requests.get("https://coinmarketcap.com/ru/").text
# block = BeautifulSoup(html_resp, "lxml")
# # block = {}
# rows = block.findAll("img", class_="coin-logo")
# for i in rows:
#     a = i
#     print(i)
import time

import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sqlite3

with sqlite3.connect('../test_site/arbitrazh.db') as connect_db:
    cursor = connect_db.cursor()
    cursor.execute(F"SELECT * FROM arbitrazh_binance_all_pairs_trading_inf")
    bd_binance_all_pairs_trading_inf = cursor.fetchall()

    for i in bd_binance_all_pairs_trading_inf:
        # print(i[5])
        symbol = i[5]

        allMainCurrency = []
        for i in bd_binance_all_pairs_trading_inf:
            # print(i['quoteAsset_a'])

            if i[5] in allMainCurrency:
                pass
            else:
                allMainCurrency.append(i[5])
            if i[4] in allMainCurrency:
                pass
            else:
                allMainCurrency.append(i[4])



# count = 0

for i in allMainCurrency:

    # symbol = str(i)
    # count += 1

    print(i)
    try:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
        # parameters = {
        #   'start':'1',
        #   'limit':'5000',
        #   'convert':'USD'
        # }
        parameters = {
            'symbol':   str(i),

        }

        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': 'ffaff9ff-da78-4f0f-8756-50378f5315b9',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            img_url = json.loads(response.text)['data'][symbol]['logo']

            response = requests.get(url=img_url)
            with open('../test_site/main/static/main/images/coin_logo/' + symbol + '.png', 'wb') as file:
                file.write(response.content)


        except (ConnectionError, Timeout, TooManyRedirects) as e:
        #   print(e)
            pass

    except:
        pass
    time.sleep(5)

# print(count)
