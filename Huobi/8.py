import time
import datetime
import json
import websocket
import asyncio
from threading import *
import datetime
import gzip

usdt_count = float(11.0)


all_pribil = float(0.0)



symbol_c_g_ETHUSDT = 'ETHUSDT'
price_bids_c_g_ETHUSDT = float(0.0)
qty_bids_c_g_ETHUSDT = float(0.0)
price_asks_c_g_ETHUSDT = float(0.0)
qty_asks_c_g_ETHUSDT = float(0.0)

def on_message_ETHUSDT(ws, message):
	#locker.acquire()
    data = json.loads(gzip.decompress(message))

    if 'ping' in data:
        ws.send(json.dumps({
            'pong': data['ping']
        }))

    else:

        symbol_c_l_ETHUSDT = 'ETHUSDT'
        price_bids_c_l_ETHUSDT = data['tick']['bid']
        qty_bids_c_l_ETHUSDT = data['tick']['bidSize']
        price_asks_c_l_ETHUSDT = data['tick']['ask']
        qty_asks_c_l_ETHUSDT = data['tick']['askSize']

        global symbol_c_g_ETHUSDT
        global price_bids_c_g_ETHUSDT
        global qty_bids_c_g_ETHUSDT
        global price_asks_c_g_ETHUSDT
        global qty_asks_c_g_ETHUSDT

        symbol_c_g_ETHUSDT = symbol_c_l_ETHUSDT
        price_bids_c_g_ETHUSDT= price_bids_c_l_ETHUSDT
        qty_bids_c_g_ETHUSDT= qty_bids_c_l_ETHUSDT
        price_asks_c_g_ETHUSDT = price_asks_c_l_ETHUSDT
        qty_asks_c_g_ETHUSDT= qty_asks_c_l_ETHUSDT


def on_close_ETHUSDT(ws):
    print('### closed ###')

def on_error_ETHUSDT(ws, message):
    print(message)

def on_open_ETHUSDT(ws):
    ws.send(json.dumps({'sub': f'market.ethusdt.ticker'}))

def loop_ETHUSDT():
    ws = websocket.WebSocketApp('wss://api.huobi.pro/ws',
            on_message=on_message_ETHUSDT,
            on_close=on_close_ETHUSDT,
            on_error=on_error_ETHUSDT)
    ws.on_open = on_open_ETHUSDT
    ws.run_forever()

Thread(target=loop_ETHUSDT).start()


#
# symbol_a_g_avaxusdt = 'avaxusdt'
# price_bids_a_g_avaxusdt = float(0.0)
# qty_bids_a_g_avaxusdt = float(0.0)
# price_asks_a_g_avaxusdt = float(0.0)
# qty_asks_a_g_avaxusdt = float(0.0)
#
# def on_message_avaxusdt(ws, message):
# 	data = json.loads(gzip.decompress(message))
#
# 	if 'ping' in data:
# 		ws.send(json.dumps({
# 			'pong': data['ping']
# 		}))
#
# 	else:
#
# 		symbol_a_l_avaxusdt = 'avaxusdt'
# 		price_bids_a_l_avaxusdt = data['tick']['bid']
# 		qty_bids_a_l_avaxusdt = data['tick']['bidSize']
# 		price_asks_a_l_avaxusdt = data['tick']['ask']
# 		qty_asks_a_l_avaxusdt = data['tick']['askSize']
#
# 		global symbol_a_g_avaxusdt
# 		global price_bids_a_g_avaxusdt
# 		global qty_bids_a_g_avaxusdt
# 		global price_asks_a_g_avaxusdt
# 		global qty_asks_a_g_avaxusdt
#
# 		symbol_a_g_avaxusdt = symbol_a_l_avaxusdt
# 		price_bids_a_g_avaxusdt = price_bids_a_l_avaxusdt
# 		qty_bids_a_g_avaxusdt = qty_bids_a_l_avaxusdt
# 		price_asks_a_g_avaxusdt = price_asks_a_l_avaxusdt
# 		qty_asks_a_g_avaxusdt = qty_asks_a_l_avaxusdt
#
# def on_close_avaxusdt(ws):
# 	print('### closed ###')
#
# def on_error_avaxusdt(ws, message):
# 	print(message)
#
# def on_open_avaxusdt(ws):
# 	ws.send(json.dumps({'sub': f'market.avaxusdt.ticker'}))
#
# def loop_avaxusdt():
# 	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws',
# 		on_message=on_message_avaxusdt,
# 		on_close=on_close_avaxusdt,
# 		on_error=on_error_avaxusdt)
# 	ws.on_open = on_open_avaxusdt
# 	ws.run_forever()
#
# Thread(target=loop_avaxusdt).start()
#
# symbol_b_g_avaxeth = 'avaxeth'
# price_bids_b_g_avaxeth = float(0.0)
# qty_bids_b_g_avaxeth = float(0.0)
# price_asks_b_g_avaxeth = float(0.0)
# qty_asks_b_g_avaxeth = float(0.0)
#
# def on_message_avaxeth(ws, message):
# 	data = json.loads(gzip.decompress(message))
#
# 	if 'ping' in data:
# 		ws.send(json.dumps({
# 			'pong': data['ping']
# 		}))
#
# 	else:
#
# 		symbol_b_l_avaxeth = 'avaxeth'
# 		price_bids_b_l_avaxeth = data['tick']['bid']
# 		qty_bids_b_l_avaxeth = data['tick']['bidSize']
# 		price_asks_b_l_avaxeth = data['tick']['ask']
# 		qty_asks_b_l_avaxeth = data['tick']['askSize']
#
# 		global symbol_b_g_avaxeth
# 		global price_bids_b_g_avaxeth
# 		global qty_bids_b_g_avaxeth
# 		global price_asks_b_g_avaxeth
# 		global qty_asks_b_g_avaxeth
#
# 		symbol_b_g_avaxeth = symbol_b_l_avaxeth
# 		price_bids_b_g_avaxeth = price_bids_b_l_avaxeth
# 		qty_bids_b_g_avaxeth = qty_bids_b_l_avaxeth
# 		price_asks_b_g_avaxeth = price_asks_b_l_avaxeth
# 		qty_asks_b_g_avaxeth = qty_asks_b_l_avaxeth
#
#
# def on_close_avaxeth(ws):
# 	print('### closed ###')
#
# def on_error_avaxeth(ws, message):
# 	print(message)
#
# def on_open_avaxeth(ws):
# 	ws.send(json.dumps({'sub': f'market.avaxeth.ticker'}))
#
# def loop_avaxeth():
# 	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws',
# 		on_message=on_message_avaxeth,
# 		on_close=on_close_avaxeth,
# 		on_error=on_error_avaxeth)
# 	ws.on_open = on_open_avaxeth
# 	ws.run_forever()
#
# Thread(target=loop_avaxeth).start()
#
# def loop_avaxusdt_Trade():
# 	while True:
# 		time.sleep(0.1)
#
#
# 		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_avaxusdt != 0.0 and qty_bids_a_g_avaxusdt != 0.0 and price_asks_a_g_avaxusdt != 0.0 and qty_asks_a_g_avaxusdt != 0.0 and price_bids_b_g_avaxeth != 0.0 and qty_bids_b_g_avaxeth != 0.0 and price_asks_b_g_avaxeth != 0.0 and qty_asks_b_g_avaxeth != 0.0:
#
#
# 			price_a = usdt_count / float(price_asks_a_g_avaxusdt)
# 			price_b = float(price_bids_b_g_avaxeth) * price_a
# 			price_c = float(price_bids_c_g_ETHUSDT) * price_b
# 			pribil =  price_c - usdt_count
#
# 			# if pribil > 0:
# 			# 	print(symbol_b_g_avaxeth, pribil)
#
# Thread(target=loop_avaxusdt_Trade).start()