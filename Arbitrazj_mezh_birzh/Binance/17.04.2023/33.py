import time
import datetime
import json
import websocket
from threading import *
import sqlite3
from binance.client import Client

api_key = "A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG"
secret_key = "zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA"

client = Client(
    api_key,
    secret_key
)

db = sqlite3.connect('../../db_sql/main.db')
sql = db.cursor()


# tickers = client.get_orderbook_ticker()

binance_get_all_symboll = '../Binance/Binance_get_all_symboll.json'


def f_file_binance_get_all_symboll():
    with open(binance_get_all_symboll) as file_data:
        data_a = json.load(file_data)

    return data_a



coin = 'btcusdt'

socket1 = f'wss://stream.binance.com:9443/ws/{symbol}@bookTicker'

ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHUSDT)

# for i in f_file_binance_get_all_symboll():
#     print(i['symbol'])

# def on_message_ETHUSDT(ws, message):
#
#     data = json.loads(message)
#     print(data)
#
# def loop_ETHUSDT():
#     for i in f_file_binance_get_all_symboll():
#         s = i['symbol']
#         symbol = s.lower()
#         # a = symbol
#         socket1 = f'wss://stream.binance.com:9443/ws/{symbol}@bookTicker'
#         ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHUSDT)
#         # ws.run_forever()
#
#
# symbol = loop_ETHUSDT()
# for i in f_file_binance_get_all_symboll():
#     s = i['symbol']
#     symbol = s.lower()
#     print(symbol)
#     test = loop_ETHUSDT(symbol)
#     # break
# print('##########')
# count = 0
# start_time = time.time()
# for i in tickers:
#
#
#     for ii in f_file_binance_get_all_symboll():
#
#         if i['symbol'] == ii['symbol']:
#             pass

#             sql.execute(F"SELECT symbol FROM binance_get_orderbook_ticker WHERE symbol = '{i['symbol']}'")
#
#             if sql.fetchone() is None:
#
#                 symbol = i['symbol']
#                 bidPrice = i['bidPrice']
#                 bidQty = i['bidQty']
#                 askPrice = i['askPrice']
#                 askQty = i['askQty']
#
#                 sql.execute(F"INSERT INTO binance_get_orderbook_ticker VALUES (NULL, ?, ?, ?, ?, ?)", (symbol, bidPrice, bidQty, askPrice, askQty))
#
#                 db.commit()
#
#             else:
#
#                 symbol = i['symbol']
#                 bidPrice = i['bidPrice']
#                 bidQty = i['bidQty']
#                 askPrice = i['askPrice']
#                 askQty = i['askQty']
#
#                 sql.execute(F"UPDATE binance_get_orderbook_ticker SET bidPrice = {bidPrice}, bidQty = {bidQty}, askPrice = {askPrice}, askQty = {askQty} WHERE symbol = '{symbol}'")
#                 db.commit()
# db.close()
print((time.time() - start_time))

#     break

# api_key = 'A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG'
# secret_key = 'zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA'
#
# client = Client(api_key, secret_key)
#
#
# def on_message_ETHUSDT(ws, message):
#
#     data = json.loads(message)
#     print(data)
#
#
# def loop_ETHUSDT():
#
#     socket1 = f'wss://stream.binance.com:9443/ws/@bookTicker'
#     ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHUSDT)
#     ws.run_forever()
#
# Thread(target=loop_ETHUSDT).start()