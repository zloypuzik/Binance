import time
import datetime
import json
import websocket
import asyncio
from threading import *
import datetime
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

symbol_c_g_BTCUSDT = 'BTCUSDT'
price_bids_c_g_BTCUSDT = float(0.0)
qty_bids_c_g_BTCUSDT = float(0.0)
price_asks_c_g_BTCUSDT = float(0.0)
qty_asks_c_g_BTCUSDT = float(0.0)
stepSize_BTCUSDT = '0.00001000'

def on_message_BTCUSDT(ws, message):
	#locker.acquire()
	data = json.loads(message)

	symbol_c_l_BTCUSDT = 'BTCUSDT'
	price_bids_c_l_BTCUSDT = data['bids'][0][0]
	qty_bids_c_l_BTCUSDT = data['bids'][0][1]
	price_asks_c_l_BTCUSDT = data['asks'][0][0]
	qty_asks_c_l_BTCUSDT = data['asks'][0][1]

	global symbol_c_g_BTCUSDT
	global price_bids_c_g_BTCUSDT
	global qty_bids_c_g_BTCUSDT
	global price_asks_c_g_BTCUSDT
	global qty_asks_c_g_BTCUSDT

	symbol_c_g_BTCUSDT = symbol_c_l_BTCUSDT
	price_bids_c_g_BTCUSDT= price_bids_c_l_BTCUSDT
	qty_bids_c_g_BTCUSDT= qty_bids_c_l_BTCUSDT
	price_asks_c_g_BTCUSDT = price_asks_c_l_BTCUSDT
	qty_asks_c_g_BTCUSDT= qty_asks_c_l_BTCUSDT
	#locker.release()

def loop_BTCUSDT():
	socket1 = f'wss://stream.binance.com:9443/ws/btcusdt@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_BTCUSDT)
	ws.run_forever()

Thread(target=loop_BTCUSDT).start()
