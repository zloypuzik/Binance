import time
import datetime
import json
import websocket
from threading import *
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

usdt_count = float(0.01)

all_pribil = float(0.0)

symbol_c_g_ETHBTC = 'ETHBTC'
price_bids_c_g_ETHBTC = float(0.0)
qty_bids_c_g_ETHBTC = float(0.0)
price_asks_c_g_ETHBTC = float(0.0)
qty_asks_c_g_ETHBTC = float(0.0)
stepSize_ETHBTC = '0.00010000'


def on_message_ETHBTC(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHBTC = 'ETHBTC'
	price_bids_c_l_ETHBTC = data['bids'][0][0]
	qty_bids_c_l_ETHBTC = data['bids'][0][1]
	price_asks_c_l_ETHBTC = data['asks'][0][0]
	qty_asks_c_l_ETHBTC = data['asks'][0][1]

	global symbol_c_g_ETHBTC
	global price_bids_c_g_ETHBTC
	global qty_bids_c_g_ETHBTC
	global price_asks_c_g_ETHBTC
	global qty_asks_c_g_ETHBTC

	symbol_c_g_ETHBTC = symbol_c_l_ETHBTC
	price_bids_c_g_ETHBTC = price_bids_c_l_ETHBTC
	qty_bids_c_g_ETHBTC = qty_bids_c_l_ETHBTC
	price_asks_c_g_ETHBTC = price_asks_c_l_ETHBTC
	qty_asks_c_g_ETHBTC = qty_asks_c_l_ETHBTC


def loop_ETHBTC():

	socket1 = f'wss://stream.binance.com:9443/ws/ethbtc@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHBTC)
	ws.run_forever()


Thread(target=loop_ETHBTC).start()

symbol_c_g_ETHUSDT = 'ETHUSDT'
price_bids_c_g_ETHUSDT = float(0.0)
qty_bids_c_g_ETHUSDT = float(0.0)
price_asks_c_g_ETHUSDT = float(0.0)
qty_asks_c_g_ETHUSDT = float(0.0)
stepSize_ETHUSDT = '0.00010000'


def on_message_ETHUSDT(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHUSDT = 'ETHUSDT'
	price_bids_c_l_ETHUSDT = data['bids'][0][0]
	qty_bids_c_l_ETHUSDT = data['bids'][0][1]
	price_asks_c_l_ETHUSDT = data['asks'][0][0]
	qty_asks_c_l_ETHUSDT = data['asks'][0][1]

	global symbol_c_g_ETHUSDT
	global price_bids_c_g_ETHUSDT
	global qty_bids_c_g_ETHUSDT
	global price_asks_c_g_ETHUSDT
	global qty_asks_c_g_ETHUSDT

	symbol_c_g_ETHUSDT = symbol_c_l_ETHUSDT
	price_bids_c_g_ETHUSDT = price_bids_c_l_ETHUSDT
	qty_bids_c_g_ETHUSDT = qty_bids_c_l_ETHUSDT
	price_asks_c_g_ETHUSDT = price_asks_c_l_ETHUSDT
	qty_asks_c_g_ETHUSDT = qty_asks_c_l_ETHUSDT


def loop_ETHUSDT():

	socket1 = f'wss://stream.binance.com:9443/ws/ethusdt@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHUSDT)
	ws.run_forever()


Thread(target=loop_ETHUSDT).start()

symbol_c_g_ETHBUSD = 'ETHBUSD'
price_bids_c_g_ETHBUSD = float(0.0)
qty_bids_c_g_ETHBUSD = float(0.0)
price_asks_c_g_ETHBUSD = float(0.0)
qty_asks_c_g_ETHBUSD = float(0.0)
stepSize_ETHBUSD = '0.00010000'


def on_message_ETHBUSD(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHBUSD = 'ETHBUSD'
	price_bids_c_l_ETHBUSD = data['bids'][0][0]
	qty_bids_c_l_ETHBUSD = data['bids'][0][1]
	price_asks_c_l_ETHBUSD = data['asks'][0][0]
	qty_asks_c_l_ETHBUSD = data['asks'][0][1]

	global symbol_c_g_ETHBUSD
	global price_bids_c_g_ETHBUSD
	global qty_bids_c_g_ETHBUSD
	global price_asks_c_g_ETHBUSD
	global qty_asks_c_g_ETHBUSD

	symbol_c_g_ETHBUSD = symbol_c_l_ETHBUSD
	price_bids_c_g_ETHBUSD = price_bids_c_l_ETHBUSD
	qty_bids_c_g_ETHBUSD = qty_bids_c_l_ETHBUSD
	price_asks_c_g_ETHBUSD = price_asks_c_l_ETHBUSD
	qty_asks_c_g_ETHBUSD = qty_asks_c_l_ETHBUSD


def loop_ETHBUSD():

	socket1 = f'wss://stream.binance.com:9443/ws/ethbusd@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHBUSD)
	ws.run_forever()


Thread(target=loop_ETHBUSD).start()

symbol_c_g_BNBETH = 'BNBETH'
price_bids_c_g_BNBETH = float(0.0)
qty_bids_c_g_BNBETH = float(0.0)
price_asks_c_g_BNBETH = float(0.0)
qty_asks_c_g_BNBETH = float(0.0)
stepSize_BNBETH = '0.00100000'


def on_message_BNBETH(ws, message):

	data = json.loads(message)

	symbol_c_l_BNBETH = 'BNBETH'
	price_bids_c_l_BNBETH = data['bids'][0][0]
	qty_bids_c_l_BNBETH = data['bids'][0][1]
	price_asks_c_l_BNBETH = data['asks'][0][0]
	qty_asks_c_l_BNBETH = data['asks'][0][1]

	global symbol_c_g_BNBETH
	global price_bids_c_g_BNBETH
	global qty_bids_c_g_BNBETH
	global price_asks_c_g_BNBETH
	global qty_asks_c_g_BNBETH

	symbol_c_g_BNBETH = symbol_c_l_BNBETH
	price_bids_c_g_BNBETH = price_bids_c_l_BNBETH
	qty_bids_c_g_BNBETH = qty_bids_c_l_BNBETH
	price_asks_c_g_BNBETH = price_asks_c_l_BNBETH
	qty_asks_c_g_BNBETH = qty_asks_c_l_BNBETH


def loop_BNBETH():

	socket1 = f'wss://stream.binance.com:9443/ws/bnbeth@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_BNBETH)
	ws.run_forever()


Thread(target=loop_BNBETH).start()

symbol_c_g_ETHEUR = 'ETHEUR'
price_bids_c_g_ETHEUR = float(0.0)
qty_bids_c_g_ETHEUR = float(0.0)
price_asks_c_g_ETHEUR = float(0.0)
qty_asks_c_g_ETHEUR = float(0.0)
stepSize_ETHEUR = '0.00010000'


def on_message_ETHEUR(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHEUR = 'ETHEUR'
	price_bids_c_l_ETHEUR = data['bids'][0][0]
	qty_bids_c_l_ETHEUR = data['bids'][0][1]
	price_asks_c_l_ETHEUR = data['asks'][0][0]
	qty_asks_c_l_ETHEUR = data['asks'][0][1]

	global symbol_c_g_ETHEUR
	global price_bids_c_g_ETHEUR
	global qty_bids_c_g_ETHEUR
	global price_asks_c_g_ETHEUR
	global qty_asks_c_g_ETHEUR

	symbol_c_g_ETHEUR = symbol_c_l_ETHEUR
	price_bids_c_g_ETHEUR = price_bids_c_l_ETHEUR
	qty_bids_c_g_ETHEUR = qty_bids_c_l_ETHEUR
	price_asks_c_g_ETHEUR = price_asks_c_l_ETHEUR
	qty_asks_c_g_ETHEUR = qty_asks_c_l_ETHEUR


def loop_ETHEUR():

	socket1 = f'wss://stream.binance.com:9443/ws/etheur@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHEUR)
	ws.run_forever()


Thread(target=loop_ETHEUR).start()

symbol_c_g_ETHTRY = 'ETHTRY'
price_bids_c_g_ETHTRY = float(0.0)
qty_bids_c_g_ETHTRY = float(0.0)
price_asks_c_g_ETHTRY = float(0.0)
qty_asks_c_g_ETHTRY = float(0.0)
stepSize_ETHTRY = '0.00010000'


def on_message_ETHTRY(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHTRY = 'ETHTRY'
	price_bids_c_l_ETHTRY = data['bids'][0][0]
	qty_bids_c_l_ETHTRY = data['bids'][0][1]
	price_asks_c_l_ETHTRY = data['asks'][0][0]
	qty_asks_c_l_ETHTRY = data['asks'][0][1]

	global symbol_c_g_ETHTRY
	global price_bids_c_g_ETHTRY
	global qty_bids_c_g_ETHTRY
	global price_asks_c_g_ETHTRY
	global qty_asks_c_g_ETHTRY

	symbol_c_g_ETHTRY = symbol_c_l_ETHTRY
	price_bids_c_g_ETHTRY = price_bids_c_l_ETHTRY
	qty_bids_c_g_ETHTRY = qty_bids_c_l_ETHTRY
	price_asks_c_g_ETHTRY = price_asks_c_l_ETHTRY
	qty_asks_c_g_ETHTRY = qty_asks_c_l_ETHTRY


def loop_ETHTRY():

	socket1 = f'wss://stream.binance.com:9443/ws/ethtry@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHTRY)
	ws.run_forever()


Thread(target=loop_ETHTRY).start()

symbol_c_g_ETHRUB = 'ETHRUB'
price_bids_c_g_ETHRUB = float(0.0)
qty_bids_c_g_ETHRUB = float(0.0)
price_asks_c_g_ETHRUB = float(0.0)
qty_asks_c_g_ETHRUB = float(0.0)
stepSize_ETHRUB = '0.00010000'


def on_message_ETHRUB(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHRUB = 'ETHRUB'
	price_bids_c_l_ETHRUB = data['bids'][0][0]
	qty_bids_c_l_ETHRUB = data['bids'][0][1]
	price_asks_c_l_ETHRUB = data['asks'][0][0]
	qty_asks_c_l_ETHRUB = data['asks'][0][1]

	global symbol_c_g_ETHRUB
	global price_bids_c_g_ETHRUB
	global qty_bids_c_g_ETHRUB
	global price_asks_c_g_ETHRUB
	global qty_asks_c_g_ETHRUB

	symbol_c_g_ETHRUB = symbol_c_l_ETHRUB
	price_bids_c_g_ETHRUB = price_bids_c_l_ETHRUB
	qty_bids_c_g_ETHRUB = qty_bids_c_l_ETHRUB
	price_asks_c_g_ETHRUB = price_asks_c_l_ETHRUB
	qty_asks_c_g_ETHRUB = qty_asks_c_l_ETHRUB


def loop_ETHRUB():

	socket1 = f'wss://stream.binance.com:9443/ws/ethrub@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHRUB)
	ws.run_forever()


Thread(target=loop_ETHRUB).start()

symbol_c_g_ETHGBP = 'ETHGBP'
price_bids_c_g_ETHGBP = float(0.0)
qty_bids_c_g_ETHGBP = float(0.0)
price_asks_c_g_ETHGBP = float(0.0)
qty_asks_c_g_ETHGBP = float(0.0)
stepSize_ETHGBP = '0.00010000'


def on_message_ETHGBP(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHGBP = 'ETHGBP'
	price_bids_c_l_ETHGBP = data['bids'][0][0]
	qty_bids_c_l_ETHGBP = data['bids'][0][1]
	price_asks_c_l_ETHGBP = data['asks'][0][0]
	qty_asks_c_l_ETHGBP = data['asks'][0][1]

	global symbol_c_g_ETHGBP
	global price_bids_c_g_ETHGBP
	global qty_bids_c_g_ETHGBP
	global price_asks_c_g_ETHGBP
	global qty_asks_c_g_ETHGBP

	symbol_c_g_ETHGBP = symbol_c_l_ETHGBP
	price_bids_c_g_ETHGBP = price_bids_c_l_ETHGBP
	qty_bids_c_g_ETHGBP = qty_bids_c_l_ETHGBP
	price_asks_c_g_ETHGBP = price_asks_c_l_ETHGBP
	qty_asks_c_g_ETHGBP = qty_asks_c_l_ETHGBP


def loop_ETHGBP():

	socket1 = f'wss://stream.binance.com:9443/ws/ethgbp@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHGBP)
	ws.run_forever()


Thread(target=loop_ETHGBP).start()

symbol_c_g_ETHBIDR = 'ETHBIDR'
price_bids_c_g_ETHBIDR = float(0.0)
qty_bids_c_g_ETHBIDR = float(0.0)
price_asks_c_g_ETHBIDR = float(0.0)
qty_asks_c_g_ETHBIDR = float(0.0)
stepSize_ETHBIDR = '0.00010000'


def on_message_ETHBIDR(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHBIDR = 'ETHBIDR'
	price_bids_c_l_ETHBIDR = data['bids'][0][0]
	qty_bids_c_l_ETHBIDR = data['bids'][0][1]
	price_asks_c_l_ETHBIDR = data['asks'][0][0]
	qty_asks_c_l_ETHBIDR = data['asks'][0][1]

	global symbol_c_g_ETHBIDR
	global price_bids_c_g_ETHBIDR
	global qty_bids_c_g_ETHBIDR
	global price_asks_c_g_ETHBIDR
	global qty_asks_c_g_ETHBIDR

	symbol_c_g_ETHBIDR = symbol_c_l_ETHBIDR
	price_bids_c_g_ETHBIDR = price_bids_c_l_ETHBIDR
	qty_bids_c_g_ETHBIDR = qty_bids_c_l_ETHBIDR
	price_asks_c_g_ETHBIDR = price_asks_c_l_ETHBIDR
	qty_asks_c_g_ETHBIDR = qty_asks_c_l_ETHBIDR


def loop_ETHBIDR():

	socket1 = f'wss://stream.binance.com:9443/ws/ethbidr@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHBIDR)
	ws.run_forever()


Thread(target=loop_ETHBIDR).start()

symbol_c_g_ETHAUD = 'ETHAUD'
price_bids_c_g_ETHAUD = float(0.0)
qty_bids_c_g_ETHAUD = float(0.0)
price_asks_c_g_ETHAUD = float(0.0)
qty_asks_c_g_ETHAUD = float(0.0)
stepSize_ETHAUD = '0.00010000'


def on_message_ETHAUD(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHAUD = 'ETHAUD'
	price_bids_c_l_ETHAUD = data['bids'][0][0]
	qty_bids_c_l_ETHAUD = data['bids'][0][1]
	price_asks_c_l_ETHAUD = data['asks'][0][0]
	qty_asks_c_l_ETHAUD = data['asks'][0][1]

	global symbol_c_g_ETHAUD
	global price_bids_c_g_ETHAUD
	global qty_bids_c_g_ETHAUD
	global price_asks_c_g_ETHAUD
	global qty_asks_c_g_ETHAUD

	symbol_c_g_ETHAUD = symbol_c_l_ETHAUD
	price_bids_c_g_ETHAUD = price_bids_c_l_ETHAUD
	qty_bids_c_g_ETHAUD = qty_bids_c_l_ETHAUD
	price_asks_c_g_ETHAUD = price_asks_c_l_ETHAUD
	qty_asks_c_g_ETHAUD = qty_asks_c_l_ETHAUD


def loop_ETHAUD():

	socket1 = f'wss://stream.binance.com:9443/ws/ethaud@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHAUD)
	ws.run_forever()


Thread(target=loop_ETHAUD).start()

symbol_c_g_ETHDAI = 'ETHDAI'
price_bids_c_g_ETHDAI = float(0.0)
qty_bids_c_g_ETHDAI = float(0.0)
price_asks_c_g_ETHDAI = float(0.0)
qty_asks_c_g_ETHDAI = float(0.0)
stepSize_ETHDAI = '0.00010000'


def on_message_ETHDAI(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHDAI = 'ETHDAI'
	price_bids_c_l_ETHDAI = data['bids'][0][0]
	qty_bids_c_l_ETHDAI = data['bids'][0][1]
	price_asks_c_l_ETHDAI = data['asks'][0][0]
	qty_asks_c_l_ETHDAI = data['asks'][0][1]

	global symbol_c_g_ETHDAI
	global price_bids_c_g_ETHDAI
	global qty_bids_c_g_ETHDAI
	global price_asks_c_g_ETHDAI
	global qty_asks_c_g_ETHDAI

	symbol_c_g_ETHDAI = symbol_c_l_ETHDAI
	price_bids_c_g_ETHDAI = price_bids_c_l_ETHDAI
	qty_bids_c_g_ETHDAI = qty_bids_c_l_ETHDAI
	price_asks_c_g_ETHDAI = price_asks_c_l_ETHDAI
	qty_asks_c_g_ETHDAI = qty_asks_c_l_ETHDAI


def loop_ETHDAI():

	socket1 = f'wss://stream.binance.com:9443/ws/ethdai@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHDAI)
	ws.run_forever()


Thread(target=loop_ETHDAI).start()

symbol_c_g_ETHBRL = 'ETHBRL'
price_bids_c_g_ETHBRL = float(0.0)
qty_bids_c_g_ETHBRL = float(0.0)
price_asks_c_g_ETHBRL = float(0.0)
qty_asks_c_g_ETHBRL = float(0.0)
stepSize_ETHBRL = '0.00010000'


def on_message_ETHBRL(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHBRL = 'ETHBRL'
	price_bids_c_l_ETHBRL = data['bids'][0][0]
	qty_bids_c_l_ETHBRL = data['bids'][0][1]
	price_asks_c_l_ETHBRL = data['asks'][0][0]
	qty_asks_c_l_ETHBRL = data['asks'][0][1]

	global symbol_c_g_ETHBRL
	global price_bids_c_g_ETHBRL
	global qty_bids_c_g_ETHBRL
	global price_asks_c_g_ETHBRL
	global qty_asks_c_g_ETHBRL

	symbol_c_g_ETHBRL = symbol_c_l_ETHBRL
	price_bids_c_g_ETHBRL = price_bids_c_l_ETHBRL
	qty_bids_c_g_ETHBRL = qty_bids_c_l_ETHBRL
	price_asks_c_g_ETHBRL = price_asks_c_l_ETHBRL
	qty_asks_c_g_ETHBRL = qty_asks_c_l_ETHBRL


def loop_ETHBRL():

	socket1 = f'wss://stream.binance.com:9443/ws/ethbrl@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHBRL)
	ws.run_forever()


Thread(target=loop_ETHBRL).start()

symbol_c_g_ETHUAH = 'ETHUAH'
price_bids_c_g_ETHUAH = float(0.0)
qty_bids_c_g_ETHUAH = float(0.0)
price_asks_c_g_ETHUAH = float(0.0)
qty_asks_c_g_ETHUAH = float(0.0)
stepSize_ETHUAH = '0.00010000'


def on_message_ETHUAH(ws, message):

	data = json.loads(message)

	symbol_c_l_ETHUAH = 'ETHUAH'
	price_bids_c_l_ETHUAH = data['bids'][0][0]
	qty_bids_c_l_ETHUAH = data['bids'][0][1]
	price_asks_c_l_ETHUAH = data['asks'][0][0]
	qty_asks_c_l_ETHUAH = data['asks'][0][1]

	global symbol_c_g_ETHUAH
	global price_bids_c_g_ETHUAH
	global qty_bids_c_g_ETHUAH
	global price_asks_c_g_ETHUAH
	global qty_asks_c_g_ETHUAH

	symbol_c_g_ETHUAH = symbol_c_l_ETHUAH
	price_bids_c_g_ETHUAH = price_bids_c_l_ETHUAH
	qty_bids_c_g_ETHUAH = qty_bids_c_l_ETHUAH
	price_asks_c_g_ETHUAH = price_asks_c_l_ETHUAH
	qty_asks_c_g_ETHUAH = qty_asks_c_l_ETHUAH


def loop_ETHUAH():

	socket1 = f'wss://stream.binance.com:9443/ws/ethuah@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_ETHUAH)
	ws.run_forever()


Thread(target=loop_ETHUAH).start()

symbol_c_g_XRPETH = 'XRPETH'
price_bids_c_g_XRPETH = float(0.0)
qty_bids_c_g_XRPETH = float(0.0)
price_asks_c_g_XRPETH = float(0.0)
qty_asks_c_g_XRPETH = float(0.0)
stepSize_XRPETH = '1.00000000'


def on_message_XRPETH(ws, message):

	data = json.loads(message)

	symbol_c_l_XRPETH = 'XRPETH'
	price_bids_c_l_XRPETH = data['bids'][0][0]
	qty_bids_c_l_XRPETH = data['bids'][0][1]
	price_asks_c_l_XRPETH = data['asks'][0][0]
	qty_asks_c_l_XRPETH = data['asks'][0][1]

	global symbol_c_g_XRPETH
	global price_bids_c_g_XRPETH
	global qty_bids_c_g_XRPETH
	global price_asks_c_g_XRPETH
	global qty_asks_c_g_XRPETH

	symbol_c_g_XRPETH = symbol_c_l_XRPETH
	price_bids_c_g_XRPETH = price_bids_c_l_XRPETH
	qty_bids_c_g_XRPETH = qty_bids_c_l_XRPETH
	price_asks_c_g_XRPETH = price_asks_c_l_XRPETH
	qty_asks_c_g_XRPETH = qty_asks_c_l_XRPETH


def loop_XRPETH():

	socket1 = f'wss://stream.binance.com:9443/ws/xrpeth@depth5@100ms'
	ws = websocket.WebSocketApp(socket1, on_message=on_message_XRPETH)
	ws.run_forever()


Thread(target=loop_XRPETH).start()


########################################################################################################
streamneoethneobusd = 'neoeth@bookTicker'
streamneobusdneoeth = 'neobusd@bookTicker'

symbol_a_g_NEOETH_NEOBUSD = 'NEOETH'
price_bids_a_g_NEOETH_NEOBUSD = float(0.0)
qty_bids_a_g_NEOETH_NEOBUSD = float(0.0)
price_asks_a_g_NEOETH_NEOBUSD = float(0.0)
qty_asks_a_g_NEOETH_NEOBUSD = float(0.0)

stepSize_NEOETH_NEOBUSD = 0.01000000

symbol_b_g_NEOBUSD_NEOETH = 'NEOBUSD'
price_bids_b_g_NEOBUSD_NEOETH = float(0.0)
qty_bids_b_g_NEOBUSD_NEOETH = float(0.0)
price_asks_b_g_NEOBUSD_NEOETH = float(0.0)
qty_asks_b_g_NEOBUSD_NEOETH = float(0.0)

stepSize_NEOBUSD_NEOETH = 0.01000000


def on_message_NEOETH_NEOBUSD(ws, message):

	data = json.loads(message)

	if data['stream'] == streamneoethneobusd:
		symbol_a_l_NEOETH = data['data']['s']
		price_bids_a_l_NEOETH = data['data']['b']
		qty_bids_a_l_NEOETH = data['data']['B']
		price_asks_a_l_NEOETH = data['data']['a']
		qty_asks_a_l_NEOETH = data['data']['A']

		global symbol_a_g_NEOETH_NEOBUSD
		global price_bids_a_g_NEOETH_NEOBUSD
		global qty_bids_a_g_NEOETH_NEOBUSD
		global price_asks_a_g_NEOETH_NEOBUSD
		global qty_asks_a_g_NEOETH_NEOBUSD

		symbol_a_g_NEOETH_NEOBUSD = symbol_a_l_NEOETH
		price_bids_a_g_NEOETH_NEOBUSD = price_bids_a_l_NEOETH
		qty_bids_a_g_NEOETH_NEOBUSD = qty_bids_a_l_NEOETH
		price_asks_a_g_NEOETH_NEOBUSD = price_asks_a_l_NEOETH
		qty_asks_a_g_NEOETH_NEOBUSD = qty_asks_a_l_NEOETH

	if data['stream'] == streamneobusdneoeth:
		data = json.loads(message)

		symbol_b_l_NEOBUSD = data['data']['s']
		price_bids_b_l_NEOBUSD = data['data']['b']
		qty_bids_b_l_NEOBUSD = data['data']['B']
		price_asks_b_l_NEOBUSD = data['data']['a']
		qty_asks_b_l_NEOBUSD = data['data']['A']

		global symbol_b_g_NEOBUSD_NEOETH
		global price_bids_b_g_NEOBUSD_NEOETH
		global qty_bids_b_g_NEOBUSD_NEOETH
		global price_asks_b_g_NEOBUSD_NEOETH
		global qty_asks_b_g_NEOBUSD_NEOETH

		symbol_b_g_NEOBUSD_NEOETH = symbol_b_l_NEOBUSD
		price_bids_b_g_NEOBUSD_NEOETH = price_bids_b_l_NEOBUSD
		qty_bids_b_g_NEOBUSD_NEOETH = qty_bids_b_l_NEOBUSD
		price_asks_b_g_NEOBUSD_NEOETH = price_asks_b_l_NEOBUSD
		qty_asks_b_g_NEOBUSD_NEOETH = qty_asks_b_l_NEOBUSD


def loop_NEOETH_NEOBUSD():
	socket1 = f'wss://stream.binance.com:9443/stream?streams={streamneoethneobusd}/{streamneobusdneoeth}'

	ws = websocket.WebSocketApp(socket1, on_message=on_message_NEOETH_NEOBUSD)

	ws.run_forever()


Thread(target=loop_NEOETH_NEOBUSD).start()


def loop_NEOETH_NEOBUSD_Trade():

	while True:
		time.sleep(0.1)

		if price_bids_c_g_ETHBUSD != 0.0 and qty_bids_c_g_ETHBUSD != 0.0 and price_asks_c_g_ETHBUSD != 0.0 and qty_asks_c_g_ETHBUSD != 0.0 and price_bids_a_g_NEOETH_NEOBUSD != 0.0 and qty_bids_a_g_NEOETH_NEOBUSD != 0.0 and price_asks_a_g_NEOETH_NEOBUSD != 0.0 and qty_asks_a_g_NEOETH_NEOBUSD != 0.0 and price_bids_b_g_NEOBUSD_NEOETH != 0.0 and qty_bids_b_g_NEOBUSD_NEOETH != 0.0 and price_asks_b_g_NEOBUSD_NEOETH != 0.0 and qty_asks_b_g_NEOBUSD_NEOETH != 0.0:

			# Цепочка: NEOETH -> NEOBUSD -> ETHBUSD

			# Покупаем ETH продаем BUSD
			quantity_pair_c_raschet = usdt_count * float(price_asks_c_g_ETHBUSD)  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b'
			quantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть)
			# quantity_pair_c_raschet = количество 'BUSD'
			trade_pair_c = 'buy'

			# Продаем NEO покупаем BUSD
			quantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_b_g_NEOBUSD_NEOETH)  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a'
			quantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть)
			quantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_NEOBUSD_NEOETH))  # Округляем согласно шагу Binance 'stepSize'
			quantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть)
			# quantity_pair_c_raschet = количество 'NEO'
			trade_pair_b = 'sell'

			price_a = float(quantity_pair_b_raschet) * float(price_asks_a_g_NEOETH_NEOBUSD)
			price_a = round(price_a, 14)
			# price_a = сколько потребуется 'ETH'

			price_b = float(price_bids_b_g_NEOBUSD_NEOETH) * float(quantity_pair_b_raschet)
			price_b = round(price_b, 14)
			# price_b = сколько получим 'BUSD'

			price_c = float(price_b) / float(price_asks_c_g_ETHBUSD)
			price_cc = float(f_minqty_size_down(price_c, stepSize_ETHBUSD))
			# price_c = сколько получим 'ETH'


			#pribil = 0

			#if pribil > 0:

			print('################################################################################################################')
			print('Пара_А:', symbol_a_g_NEOETH_NEOBUSD)
			print('Покупаем', quantity_pair_b_raschet, 'NEO', 'за', price_a, 'ETH', 'по цене', price_asks_a_g_NEOETH_NEOBUSD)
			print('Пара_B:', symbol_b_g_NEOBUSD_NEOETH)
			print('Продаем', quantity_pair_b_raschet, 'NEO', 'за', price_b, 'BUSD', 'по цене', price_bids_b_g_NEOBUSD_NEOETH)
			print('Пара_C:', symbol_c_g_ETHBUSD)
			print('Покупаем', price_c, 'ETH', 'за', price_b, 'BUSD', 'по цене', price_asks_c_g_ETHBUSD)
			print(price_cc )

Thread(target=loop_NEOETH_NEOBUSD_Trade).start()