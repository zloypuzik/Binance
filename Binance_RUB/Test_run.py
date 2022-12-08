import time
import datetime
import json
import websocket
import asyncio
from threading import *
import datetime
from binance.client import Client
from binance.client import Client


def f_minqty_size_up(kolichestvo, stepSize):
    def adjust_to_step(value, step, increase=True):
        return ((int(value * 100000000) - int(value * 100000000) % int(
            float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)

    sell_amount_a = adjust_to_step(kolichestvo, stepSize)

    return sell_amount_a


def f_minqty_size_down(kolichestvo, stepSize):
    def adjust_to_step(value, step, increase=False):
        return ((int(value * 100000000) - int(value * 100000000) % int(
            float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)

    sell_amount_a = adjust_to_step(kolichestvo, stepSize)

    return sell_amount_a


api_key = 'A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG'
secret_key = 'zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA'

client = Client(api_key, secret_key)

usdt_count = float(11.0)

all_pribil = float(0.0)

symbol_c_g_RUB_USDT = 'RUBUSDT'
price_bids_c_g_RUB_USDT = float(0.0)
qty_bids_c_g_RUB_USDT = float(0.0)
price_asks_c_g_RUB_USDT = float(0.0)
qty_asks_c_g_RUB_USDT = float(0.0)
stepSize_RUB_USDT = '0.00001000'


def on_message_RUB_USDT(ws, message):
    data = json.loads(message)

    symbol_c_l_RUB_USDT = 'RUBUSDT'
    price_bids_c_l_RUB_USDT = data['bids'][0][0]
    qty_bids_c_l_RUB_USDT = data['bids'][0][1]
    price_asks_c_l_RUB_USDT = data['asks'][0][0]
    qty_asks_c_l_RUB_USDT = data['asks'][0][1]

    global symbol_c_g_RUB_USDT
    global price_bids_c_g_RUB_USDT
    global qty_bids_c_g_RUB_USDT
    global price_asks_c_g_RUB_USDT
    global qty_asks_c_g_RUB_USDT

    symbol_c_g_RUB_USDT = symbol_c_l_RUB_USDT
    price_bids_c_g_RUB_USDT = price_bids_c_l_RUB_USDT
    qty_bids_c_g_RUB_USDT = qty_bids_c_l_RUB_USDT
    price_asks_c_g_RUB_USDT = price_asks_c_l_RUB_USDT
    qty_asks_c_g_RUB_USDT = qty_asks_c_l_RUB_USDT


def loop_RUB_USDT():
    socket1 = f'wss://stream.binance.com:9443/ws/usdtrub@depth5@100ms'
    ws = websocket.WebSocketApp(socket1, on_message=on_message_RUB_USDT)
    ws.run_forever()


Thread(target=loop_RUB_USDT).start()

symbol_c_g_BUSD_USDT = 'RUBUSDT'
price_bids_c_g_BUSD_USDT = float(0.0)
qty_bids_c_g_BUSD_USDT = float(0.0)
price_asks_c_g_BUSD_USDT = float(0.0)
qty_asks_c_g_BUSD_USDT = float(0.0)
stepSize_BUSD_USDT = '0.00001000'


def on_message_BUSD_USDT(ws, message):
    data = json.loads(message)

    symbol_c_l_BUSD_USDT = 'BTCUSDT'
    price_bids_c_l_BUSD_USDT = data['bids'][0][0]
    qty_bids_c_l_BUSD_USDT = data['bids'][0][1]
    price_asks_c_l_BUSD_USDT = data['asks'][0][0]
    priqty_asks_c_l_BUSD_USDT = data['asks'][0][1]

    global symbol_c_g_BUSD_USDT
    global price_bids_c_g_BUSD_USDT
    global qty_bids_c_g_BUSD_USDT
    global price_asks_c_g_BUSD_USDT
    global qty_asks_c_g_BUSD_USDT

    symbol_c_g_BUSD_USDT = symbol_c_l_BUSD_USDT
    price_bids_c_g_BUSD_USDT = price_bids_c_l_BUSD_USDT
    qty_bids_c_g_BUSD_USDT = qty_bids_c_l_BUSD_USDT
    price_asks_c_g_BUSD_USDT = price_asks_c_l_BUSD_USDT
    qty_asks_c_g_BUSD_USDT = priqty_asks_c_l_BUSD_USDT


def loop_BUSD_USDT():
    socket1 = f'wss://stream.binance.com:9443/ws/busdusdt@depth5@100ms'
    ws = websocket.WebSocketApp(socket1, on_message=on_message_BUSD_USDT)
    ws.run_forever()


Thread(target=loop_BUSD_USDT).start() \
 \
symbol_c_g_BNB_USDT = 'BTCUSDT'
price_bids_c_g_BNB_USDT = float(0.0)
qty_bids_c_g_BNB_USDT = float(0.0)
price_asks_c_g_BNB_USDT = float(0.0)
qty_asks_c_g_BNB_USDT = float(0.0)
stepSize_BNB_USDT = '0.00001000'


def on_message_BNB_USDT(ws, message):
    data = json.loads(message)

    symbol_c_l_BNB_USDT = 'BTCUSDT'
    price_bids_c_l_BNB_USDT = data['bids'][0][0]
    qty_bids_c_l_BNB_USDT = data['bids'][0][1]
    price_asks_c_l_BNB_USDT = data['asks'][0][0]
    qty_asks_c_l_BNB_USDT = data['asks'][0][1]

    global symbol_c_g_BNB_USDT
    global price_bids_c_g_BNB_USDT
    global qty_bids_c_g_BNB_USDT
    global price_asks_c_g_BNB_USDT
    global qty_asks_c_g_BNB_USDT

    symbol_c_g_BNB_USDT = symbol_c_l_BNB_USDT
    price_bids_c_g_BNB_USDT = price_bids_c_l_BNB_USDT
    qty_bids_c_g_BNB_USDT = qty_bids_c_l_BNB_USDT
    price_asks_c_g_BNB_USDT = price_asks_c_l_BNB_USDT
    qty_asks_c_g_BNB_USDT = qty_asks_c_l_BNB_USDT


def loop_BNB_USDT():
    socket1 = f'wss://stream.binance.com:9443/ws/bnbusdt@depth5@100ms'
    ws = websocket.WebSocketApp(socket1, on_message=on_message_BNB_USDT)
    ws.run_forever()


Thread(target=loop_BNB_USDT).start()

symbol_c_g_AUD_USDT = 'BTCUSDT'
price_bids_c_g_AUD_USDT = float(0.0)
qty_bids_c_g_AUD_USDT = float(0.0)
price_asks_c_g_AUD_USDT = float(0.0)
qty_asks_c_g_AUD_USDT = float(0.0)
stepSize_AUD_USDT = '0.00001000'


def on_message_AUD_USDT(ws, message):
    data = json.loads(message)

    symbol_c_l_AUD_USDT = 'BTCUSDT'
    price_bids_c_l_AUD_USDT = data['bids'][0][0]
    qty_bids_c_l_AUD_USDT = data['bids'][0][1]
    price_asks_c_l_AUD_USDT = data['asks'][0][0]
    qty_asks_c_l_AUD_USDT = data['asks'][0][1]

    global symbol_c_g_AUD_USDT
    global price_bids_c_g_AUD_USDT
    global qty_bids_c_g_AUD_USDT
    global price_asks_c_g_AUD_USDT
    global qty_asks_c_g_AUD_USDT

    symbol_c_g_AUD_USDT = symbol_c_l_AUD_USDT
    price_bids_c_g_AUD_USDT = price_bids_c_l_AUD_USDT
    qty_bids_c_g_AUD_USDT = qty_bids_c_l_AUD_USDT
    price_asks_c_g_AUD_USDT = price_asks_c_l_AUD_USDT
    qty_asks_c_g_AUD_USDT = qty_asks_c_l_AUD_USDT


def loop_AUD_USDT():
    socket1 = f'wss://stream.binance.com:9443/ws/btcusdt@depth5@100ms'
    ws = websocket.WebSocketApp(socket1, on_message=on_message_AUD_USDT)
    ws.run_forever()


Thread(target=loop_AUD_USDT).start()
