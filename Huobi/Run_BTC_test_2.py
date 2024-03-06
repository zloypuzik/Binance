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

symbol_c_g_BTCUSDT = 'BTCUSDT' 
price_bids_c_g_BTCUSDT = float(0.0) 
qty_bids_c_g_BTCUSDT = float(0.0) 
price_asks_c_g_BTCUSDT = float(0.0) 
qty_asks_c_g_BTCUSDT = float(0.0) 

def on_message_BTCUSDT(ws, message): 
	#locker.acquire() 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_c_l_BTCUSDT = 'BTCUSDT' 
		price_bids_c_l_BTCUSDT = data['tick']['bid'] 
		qty_bids_c_l_BTCUSDT = data['tick']['bidSize'] 
		price_asks_c_l_BTCUSDT = data['tick']['ask'] 
		qty_asks_c_l_BTCUSDT = data['tick']['askSize'] 

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

def on_close_BTCUSDT(ws): 
	print('### closed ###') 

def on_error_BTCUSDT(ws, message): 
	print(message) 

def on_open_BTCUSDT(ws): 
	ws.send(json.dumps({'sub': f'market.btcusdt.ticker'})) 

def loop_BTCUSDT(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_BTCUSDT, 
		on_close=on_close_BTCUSDT, 
		on_error=on_error_BTCUSDT) 
	ws.on_open = on_open_BTCUSDT 
	ws.run_forever() 

Thread(target=loop_BTCUSDT).start() 

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
	#locker.release() 

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

symbol_c_g_USDCUSDT = 'USDCUSDT' 
price_bids_c_g_USDCUSDT = float(0.0) 
qty_bids_c_g_USDCUSDT = float(0.0) 
price_asks_c_g_USDCUSDT = float(0.0) 
qty_asks_c_g_USDCUSDT = float(0.0) 

def on_message_USDCUSDT(ws, message): 
	#locker.acquire() 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_c_l_USDCUSDT = 'USDCUSDT' 
		price_bids_c_l_USDCUSDT = data['tick']['bid'] 
		qty_bids_c_l_USDCUSDT = data['tick']['bidSize'] 
		price_asks_c_l_USDCUSDT = data['tick']['ask'] 
		qty_asks_c_l_USDCUSDT = data['tick']['askSize'] 

		global symbol_c_g_USDCUSDT 
		global price_bids_c_g_USDCUSDT 
		global qty_bids_c_g_USDCUSDT 
		global price_asks_c_g_USDCUSDT 
		global qty_asks_c_g_USDCUSDT 

		symbol_c_g_USDCUSDT = symbol_c_l_USDCUSDT 
		price_bids_c_g_USDCUSDT= price_bids_c_l_USDCUSDT 
		qty_bids_c_g_USDCUSDT= qty_bids_c_l_USDCUSDT 
		price_asks_c_g_USDCUSDT = price_asks_c_l_USDCUSDT 
		qty_asks_c_g_USDCUSDT= qty_asks_c_l_USDCUSDT 
	#locker.release() 

def on_close_USDCUSDT(ws): 
	print('### closed ###') 

def on_error_USDCUSDT(ws, message): 
	print(message) 

def on_open_USDCUSDT(ws): 
	ws.send(json.dumps({'sub': f'market.usdcusdt.ticker'})) 

def oloop_USDCUSDT(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_USDCUSDT, 
		on_close=on_close_USDCUSDT, 
		on_error=on_error_USDCUSDT) 
	ws.on_open = on_open_USDCUSDT 
	ws.run_forever() 

Thread(target=oloop_USDCUSDT).start() 

symbol_c_g_USDDUSDT = 'USDDUSDT' 
price_bids_c_g_USDDUSDT = float(0.0) 
qty_bids_c_g_USDDUSDT = float(0.0) 
price_asks_c_g_USDDUSDT = float(0.0) 
qty_asks_c_g_USDDUSDT = float(0.0) 

def on_message_USDDUSDT(ws, message): 
	#locker.acquire() 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_c_l_USDDUSDT = 'USDDUSDT' 
		price_bids_c_l_USDDUSDT = data['tick']['bid'] 
		qty_bids_c_l_USDDUSDT = data['tick']['bidSize'] 
		price_asks_c_l_USDDUSDT = data['tick']['ask'] 
		qty_asks_c_l_USDDUSDT = data['tick']['askSize'] 

		global symbol_c_g_USDDUSDT 
		global price_bids_c_g_USDDUSDT 
		global qty_bids_c_g_USDDUSDT 
		global price_asks_c_g_USDDUSDT 
		global qty_asks_c_g_USDDUSDT 

		symbol_c_g_USDDUSDT = symbol_c_l_USDDUSDT 
		price_bids_c_g_USDDUSDT= price_bids_c_l_USDDUSDT 
		qty_bids_c_g_USDDUSDT= qty_bids_c_l_USDDUSDT 
		price_asks_c_g_USDDUSDT = price_asks_c_l_USDDUSDT 
		qty_asks_c_g_USDDUSDT= qty_asks_c_l_USDDUSDT 
	#locker.release() 

def on_close_USDDUSDT(ws): 
	print('### closed ###') 

def on_error_USDDUSDT(ws, message): 
	print(message) 

def on_open_USDDUSDT(ws): 
	ws.send(json.dumps({'sub': f'market.usddusdt.ticker'})) 

def oloop_USDDUSDT(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_USDDUSDT, 
		on_close=on_close_USDDUSDT, 
		on_error=on_error_USDDUSDT) 
	ws.on_open = on_open_USDDUSDT 
	ws.run_forever() 

Thread(target=oloop_USDDUSDT).start() 

symbol_c_g_HTUSDT = 'HTUSDT' 
price_bids_c_g_HTUSDT = float(0.0) 
qty_bids_c_g_HTUSDT = float(0.0) 
price_asks_c_g_HTUSDT = float(0.0) 
qty_asks_c_g_HTUSDT = float(0.0) 

def on_message_HTUSDT(ws, message): 
	#locker.acquire() 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_c_l_HTUSDT = 'HTUSDT' 
		price_bids_c_l_HTUSDT = data['tick']['bid'] 
		qty_bids_c_l_HTUSDT = data['tick']['bidSize'] 
		price_asks_c_l_HTUSDT = data['tick']['ask'] 
		qty_asks_c_l_HTUSDT = data['tick']['askSize'] 

		global symbol_c_g_HTUSDT 
		global price_bids_c_g_HTUSDT 
		global qty_bids_c_g_HTUSDT 
		global price_asks_c_g_HTUSDT 
		global qty_asks_c_g_HTUSDT 

		symbol_c_g_HTUSDT = symbol_c_l_HTUSDT 
		price_bids_c_g_HTUSDT= price_bids_c_l_HTUSDT 
		qty_bids_c_g_HTUSDT= qty_bids_c_l_HTUSDT 
		price_asks_c_g_HTUSDT = price_asks_c_l_HTUSDT 
		qty_asks_c_g_HTUSDT= qty_asks_c_l_HTUSDT 
	#locker.release() 

def on_close_HTUSDT(ws): 
	print('### closed ###') 

def on_error_HTUSDT(ws, message): 
	print(message) 

def on_open_HTUSDT(ws): 
	ws.send(json.dumps({'sub': f'market.htusdt.ticker'})) 

def oloop_HTUSDT(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_HTUSDT, 
		on_close=on_close_HTUSDT, 
		on_error=on_error_HTUSDT) 
	ws.on_open = on_open_HTUSDT 
	ws.run_forever() 

Thread(target=oloop_HTUSDT).start() 

symbol_a_g_avaxusdt = 'avaxusdt' 
price_bids_a_g_avaxusdt = float(0.0) 
qty_bids_a_g_avaxusdt = float(0.0) 
price_asks_a_g_avaxusdt = float(0.0) 
qty_asks_a_g_avaxusdt = float(0.0) 

def on_message_avaxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_avaxusdt = 'avaxusdt' 
		price_bids_a_l_avaxusdt = data['tick']['bid'] 
		qty_bids_a_l_avaxusdt = data['tick']['bidSize'] 
		price_asks_a_l_avaxusdt = data['tick']['ask'] 
		qty_asks_a_l_avaxusdt = data['tick']['askSize'] 

		global symbol_a_g_avaxusdt 
		global price_bids_a_g_avaxusdt 
		global qty_bids_a_g_avaxusdt 
		global price_asks_a_g_avaxusdt 
		global qty_asks_a_g_avaxusdt 

		symbol_a_g_avaxusdt = symbol_a_l_avaxusdt 
		price_bids_a_g_avaxusdt = price_bids_a_l_avaxusdt 
		qty_bids_a_g_avaxusdt = qty_bids_a_l_avaxusdt 
		price_asks_a_g_avaxusdt = price_asks_a_l_avaxusdt 
		qty_asks_a_g_avaxusdt = qty_asks_a_l_avaxusdt 

def on_close_avaxusdt(ws): 
	print('### closed ###') 

def on_error_avaxusdt(ws, message): 
	print(message) 

def on_open_avaxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.avaxusdt.ticker'})) 

def loop_avaxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_avaxusdt, 
		on_close=on_close_avaxusdt, 
		on_error=on_error_avaxusdt) 
	ws.on_open = on_open_avaxusdt 
	ws.run_forever() 

Thread(target=loop_avaxusdt).start() 

symbol_b_g_avaxeth = 'avaxeth' 
price_bids_b_g_avaxeth = float(0.0) 
qty_bids_b_g_avaxeth = float(0.0) 
price_asks_b_g_avaxeth = float(0.0) 
qty_asks_b_g_avaxeth = float(0.0) 

def on_message_avaxeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_avaxeth = 'avaxeth' 
		price_bids_b_l_avaxeth = data['tick']['bid'] 
		qty_bids_b_l_avaxeth = data['tick']['bidSize']
		price_asks_b_l_avaxeth = data['tick']['ask'] 
		qty_asks_b_l_avaxeth = data['tick']['askSize'] 

		global symbol_b_g_avaxeth 
		global price_bids_b_g_avaxeth 
		global qty_bids_b_g_avaxeth 
		global price_asks_b_g_avaxeth 
		global qty_asks_b_g_avaxeth 

		symbol_b_g_avaxeth = symbol_b_l_avaxeth 
		price_bids_b_g_avaxeth = price_bids_b_l_avaxeth 
		qty_bids_b_g_avaxeth = qty_bids_b_l_avaxeth 
		price_asks_b_g_avaxeth = price_asks_b_l_avaxeth 
		qty_asks_b_g_avaxeth = qty_asks_b_l_avaxeth 


def on_close_avaxeth(ws): 
	print('### closed ###') 

def on_error_avaxeth(ws, message): 
	print(message) 

def on_open_avaxeth(ws): 
	ws.send(json.dumps({'sub': f'market.avaxeth.ticker'})) 

def loop_avaxeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_avaxeth, 
		on_close=on_close_avaxeth, 
		on_error=on_error_avaxeth) 
	ws.on_open = on_open_avaxeth 
	ws.run_forever() 

Thread(target=loop_avaxeth).start() 

def loop_avaxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_avaxusdt != 0.0 and qty_bids_a_g_avaxusdt != 0.0 and price_asks_a_g_avaxusdt != 0.0 and qty_asks_a_g_avaxusdt != 0.0 and price_bids_b_g_avaxeth != 0.0 and qty_bids_b_g_avaxeth != 0.0 and price_asks_b_g_avaxeth != 0.0 and qty_asks_b_g_avaxeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_avaxusdt) 
			price_b = float(price_bids_b_g_avaxeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_avaxeth, pribil)

Thread(target=loop_avaxusdt_Trade).start() 

symbol_a_g_htusdt = 'htusdt' 
price_bids_a_g_htusdt = float(0.0) 
qty_bids_a_g_htusdt = float(0.0) 
price_asks_a_g_htusdt = float(0.0) 
qty_asks_a_g_htusdt = float(0.0) 

def on_message_htusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_htusdt = 'htusdt' 
		price_bids_a_l_htusdt = data['tick']['bid'] 
		qty_bids_a_l_htusdt = data['tick']['bidSize'] 
		price_asks_a_l_htusdt = data['tick']['ask'] 
		qty_asks_a_l_htusdt = data['tick']['askSize'] 

		global symbol_a_g_htusdt 
		global price_bids_a_g_htusdt 
		global qty_bids_a_g_htusdt 
		global price_asks_a_g_htusdt 
		global qty_asks_a_g_htusdt 

		symbol_a_g_htusdt = symbol_a_l_htusdt 
		price_bids_a_g_htusdt = price_bids_a_l_htusdt 
		qty_bids_a_g_htusdt = qty_bids_a_l_htusdt 
		price_asks_a_g_htusdt = price_asks_a_l_htusdt 
		qty_asks_a_g_htusdt = qty_asks_a_l_htusdt 

def on_close_htusdt(ws): 
	print('### closed ###') 

def on_error_htusdt(ws, message): 
	print(message) 

def on_open_htusdt(ws): 
	ws.send(json.dumps({'sub': f'market.htusdt.ticker'})) 

def loop_htusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_htusdt, 
		on_close=on_close_htusdt, 
		on_error=on_error_htusdt) 
	ws.on_open = on_open_htusdt 
	ws.run_forever() 

Thread(target=loop_htusdt).start() 

symbol_b_g_htusdc = 'htusdc' 
price_bids_b_g_htusdc = float(0.0) 
qty_bids_b_g_htusdc = float(0.0) 
price_asks_b_g_htusdc = float(0.0) 
qty_asks_b_g_htusdc = float(0.0) 

def on_message_htusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_htusdc = 'htusdc' 
		price_bids_b_l_htusdc = data['tick']['bid'] 
		qty_bids_b_l_htusdc = data['tick']['bidSize']
		price_asks_b_l_htusdc = data['tick']['ask'] 
		qty_asks_b_l_htusdc = data['tick']['askSize'] 

		global symbol_b_g_htusdc 
		global price_bids_b_g_htusdc 
		global qty_bids_b_g_htusdc 
		global price_asks_b_g_htusdc 
		global qty_asks_b_g_htusdc 

		symbol_b_g_htusdc = symbol_b_l_htusdc 
		price_bids_b_g_htusdc = price_bids_b_l_htusdc 
		qty_bids_b_g_htusdc = qty_bids_b_l_htusdc 
		price_asks_b_g_htusdc = price_asks_b_l_htusdc 
		qty_asks_b_g_htusdc = qty_asks_b_l_htusdc 


def on_close_htusdc(ws): 
	print('### closed ###') 

def on_error_htusdc(ws, message): 
	print(message) 

def on_open_htusdc(ws): 
	ws.send(json.dumps({'sub': f'market.htusdc.ticker'})) 

def loop_htusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_htusdc, 
		on_close=on_close_htusdc, 
		on_error=on_error_htusdc) 
	ws.on_open = on_open_htusdc 
	ws.run_forever() 

Thread(target=loop_htusdc).start() 

def loop_htusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_htusdt != 0.0 and qty_bids_a_g_htusdt != 0.0 and price_asks_a_g_htusdt != 0.0 and qty_asks_a_g_htusdt != 0.0 and price_bids_b_g_htusdc != 0.0 and qty_bids_b_g_htusdc != 0.0 and price_asks_b_g_htusdc != 0.0 and qty_asks_b_g_htusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_htusdt) 
			price_b = float(price_bids_b_g_htusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_htusdc, pribil)

Thread(target=loop_htusdt_Trade).start() 

symbol_a_g_maticusdt = 'maticusdt' 
price_bids_a_g_maticusdt = float(0.0) 
qty_bids_a_g_maticusdt = float(0.0) 
price_asks_a_g_maticusdt = float(0.0) 
qty_asks_a_g_maticusdt = float(0.0) 

def on_message_maticusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_maticusdt = 'maticusdt' 
		price_bids_a_l_maticusdt = data['tick']['bid'] 
		qty_bids_a_l_maticusdt = data['tick']['bidSize'] 
		price_asks_a_l_maticusdt = data['tick']['ask'] 
		qty_asks_a_l_maticusdt = data['tick']['askSize'] 

		global symbol_a_g_maticusdt 
		global price_bids_a_g_maticusdt 
		global qty_bids_a_g_maticusdt 
		global price_asks_a_g_maticusdt 
		global qty_asks_a_g_maticusdt 

		symbol_a_g_maticusdt = symbol_a_l_maticusdt 
		price_bids_a_g_maticusdt = price_bids_a_l_maticusdt 
		qty_bids_a_g_maticusdt = qty_bids_a_l_maticusdt 
		price_asks_a_g_maticusdt = price_asks_a_l_maticusdt 
		qty_asks_a_g_maticusdt = qty_asks_a_l_maticusdt 

def on_close_maticusdt(ws): 
	print('### closed ###') 

def on_error_maticusdt(ws, message): 
	print(message) 

def on_open_maticusdt(ws): 
	ws.send(json.dumps({'sub': f'market.maticusdt.ticker'})) 

def loop_maticusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_maticusdt, 
		on_close=on_close_maticusdt, 
		on_error=on_error_maticusdt) 
	ws.on_open = on_open_maticusdt 
	ws.run_forever() 

Thread(target=loop_maticusdt).start() 

symbol_b_g_maticusdd = 'maticusdd' 
price_bids_b_g_maticusdd = float(0.0) 
qty_bids_b_g_maticusdd = float(0.0) 
price_asks_b_g_maticusdd = float(0.0) 
qty_asks_b_g_maticusdd = float(0.0) 

def on_message_maticusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_maticusdd = 'maticusdd' 
		price_bids_b_l_maticusdd = data['tick']['bid'] 
		qty_bids_b_l_maticusdd = data['tick']['bidSize']
		price_asks_b_l_maticusdd = data['tick']['ask'] 
		qty_asks_b_l_maticusdd = data['tick']['askSize'] 

		global symbol_b_g_maticusdd 
		global price_bids_b_g_maticusdd 
		global qty_bids_b_g_maticusdd 
		global price_asks_b_g_maticusdd 
		global qty_asks_b_g_maticusdd 

		symbol_b_g_maticusdd = symbol_b_l_maticusdd 
		price_bids_b_g_maticusdd = price_bids_b_l_maticusdd 
		qty_bids_b_g_maticusdd = qty_bids_b_l_maticusdd 
		price_asks_b_g_maticusdd = price_asks_b_l_maticusdd 
		qty_asks_b_g_maticusdd = qty_asks_b_l_maticusdd 


def on_close_maticusdd(ws): 
	print('### closed ###') 

def on_error_maticusdd(ws, message): 
	print(message) 

def on_open_maticusdd(ws): 
	ws.send(json.dumps({'sub': f'market.maticusdd.ticker'})) 

def loop_maticusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_maticusdd, 
		on_close=on_close_maticusdd, 
		on_error=on_error_maticusdd) 
	ws.on_open = on_open_maticusdd 
	ws.run_forever() 

Thread(target=loop_maticusdd).start() 

def loop_maticusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_maticusdt != 0.0 and qty_bids_a_g_maticusdt != 0.0 and price_asks_a_g_maticusdt != 0.0 and qty_asks_a_g_maticusdt != 0.0 and price_bids_b_g_maticusdd != 0.0 and qty_bids_b_g_maticusdd != 0.0 and price_asks_b_g_maticusdd != 0.0 and qty_asks_b_g_maticusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_maticusdt) 
			price_b = float(price_bids_b_g_maticusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_maticusdd, pribil)

Thread(target=loop_maticusdt_Trade).start() 

symbol_a_g_xrpusdt = 'xrpusdt' 
price_bids_a_g_xrpusdt = float(0.0) 
qty_bids_a_g_xrpusdt = float(0.0) 
price_asks_a_g_xrpusdt = float(0.0) 
qty_asks_a_g_xrpusdt = float(0.0) 

def on_message_xrpusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_xrpusdt = 'xrpusdt' 
		price_bids_a_l_xrpusdt = data['tick']['bid'] 
		qty_bids_a_l_xrpusdt = data['tick']['bidSize'] 
		price_asks_a_l_xrpusdt = data['tick']['ask'] 
		qty_asks_a_l_xrpusdt = data['tick']['askSize'] 

		global symbol_a_g_xrpusdt 
		global price_bids_a_g_xrpusdt 
		global qty_bids_a_g_xrpusdt 
		global price_asks_a_g_xrpusdt 
		global qty_asks_a_g_xrpusdt 

		symbol_a_g_xrpusdt = symbol_a_l_xrpusdt 
		price_bids_a_g_xrpusdt = price_bids_a_l_xrpusdt 
		qty_bids_a_g_xrpusdt = qty_bids_a_l_xrpusdt 
		price_asks_a_g_xrpusdt = price_asks_a_l_xrpusdt 
		qty_asks_a_g_xrpusdt = qty_asks_a_l_xrpusdt 

def on_close_xrpusdt(ws): 
	print('### closed ###') 

def on_error_xrpusdt(ws, message): 
	print(message) 

def on_open_xrpusdt(ws): 
	ws.send(json.dumps({'sub': f'market.xrpusdt.ticker'})) 

def loop_xrpusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xrpusdt, 
		on_close=on_close_xrpusdt, 
		on_error=on_error_xrpusdt) 
	ws.on_open = on_open_xrpusdt 
	ws.run_forever() 

Thread(target=loop_xrpusdt).start() 

symbol_b_g_xrpht = 'xrpht' 
price_bids_b_g_xrpht = float(0.0) 
qty_bids_b_g_xrpht = float(0.0) 
price_asks_b_g_xrpht = float(0.0) 
qty_asks_b_g_xrpht = float(0.0) 

def on_message_xrpht(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_xrpht = 'xrpht' 
		price_bids_b_l_xrpht = data['tick']['bid'] 
		qty_bids_b_l_xrpht = data['tick']['bidSize']
		price_asks_b_l_xrpht = data['tick']['ask'] 
		qty_asks_b_l_xrpht = data['tick']['askSize'] 

		global symbol_b_g_xrpht 
		global price_bids_b_g_xrpht 
		global qty_bids_b_g_xrpht 
		global price_asks_b_g_xrpht 
		global qty_asks_b_g_xrpht 

		symbol_b_g_xrpht = symbol_b_l_xrpht 
		price_bids_b_g_xrpht = price_bids_b_l_xrpht 
		qty_bids_b_g_xrpht = qty_bids_b_l_xrpht 
		price_asks_b_g_xrpht = price_asks_b_l_xrpht 
		qty_asks_b_g_xrpht = qty_asks_b_l_xrpht 


def on_close_xrpht(ws): 
	print('### closed ###') 

def on_error_xrpht(ws, message): 
	print(message) 

def on_open_xrpht(ws): 
	ws.send(json.dumps({'sub': f'market.xrpht.ticker'})) 

def loop_xrpht(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xrpht, 
		on_close=on_close_xrpht, 
		on_error=on_error_xrpht) 
	ws.on_open = on_open_xrpht 
	ws.run_forever() 

Thread(target=loop_xrpht).start() 

def loop_xrpusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_HTUSDT != 0.0 and qty_bids_c_g_HTUSDT != 0.0 and price_asks_c_g_HTUSDT != 0.0 and qty_asks_c_g_HTUSDT != 0.0 and price_bids_a_g_xrpusdt != 0.0 and qty_bids_a_g_xrpusdt != 0.0 and price_asks_a_g_xrpusdt != 0.0 and qty_asks_a_g_xrpusdt != 0.0 and price_bids_b_g_xrpht != 0.0 and qty_bids_b_g_xrpht != 0.0 and price_asks_b_g_xrpht != 0.0 and qty_asks_b_g_xrpht != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_xrpusdt) 
			price_b = float(price_bids_b_g_xrpht) * price_a 
			price_c = float(price_bids_c_g_HTUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_xrpht, pribil)

Thread(target=loop_xrpusdt_Trade).start() 

symbol_a_g_apeusdt = 'apeusdt' 
price_bids_a_g_apeusdt = float(0.0) 
qty_bids_a_g_apeusdt = float(0.0) 
price_asks_a_g_apeusdt = float(0.0) 
qty_asks_a_g_apeusdt = float(0.0) 

def on_message_apeusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_apeusdt = 'apeusdt' 
		price_bids_a_l_apeusdt = data['tick']['bid'] 
		qty_bids_a_l_apeusdt = data['tick']['bidSize'] 
		price_asks_a_l_apeusdt = data['tick']['ask'] 
		qty_asks_a_l_apeusdt = data['tick']['askSize'] 

		global symbol_a_g_apeusdt 
		global price_bids_a_g_apeusdt 
		global qty_bids_a_g_apeusdt 
		global price_asks_a_g_apeusdt 
		global qty_asks_a_g_apeusdt 

		symbol_a_g_apeusdt = symbol_a_l_apeusdt 
		price_bids_a_g_apeusdt = price_bids_a_l_apeusdt 
		qty_bids_a_g_apeusdt = qty_bids_a_l_apeusdt 
		price_asks_a_g_apeusdt = price_asks_a_l_apeusdt 
		qty_asks_a_g_apeusdt = qty_asks_a_l_apeusdt 

def on_close_apeusdt(ws): 
	print('### closed ###') 

def on_error_apeusdt(ws, message): 
	print(message) 

def on_open_apeusdt(ws): 
	ws.send(json.dumps({'sub': f'market.apeusdt.ticker'})) 

def loop_apeusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_apeusdt, 
		on_close=on_close_apeusdt, 
		on_error=on_error_apeusdt) 
	ws.on_open = on_open_apeusdt 
	ws.run_forever() 

Thread(target=loop_apeusdt).start() 

symbol_b_g_apeusdd = 'apeusdd' 
price_bids_b_g_apeusdd = float(0.0) 
qty_bids_b_g_apeusdd = float(0.0) 
price_asks_b_g_apeusdd = float(0.0) 
qty_asks_b_g_apeusdd = float(0.0) 

def on_message_apeusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_apeusdd = 'apeusdd' 
		price_bids_b_l_apeusdd = data['tick']['bid'] 
		qty_bids_b_l_apeusdd = data['tick']['bidSize']
		price_asks_b_l_apeusdd = data['tick']['ask'] 
		qty_asks_b_l_apeusdd = data['tick']['askSize'] 

		global symbol_b_g_apeusdd 
		global price_bids_b_g_apeusdd 
		global qty_bids_b_g_apeusdd 
		global price_asks_b_g_apeusdd 
		global qty_asks_b_g_apeusdd 

		symbol_b_g_apeusdd = symbol_b_l_apeusdd 
		price_bids_b_g_apeusdd = price_bids_b_l_apeusdd 
		qty_bids_b_g_apeusdd = qty_bids_b_l_apeusdd 
		price_asks_b_g_apeusdd = price_asks_b_l_apeusdd 
		qty_asks_b_g_apeusdd = qty_asks_b_l_apeusdd 


def on_close_apeusdd(ws): 
	print('### closed ###') 

def on_error_apeusdd(ws, message): 
	print(message) 

def on_open_apeusdd(ws): 
	ws.send(json.dumps({'sub': f'market.apeusdd.ticker'})) 

def loop_apeusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_apeusdd, 
		on_close=on_close_apeusdd, 
		on_error=on_error_apeusdd) 
	ws.on_open = on_open_apeusdd 
	ws.run_forever() 

Thread(target=loop_apeusdd).start() 

def loop_apeusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_apeusdt != 0.0 and qty_bids_a_g_apeusdt != 0.0 and price_asks_a_g_apeusdt != 0.0 and qty_asks_a_g_apeusdt != 0.0 and price_bids_b_g_apeusdd != 0.0 and qty_bids_b_g_apeusdd != 0.0 and price_asks_b_g_apeusdd != 0.0 and qty_asks_b_g_apeusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_apeusdt) 
			price_b = float(price_bids_b_g_apeusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_apeusdd, pribil)

Thread(target=loop_apeusdt_Trade).start() 

symbol_a_g_egldusdt = 'egldusdt' 
price_bids_a_g_egldusdt = float(0.0) 
qty_bids_a_g_egldusdt = float(0.0) 
price_asks_a_g_egldusdt = float(0.0) 
qty_asks_a_g_egldusdt = float(0.0) 

def on_message_egldusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_egldusdt = 'egldusdt' 
		price_bids_a_l_egldusdt = data['tick']['bid'] 
		qty_bids_a_l_egldusdt = data['tick']['bidSize'] 
		price_asks_a_l_egldusdt = data['tick']['ask'] 
		qty_asks_a_l_egldusdt = data['tick']['askSize'] 

		global symbol_a_g_egldusdt 
		global price_bids_a_g_egldusdt 
		global qty_bids_a_g_egldusdt 
		global price_asks_a_g_egldusdt 
		global qty_asks_a_g_egldusdt 

		symbol_a_g_egldusdt = symbol_a_l_egldusdt 
		price_bids_a_g_egldusdt = price_bids_a_l_egldusdt 
		qty_bids_a_g_egldusdt = qty_bids_a_l_egldusdt 
		price_asks_a_g_egldusdt = price_asks_a_l_egldusdt 
		qty_asks_a_g_egldusdt = qty_asks_a_l_egldusdt 

def on_close_egldusdt(ws): 
	print('### closed ###') 

def on_error_egldusdt(ws, message): 
	print(message) 

def on_open_egldusdt(ws): 
	ws.send(json.dumps({'sub': f'market.egldusdt.ticker'})) 

def loop_egldusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_egldusdt, 
		on_close=on_close_egldusdt, 
		on_error=on_error_egldusdt) 
	ws.on_open = on_open_egldusdt 
	ws.run_forever() 

Thread(target=loop_egldusdt).start() 

symbol_b_g_egldusdc = 'egldusdc' 
price_bids_b_g_egldusdc = float(0.0) 
qty_bids_b_g_egldusdc = float(0.0) 
price_asks_b_g_egldusdc = float(0.0) 
qty_asks_b_g_egldusdc = float(0.0) 

def on_message_egldusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_egldusdc = 'egldusdc' 
		price_bids_b_l_egldusdc = data['tick']['bid'] 
		qty_bids_b_l_egldusdc = data['tick']['bidSize']
		price_asks_b_l_egldusdc = data['tick']['ask'] 
		qty_asks_b_l_egldusdc = data['tick']['askSize'] 

		global symbol_b_g_egldusdc 
		global price_bids_b_g_egldusdc 
		global qty_bids_b_g_egldusdc 
		global price_asks_b_g_egldusdc 
		global qty_asks_b_g_egldusdc 

		symbol_b_g_egldusdc = symbol_b_l_egldusdc 
		price_bids_b_g_egldusdc = price_bids_b_l_egldusdc 
		qty_bids_b_g_egldusdc = qty_bids_b_l_egldusdc 
		price_asks_b_g_egldusdc = price_asks_b_l_egldusdc 
		qty_asks_b_g_egldusdc = qty_asks_b_l_egldusdc 


def on_close_egldusdc(ws): 
	print('### closed ###') 

def on_error_egldusdc(ws, message): 
	print(message) 

def on_open_egldusdc(ws): 
	ws.send(json.dumps({'sub': f'market.egldusdc.ticker'})) 

def loop_egldusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_egldusdc, 
		on_close=on_close_egldusdc, 
		on_error=on_error_egldusdc) 
	ws.on_open = on_open_egldusdc 
	ws.run_forever() 

Thread(target=loop_egldusdc).start() 

def loop_egldusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_egldusdt != 0.0 and qty_bids_a_g_egldusdt != 0.0 and price_asks_a_g_egldusdt != 0.0 and qty_asks_a_g_egldusdt != 0.0 and price_bids_b_g_egldusdc != 0.0 and qty_bids_b_g_egldusdc != 0.0 and price_asks_b_g_egldusdc != 0.0 and qty_asks_b_g_egldusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_egldusdt) 
			price_b = float(price_bids_b_g_egldusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_egldusdc, pribil)

Thread(target=loop_egldusdt_Trade).start() 

symbol_a_g_linkusdt = 'linkusdt' 
price_bids_a_g_linkusdt = float(0.0) 
qty_bids_a_g_linkusdt = float(0.0) 
price_asks_a_g_linkusdt = float(0.0) 
qty_asks_a_g_linkusdt = float(0.0) 

def on_message_linkusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_linkusdt = 'linkusdt' 
		price_bids_a_l_linkusdt = data['tick']['bid'] 
		qty_bids_a_l_linkusdt = data['tick']['bidSize'] 
		price_asks_a_l_linkusdt = data['tick']['ask'] 
		qty_asks_a_l_linkusdt = data['tick']['askSize'] 

		global symbol_a_g_linkusdt 
		global price_bids_a_g_linkusdt 
		global qty_bids_a_g_linkusdt 
		global price_asks_a_g_linkusdt 
		global qty_asks_a_g_linkusdt 

		symbol_a_g_linkusdt = symbol_a_l_linkusdt 
		price_bids_a_g_linkusdt = price_bids_a_l_linkusdt 
		qty_bids_a_g_linkusdt = qty_bids_a_l_linkusdt 
		price_asks_a_g_linkusdt = price_asks_a_l_linkusdt 
		qty_asks_a_g_linkusdt = qty_asks_a_l_linkusdt 

def on_close_linkusdt(ws): 
	print('### closed ###') 

def on_error_linkusdt(ws, message): 
	print(message) 

def on_open_linkusdt(ws): 
	ws.send(json.dumps({'sub': f'market.linkusdt.ticker'})) 

def loop_linkusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_linkusdt, 
		on_close=on_close_linkusdt, 
		on_error=on_error_linkusdt) 
	ws.on_open = on_open_linkusdt 
	ws.run_forever() 

Thread(target=loop_linkusdt).start() 

symbol_b_g_linketh = 'linketh' 
price_bids_b_g_linketh = float(0.0) 
qty_bids_b_g_linketh = float(0.0) 
price_asks_b_g_linketh = float(0.0) 
qty_asks_b_g_linketh = float(0.0) 

def on_message_linketh(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_linketh = 'linketh' 
		price_bids_b_l_linketh = data['tick']['bid'] 
		qty_bids_b_l_linketh = data['tick']['bidSize']
		price_asks_b_l_linketh = data['tick']['ask'] 
		qty_asks_b_l_linketh = data['tick']['askSize'] 

		global symbol_b_g_linketh 
		global price_bids_b_g_linketh 
		global qty_bids_b_g_linketh 
		global price_asks_b_g_linketh 
		global qty_asks_b_g_linketh 

		symbol_b_g_linketh = symbol_b_l_linketh 
		price_bids_b_g_linketh = price_bids_b_l_linketh 
		qty_bids_b_g_linketh = qty_bids_b_l_linketh 
		price_asks_b_g_linketh = price_asks_b_l_linketh 
		qty_asks_b_g_linketh = qty_asks_b_l_linketh 


def on_close_linketh(ws): 
	print('### closed ###') 

def on_error_linketh(ws, message): 
	print(message) 

def on_open_linketh(ws): 
	ws.send(json.dumps({'sub': f'market.linketh.ticker'})) 

def loop_linketh(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_linketh, 
		on_close=on_close_linketh, 
		on_error=on_error_linketh) 
	ws.on_open = on_open_linketh 
	ws.run_forever() 

Thread(target=loop_linketh).start() 

def loop_linkusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_linkusdt != 0.0 and qty_bids_a_g_linkusdt != 0.0 and price_asks_a_g_linkusdt != 0.0 and qty_asks_a_g_linkusdt != 0.0 and price_bids_b_g_linketh != 0.0 and qty_bids_b_g_linketh != 0.0 and price_asks_b_g_linketh != 0.0 and qty_asks_b_g_linketh != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_linkusdt) 
			price_b = float(price_bids_b_g_linketh) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_linketh, pribil)

Thread(target=loop_linkusdt_Trade).start() 

symbol_a_g_bttusdt = 'bttusdt' 
price_bids_a_g_bttusdt = float(0.0) 
qty_bids_a_g_bttusdt = float(0.0) 
price_asks_a_g_bttusdt = float(0.0) 
qty_asks_a_g_bttusdt = float(0.0) 

def on_message_bttusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_bttusdt = 'bttusdt' 
		price_bids_a_l_bttusdt = data['tick']['bid'] 
		qty_bids_a_l_bttusdt = data['tick']['bidSize'] 
		price_asks_a_l_bttusdt = data['tick']['ask'] 
		qty_asks_a_l_bttusdt = data['tick']['askSize'] 

		global symbol_a_g_bttusdt 
		global price_bids_a_g_bttusdt 
		global qty_bids_a_g_bttusdt 
		global price_asks_a_g_bttusdt 
		global qty_asks_a_g_bttusdt 

		symbol_a_g_bttusdt = symbol_a_l_bttusdt 
		price_bids_a_g_bttusdt = price_bids_a_l_bttusdt 
		qty_bids_a_g_bttusdt = qty_bids_a_l_bttusdt 
		price_asks_a_g_bttusdt = price_asks_a_l_bttusdt 
		qty_asks_a_g_bttusdt = qty_asks_a_l_bttusdt 

def on_close_bttusdt(ws): 
	print('### closed ###') 

def on_error_bttusdt(ws, message): 
	print(message) 

def on_open_bttusdt(ws): 
	ws.send(json.dumps({'sub': f'market.bttusdt.ticker'})) 

def loop_bttusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bttusdt, 
		on_close=on_close_bttusdt, 
		on_error=on_error_bttusdt) 
	ws.on_open = on_open_bttusdt 
	ws.run_forever() 

Thread(target=loop_bttusdt).start() 

symbol_b_g_bttusdd = 'bttusdd' 
price_bids_b_g_bttusdd = float(0.0) 
qty_bids_b_g_bttusdd = float(0.0) 
price_asks_b_g_bttusdd = float(0.0) 
qty_asks_b_g_bttusdd = float(0.0) 

def on_message_bttusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_bttusdd = 'bttusdd' 
		price_bids_b_l_bttusdd = data['tick']['bid'] 
		qty_bids_b_l_bttusdd = data['tick']['bidSize']
		price_asks_b_l_bttusdd = data['tick']['ask'] 
		qty_asks_b_l_bttusdd = data['tick']['askSize'] 

		global symbol_b_g_bttusdd 
		global price_bids_b_g_bttusdd 
		global qty_bids_b_g_bttusdd 
		global price_asks_b_g_bttusdd 
		global qty_asks_b_g_bttusdd 

		symbol_b_g_bttusdd = symbol_b_l_bttusdd 
		price_bids_b_g_bttusdd = price_bids_b_l_bttusdd 
		qty_bids_b_g_bttusdd = qty_bids_b_l_bttusdd 
		price_asks_b_g_bttusdd = price_asks_b_l_bttusdd 
		qty_asks_b_g_bttusdd = qty_asks_b_l_bttusdd 


def on_close_bttusdd(ws): 
	print('### closed ###') 

def on_error_bttusdd(ws, message): 
	print(message) 

def on_open_bttusdd(ws): 
	ws.send(json.dumps({'sub': f'market.bttusdd.ticker'})) 

def loop_bttusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bttusdd, 
		on_close=on_close_bttusdd, 
		on_error=on_error_bttusdd) 
	ws.on_open = on_open_bttusdd 
	ws.run_forever() 

Thread(target=loop_bttusdd).start() 

def loop_bttusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_bttusdt != 0.0 and qty_bids_a_g_bttusdt != 0.0 and price_asks_a_g_bttusdt != 0.0 and qty_asks_a_g_bttusdt != 0.0 and price_bids_b_g_bttusdd != 0.0 and qty_bids_b_g_bttusdd != 0.0 and price_asks_b_g_bttusdd != 0.0 and qty_asks_b_g_bttusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_bttusdt) 
			price_b = float(price_bids_b_g_bttusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_bttusdd, pribil)

Thread(target=loop_bttusdt_Trade).start() 

symbol_a_g_atomusdt = 'atomusdt' 
price_bids_a_g_atomusdt = float(0.0) 
qty_bids_a_g_atomusdt = float(0.0) 
price_asks_a_g_atomusdt = float(0.0) 
qty_asks_a_g_atomusdt = float(0.0) 

def on_message_atomusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_atomusdt = 'atomusdt' 
		price_bids_a_l_atomusdt = data['tick']['bid'] 
		qty_bids_a_l_atomusdt = data['tick']['bidSize'] 
		price_asks_a_l_atomusdt = data['tick']['ask'] 
		qty_asks_a_l_atomusdt = data['tick']['askSize'] 

		global symbol_a_g_atomusdt 
		global price_bids_a_g_atomusdt 
		global qty_bids_a_g_atomusdt 
		global price_asks_a_g_atomusdt 
		global qty_asks_a_g_atomusdt 

		symbol_a_g_atomusdt = symbol_a_l_atomusdt 
		price_bids_a_g_atomusdt = price_bids_a_l_atomusdt 
		qty_bids_a_g_atomusdt = qty_bids_a_l_atomusdt 
		price_asks_a_g_atomusdt = price_asks_a_l_atomusdt 
		qty_asks_a_g_atomusdt = qty_asks_a_l_atomusdt 

def on_close_atomusdt(ws): 
	print('### closed ###') 

def on_error_atomusdt(ws, message): 
	print(message) 

def on_open_atomusdt(ws): 
	ws.send(json.dumps({'sub': f'market.atomusdt.ticker'})) 

def loop_atomusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_atomusdt, 
		on_close=on_close_atomusdt, 
		on_error=on_error_atomusdt) 
	ws.on_open = on_open_atomusdt 
	ws.run_forever() 

Thread(target=loop_atomusdt).start() 

symbol_b_g_atometh = 'atometh' 
price_bids_b_g_atometh = float(0.0) 
qty_bids_b_g_atometh = float(0.0) 
price_asks_b_g_atometh = float(0.0) 
qty_asks_b_g_atometh = float(0.0) 

def on_message_atometh(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_atometh = 'atometh' 
		price_bids_b_l_atometh = data['tick']['bid'] 
		qty_bids_b_l_atometh = data['tick']['bidSize']
		price_asks_b_l_atometh = data['tick']['ask'] 
		qty_asks_b_l_atometh = data['tick']['askSize'] 

		global symbol_b_g_atometh 
		global price_bids_b_g_atometh 
		global qty_bids_b_g_atometh 
		global price_asks_b_g_atometh 
		global qty_asks_b_g_atometh 

		symbol_b_g_atometh = symbol_b_l_atometh 
		price_bids_b_g_atometh = price_bids_b_l_atometh 
		qty_bids_b_g_atometh = qty_bids_b_l_atometh 
		price_asks_b_g_atometh = price_asks_b_l_atometh 
		qty_asks_b_g_atometh = qty_asks_b_l_atometh 


def on_close_atometh(ws): 
	print('### closed ###') 

def on_error_atometh(ws, message): 
	print(message) 

def on_open_atometh(ws): 
	ws.send(json.dumps({'sub': f'market.atometh.ticker'})) 

def loop_atometh(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_atometh, 
		on_close=on_close_atometh, 
		on_error=on_error_atometh) 
	ws.on_open = on_open_atometh 
	ws.run_forever() 

Thread(target=loop_atometh).start() 

def loop_atomusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_atomusdt != 0.0 and qty_bids_a_g_atomusdt != 0.0 and price_asks_a_g_atomusdt != 0.0 and qty_asks_a_g_atomusdt != 0.0 and price_bids_b_g_atometh != 0.0 and qty_bids_b_g_atometh != 0.0 and price_asks_b_g_atometh != 0.0 and qty_asks_b_g_atometh != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_atomusdt) 
			price_b = float(price_bids_b_g_atometh) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_atometh, pribil)

Thread(target=loop_atomusdt_Trade).start() 

symbol_a_g_xlmusdt = 'xlmusdt' 
price_bids_a_g_xlmusdt = float(0.0) 
qty_bids_a_g_xlmusdt = float(0.0) 
price_asks_a_g_xlmusdt = float(0.0) 
qty_asks_a_g_xlmusdt = float(0.0) 

def on_message_xlmusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_xlmusdt = 'xlmusdt' 
		price_bids_a_l_xlmusdt = data['tick']['bid'] 
		qty_bids_a_l_xlmusdt = data['tick']['bidSize'] 
		price_asks_a_l_xlmusdt = data['tick']['ask'] 
		qty_asks_a_l_xlmusdt = data['tick']['askSize'] 

		global symbol_a_g_xlmusdt 
		global price_bids_a_g_xlmusdt 
		global qty_bids_a_g_xlmusdt 
		global price_asks_a_g_xlmusdt 
		global qty_asks_a_g_xlmusdt 

		symbol_a_g_xlmusdt = symbol_a_l_xlmusdt 
		price_bids_a_g_xlmusdt = price_bids_a_l_xlmusdt 
		qty_bids_a_g_xlmusdt = qty_bids_a_l_xlmusdt 
		price_asks_a_g_xlmusdt = price_asks_a_l_xlmusdt 
		qty_asks_a_g_xlmusdt = qty_asks_a_l_xlmusdt 

def on_close_xlmusdt(ws): 
	print('### closed ###') 

def on_error_xlmusdt(ws, message): 
	print(message) 

def on_open_xlmusdt(ws): 
	ws.send(json.dumps({'sub': f'market.xlmusdt.ticker'})) 

def loop_xlmusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xlmusdt, 
		on_close=on_close_xlmusdt, 
		on_error=on_error_xlmusdt) 
	ws.on_open = on_open_xlmusdt 
	ws.run_forever() 

Thread(target=loop_xlmusdt).start() 

symbol_b_g_xlmeth = 'xlmeth' 
price_bids_b_g_xlmeth = float(0.0) 
qty_bids_b_g_xlmeth = float(0.0) 
price_asks_b_g_xlmeth = float(0.0) 
qty_asks_b_g_xlmeth = float(0.0) 

def on_message_xlmeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_xlmeth = 'xlmeth' 
		price_bids_b_l_xlmeth = data['tick']['bid'] 
		qty_bids_b_l_xlmeth = data['tick']['bidSize']
		price_asks_b_l_xlmeth = data['tick']['ask'] 
		qty_asks_b_l_xlmeth = data['tick']['askSize'] 

		global symbol_b_g_xlmeth 
		global price_bids_b_g_xlmeth 
		global qty_bids_b_g_xlmeth 
		global price_asks_b_g_xlmeth 
		global qty_asks_b_g_xlmeth 

		symbol_b_g_xlmeth = symbol_b_l_xlmeth 
		price_bids_b_g_xlmeth = price_bids_b_l_xlmeth 
		qty_bids_b_g_xlmeth = qty_bids_b_l_xlmeth 
		price_asks_b_g_xlmeth = price_asks_b_l_xlmeth 
		qty_asks_b_g_xlmeth = qty_asks_b_l_xlmeth 


def on_close_xlmeth(ws): 
	print('### closed ###') 

def on_error_xlmeth(ws, message): 
	print(message) 

def on_open_xlmeth(ws): 
	ws.send(json.dumps({'sub': f'market.xlmeth.ticker'})) 

def loop_xlmeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xlmeth, 
		on_close=on_close_xlmeth, 
		on_error=on_error_xlmeth) 
	ws.on_open = on_open_xlmeth 
	ws.run_forever() 

Thread(target=loop_xlmeth).start() 

def loop_xlmusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_xlmusdt != 0.0 and qty_bids_a_g_xlmusdt != 0.0 and price_asks_a_g_xlmusdt != 0.0 and qty_asks_a_g_xlmusdt != 0.0 and price_bids_b_g_xlmeth != 0.0 and qty_bids_b_g_xlmeth != 0.0 and price_asks_b_g_xlmeth != 0.0 and qty_asks_b_g_xlmeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_xlmusdt) 
			price_b = float(price_bids_b_g_xlmeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_xlmeth, pribil)

Thread(target=loop_xlmusdt_Trade).start() 

symbol_a_g_lnusdt = 'lnusdt' 
price_bids_a_g_lnusdt = float(0.0) 
qty_bids_a_g_lnusdt = float(0.0) 
price_asks_a_g_lnusdt = float(0.0) 
qty_asks_a_g_lnusdt = float(0.0) 

def on_message_lnusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_lnusdt = 'lnusdt' 
		price_bids_a_l_lnusdt = data['tick']['bid'] 
		qty_bids_a_l_lnusdt = data['tick']['bidSize'] 
		price_asks_a_l_lnusdt = data['tick']['ask'] 
		qty_asks_a_l_lnusdt = data['tick']['askSize'] 

		global symbol_a_g_lnusdt 
		global price_bids_a_g_lnusdt 
		global qty_bids_a_g_lnusdt 
		global price_asks_a_g_lnusdt 
		global qty_asks_a_g_lnusdt 

		symbol_a_g_lnusdt = symbol_a_l_lnusdt 
		price_bids_a_g_lnusdt = price_bids_a_l_lnusdt 
		qty_bids_a_g_lnusdt = qty_bids_a_l_lnusdt 
		price_asks_a_g_lnusdt = price_asks_a_l_lnusdt 
		qty_asks_a_g_lnusdt = qty_asks_a_l_lnusdt 

def on_close_lnusdt(ws): 
	print('### closed ###') 

def on_error_lnusdt(ws, message): 
	print(message) 

def on_open_lnusdt(ws): 
	ws.send(json.dumps({'sub': f'market.lnusdt.ticker'})) 

def loop_lnusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_lnusdt, 
		on_close=on_close_lnusdt, 
		on_error=on_error_lnusdt) 
	ws.on_open = on_open_lnusdt 
	ws.run_forever() 

Thread(target=loop_lnusdt).start() 

symbol_b_g_lnbtc = 'lnbtc' 
price_bids_b_g_lnbtc = float(0.0) 
qty_bids_b_g_lnbtc = float(0.0) 
price_asks_b_g_lnbtc = float(0.0) 
qty_asks_b_g_lnbtc = float(0.0) 

def on_message_lnbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_lnbtc = 'lnbtc' 
		price_bids_b_l_lnbtc = data['tick']['bid'] 
		qty_bids_b_l_lnbtc = data['tick']['bidSize']
		price_asks_b_l_lnbtc = data['tick']['ask'] 
		qty_asks_b_l_lnbtc = data['tick']['askSize'] 

		global symbol_b_g_lnbtc 
		global price_bids_b_g_lnbtc 
		global qty_bids_b_g_lnbtc 
		global price_asks_b_g_lnbtc 
		global qty_asks_b_g_lnbtc 

		symbol_b_g_lnbtc = symbol_b_l_lnbtc 
		price_bids_b_g_lnbtc = price_bids_b_l_lnbtc 
		qty_bids_b_g_lnbtc = qty_bids_b_l_lnbtc 
		price_asks_b_g_lnbtc = price_asks_b_l_lnbtc 
		qty_asks_b_g_lnbtc = qty_asks_b_l_lnbtc 


def on_close_lnbtc(ws): 
	print('### closed ###') 

def on_error_lnbtc(ws, message): 
	print(message) 

def on_open_lnbtc(ws): 
	ws.send(json.dumps({'sub': f'market.lnbtc.ticker'})) 

def loop_lnbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_lnbtc, 
		on_close=on_close_lnbtc, 
		on_error=on_error_lnbtc) 
	ws.on_open = on_open_lnbtc 
	ws.run_forever() 

Thread(target=loop_lnbtc).start() 

def loop_lnusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_lnusdt != 0.0 and qty_bids_a_g_lnusdt != 0.0 and price_asks_a_g_lnusdt != 0.0 and qty_asks_a_g_lnusdt != 0.0 and price_bids_b_g_lnbtc != 0.0 and qty_bids_b_g_lnbtc != 0.0 and price_asks_b_g_lnbtc != 0.0 and qty_asks_b_g_lnbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_lnusdt) 
			price_b = float(price_bids_b_g_lnbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_lnbtc, pribil)

Thread(target=loop_lnusdt_Trade).start() 

symbol_a_g_eosusdt = 'eosusdt' 
price_bids_a_g_eosusdt = float(0.0) 
qty_bids_a_g_eosusdt = float(0.0) 
price_asks_a_g_eosusdt = float(0.0) 
qty_asks_a_g_eosusdt = float(0.0) 

def on_message_eosusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_eosusdt = 'eosusdt' 
		price_bids_a_l_eosusdt = data['tick']['bid'] 
		qty_bids_a_l_eosusdt = data['tick']['bidSize'] 
		price_asks_a_l_eosusdt = data['tick']['ask'] 
		qty_asks_a_l_eosusdt = data['tick']['askSize'] 

		global symbol_a_g_eosusdt 
		global price_bids_a_g_eosusdt 
		global qty_bids_a_g_eosusdt 
		global price_asks_a_g_eosusdt 
		global qty_asks_a_g_eosusdt 

		symbol_a_g_eosusdt = symbol_a_l_eosusdt 
		price_bids_a_g_eosusdt = price_bids_a_l_eosusdt 
		qty_bids_a_g_eosusdt = qty_bids_a_l_eosusdt 
		price_asks_a_g_eosusdt = price_asks_a_l_eosusdt 
		qty_asks_a_g_eosusdt = qty_asks_a_l_eosusdt 

def on_close_eosusdt(ws): 
	print('### closed ###') 

def on_error_eosusdt(ws, message): 
	print(message) 

def on_open_eosusdt(ws): 
	ws.send(json.dumps({'sub': f'market.eosusdt.ticker'})) 

def loop_eosusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_eosusdt, 
		on_close=on_close_eosusdt, 
		on_error=on_error_eosusdt) 
	ws.on_open = on_open_eosusdt 
	ws.run_forever() 

Thread(target=loop_eosusdt).start() 

symbol_b_g_eoseth = 'eoseth' 
price_bids_b_g_eoseth = float(0.0) 
qty_bids_b_g_eoseth = float(0.0) 
price_asks_b_g_eoseth = float(0.0) 
qty_asks_b_g_eoseth = float(0.0) 

def on_message_eoseth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_eoseth = 'eoseth' 
		price_bids_b_l_eoseth = data['tick']['bid'] 
		qty_bids_b_l_eoseth = data['tick']['bidSize']
		price_asks_b_l_eoseth = data['tick']['ask'] 
		qty_asks_b_l_eoseth = data['tick']['askSize'] 

		global symbol_b_g_eoseth 
		global price_bids_b_g_eoseth 
		global qty_bids_b_g_eoseth 
		global price_asks_b_g_eoseth 
		global qty_asks_b_g_eoseth 

		symbol_b_g_eoseth = symbol_b_l_eoseth 
		price_bids_b_g_eoseth = price_bids_b_l_eoseth 
		qty_bids_b_g_eoseth = qty_bids_b_l_eoseth 
		price_asks_b_g_eoseth = price_asks_b_l_eoseth 
		qty_asks_b_g_eoseth = qty_asks_b_l_eoseth 


def on_close_eoseth(ws): 
	print('### closed ###') 

def on_error_eoseth(ws, message): 
	print(message) 

def on_open_eoseth(ws): 
	ws.send(json.dumps({'sub': f'market.eoseth.ticker'})) 

def loop_eoseth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_eoseth, 
		on_close=on_close_eoseth, 
		on_error=on_error_eoseth) 
	ws.on_open = on_open_eoseth 
	ws.run_forever() 

Thread(target=loop_eoseth).start() 

def loop_eosusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_eosusdt != 0.0 and qty_bids_a_g_eosusdt != 0.0 and price_asks_a_g_eosusdt != 0.0 and qty_asks_a_g_eosusdt != 0.0 and price_bids_b_g_eoseth != 0.0 and qty_bids_b_g_eoseth != 0.0 and price_asks_b_g_eoseth != 0.0 and qty_asks_b_g_eoseth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_eosusdt) 
			price_b = float(price_bids_b_g_eoseth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_eoseth, pribil)

Thread(target=loop_eosusdt_Trade).start() 

symbol_a_g_bethusdt = 'bethusdt' 
price_bids_a_g_bethusdt = float(0.0) 
qty_bids_a_g_bethusdt = float(0.0) 
price_asks_a_g_bethusdt = float(0.0) 
qty_asks_a_g_bethusdt = float(0.0) 

def on_message_bethusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_bethusdt = 'bethusdt' 
		price_bids_a_l_bethusdt = data['tick']['bid'] 
		qty_bids_a_l_bethusdt = data['tick']['bidSize'] 
		price_asks_a_l_bethusdt = data['tick']['ask'] 
		qty_asks_a_l_bethusdt = data['tick']['askSize'] 

		global symbol_a_g_bethusdt 
		global price_bids_a_g_bethusdt 
		global qty_bids_a_g_bethusdt 
		global price_asks_a_g_bethusdt 
		global qty_asks_a_g_bethusdt 

		symbol_a_g_bethusdt = symbol_a_l_bethusdt 
		price_bids_a_g_bethusdt = price_bids_a_l_bethusdt 
		qty_bids_a_g_bethusdt = qty_bids_a_l_bethusdt 
		price_asks_a_g_bethusdt = price_asks_a_l_bethusdt 
		qty_asks_a_g_bethusdt = qty_asks_a_l_bethusdt 

def on_close_bethusdt(ws): 
	print('### closed ###') 

def on_error_bethusdt(ws, message): 
	print(message) 

def on_open_bethusdt(ws): 
	ws.send(json.dumps({'sub': f'market.bethusdt.ticker'})) 

def loop_bethusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bethusdt, 
		on_close=on_close_bethusdt, 
		on_error=on_error_bethusdt) 
	ws.on_open = on_open_bethusdt 
	ws.run_forever() 

Thread(target=loop_bethusdt).start() 

symbol_b_g_betheth = 'betheth' 
price_bids_b_g_betheth = float(0.0) 
qty_bids_b_g_betheth = float(0.0) 
price_asks_b_g_betheth = float(0.0) 
qty_asks_b_g_betheth = float(0.0) 

def on_message_betheth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_betheth = 'betheth' 
		price_bids_b_l_betheth = data['tick']['bid'] 
		qty_bids_b_l_betheth = data['tick']['bidSize']
		price_asks_b_l_betheth = data['tick']['ask'] 
		qty_asks_b_l_betheth = data['tick']['askSize'] 

		global symbol_b_g_betheth 
		global price_bids_b_g_betheth 
		global qty_bids_b_g_betheth 
		global price_asks_b_g_betheth 
		global qty_asks_b_g_betheth 

		symbol_b_g_betheth = symbol_b_l_betheth 
		price_bids_b_g_betheth = price_bids_b_l_betheth 
		qty_bids_b_g_betheth = qty_bids_b_l_betheth 
		price_asks_b_g_betheth = price_asks_b_l_betheth 
		qty_asks_b_g_betheth = qty_asks_b_l_betheth 


def on_close_betheth(ws): 
	print('### closed ###') 

def on_error_betheth(ws, message): 
	print(message) 

def on_open_betheth(ws): 
	ws.send(json.dumps({'sub': f'market.betheth.ticker'})) 

def loop_betheth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_betheth, 
		on_close=on_close_betheth, 
		on_error=on_error_betheth) 
	ws.on_open = on_open_betheth 
	ws.run_forever() 

Thread(target=loop_betheth).start() 

def loop_bethusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_bethusdt != 0.0 and qty_bids_a_g_bethusdt != 0.0 and price_asks_a_g_bethusdt != 0.0 and qty_asks_a_g_bethusdt != 0.0 and price_bids_b_g_betheth != 0.0 and qty_bids_b_g_betheth != 0.0 and price_asks_b_g_betheth != 0.0 and qty_asks_b_g_betheth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_bethusdt) 
			price_b = float(price_bids_b_g_betheth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_betheth, pribil)

Thread(target=loop_bethusdt_Trade).start() 

symbol_a_g_elausdt = 'elausdt' 
price_bids_a_g_elausdt = float(0.0) 
qty_bids_a_g_elausdt = float(0.0) 
price_asks_a_g_elausdt = float(0.0) 
qty_asks_a_g_elausdt = float(0.0) 

def on_message_elausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_elausdt = 'elausdt' 
		price_bids_a_l_elausdt = data['tick']['bid'] 
		qty_bids_a_l_elausdt = data['tick']['bidSize'] 
		price_asks_a_l_elausdt = data['tick']['ask'] 
		qty_asks_a_l_elausdt = data['tick']['askSize'] 

		global symbol_a_g_elausdt 
		global price_bids_a_g_elausdt 
		global qty_bids_a_g_elausdt 
		global price_asks_a_g_elausdt 
		global qty_asks_a_g_elausdt 

		symbol_a_g_elausdt = symbol_a_l_elausdt 
		price_bids_a_g_elausdt = price_bids_a_l_elausdt 
		qty_bids_a_g_elausdt = qty_bids_a_l_elausdt 
		price_asks_a_g_elausdt = price_asks_a_l_elausdt 
		qty_asks_a_g_elausdt = qty_asks_a_l_elausdt 

def on_close_elausdt(ws): 
	print('### closed ###') 

def on_error_elausdt(ws, message): 
	print(message) 

def on_open_elausdt(ws): 
	ws.send(json.dumps({'sub': f'market.elausdt.ticker'})) 

def loop_elausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_elausdt, 
		on_close=on_close_elausdt, 
		on_error=on_error_elausdt) 
	ws.on_open = on_open_elausdt 
	ws.run_forever() 

Thread(target=loop_elausdt).start() 

symbol_b_g_elabtc = 'elabtc' 
price_bids_b_g_elabtc = float(0.0) 
qty_bids_b_g_elabtc = float(0.0) 
price_asks_b_g_elabtc = float(0.0) 
qty_asks_b_g_elabtc = float(0.0) 

def on_message_elabtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_elabtc = 'elabtc' 
		price_bids_b_l_elabtc = data['tick']['bid'] 
		qty_bids_b_l_elabtc = data['tick']['bidSize']
		price_asks_b_l_elabtc = data['tick']['ask'] 
		qty_asks_b_l_elabtc = data['tick']['askSize'] 

		global symbol_b_g_elabtc 
		global price_bids_b_g_elabtc 
		global qty_bids_b_g_elabtc 
		global price_asks_b_g_elabtc 
		global qty_asks_b_g_elabtc 

		symbol_b_g_elabtc = symbol_b_l_elabtc 
		price_bids_b_g_elabtc = price_bids_b_l_elabtc 
		qty_bids_b_g_elabtc = qty_bids_b_l_elabtc 
		price_asks_b_g_elabtc = price_asks_b_l_elabtc 
		qty_asks_b_g_elabtc = qty_asks_b_l_elabtc 


def on_close_elabtc(ws): 
	print('### closed ###') 

def on_error_elabtc(ws, message): 
	print(message) 

def on_open_elabtc(ws): 
	ws.send(json.dumps({'sub': f'market.elabtc.ticker'})) 

def loop_elabtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_elabtc, 
		on_close=on_close_elabtc, 
		on_error=on_error_elabtc) 
	ws.on_open = on_open_elabtc 
	ws.run_forever() 

Thread(target=loop_elabtc).start() 

def loop_elausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_elausdt != 0.0 and qty_bids_a_g_elausdt != 0.0 and price_asks_a_g_elausdt != 0.0 and qty_asks_a_g_elausdt != 0.0 and price_bids_b_g_elabtc != 0.0 and qty_bids_b_g_elabtc != 0.0 and price_asks_b_g_elabtc != 0.0 and qty_asks_b_g_elabtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_elausdt) 
			price_b = float(price_bids_b_g_elabtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_elabtc, pribil)

Thread(target=loop_elausdt_Trade).start() 

symbol_a_g_axsusdt = 'axsusdt' 
price_bids_a_g_axsusdt = float(0.0) 
qty_bids_a_g_axsusdt = float(0.0) 
price_asks_a_g_axsusdt = float(0.0) 
qty_asks_a_g_axsusdt = float(0.0) 

def on_message_axsusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_axsusdt = 'axsusdt' 
		price_bids_a_l_axsusdt = data['tick']['bid'] 
		qty_bids_a_l_axsusdt = data['tick']['bidSize'] 
		price_asks_a_l_axsusdt = data['tick']['ask'] 
		qty_asks_a_l_axsusdt = data['tick']['askSize'] 

		global symbol_a_g_axsusdt 
		global price_bids_a_g_axsusdt 
		global qty_bids_a_g_axsusdt 
		global price_asks_a_g_axsusdt 
		global qty_asks_a_g_axsusdt 

		symbol_a_g_axsusdt = symbol_a_l_axsusdt 
		price_bids_a_g_axsusdt = price_bids_a_l_axsusdt 
		qty_bids_a_g_axsusdt = qty_bids_a_l_axsusdt 
		price_asks_a_g_axsusdt = price_asks_a_l_axsusdt 
		qty_asks_a_g_axsusdt = qty_asks_a_l_axsusdt 

def on_close_axsusdt(ws): 
	print('### closed ###') 

def on_error_axsusdt(ws, message): 
	print(message) 

def on_open_axsusdt(ws): 
	ws.send(json.dumps({'sub': f'market.axsusdt.ticker'})) 

def loop_axsusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_axsusdt, 
		on_close=on_close_axsusdt, 
		on_error=on_error_axsusdt) 
	ws.on_open = on_open_axsusdt 
	ws.run_forever() 

Thread(target=loop_axsusdt).start() 

symbol_b_g_axseth = 'axseth' 
price_bids_b_g_axseth = float(0.0) 
qty_bids_b_g_axseth = float(0.0) 
price_asks_b_g_axseth = float(0.0) 
qty_asks_b_g_axseth = float(0.0) 

def on_message_axseth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_axseth = 'axseth' 
		price_bids_b_l_axseth = data['tick']['bid'] 
		qty_bids_b_l_axseth = data['tick']['bidSize']
		price_asks_b_l_axseth = data['tick']['ask'] 
		qty_asks_b_l_axseth = data['tick']['askSize'] 

		global symbol_b_g_axseth 
		global price_bids_b_g_axseth 
		global qty_bids_b_g_axseth 
		global price_asks_b_g_axseth 
		global qty_asks_b_g_axseth 

		symbol_b_g_axseth = symbol_b_l_axseth 
		price_bids_b_g_axseth = price_bids_b_l_axseth 
		qty_bids_b_g_axseth = qty_bids_b_l_axseth 
		price_asks_b_g_axseth = price_asks_b_l_axseth 
		qty_asks_b_g_axseth = qty_asks_b_l_axseth 


def on_close_axseth(ws): 
	print('### closed ###') 

def on_error_axseth(ws, message): 
	print(message) 

def on_open_axseth(ws): 
	ws.send(json.dumps({'sub': f'market.axseth.ticker'})) 

def loop_axseth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_axseth, 
		on_close=on_close_axseth, 
		on_error=on_error_axseth) 
	ws.on_open = on_open_axseth 
	ws.run_forever() 

Thread(target=loop_axseth).start() 

def loop_axsusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_axsusdt != 0.0 and qty_bids_a_g_axsusdt != 0.0 and price_asks_a_g_axsusdt != 0.0 and qty_asks_a_g_axsusdt != 0.0 and price_bids_b_g_axseth != 0.0 and qty_bids_b_g_axseth != 0.0 and price_asks_b_g_axseth != 0.0 and qty_asks_b_g_axseth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_axsusdt) 
			price_b = float(price_bids_b_g_axseth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_axseth, pribil)

Thread(target=loop_axsusdt_Trade).start() 

symbol_a_g_gnousdt = 'gnousdt' 
price_bids_a_g_gnousdt = float(0.0) 
qty_bids_a_g_gnousdt = float(0.0) 
price_asks_a_g_gnousdt = float(0.0) 
qty_asks_a_g_gnousdt = float(0.0) 

def on_message_gnousdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_gnousdt = 'gnousdt' 
		price_bids_a_l_gnousdt = data['tick']['bid'] 
		qty_bids_a_l_gnousdt = data['tick']['bidSize'] 
		price_asks_a_l_gnousdt = data['tick']['ask'] 
		qty_asks_a_l_gnousdt = data['tick']['askSize'] 

		global symbol_a_g_gnousdt 
		global price_bids_a_g_gnousdt 
		global qty_bids_a_g_gnousdt 
		global price_asks_a_g_gnousdt 
		global qty_asks_a_g_gnousdt 

		symbol_a_g_gnousdt = symbol_a_l_gnousdt 
		price_bids_a_g_gnousdt = price_bids_a_l_gnousdt 
		qty_bids_a_g_gnousdt = qty_bids_a_l_gnousdt 
		price_asks_a_g_gnousdt = price_asks_a_l_gnousdt 
		qty_asks_a_g_gnousdt = qty_asks_a_l_gnousdt 

def on_close_gnousdt(ws): 
	print('### closed ###') 

def on_error_gnousdt(ws, message): 
	print(message) 

def on_open_gnousdt(ws): 
	ws.send(json.dumps({'sub': f'market.gnousdt.ticker'})) 

def loop_gnousdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_gnousdt, 
		on_close=on_close_gnousdt, 
		on_error=on_error_gnousdt) 
	ws.on_open = on_open_gnousdt 
	ws.run_forever() 

Thread(target=loop_gnousdt).start() 

symbol_b_g_gnobtc = 'gnobtc' 
price_bids_b_g_gnobtc = float(0.0) 
qty_bids_b_g_gnobtc = float(0.0) 
price_asks_b_g_gnobtc = float(0.0) 
qty_asks_b_g_gnobtc = float(0.0) 

def on_message_gnobtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_gnobtc = 'gnobtc' 
		price_bids_b_l_gnobtc = data['tick']['bid'] 
		qty_bids_b_l_gnobtc = data['tick']['bidSize']
		price_asks_b_l_gnobtc = data['tick']['ask'] 
		qty_asks_b_l_gnobtc = data['tick']['askSize'] 

		global symbol_b_g_gnobtc 
		global price_bids_b_g_gnobtc 
		global qty_bids_b_g_gnobtc 
		global price_asks_b_g_gnobtc 
		global qty_asks_b_g_gnobtc 

		symbol_b_g_gnobtc = symbol_b_l_gnobtc 
		price_bids_b_g_gnobtc = price_bids_b_l_gnobtc 
		qty_bids_b_g_gnobtc = qty_bids_b_l_gnobtc 
		price_asks_b_g_gnobtc = price_asks_b_l_gnobtc 
		qty_asks_b_g_gnobtc = qty_asks_b_l_gnobtc 


def on_close_gnobtc(ws): 
	print('### closed ###') 

def on_error_gnobtc(ws, message): 
	print(message) 

def on_open_gnobtc(ws): 
	ws.send(json.dumps({'sub': f'market.gnobtc.ticker'})) 

def loop_gnobtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_gnobtc, 
		on_close=on_close_gnobtc, 
		on_error=on_error_gnobtc) 
	ws.on_open = on_open_gnobtc 
	ws.run_forever() 

Thread(target=loop_gnobtc).start() 

def loop_gnousdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_gnousdt != 0.0 and qty_bids_a_g_gnousdt != 0.0 and price_asks_a_g_gnousdt != 0.0 and qty_asks_a_g_gnousdt != 0.0 and price_bids_b_g_gnobtc != 0.0 and qty_bids_b_g_gnobtc != 0.0 and price_asks_b_g_gnobtc != 0.0 and qty_asks_b_g_gnobtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_gnousdt) 
			price_b = float(price_bids_b_g_gnobtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_gnobtc, pribil)

Thread(target=loop_gnousdt_Trade).start() 

symbol_a_g_woousdt = 'woousdt' 
price_bids_a_g_woousdt = float(0.0) 
qty_bids_a_g_woousdt = float(0.0) 
price_asks_a_g_woousdt = float(0.0) 
qty_asks_a_g_woousdt = float(0.0) 

def on_message_woousdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_woousdt = 'woousdt' 
		price_bids_a_l_woousdt = data['tick']['bid'] 
		qty_bids_a_l_woousdt = data['tick']['bidSize'] 
		price_asks_a_l_woousdt = data['tick']['ask'] 
		qty_asks_a_l_woousdt = data['tick']['askSize'] 

		global symbol_a_g_woousdt 
		global price_bids_a_g_woousdt 
		global qty_bids_a_g_woousdt 
		global price_asks_a_g_woousdt 
		global qty_asks_a_g_woousdt 

		symbol_a_g_woousdt = symbol_a_l_woousdt 
		price_bids_a_g_woousdt = price_bids_a_l_woousdt 
		qty_bids_a_g_woousdt = qty_bids_a_l_woousdt 
		price_asks_a_g_woousdt = price_asks_a_l_woousdt 
		qty_asks_a_g_woousdt = qty_asks_a_l_woousdt 

def on_close_woousdt(ws): 
	print('### closed ###') 

def on_error_woousdt(ws, message): 
	print(message) 

def on_open_woousdt(ws): 
	ws.send(json.dumps({'sub': f'market.woousdt.ticker'})) 

def loop_woousdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_woousdt, 
		on_close=on_close_woousdt, 
		on_error=on_error_woousdt) 
	ws.on_open = on_open_woousdt 
	ws.run_forever() 

Thread(target=loop_woousdt).start() 

symbol_b_g_woobtc = 'woobtc' 
price_bids_b_g_woobtc = float(0.0) 
qty_bids_b_g_woobtc = float(0.0) 
price_asks_b_g_woobtc = float(0.0) 
qty_asks_b_g_woobtc = float(0.0) 

def on_message_woobtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_woobtc = 'woobtc' 
		price_bids_b_l_woobtc = data['tick']['bid'] 
		qty_bids_b_l_woobtc = data['tick']['bidSize']
		price_asks_b_l_woobtc = data['tick']['ask'] 
		qty_asks_b_l_woobtc = data['tick']['askSize'] 

		global symbol_b_g_woobtc 
		global price_bids_b_g_woobtc 
		global qty_bids_b_g_woobtc 
		global price_asks_b_g_woobtc 
		global qty_asks_b_g_woobtc 

		symbol_b_g_woobtc = symbol_b_l_woobtc 
		price_bids_b_g_woobtc = price_bids_b_l_woobtc 
		qty_bids_b_g_woobtc = qty_bids_b_l_woobtc 
		price_asks_b_g_woobtc = price_asks_b_l_woobtc 
		qty_asks_b_g_woobtc = qty_asks_b_l_woobtc 


def on_close_woobtc(ws): 
	print('### closed ###') 

def on_error_woobtc(ws, message): 
	print(message) 

def on_open_woobtc(ws): 
	ws.send(json.dumps({'sub': f'market.woobtc.ticker'})) 

def loop_woobtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_woobtc, 
		on_close=on_close_woobtc, 
		on_error=on_error_woobtc) 
	ws.on_open = on_open_woobtc 
	ws.run_forever() 

Thread(target=loop_woobtc).start() 

def loop_woousdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_woousdt != 0.0 and qty_bids_a_g_woousdt != 0.0 and price_asks_a_g_woousdt != 0.0 and qty_asks_a_g_woousdt != 0.0 and price_bids_b_g_woobtc != 0.0 and qty_bids_b_g_woobtc != 0.0 and price_asks_b_g_woobtc != 0.0 and qty_asks_b_g_woobtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_woousdt) 
			price_b = float(price_bids_b_g_woobtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_woobtc, pribil)

Thread(target=loop_woousdt_Trade).start() 

symbol_a_g_mkrusdt = 'mkrusdt' 
price_bids_a_g_mkrusdt = float(0.0) 
qty_bids_a_g_mkrusdt = float(0.0) 
price_asks_a_g_mkrusdt = float(0.0) 
qty_asks_a_g_mkrusdt = float(0.0) 

def on_message_mkrusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_mkrusdt = 'mkrusdt' 
		price_bids_a_l_mkrusdt = data['tick']['bid'] 
		qty_bids_a_l_mkrusdt = data['tick']['bidSize'] 
		price_asks_a_l_mkrusdt = data['tick']['ask'] 
		qty_asks_a_l_mkrusdt = data['tick']['askSize'] 

		global symbol_a_g_mkrusdt 
		global price_bids_a_g_mkrusdt 
		global qty_bids_a_g_mkrusdt 
		global price_asks_a_g_mkrusdt 
		global qty_asks_a_g_mkrusdt 

		symbol_a_g_mkrusdt = symbol_a_l_mkrusdt 
		price_bids_a_g_mkrusdt = price_bids_a_l_mkrusdt 
		qty_bids_a_g_mkrusdt = qty_bids_a_l_mkrusdt 
		price_asks_a_g_mkrusdt = price_asks_a_l_mkrusdt 
		qty_asks_a_g_mkrusdt = qty_asks_a_l_mkrusdt 

def on_close_mkrusdt(ws): 
	print('### closed ###') 

def on_error_mkrusdt(ws, message): 
	print(message) 

def on_open_mkrusdt(ws): 
	ws.send(json.dumps({'sub': f'market.mkrusdt.ticker'})) 

def loop_mkrusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_mkrusdt, 
		on_close=on_close_mkrusdt, 
		on_error=on_error_mkrusdt) 
	ws.on_open = on_open_mkrusdt 
	ws.run_forever() 

Thread(target=loop_mkrusdt).start() 

symbol_b_g_mkrbtc = 'mkrbtc' 
price_bids_b_g_mkrbtc = float(0.0) 
qty_bids_b_g_mkrbtc = float(0.0) 
price_asks_b_g_mkrbtc = float(0.0) 
qty_asks_b_g_mkrbtc = float(0.0) 

def on_message_mkrbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_mkrbtc = 'mkrbtc' 
		price_bids_b_l_mkrbtc = data['tick']['bid'] 
		qty_bids_b_l_mkrbtc = data['tick']['bidSize']
		price_asks_b_l_mkrbtc = data['tick']['ask'] 
		qty_asks_b_l_mkrbtc = data['tick']['askSize'] 

		global symbol_b_g_mkrbtc 
		global price_bids_b_g_mkrbtc 
		global qty_bids_b_g_mkrbtc 
		global price_asks_b_g_mkrbtc 
		global qty_asks_b_g_mkrbtc 

		symbol_b_g_mkrbtc = symbol_b_l_mkrbtc 
		price_bids_b_g_mkrbtc = price_bids_b_l_mkrbtc 
		qty_bids_b_g_mkrbtc = qty_bids_b_l_mkrbtc 
		price_asks_b_g_mkrbtc = price_asks_b_l_mkrbtc 
		qty_asks_b_g_mkrbtc = qty_asks_b_l_mkrbtc 


def on_close_mkrbtc(ws): 
	print('### closed ###') 

def on_error_mkrbtc(ws, message): 
	print(message) 

def on_open_mkrbtc(ws): 
	ws.send(json.dumps({'sub': f'market.mkrbtc.ticker'})) 

def loop_mkrbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_mkrbtc, 
		on_close=on_close_mkrbtc, 
		on_error=on_error_mkrbtc) 
	ws.on_open = on_open_mkrbtc 
	ws.run_forever() 

Thread(target=loop_mkrbtc).start() 

def loop_mkrusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_mkrusdt != 0.0 and qty_bids_a_g_mkrusdt != 0.0 and price_asks_a_g_mkrusdt != 0.0 and qty_asks_a_g_mkrusdt != 0.0 and price_bids_b_g_mkrbtc != 0.0 and qty_bids_b_g_mkrbtc != 0.0 and price_asks_b_g_mkrbtc != 0.0 and qty_asks_b_g_mkrbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_mkrusdt) 
			price_b = float(price_bids_b_g_mkrbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_mkrbtc, pribil)

Thread(target=loop_mkrusdt_Trade).start() 

symbol_a_g_solusdt = 'solusdt' 
price_bids_a_g_solusdt = float(0.0) 
qty_bids_a_g_solusdt = float(0.0) 
price_asks_a_g_solusdt = float(0.0) 
qty_asks_a_g_solusdt = float(0.0) 

def on_message_solusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_solusdt = 'solusdt' 
		price_bids_a_l_solusdt = data['tick']['bid'] 
		qty_bids_a_l_solusdt = data['tick']['bidSize'] 
		price_asks_a_l_solusdt = data['tick']['ask'] 
		qty_asks_a_l_solusdt = data['tick']['askSize'] 

		global symbol_a_g_solusdt 
		global price_bids_a_g_solusdt 
		global qty_bids_a_g_solusdt 
		global price_asks_a_g_solusdt 
		global qty_asks_a_g_solusdt 

		symbol_a_g_solusdt = symbol_a_l_solusdt 
		price_bids_a_g_solusdt = price_bids_a_l_solusdt 
		qty_bids_a_g_solusdt = qty_bids_a_l_solusdt 
		price_asks_a_g_solusdt = price_asks_a_l_solusdt 
		qty_asks_a_g_solusdt = qty_asks_a_l_solusdt 

def on_close_solusdt(ws): 
	print('### closed ###') 

def on_error_solusdt(ws, message): 
	print(message) 

def on_open_solusdt(ws): 
	ws.send(json.dumps({'sub': f'market.solusdt.ticker'})) 

def loop_solusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_solusdt, 
		on_close=on_close_solusdt, 
		on_error=on_error_solusdt) 
	ws.on_open = on_open_solusdt 
	ws.run_forever() 

Thread(target=loop_solusdt).start() 

symbol_b_g_solusdd = 'solusdd' 
price_bids_b_g_solusdd = float(0.0) 
qty_bids_b_g_solusdd = float(0.0) 
price_asks_b_g_solusdd = float(0.0) 
qty_asks_b_g_solusdd = float(0.0) 

def on_message_solusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_solusdd = 'solusdd' 
		price_bids_b_l_solusdd = data['tick']['bid'] 
		qty_bids_b_l_solusdd = data['tick']['bidSize']
		price_asks_b_l_solusdd = data['tick']['ask'] 
		qty_asks_b_l_solusdd = data['tick']['askSize'] 

		global symbol_b_g_solusdd 
		global price_bids_b_g_solusdd 
		global qty_bids_b_g_solusdd 
		global price_asks_b_g_solusdd 
		global qty_asks_b_g_solusdd 

		symbol_b_g_solusdd = symbol_b_l_solusdd 
		price_bids_b_g_solusdd = price_bids_b_l_solusdd 
		qty_bids_b_g_solusdd = qty_bids_b_l_solusdd 
		price_asks_b_g_solusdd = price_asks_b_l_solusdd 
		qty_asks_b_g_solusdd = qty_asks_b_l_solusdd 


def on_close_solusdd(ws): 
	print('### closed ###') 

def on_error_solusdd(ws, message): 
	print(message) 

def on_open_solusdd(ws): 
	ws.send(json.dumps({'sub': f'market.solusdd.ticker'})) 

def loop_solusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_solusdd, 
		on_close=on_close_solusdd, 
		on_error=on_error_solusdd) 
	ws.on_open = on_open_solusdd 
	ws.run_forever() 

Thread(target=loop_solusdd).start() 

def loop_solusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_solusdt != 0.0 and qty_bids_a_g_solusdt != 0.0 and price_asks_a_g_solusdt != 0.0 and qty_asks_a_g_solusdt != 0.0 and price_bids_b_g_solusdd != 0.0 and qty_bids_b_g_solusdd != 0.0 and price_asks_b_g_solusdd != 0.0 and qty_asks_b_g_solusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_solusdt) 
			price_b = float(price_bids_b_g_solusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_solusdd, pribil)

Thread(target=loop_solusdt_Trade).start() 

symbol_a_g_srmusdt = 'srmusdt' 
price_bids_a_g_srmusdt = float(0.0) 
qty_bids_a_g_srmusdt = float(0.0) 
price_asks_a_g_srmusdt = float(0.0) 
qty_asks_a_g_srmusdt = float(0.0) 

def on_message_srmusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_srmusdt = 'srmusdt' 
		price_bids_a_l_srmusdt = data['tick']['bid'] 
		qty_bids_a_l_srmusdt = data['tick']['bidSize'] 
		price_asks_a_l_srmusdt = data['tick']['ask'] 
		qty_asks_a_l_srmusdt = data['tick']['askSize'] 

		global symbol_a_g_srmusdt 
		global price_bids_a_g_srmusdt 
		global qty_bids_a_g_srmusdt 
		global price_asks_a_g_srmusdt 
		global qty_asks_a_g_srmusdt 

		symbol_a_g_srmusdt = symbol_a_l_srmusdt 
		price_bids_a_g_srmusdt = price_bids_a_l_srmusdt 
		qty_bids_a_g_srmusdt = qty_bids_a_l_srmusdt 
		price_asks_a_g_srmusdt = price_asks_a_l_srmusdt 
		qty_asks_a_g_srmusdt = qty_asks_a_l_srmusdt 

def on_close_srmusdt(ws): 
	print('### closed ###') 

def on_error_srmusdt(ws, message): 
	print(message) 

def on_open_srmusdt(ws): 
	ws.send(json.dumps({'sub': f'market.srmusdt.ticker'})) 

def loop_srmusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_srmusdt, 
		on_close=on_close_srmusdt, 
		on_error=on_error_srmusdt) 
	ws.on_open = on_open_srmusdt 
	ws.run_forever() 

Thread(target=loop_srmusdt).start() 

symbol_b_g_srmbtc = 'srmbtc' 
price_bids_b_g_srmbtc = float(0.0) 
qty_bids_b_g_srmbtc = float(0.0) 
price_asks_b_g_srmbtc = float(0.0) 
qty_asks_b_g_srmbtc = float(0.0) 

def on_message_srmbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_srmbtc = 'srmbtc' 
		price_bids_b_l_srmbtc = data['tick']['bid'] 
		qty_bids_b_l_srmbtc = data['tick']['bidSize']
		price_asks_b_l_srmbtc = data['tick']['ask'] 
		qty_asks_b_l_srmbtc = data['tick']['askSize'] 

		global symbol_b_g_srmbtc 
		global price_bids_b_g_srmbtc 
		global qty_bids_b_g_srmbtc 
		global price_asks_b_g_srmbtc 
		global qty_asks_b_g_srmbtc 

		symbol_b_g_srmbtc = symbol_b_l_srmbtc 
		price_bids_b_g_srmbtc = price_bids_b_l_srmbtc 
		qty_bids_b_g_srmbtc = qty_bids_b_l_srmbtc 
		price_asks_b_g_srmbtc = price_asks_b_l_srmbtc 
		qty_asks_b_g_srmbtc = qty_asks_b_l_srmbtc 


def on_close_srmbtc(ws): 
	print('### closed ###') 

def on_error_srmbtc(ws, message): 
	print(message) 

def on_open_srmbtc(ws): 
	ws.send(json.dumps({'sub': f'market.srmbtc.ticker'})) 

def loop_srmbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_srmbtc, 
		on_close=on_close_srmbtc, 
		on_error=on_error_srmbtc) 
	ws.on_open = on_open_srmbtc 
	ws.run_forever() 

Thread(target=loop_srmbtc).start() 

def loop_srmusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_srmusdt != 0.0 and qty_bids_a_g_srmusdt != 0.0 and price_asks_a_g_srmusdt != 0.0 and qty_asks_a_g_srmusdt != 0.0 and price_bids_b_g_srmbtc != 0.0 and qty_bids_b_g_srmbtc != 0.0 and price_asks_b_g_srmbtc != 0.0 and qty_asks_b_g_srmbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_srmusdt) 
			price_b = float(price_bids_b_g_srmbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_srmbtc, pribil)

Thread(target=loop_srmusdt_Trade).start() 

symbol_a_g_zksusdt = 'zksusdt' 
price_bids_a_g_zksusdt = float(0.0) 
qty_bids_a_g_zksusdt = float(0.0) 
price_asks_a_g_zksusdt = float(0.0) 
qty_asks_a_g_zksusdt = float(0.0) 

def on_message_zksusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_zksusdt = 'zksusdt' 
		price_bids_a_l_zksusdt = data['tick']['bid'] 
		qty_bids_a_l_zksusdt = data['tick']['bidSize'] 
		price_asks_a_l_zksusdt = data['tick']['ask'] 
		qty_asks_a_l_zksusdt = data['tick']['askSize'] 

		global symbol_a_g_zksusdt 
		global price_bids_a_g_zksusdt 
		global qty_bids_a_g_zksusdt 
		global price_asks_a_g_zksusdt 
		global qty_asks_a_g_zksusdt 

		symbol_a_g_zksusdt = symbol_a_l_zksusdt 
		price_bids_a_g_zksusdt = price_bids_a_l_zksusdt 
		qty_bids_a_g_zksusdt = qty_bids_a_l_zksusdt 
		price_asks_a_g_zksusdt = price_asks_a_l_zksusdt 
		qty_asks_a_g_zksusdt = qty_asks_a_l_zksusdt 

def on_close_zksusdt(ws): 
	print('### closed ###') 

def on_error_zksusdt(ws, message): 
	print(message) 

def on_open_zksusdt(ws): 
	ws.send(json.dumps({'sub': f'market.zksusdt.ticker'})) 

def loop_zksusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_zksusdt, 
		on_close=on_close_zksusdt, 
		on_error=on_error_zksusdt) 
	ws.on_open = on_open_zksusdt 
	ws.run_forever() 

Thread(target=loop_zksusdt).start() 

symbol_b_g_zkseth = 'zkseth' 
price_bids_b_g_zkseth = float(0.0) 
qty_bids_b_g_zkseth = float(0.0) 
price_asks_b_g_zkseth = float(0.0) 
qty_asks_b_g_zkseth = float(0.0) 

def on_message_zkseth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_zkseth = 'zkseth' 
		price_bids_b_l_zkseth = data['tick']['bid'] 
		qty_bids_b_l_zkseth = data['tick']['bidSize']
		price_asks_b_l_zkseth = data['tick']['ask'] 
		qty_asks_b_l_zkseth = data['tick']['askSize'] 

		global symbol_b_g_zkseth 
		global price_bids_b_g_zkseth 
		global qty_bids_b_g_zkseth 
		global price_asks_b_g_zkseth 
		global qty_asks_b_g_zkseth 

		symbol_b_g_zkseth = symbol_b_l_zkseth 
		price_bids_b_g_zkseth = price_bids_b_l_zkseth 
		qty_bids_b_g_zkseth = qty_bids_b_l_zkseth 
		price_asks_b_g_zkseth = price_asks_b_l_zkseth 
		qty_asks_b_g_zkseth = qty_asks_b_l_zkseth 


def on_close_zkseth(ws): 
	print('### closed ###') 

def on_error_zkseth(ws, message): 
	print(message) 

def on_open_zkseth(ws): 
	ws.send(json.dumps({'sub': f'market.zkseth.ticker'})) 

def loop_zkseth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_zkseth, 
		on_close=on_close_zkseth, 
		on_error=on_error_zkseth) 
	ws.on_open = on_open_zkseth 
	ws.run_forever() 

Thread(target=loop_zkseth).start() 

def loop_zksusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_zksusdt != 0.0 and qty_bids_a_g_zksusdt != 0.0 and price_asks_a_g_zksusdt != 0.0 and qty_asks_a_g_zksusdt != 0.0 and price_bids_b_g_zkseth != 0.0 and qty_bids_b_g_zkseth != 0.0 and price_asks_b_g_zkseth != 0.0 and qty_asks_b_g_zkseth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_zksusdt) 
			price_b = float(price_bids_b_g_zkseth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_zkseth, pribil)

Thread(target=loop_zksusdt_Trade).start() 

symbol_a_g_lrcusdt = 'lrcusdt' 
price_bids_a_g_lrcusdt = float(0.0) 
qty_bids_a_g_lrcusdt = float(0.0) 
price_asks_a_g_lrcusdt = float(0.0) 
qty_asks_a_g_lrcusdt = float(0.0) 

def on_message_lrcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_lrcusdt = 'lrcusdt' 
		price_bids_a_l_lrcusdt = data['tick']['bid'] 
		qty_bids_a_l_lrcusdt = data['tick']['bidSize'] 
		price_asks_a_l_lrcusdt = data['tick']['ask'] 
		qty_asks_a_l_lrcusdt = data['tick']['askSize'] 

		global symbol_a_g_lrcusdt 
		global price_bids_a_g_lrcusdt 
		global qty_bids_a_g_lrcusdt 
		global price_asks_a_g_lrcusdt 
		global qty_asks_a_g_lrcusdt 

		symbol_a_g_lrcusdt = symbol_a_l_lrcusdt 
		price_bids_a_g_lrcusdt = price_bids_a_l_lrcusdt 
		qty_bids_a_g_lrcusdt = qty_bids_a_l_lrcusdt 
		price_asks_a_g_lrcusdt = price_asks_a_l_lrcusdt 
		qty_asks_a_g_lrcusdt = qty_asks_a_l_lrcusdt 

def on_close_lrcusdt(ws): 
	print('### closed ###') 

def on_error_lrcusdt(ws, message): 
	print(message) 

def on_open_lrcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.lrcusdt.ticker'})) 

def loop_lrcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_lrcusdt, 
		on_close=on_close_lrcusdt, 
		on_error=on_error_lrcusdt) 
	ws.on_open = on_open_lrcusdt 
	ws.run_forever() 

Thread(target=loop_lrcusdt).start() 

symbol_b_g_lrcusdc = 'lrcusdc' 
price_bids_b_g_lrcusdc = float(0.0) 
qty_bids_b_g_lrcusdc = float(0.0) 
price_asks_b_g_lrcusdc = float(0.0) 
qty_asks_b_g_lrcusdc = float(0.0) 

def on_message_lrcusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_lrcusdc = 'lrcusdc' 
		price_bids_b_l_lrcusdc = data['tick']['bid'] 
		qty_bids_b_l_lrcusdc = data['tick']['bidSize']
		price_asks_b_l_lrcusdc = data['tick']['ask'] 
		qty_asks_b_l_lrcusdc = data['tick']['askSize'] 

		global symbol_b_g_lrcusdc 
		global price_bids_b_g_lrcusdc 
		global qty_bids_b_g_lrcusdc 
		global price_asks_b_g_lrcusdc 
		global qty_asks_b_g_lrcusdc 

		symbol_b_g_lrcusdc = symbol_b_l_lrcusdc 
		price_bids_b_g_lrcusdc = price_bids_b_l_lrcusdc 
		qty_bids_b_g_lrcusdc = qty_bids_b_l_lrcusdc 
		price_asks_b_g_lrcusdc = price_asks_b_l_lrcusdc 
		qty_asks_b_g_lrcusdc = qty_asks_b_l_lrcusdc 


def on_close_lrcusdc(ws): 
	print('### closed ###') 

def on_error_lrcusdc(ws, message): 
	print(message) 

def on_open_lrcusdc(ws): 
	ws.send(json.dumps({'sub': f'market.lrcusdc.ticker'})) 

def loop_lrcusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_lrcusdc, 
		on_close=on_close_lrcusdc, 
		on_error=on_error_lrcusdc) 
	ws.on_open = on_open_lrcusdc 
	ws.run_forever() 

Thread(target=loop_lrcusdc).start() 

def loop_lrcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_lrcusdt != 0.0 and qty_bids_a_g_lrcusdt != 0.0 and price_asks_a_g_lrcusdt != 0.0 and qty_asks_a_g_lrcusdt != 0.0 and price_bids_b_g_lrcusdc != 0.0 and qty_bids_b_g_lrcusdc != 0.0 and price_asks_b_g_lrcusdc != 0.0 and qty_asks_b_g_lrcusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_lrcusdt) 
			price_b = float(price_bids_b_g_lrcusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_lrcusdc, pribil)

Thread(target=loop_lrcusdt_Trade).start() 

symbol_a_g_sntusdt = 'sntusdt' 
price_bids_a_g_sntusdt = float(0.0) 
qty_bids_a_g_sntusdt = float(0.0) 
price_asks_a_g_sntusdt = float(0.0) 
qty_asks_a_g_sntusdt = float(0.0) 

def on_message_sntusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_sntusdt = 'sntusdt' 
		price_bids_a_l_sntusdt = data['tick']['bid'] 
		qty_bids_a_l_sntusdt = data['tick']['bidSize'] 
		price_asks_a_l_sntusdt = data['tick']['ask'] 
		qty_asks_a_l_sntusdt = data['tick']['askSize'] 

		global symbol_a_g_sntusdt 
		global price_bids_a_g_sntusdt 
		global qty_bids_a_g_sntusdt 
		global price_asks_a_g_sntusdt 
		global qty_asks_a_g_sntusdt 

		symbol_a_g_sntusdt = symbol_a_l_sntusdt 
		price_bids_a_g_sntusdt = price_bids_a_l_sntusdt 
		qty_bids_a_g_sntusdt = qty_bids_a_l_sntusdt 
		price_asks_a_g_sntusdt = price_asks_a_l_sntusdt 
		qty_asks_a_g_sntusdt = qty_asks_a_l_sntusdt 

def on_close_sntusdt(ws): 
	print('### closed ###') 

def on_error_sntusdt(ws, message): 
	print(message) 

def on_open_sntusdt(ws): 
	ws.send(json.dumps({'sub': f'market.sntusdt.ticker'})) 

def loop_sntusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sntusdt, 
		on_close=on_close_sntusdt, 
		on_error=on_error_sntusdt) 
	ws.on_open = on_open_sntusdt 
	ws.run_forever() 

Thread(target=loop_sntusdt).start() 

symbol_b_g_sntbtc = 'sntbtc' 
price_bids_b_g_sntbtc = float(0.0) 
qty_bids_b_g_sntbtc = float(0.0) 
price_asks_b_g_sntbtc = float(0.0) 
qty_asks_b_g_sntbtc = float(0.0) 

def on_message_sntbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_sntbtc = 'sntbtc' 
		price_bids_b_l_sntbtc = data['tick']['bid'] 
		qty_bids_b_l_sntbtc = data['tick']['bidSize']
		price_asks_b_l_sntbtc = data['tick']['ask'] 
		qty_asks_b_l_sntbtc = data['tick']['askSize'] 

		global symbol_b_g_sntbtc 
		global price_bids_b_g_sntbtc 
		global qty_bids_b_g_sntbtc 
		global price_asks_b_g_sntbtc 
		global qty_asks_b_g_sntbtc 

		symbol_b_g_sntbtc = symbol_b_l_sntbtc 
		price_bids_b_g_sntbtc = price_bids_b_l_sntbtc 
		qty_bids_b_g_sntbtc = qty_bids_b_l_sntbtc 
		price_asks_b_g_sntbtc = price_asks_b_l_sntbtc 
		qty_asks_b_g_sntbtc = qty_asks_b_l_sntbtc 


def on_close_sntbtc(ws): 
	print('### closed ###') 

def on_error_sntbtc(ws, message): 
	print(message) 

def on_open_sntbtc(ws): 
	ws.send(json.dumps({'sub': f'market.sntbtc.ticker'})) 

def loop_sntbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sntbtc, 
		on_close=on_close_sntbtc, 
		on_error=on_error_sntbtc) 
	ws.on_open = on_open_sntbtc 
	ws.run_forever() 

Thread(target=loop_sntbtc).start() 

def loop_sntusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_sntusdt != 0.0 and qty_bids_a_g_sntusdt != 0.0 and price_asks_a_g_sntusdt != 0.0 and qty_asks_a_g_sntusdt != 0.0 and price_bids_b_g_sntbtc != 0.0 and qty_bids_b_g_sntbtc != 0.0 and price_asks_b_g_sntbtc != 0.0 and qty_asks_b_g_sntbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_sntusdt) 
			price_b = float(price_bids_b_g_sntbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_sntbtc, pribil)

Thread(target=loop_sntusdt_Trade).start() 

symbol_a_g_shibusdt = 'shibusdt' 
price_bids_a_g_shibusdt = float(0.0) 
qty_bids_a_g_shibusdt = float(0.0) 
price_asks_a_g_shibusdt = float(0.0) 
qty_asks_a_g_shibusdt = float(0.0) 

def on_message_shibusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_shibusdt = 'shibusdt' 
		price_bids_a_l_shibusdt = data['tick']['bid'] 
		qty_bids_a_l_shibusdt = data['tick']['bidSize'] 
		price_asks_a_l_shibusdt = data['tick']['ask'] 
		qty_asks_a_l_shibusdt = data['tick']['askSize'] 

		global symbol_a_g_shibusdt 
		global price_bids_a_g_shibusdt 
		global qty_bids_a_g_shibusdt 
		global price_asks_a_g_shibusdt 
		global qty_asks_a_g_shibusdt 

		symbol_a_g_shibusdt = symbol_a_l_shibusdt 
		price_bids_a_g_shibusdt = price_bids_a_l_shibusdt 
		qty_bids_a_g_shibusdt = qty_bids_a_l_shibusdt 
		price_asks_a_g_shibusdt = price_asks_a_l_shibusdt 
		qty_asks_a_g_shibusdt = qty_asks_a_l_shibusdt 

def on_close_shibusdt(ws): 
	print('### closed ###') 

def on_error_shibusdt(ws, message): 
	print(message) 

def on_open_shibusdt(ws): 
	ws.send(json.dumps({'sub': f'market.shibusdt.ticker'})) 

def loop_shibusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_shibusdt, 
		on_close=on_close_shibusdt, 
		on_error=on_error_shibusdt) 
	ws.on_open = on_open_shibusdt 
	ws.run_forever() 

Thread(target=loop_shibusdt).start() 

symbol_b_g_shibusdc = 'shibusdc' 
price_bids_b_g_shibusdc = float(0.0) 
qty_bids_b_g_shibusdc = float(0.0) 
price_asks_b_g_shibusdc = float(0.0) 
qty_asks_b_g_shibusdc = float(0.0) 

def on_message_shibusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_shibusdc = 'shibusdc' 
		price_bids_b_l_shibusdc = data['tick']['bid'] 
		qty_bids_b_l_shibusdc = data['tick']['bidSize']
		price_asks_b_l_shibusdc = data['tick']['ask'] 
		qty_asks_b_l_shibusdc = data['tick']['askSize'] 

		global symbol_b_g_shibusdc 
		global price_bids_b_g_shibusdc 
		global qty_bids_b_g_shibusdc 
		global price_asks_b_g_shibusdc 
		global qty_asks_b_g_shibusdc 

		symbol_b_g_shibusdc = symbol_b_l_shibusdc 
		price_bids_b_g_shibusdc = price_bids_b_l_shibusdc 
		qty_bids_b_g_shibusdc = qty_bids_b_l_shibusdc 
		price_asks_b_g_shibusdc = price_asks_b_l_shibusdc 
		qty_asks_b_g_shibusdc = qty_asks_b_l_shibusdc 


def on_close_shibusdc(ws): 
	print('### closed ###') 

def on_error_shibusdc(ws, message): 
	print(message) 

def on_open_shibusdc(ws): 
	ws.send(json.dumps({'sub': f'market.shibusdc.ticker'})) 

def loop_shibusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_shibusdc, 
		on_close=on_close_shibusdc, 
		on_error=on_error_shibusdc) 
	ws.on_open = on_open_shibusdc 
	ws.run_forever() 

Thread(target=loop_shibusdc).start() 

def loop_shibusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_shibusdt != 0.0 and qty_bids_a_g_shibusdt != 0.0 and price_asks_a_g_shibusdt != 0.0 and qty_asks_a_g_shibusdt != 0.0 and price_bids_b_g_shibusdc != 0.0 and qty_bids_b_g_shibusdc != 0.0 and price_asks_b_g_shibusdc != 0.0 and qty_asks_b_g_shibusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_shibusdt) 
			price_b = float(price_bids_b_g_shibusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_shibusdc, pribil)

Thread(target=loop_shibusdt_Trade).start() 

symbol_a_g_ontusdt = 'ontusdt' 
price_bids_a_g_ontusdt = float(0.0) 
qty_bids_a_g_ontusdt = float(0.0) 
price_asks_a_g_ontusdt = float(0.0) 
qty_asks_a_g_ontusdt = float(0.0) 

def on_message_ontusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ontusdt = 'ontusdt' 
		price_bids_a_l_ontusdt = data['tick']['bid'] 
		qty_bids_a_l_ontusdt = data['tick']['bidSize'] 
		price_asks_a_l_ontusdt = data['tick']['ask'] 
		qty_asks_a_l_ontusdt = data['tick']['askSize'] 

		global symbol_a_g_ontusdt 
		global price_bids_a_g_ontusdt 
		global qty_bids_a_g_ontusdt 
		global price_asks_a_g_ontusdt 
		global qty_asks_a_g_ontusdt 

		symbol_a_g_ontusdt = symbol_a_l_ontusdt 
		price_bids_a_g_ontusdt = price_bids_a_l_ontusdt 
		qty_bids_a_g_ontusdt = qty_bids_a_l_ontusdt 
		price_asks_a_g_ontusdt = price_asks_a_l_ontusdt 
		qty_asks_a_g_ontusdt = qty_asks_a_l_ontusdt 

def on_close_ontusdt(ws): 
	print('### closed ###') 

def on_error_ontusdt(ws, message): 
	print(message) 

def on_open_ontusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ontusdt.ticker'})) 

def loop_ontusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ontusdt, 
		on_close=on_close_ontusdt, 
		on_error=on_error_ontusdt) 
	ws.on_open = on_open_ontusdt 
	ws.run_forever() 

Thread(target=loop_ontusdt).start() 

symbol_b_g_ontbtc = 'ontbtc' 
price_bids_b_g_ontbtc = float(0.0) 
qty_bids_b_g_ontbtc = float(0.0) 
price_asks_b_g_ontbtc = float(0.0) 
qty_asks_b_g_ontbtc = float(0.0) 

def on_message_ontbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ontbtc = 'ontbtc' 
		price_bids_b_l_ontbtc = data['tick']['bid'] 
		qty_bids_b_l_ontbtc = data['tick']['bidSize']
		price_asks_b_l_ontbtc = data['tick']['ask'] 
		qty_asks_b_l_ontbtc = data['tick']['askSize'] 

		global symbol_b_g_ontbtc 
		global price_bids_b_g_ontbtc 
		global qty_bids_b_g_ontbtc 
		global price_asks_b_g_ontbtc 
		global qty_asks_b_g_ontbtc 

		symbol_b_g_ontbtc = symbol_b_l_ontbtc 
		price_bids_b_g_ontbtc = price_bids_b_l_ontbtc 
		qty_bids_b_g_ontbtc = qty_bids_b_l_ontbtc 
		price_asks_b_g_ontbtc = price_asks_b_l_ontbtc 
		qty_asks_b_g_ontbtc = qty_asks_b_l_ontbtc 


def on_close_ontbtc(ws): 
	print('### closed ###') 

def on_error_ontbtc(ws, message): 
	print(message) 

def on_open_ontbtc(ws): 
	ws.send(json.dumps({'sub': f'market.ontbtc.ticker'})) 

def loop_ontbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ontbtc, 
		on_close=on_close_ontbtc, 
		on_error=on_error_ontbtc) 
	ws.on_open = on_open_ontbtc 
	ws.run_forever() 

Thread(target=loop_ontbtc).start() 

def loop_ontusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_ontusdt != 0.0 and qty_bids_a_g_ontusdt != 0.0 and price_asks_a_g_ontusdt != 0.0 and qty_asks_a_g_ontusdt != 0.0 and price_bids_b_g_ontbtc != 0.0 and qty_bids_b_g_ontbtc != 0.0 and price_asks_b_g_ontbtc != 0.0 and qty_asks_b_g_ontbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ontusdt) 
			price_b = float(price_bids_b_g_ontbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ontbtc, pribil)

Thread(target=loop_ontusdt_Trade).start() 

symbol_a_g_adausdt = 'adausdt' 
price_bids_a_g_adausdt = float(0.0) 
qty_bids_a_g_adausdt = float(0.0) 
price_asks_a_g_adausdt = float(0.0) 
qty_asks_a_g_adausdt = float(0.0) 

def on_message_adausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_adausdt = 'adausdt' 
		price_bids_a_l_adausdt = data['tick']['bid'] 
		qty_bids_a_l_adausdt = data['tick']['bidSize'] 
		price_asks_a_l_adausdt = data['tick']['ask'] 
		qty_asks_a_l_adausdt = data['tick']['askSize'] 

		global symbol_a_g_adausdt 
		global price_bids_a_g_adausdt 
		global qty_bids_a_g_adausdt 
		global price_asks_a_g_adausdt 
		global qty_asks_a_g_adausdt 

		symbol_a_g_adausdt = symbol_a_l_adausdt 
		price_bids_a_g_adausdt = price_bids_a_l_adausdt 
		qty_bids_a_g_adausdt = qty_bids_a_l_adausdt 
		price_asks_a_g_adausdt = price_asks_a_l_adausdt 
		qty_asks_a_g_adausdt = qty_asks_a_l_adausdt 

def on_close_adausdt(ws): 
	print('### closed ###') 

def on_error_adausdt(ws, message): 
	print(message) 

def on_open_adausdt(ws): 
	ws.send(json.dumps({'sub': f'market.adausdt.ticker'})) 

def loop_adausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_adausdt, 
		on_close=on_close_adausdt, 
		on_error=on_error_adausdt) 
	ws.on_open = on_open_adausdt 
	ws.run_forever() 

Thread(target=loop_adausdt).start() 

symbol_b_g_adausdd = 'adausdd' 
price_bids_b_g_adausdd = float(0.0) 
qty_bids_b_g_adausdd = float(0.0) 
price_asks_b_g_adausdd = float(0.0) 
qty_asks_b_g_adausdd = float(0.0) 

def on_message_adausdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_adausdd = 'adausdd' 
		price_bids_b_l_adausdd = data['tick']['bid'] 
		qty_bids_b_l_adausdd = data['tick']['bidSize']
		price_asks_b_l_adausdd = data['tick']['ask'] 
		qty_asks_b_l_adausdd = data['tick']['askSize'] 

		global symbol_b_g_adausdd 
		global price_bids_b_g_adausdd 
		global qty_bids_b_g_adausdd 
		global price_asks_b_g_adausdd 
		global qty_asks_b_g_adausdd 

		symbol_b_g_adausdd = symbol_b_l_adausdd 
		price_bids_b_g_adausdd = price_bids_b_l_adausdd 
		qty_bids_b_g_adausdd = qty_bids_b_l_adausdd 
		price_asks_b_g_adausdd = price_asks_b_l_adausdd 
		qty_asks_b_g_adausdd = qty_asks_b_l_adausdd 


def on_close_adausdd(ws): 
	print('### closed ###') 

def on_error_adausdd(ws, message): 
	print(message) 

def on_open_adausdd(ws): 
	ws.send(json.dumps({'sub': f'market.adausdd.ticker'})) 

def loop_adausdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_adausdd, 
		on_close=on_close_adausdd, 
		on_error=on_error_adausdd) 
	ws.on_open = on_open_adausdd 
	ws.run_forever() 

Thread(target=loop_adausdd).start() 

def loop_adausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_adausdt != 0.0 and qty_bids_a_g_adausdt != 0.0 and price_asks_a_g_adausdt != 0.0 and qty_asks_a_g_adausdt != 0.0 and price_bids_b_g_adausdd != 0.0 and qty_bids_b_g_adausdd != 0.0 and price_asks_b_g_adausdd != 0.0 and qty_asks_b_g_adausdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_adausdt) 
			price_b = float(price_bids_b_g_adausdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_adausdd, pribil)

Thread(target=loop_adausdt_Trade).start() 

symbol_a_g_waxpusdt = 'waxpusdt' 
price_bids_a_g_waxpusdt = float(0.0) 
qty_bids_a_g_waxpusdt = float(0.0) 
price_asks_a_g_waxpusdt = float(0.0) 
qty_asks_a_g_waxpusdt = float(0.0) 

def on_message_waxpusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_waxpusdt = 'waxpusdt' 
		price_bids_a_l_waxpusdt = data['tick']['bid'] 
		qty_bids_a_l_waxpusdt = data['tick']['bidSize'] 
		price_asks_a_l_waxpusdt = data['tick']['ask'] 
		qty_asks_a_l_waxpusdt = data['tick']['askSize'] 

		global symbol_a_g_waxpusdt 
		global price_bids_a_g_waxpusdt 
		global qty_bids_a_g_waxpusdt 
		global price_asks_a_g_waxpusdt 
		global qty_asks_a_g_waxpusdt 

		symbol_a_g_waxpusdt = symbol_a_l_waxpusdt 
		price_bids_a_g_waxpusdt = price_bids_a_l_waxpusdt 
		qty_bids_a_g_waxpusdt = qty_bids_a_l_waxpusdt 
		price_asks_a_g_waxpusdt = price_asks_a_l_waxpusdt 
		qty_asks_a_g_waxpusdt = qty_asks_a_l_waxpusdt 

def on_close_waxpusdt(ws): 
	print('### closed ###') 

def on_error_waxpusdt(ws, message): 
	print(message) 

def on_open_waxpusdt(ws): 
	ws.send(json.dumps({'sub': f'market.waxpusdt.ticker'})) 

def loop_waxpusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_waxpusdt, 
		on_close=on_close_waxpusdt, 
		on_error=on_error_waxpusdt) 
	ws.on_open = on_open_waxpusdt 
	ws.run_forever() 

Thread(target=loop_waxpusdt).start() 

symbol_b_g_waxpbtc = 'waxpbtc' 
price_bids_b_g_waxpbtc = float(0.0) 
qty_bids_b_g_waxpbtc = float(0.0) 
price_asks_b_g_waxpbtc = float(0.0) 
qty_asks_b_g_waxpbtc = float(0.0) 

def on_message_waxpbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_waxpbtc = 'waxpbtc' 
		price_bids_b_l_waxpbtc = data['tick']['bid'] 
		qty_bids_b_l_waxpbtc = data['tick']['bidSize']
		price_asks_b_l_waxpbtc = data['tick']['ask'] 
		qty_asks_b_l_waxpbtc = data['tick']['askSize'] 

		global symbol_b_g_waxpbtc 
		global price_bids_b_g_waxpbtc 
		global qty_bids_b_g_waxpbtc 
		global price_asks_b_g_waxpbtc 
		global qty_asks_b_g_waxpbtc 

		symbol_b_g_waxpbtc = symbol_b_l_waxpbtc 
		price_bids_b_g_waxpbtc = price_bids_b_l_waxpbtc 
		qty_bids_b_g_waxpbtc = qty_bids_b_l_waxpbtc 
		price_asks_b_g_waxpbtc = price_asks_b_l_waxpbtc 
		qty_asks_b_g_waxpbtc = qty_asks_b_l_waxpbtc 


def on_close_waxpbtc(ws): 
	print('### closed ###') 

def on_error_waxpbtc(ws, message): 
	print(message) 

def on_open_waxpbtc(ws): 
	ws.send(json.dumps({'sub': f'market.waxpbtc.ticker'})) 

def loop_waxpbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_waxpbtc, 
		on_close=on_close_waxpbtc, 
		on_error=on_error_waxpbtc) 
	ws.on_open = on_open_waxpbtc 
	ws.run_forever() 

Thread(target=loop_waxpbtc).start() 

def loop_waxpusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_waxpusdt != 0.0 and qty_bids_a_g_waxpusdt != 0.0 and price_asks_a_g_waxpusdt != 0.0 and qty_asks_a_g_waxpusdt != 0.0 and price_bids_b_g_waxpbtc != 0.0 and qty_bids_b_g_waxpbtc != 0.0 and price_asks_b_g_waxpbtc != 0.0 and qty_asks_b_g_waxpbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_waxpusdt) 
			price_b = float(price_bids_b_g_waxpbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_waxpbtc, pribil)

Thread(target=loop_waxpusdt_Trade).start() 

symbol_a_g_eulusdt = 'eulusdt' 
price_bids_a_g_eulusdt = float(0.0) 
qty_bids_a_g_eulusdt = float(0.0) 
price_asks_a_g_eulusdt = float(0.0) 
qty_asks_a_g_eulusdt = float(0.0) 

def on_message_eulusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_eulusdt = 'eulusdt' 
		price_bids_a_l_eulusdt = data['tick']['bid'] 
		qty_bids_a_l_eulusdt = data['tick']['bidSize'] 
		price_asks_a_l_eulusdt = data['tick']['ask'] 
		qty_asks_a_l_eulusdt = data['tick']['askSize'] 

		global symbol_a_g_eulusdt 
		global price_bids_a_g_eulusdt 
		global qty_bids_a_g_eulusdt 
		global price_asks_a_g_eulusdt 
		global qty_asks_a_g_eulusdt 

		symbol_a_g_eulusdt = symbol_a_l_eulusdt 
		price_bids_a_g_eulusdt = price_bids_a_l_eulusdt 
		qty_bids_a_g_eulusdt = qty_bids_a_l_eulusdt 
		price_asks_a_g_eulusdt = price_asks_a_l_eulusdt 
		qty_asks_a_g_eulusdt = qty_asks_a_l_eulusdt 

def on_close_eulusdt(ws): 
	print('### closed ###') 

def on_error_eulusdt(ws, message): 
	print(message) 

def on_open_eulusdt(ws): 
	ws.send(json.dumps({'sub': f'market.eulusdt.ticker'})) 

def loop_eulusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_eulusdt, 
		on_close=on_close_eulusdt, 
		on_error=on_error_eulusdt) 
	ws.on_open = on_open_eulusdt 
	ws.run_forever() 

Thread(target=loop_eulusdt).start() 

symbol_b_g_eulusdc = 'eulusdc' 
price_bids_b_g_eulusdc = float(0.0) 
qty_bids_b_g_eulusdc = float(0.0) 
price_asks_b_g_eulusdc = float(0.0) 
qty_asks_b_g_eulusdc = float(0.0) 

def on_message_eulusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_eulusdc = 'eulusdc' 
		price_bids_b_l_eulusdc = data['tick']['bid'] 
		qty_bids_b_l_eulusdc = data['tick']['bidSize']
		price_asks_b_l_eulusdc = data['tick']['ask'] 
		qty_asks_b_l_eulusdc = data['tick']['askSize'] 

		global symbol_b_g_eulusdc 
		global price_bids_b_g_eulusdc 
		global qty_bids_b_g_eulusdc 
		global price_asks_b_g_eulusdc 
		global qty_asks_b_g_eulusdc 

		symbol_b_g_eulusdc = symbol_b_l_eulusdc 
		price_bids_b_g_eulusdc = price_bids_b_l_eulusdc 
		qty_bids_b_g_eulusdc = qty_bids_b_l_eulusdc 
		price_asks_b_g_eulusdc = price_asks_b_l_eulusdc 
		qty_asks_b_g_eulusdc = qty_asks_b_l_eulusdc 


def on_close_eulusdc(ws): 
	print('### closed ###') 

def on_error_eulusdc(ws, message): 
	print(message) 

def on_open_eulusdc(ws): 
	ws.send(json.dumps({'sub': f'market.eulusdc.ticker'})) 

def loop_eulusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_eulusdc, 
		on_close=on_close_eulusdc, 
		on_error=on_error_eulusdc) 
	ws.on_open = on_open_eulusdc 
	ws.run_forever() 

Thread(target=loop_eulusdc).start() 

def loop_eulusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_eulusdt != 0.0 and qty_bids_a_g_eulusdt != 0.0 and price_asks_a_g_eulusdt != 0.0 and qty_asks_a_g_eulusdt != 0.0 and price_bids_b_g_eulusdc != 0.0 and qty_bids_b_g_eulusdc != 0.0 and price_asks_b_g_eulusdc != 0.0 and qty_asks_b_g_eulusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_eulusdt) 
			price_b = float(price_bids_b_g_eulusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_eulusdc, pribil)

Thread(target=loop_eulusdt_Trade).start() 

symbol_a_g_nulsusdt = 'nulsusdt' 
price_bids_a_g_nulsusdt = float(0.0) 
qty_bids_a_g_nulsusdt = float(0.0) 
price_asks_a_g_nulsusdt = float(0.0) 
qty_asks_a_g_nulsusdt = float(0.0) 

def on_message_nulsusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_nulsusdt = 'nulsusdt' 
		price_bids_a_l_nulsusdt = data['tick']['bid'] 
		qty_bids_a_l_nulsusdt = data['tick']['bidSize'] 
		price_asks_a_l_nulsusdt = data['tick']['ask'] 
		qty_asks_a_l_nulsusdt = data['tick']['askSize'] 

		global symbol_a_g_nulsusdt 
		global price_bids_a_g_nulsusdt 
		global qty_bids_a_g_nulsusdt 
		global price_asks_a_g_nulsusdt 
		global qty_asks_a_g_nulsusdt 

		symbol_a_g_nulsusdt = symbol_a_l_nulsusdt 
		price_bids_a_g_nulsusdt = price_bids_a_l_nulsusdt 
		qty_bids_a_g_nulsusdt = qty_bids_a_l_nulsusdt 
		price_asks_a_g_nulsusdt = price_asks_a_l_nulsusdt 
		qty_asks_a_g_nulsusdt = qty_asks_a_l_nulsusdt 

def on_close_nulsusdt(ws): 
	print('### closed ###') 

def on_error_nulsusdt(ws, message): 
	print(message) 

def on_open_nulsusdt(ws): 
	ws.send(json.dumps({'sub': f'market.nulsusdt.ticker'})) 

def loop_nulsusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nulsusdt, 
		on_close=on_close_nulsusdt, 
		on_error=on_error_nulsusdt) 
	ws.on_open = on_open_nulsusdt 
	ws.run_forever() 

Thread(target=loop_nulsusdt).start() 

symbol_b_g_nulsbtc = 'nulsbtc' 
price_bids_b_g_nulsbtc = float(0.0) 
qty_bids_b_g_nulsbtc = float(0.0) 
price_asks_b_g_nulsbtc = float(0.0) 
qty_asks_b_g_nulsbtc = float(0.0) 

def on_message_nulsbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_nulsbtc = 'nulsbtc' 
		price_bids_b_l_nulsbtc = data['tick']['bid'] 
		qty_bids_b_l_nulsbtc = data['tick']['bidSize']
		price_asks_b_l_nulsbtc = data['tick']['ask'] 
		qty_asks_b_l_nulsbtc = data['tick']['askSize'] 

		global symbol_b_g_nulsbtc 
		global price_bids_b_g_nulsbtc 
		global qty_bids_b_g_nulsbtc 
		global price_asks_b_g_nulsbtc 
		global qty_asks_b_g_nulsbtc 

		symbol_b_g_nulsbtc = symbol_b_l_nulsbtc 
		price_bids_b_g_nulsbtc = price_bids_b_l_nulsbtc 
		qty_bids_b_g_nulsbtc = qty_bids_b_l_nulsbtc 
		price_asks_b_g_nulsbtc = price_asks_b_l_nulsbtc 
		qty_asks_b_g_nulsbtc = qty_asks_b_l_nulsbtc 


def on_close_nulsbtc(ws): 
	print('### closed ###') 

def on_error_nulsbtc(ws, message): 
	print(message) 

def on_open_nulsbtc(ws): 
	ws.send(json.dumps({'sub': f'market.nulsbtc.ticker'})) 

def loop_nulsbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nulsbtc, 
		on_close=on_close_nulsbtc, 
		on_error=on_error_nulsbtc) 
	ws.on_open = on_open_nulsbtc 
	ws.run_forever() 

Thread(target=loop_nulsbtc).start() 

def loop_nulsusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_nulsusdt != 0.0 and qty_bids_a_g_nulsusdt != 0.0 and price_asks_a_g_nulsusdt != 0.0 and qty_asks_a_g_nulsusdt != 0.0 and price_bids_b_g_nulsbtc != 0.0 and qty_bids_b_g_nulsbtc != 0.0 and price_asks_b_g_nulsbtc != 0.0 and qty_asks_b_g_nulsbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_nulsusdt) 
			price_b = float(price_bids_b_g_nulsbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_nulsbtc, pribil)

Thread(target=loop_nulsusdt_Trade).start() 

symbol_a_g_renusdt = 'renusdt' 
price_bids_a_g_renusdt = float(0.0) 
qty_bids_a_g_renusdt = float(0.0) 
price_asks_a_g_renusdt = float(0.0) 
qty_asks_a_g_renusdt = float(0.0) 

def on_message_renusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_renusdt = 'renusdt' 
		price_bids_a_l_renusdt = data['tick']['bid'] 
		qty_bids_a_l_renusdt = data['tick']['bidSize'] 
		price_asks_a_l_renusdt = data['tick']['ask'] 
		qty_asks_a_l_renusdt = data['tick']['askSize'] 

		global symbol_a_g_renusdt 
		global price_bids_a_g_renusdt 
		global qty_bids_a_g_renusdt 
		global price_asks_a_g_renusdt 
		global qty_asks_a_g_renusdt 

		symbol_a_g_renusdt = symbol_a_l_renusdt 
		price_bids_a_g_renusdt = price_bids_a_l_renusdt 
		qty_bids_a_g_renusdt = qty_bids_a_l_renusdt 
		price_asks_a_g_renusdt = price_asks_a_l_renusdt 
		qty_asks_a_g_renusdt = qty_asks_a_l_renusdt 

def on_close_renusdt(ws): 
	print('### closed ###') 

def on_error_renusdt(ws, message): 
	print(message) 

def on_open_renusdt(ws): 
	ws.send(json.dumps({'sub': f'market.renusdt.ticker'})) 

def loop_renusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_renusdt, 
		on_close=on_close_renusdt, 
		on_error=on_error_renusdt) 
	ws.on_open = on_open_renusdt 
	ws.run_forever() 

Thread(target=loop_renusdt).start() 

symbol_b_g_reneth = 'reneth' 
price_bids_b_g_reneth = float(0.0) 
qty_bids_b_g_reneth = float(0.0) 
price_asks_b_g_reneth = float(0.0) 
qty_asks_b_g_reneth = float(0.0) 

def on_message_reneth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_reneth = 'reneth' 
		price_bids_b_l_reneth = data['tick']['bid'] 
		qty_bids_b_l_reneth = data['tick']['bidSize']
		price_asks_b_l_reneth = data['tick']['ask'] 
		qty_asks_b_l_reneth = data['tick']['askSize'] 

		global symbol_b_g_reneth 
		global price_bids_b_g_reneth 
		global qty_bids_b_g_reneth 
		global price_asks_b_g_reneth 
		global qty_asks_b_g_reneth 

		symbol_b_g_reneth = symbol_b_l_reneth 
		price_bids_b_g_reneth = price_bids_b_l_reneth 
		qty_bids_b_g_reneth = qty_bids_b_l_reneth 
		price_asks_b_g_reneth = price_asks_b_l_reneth 
		qty_asks_b_g_reneth = qty_asks_b_l_reneth 


def on_close_reneth(ws): 
	print('### closed ###') 

def on_error_reneth(ws, message): 
	print(message) 

def on_open_reneth(ws): 
	ws.send(json.dumps({'sub': f'market.reneth.ticker'})) 

def loop_reneth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_reneth, 
		on_close=on_close_reneth, 
		on_error=on_error_reneth) 
	ws.on_open = on_open_reneth 
	ws.run_forever() 

Thread(target=loop_reneth).start() 

def loop_renusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_renusdt != 0.0 and qty_bids_a_g_renusdt != 0.0 and price_asks_a_g_renusdt != 0.0 and qty_asks_a_g_renusdt != 0.0 and price_bids_b_g_reneth != 0.0 and qty_bids_b_g_reneth != 0.0 and price_asks_b_g_reneth != 0.0 and qty_asks_b_g_reneth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_renusdt) 
			price_b = float(price_bids_b_g_reneth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_reneth, pribil)

Thread(target=loop_renusdt_Trade).start() 

symbol_a_g_gofusdt = 'gofusdt' 
price_bids_a_g_gofusdt = float(0.0) 
qty_bids_a_g_gofusdt = float(0.0) 
price_asks_a_g_gofusdt = float(0.0) 
qty_asks_a_g_gofusdt = float(0.0) 

def on_message_gofusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_gofusdt = 'gofusdt' 
		price_bids_a_l_gofusdt = data['tick']['bid'] 
		qty_bids_a_l_gofusdt = data['tick']['bidSize'] 
		price_asks_a_l_gofusdt = data['tick']['ask'] 
		qty_asks_a_l_gofusdt = data['tick']['askSize'] 

		global symbol_a_g_gofusdt 
		global price_bids_a_g_gofusdt 
		global qty_bids_a_g_gofusdt 
		global price_asks_a_g_gofusdt 
		global qty_asks_a_g_gofusdt 

		symbol_a_g_gofusdt = symbol_a_l_gofusdt 
		price_bids_a_g_gofusdt = price_bids_a_l_gofusdt 
		qty_bids_a_g_gofusdt = qty_bids_a_l_gofusdt 
		price_asks_a_g_gofusdt = price_asks_a_l_gofusdt 
		qty_asks_a_g_gofusdt = qty_asks_a_l_gofusdt 

def on_close_gofusdt(ws): 
	print('### closed ###') 

def on_error_gofusdt(ws, message): 
	print(message) 

def on_open_gofusdt(ws): 
	ws.send(json.dumps({'sub': f'market.gofusdt.ticker'})) 

def loop_gofusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_gofusdt, 
		on_close=on_close_gofusdt, 
		on_error=on_error_gofusdt) 
	ws.on_open = on_open_gofusdt 
	ws.run_forever() 

Thread(target=loop_gofusdt).start() 

symbol_b_g_gofeth = 'gofeth' 
price_bids_b_g_gofeth = float(0.0) 
qty_bids_b_g_gofeth = float(0.0) 
price_asks_b_g_gofeth = float(0.0) 
qty_asks_b_g_gofeth = float(0.0) 

def on_message_gofeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_gofeth = 'gofeth' 
		price_bids_b_l_gofeth = data['tick']['bid'] 
		qty_bids_b_l_gofeth = data['tick']['bidSize']
		price_asks_b_l_gofeth = data['tick']['ask'] 
		qty_asks_b_l_gofeth = data['tick']['askSize'] 

		global symbol_b_g_gofeth 
		global price_bids_b_g_gofeth 
		global qty_bids_b_g_gofeth 
		global price_asks_b_g_gofeth 
		global qty_asks_b_g_gofeth 

		symbol_b_g_gofeth = symbol_b_l_gofeth 
		price_bids_b_g_gofeth = price_bids_b_l_gofeth 
		qty_bids_b_g_gofeth = qty_bids_b_l_gofeth 
		price_asks_b_g_gofeth = price_asks_b_l_gofeth 
		qty_asks_b_g_gofeth = qty_asks_b_l_gofeth 


def on_close_gofeth(ws): 
	print('### closed ###') 

def on_error_gofeth(ws, message): 
	print(message) 

def on_open_gofeth(ws): 
	ws.send(json.dumps({'sub': f'market.gofeth.ticker'})) 

def loop_gofeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_gofeth, 
		on_close=on_close_gofeth, 
		on_error=on_error_gofeth) 
	ws.on_open = on_open_gofeth 
	ws.run_forever() 

Thread(target=loop_gofeth).start() 

def loop_gofusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_gofusdt != 0.0 and qty_bids_a_g_gofusdt != 0.0 and price_asks_a_g_gofusdt != 0.0 and qty_asks_a_g_gofusdt != 0.0 and price_bids_b_g_gofeth != 0.0 and qty_bids_b_g_gofeth != 0.0 and price_asks_b_g_gofeth != 0.0 and qty_asks_b_g_gofeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_gofusdt) 
			price_b = float(price_bids_b_g_gofeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_gofeth, pribil)

Thread(target=loop_gofusdt_Trade).start() 

symbol_a_g_ksmusdt = 'ksmusdt' 
price_bids_a_g_ksmusdt = float(0.0) 
qty_bids_a_g_ksmusdt = float(0.0) 
price_asks_a_g_ksmusdt = float(0.0) 
qty_asks_a_g_ksmusdt = float(0.0) 

def on_message_ksmusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ksmusdt = 'ksmusdt' 
		price_bids_a_l_ksmusdt = data['tick']['bid'] 
		qty_bids_a_l_ksmusdt = data['tick']['bidSize'] 
		price_asks_a_l_ksmusdt = data['tick']['ask'] 
		qty_asks_a_l_ksmusdt = data['tick']['askSize'] 

		global symbol_a_g_ksmusdt 
		global price_bids_a_g_ksmusdt 
		global qty_bids_a_g_ksmusdt 
		global price_asks_a_g_ksmusdt 
		global qty_asks_a_g_ksmusdt 

		symbol_a_g_ksmusdt = symbol_a_l_ksmusdt 
		price_bids_a_g_ksmusdt = price_bids_a_l_ksmusdt 
		qty_bids_a_g_ksmusdt = qty_bids_a_l_ksmusdt 
		price_asks_a_g_ksmusdt = price_asks_a_l_ksmusdt 
		qty_asks_a_g_ksmusdt = qty_asks_a_l_ksmusdt 

def on_close_ksmusdt(ws): 
	print('### closed ###') 

def on_error_ksmusdt(ws, message): 
	print(message) 

def on_open_ksmusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ksmusdt.ticker'})) 

def loop_ksmusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ksmusdt, 
		on_close=on_close_ksmusdt, 
		on_error=on_error_ksmusdt) 
	ws.on_open = on_open_ksmusdt 
	ws.run_forever() 

Thread(target=loop_ksmusdt).start() 

symbol_b_g_ksmbtc = 'ksmbtc' 
price_bids_b_g_ksmbtc = float(0.0) 
qty_bids_b_g_ksmbtc = float(0.0) 
price_asks_b_g_ksmbtc = float(0.0) 
qty_asks_b_g_ksmbtc = float(0.0) 

def on_message_ksmbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ksmbtc = 'ksmbtc' 
		price_bids_b_l_ksmbtc = data['tick']['bid'] 
		qty_bids_b_l_ksmbtc = data['tick']['bidSize']
		price_asks_b_l_ksmbtc = data['tick']['ask'] 
		qty_asks_b_l_ksmbtc = data['tick']['askSize'] 

		global symbol_b_g_ksmbtc 
		global price_bids_b_g_ksmbtc 
		global qty_bids_b_g_ksmbtc 
		global price_asks_b_g_ksmbtc 
		global qty_asks_b_g_ksmbtc 

		symbol_b_g_ksmbtc = symbol_b_l_ksmbtc 
		price_bids_b_g_ksmbtc = price_bids_b_l_ksmbtc 
		qty_bids_b_g_ksmbtc = qty_bids_b_l_ksmbtc 
		price_asks_b_g_ksmbtc = price_asks_b_l_ksmbtc 
		qty_asks_b_g_ksmbtc = qty_asks_b_l_ksmbtc 


def on_close_ksmbtc(ws): 
	print('### closed ###') 

def on_error_ksmbtc(ws, message): 
	print(message) 

def on_open_ksmbtc(ws): 
	ws.send(json.dumps({'sub': f'market.ksmbtc.ticker'})) 

def loop_ksmbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ksmbtc, 
		on_close=on_close_ksmbtc, 
		on_error=on_error_ksmbtc) 
	ws.on_open = on_open_ksmbtc 
	ws.run_forever() 

Thread(target=loop_ksmbtc).start() 

def loop_ksmusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_ksmusdt != 0.0 and qty_bids_a_g_ksmusdt != 0.0 and price_asks_a_g_ksmusdt != 0.0 and qty_asks_a_g_ksmusdt != 0.0 and price_bids_b_g_ksmbtc != 0.0 and qty_bids_b_g_ksmbtc != 0.0 and price_asks_b_g_ksmbtc != 0.0 and qty_asks_b_g_ksmbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ksmusdt) 
			price_b = float(price_bids_b_g_ksmbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ksmbtc, pribil)

Thread(target=loop_ksmusdt_Trade).start() 

symbol_a_g_boxusdt = 'boxusdt' 
price_bids_a_g_boxusdt = float(0.0) 
qty_bids_a_g_boxusdt = float(0.0) 
price_asks_a_g_boxusdt = float(0.0) 
qty_asks_a_g_boxusdt = float(0.0) 

def on_message_boxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_boxusdt = 'boxusdt' 
		price_bids_a_l_boxusdt = data['tick']['bid'] 
		qty_bids_a_l_boxusdt = data['tick']['bidSize'] 
		price_asks_a_l_boxusdt = data['tick']['ask'] 
		qty_asks_a_l_boxusdt = data['tick']['askSize'] 

		global symbol_a_g_boxusdt 
		global price_bids_a_g_boxusdt 
		global qty_bids_a_g_boxusdt 
		global price_asks_a_g_boxusdt 
		global qty_asks_a_g_boxusdt 

		symbol_a_g_boxusdt = symbol_a_l_boxusdt 
		price_bids_a_g_boxusdt = price_bids_a_l_boxusdt 
		qty_bids_a_g_boxusdt = qty_bids_a_l_boxusdt 
		price_asks_a_g_boxusdt = price_asks_a_l_boxusdt 
		qty_asks_a_g_boxusdt = qty_asks_a_l_boxusdt 

def on_close_boxusdt(ws): 
	print('### closed ###') 

def on_error_boxusdt(ws, message): 
	print(message) 

def on_open_boxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.boxusdt.ticker'})) 

def loop_boxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_boxusdt, 
		on_close=on_close_boxusdt, 
		on_error=on_error_boxusdt) 
	ws.on_open = on_open_boxusdt 
	ws.run_forever() 

Thread(target=loop_boxusdt).start() 

symbol_b_g_boxbtc = 'boxbtc' 
price_bids_b_g_boxbtc = float(0.0) 
qty_bids_b_g_boxbtc = float(0.0) 
price_asks_b_g_boxbtc = float(0.0) 
qty_asks_b_g_boxbtc = float(0.0) 

def on_message_boxbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_boxbtc = 'boxbtc' 
		price_bids_b_l_boxbtc = data['tick']['bid'] 
		qty_bids_b_l_boxbtc = data['tick']['bidSize']
		price_asks_b_l_boxbtc = data['tick']['ask'] 
		qty_asks_b_l_boxbtc = data['tick']['askSize'] 

		global symbol_b_g_boxbtc 
		global price_bids_b_g_boxbtc 
		global qty_bids_b_g_boxbtc 
		global price_asks_b_g_boxbtc 
		global qty_asks_b_g_boxbtc 

		symbol_b_g_boxbtc = symbol_b_l_boxbtc 
		price_bids_b_g_boxbtc = price_bids_b_l_boxbtc 
		qty_bids_b_g_boxbtc = qty_bids_b_l_boxbtc 
		price_asks_b_g_boxbtc = price_asks_b_l_boxbtc 
		qty_asks_b_g_boxbtc = qty_asks_b_l_boxbtc 


def on_close_boxbtc(ws): 
	print('### closed ###') 

def on_error_boxbtc(ws, message): 
	print(message) 

def on_open_boxbtc(ws): 
	ws.send(json.dumps({'sub': f'market.boxbtc.ticker'})) 

def loop_boxbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_boxbtc, 
		on_close=on_close_boxbtc, 
		on_error=on_error_boxbtc) 
	ws.on_open = on_open_boxbtc 
	ws.run_forever() 

Thread(target=loop_boxbtc).start() 

def loop_boxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_boxusdt != 0.0 and qty_bids_a_g_boxusdt != 0.0 and price_asks_a_g_boxusdt != 0.0 and qty_asks_a_g_boxusdt != 0.0 and price_bids_b_g_boxbtc != 0.0 and qty_bids_b_g_boxbtc != 0.0 and price_asks_b_g_boxbtc != 0.0 and qty_asks_b_g_boxbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_boxusdt) 
			price_b = float(price_bids_b_g_boxbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_boxbtc, pribil)

Thread(target=loop_boxusdt_Trade).start() 

symbol_a_g_vetusdt = 'vetusdt' 
price_bids_a_g_vetusdt = float(0.0) 
qty_bids_a_g_vetusdt = float(0.0) 
price_asks_a_g_vetusdt = float(0.0) 
qty_asks_a_g_vetusdt = float(0.0) 

def on_message_vetusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_vetusdt = 'vetusdt' 
		price_bids_a_l_vetusdt = data['tick']['bid'] 
		qty_bids_a_l_vetusdt = data['tick']['bidSize'] 
		price_asks_a_l_vetusdt = data['tick']['ask'] 
		qty_asks_a_l_vetusdt = data['tick']['askSize'] 

		global symbol_a_g_vetusdt 
		global price_bids_a_g_vetusdt 
		global qty_bids_a_g_vetusdt 
		global price_asks_a_g_vetusdt 
		global qty_asks_a_g_vetusdt 

		symbol_a_g_vetusdt = symbol_a_l_vetusdt 
		price_bids_a_g_vetusdt = price_bids_a_l_vetusdt 
		qty_bids_a_g_vetusdt = qty_bids_a_l_vetusdt 
		price_asks_a_g_vetusdt = price_asks_a_l_vetusdt 
		qty_asks_a_g_vetusdt = qty_asks_a_l_vetusdt 

def on_close_vetusdt(ws): 
	print('### closed ###') 

def on_error_vetusdt(ws, message): 
	print(message) 

def on_open_vetusdt(ws): 
	ws.send(json.dumps({'sub': f'market.vetusdt.ticker'})) 

def loop_vetusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_vetusdt, 
		on_close=on_close_vetusdt, 
		on_error=on_error_vetusdt) 
	ws.on_open = on_open_vetusdt 
	ws.run_forever() 

Thread(target=loop_vetusdt).start() 

symbol_b_g_veteth = 'veteth' 
price_bids_b_g_veteth = float(0.0) 
qty_bids_b_g_veteth = float(0.0) 
price_asks_b_g_veteth = float(0.0) 
qty_asks_b_g_veteth = float(0.0) 

def on_message_veteth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_veteth = 'veteth' 
		price_bids_b_l_veteth = data['tick']['bid'] 
		qty_bids_b_l_veteth = data['tick']['bidSize']
		price_asks_b_l_veteth = data['tick']['ask'] 
		qty_asks_b_l_veteth = data['tick']['askSize'] 

		global symbol_b_g_veteth 
		global price_bids_b_g_veteth 
		global qty_bids_b_g_veteth 
		global price_asks_b_g_veteth 
		global qty_asks_b_g_veteth 

		symbol_b_g_veteth = symbol_b_l_veteth 
		price_bids_b_g_veteth = price_bids_b_l_veteth 
		qty_bids_b_g_veteth = qty_bids_b_l_veteth 
		price_asks_b_g_veteth = price_asks_b_l_veteth 
		qty_asks_b_g_veteth = qty_asks_b_l_veteth 


def on_close_veteth(ws): 
	print('### closed ###') 

def on_error_veteth(ws, message): 
	print(message) 

def on_open_veteth(ws): 
	ws.send(json.dumps({'sub': f'market.veteth.ticker'})) 

def loop_veteth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_veteth, 
		on_close=on_close_veteth, 
		on_error=on_error_veteth) 
	ws.on_open = on_open_veteth 
	ws.run_forever() 

Thread(target=loop_veteth).start() 

def loop_vetusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_vetusdt != 0.0 and qty_bids_a_g_vetusdt != 0.0 and price_asks_a_g_vetusdt != 0.0 and qty_asks_a_g_vetusdt != 0.0 and price_bids_b_g_veteth != 0.0 and qty_bids_b_g_veteth != 0.0 and price_asks_b_g_veteth != 0.0 and qty_asks_b_g_veteth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_vetusdt) 
			price_b = float(price_bids_b_g_veteth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_veteth, pribil)

Thread(target=loop_vetusdt_Trade).start() 

symbol_a_g_arpausdt = 'arpausdt' 
price_bids_a_g_arpausdt = float(0.0) 
qty_bids_a_g_arpausdt = float(0.0) 
price_asks_a_g_arpausdt = float(0.0) 
qty_asks_a_g_arpausdt = float(0.0) 

def on_message_arpausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_arpausdt = 'arpausdt' 
		price_bids_a_l_arpausdt = data['tick']['bid'] 
		qty_bids_a_l_arpausdt = data['tick']['bidSize'] 
		price_asks_a_l_arpausdt = data['tick']['ask'] 
		qty_asks_a_l_arpausdt = data['tick']['askSize'] 

		global symbol_a_g_arpausdt 
		global price_bids_a_g_arpausdt 
		global qty_bids_a_g_arpausdt 
		global price_asks_a_g_arpausdt 
		global qty_asks_a_g_arpausdt 

		symbol_a_g_arpausdt = symbol_a_l_arpausdt 
		price_bids_a_g_arpausdt = price_bids_a_l_arpausdt 
		qty_bids_a_g_arpausdt = qty_bids_a_l_arpausdt 
		price_asks_a_g_arpausdt = price_asks_a_l_arpausdt 
		qty_asks_a_g_arpausdt = qty_asks_a_l_arpausdt 

def on_close_arpausdt(ws): 
	print('### closed ###') 

def on_error_arpausdt(ws, message): 
	print(message) 

def on_open_arpausdt(ws): 
	ws.send(json.dumps({'sub': f'market.arpausdt.ticker'})) 

def loop_arpausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_arpausdt, 
		on_close=on_close_arpausdt, 
		on_error=on_error_arpausdt) 
	ws.on_open = on_open_arpausdt 
	ws.run_forever() 

Thread(target=loop_arpausdt).start() 

symbol_b_g_arpabtc = 'arpabtc' 
price_bids_b_g_arpabtc = float(0.0) 
qty_bids_b_g_arpabtc = float(0.0) 
price_asks_b_g_arpabtc = float(0.0) 
qty_asks_b_g_arpabtc = float(0.0) 

def on_message_arpabtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_arpabtc = 'arpabtc' 
		price_bids_b_l_arpabtc = data['tick']['bid'] 
		qty_bids_b_l_arpabtc = data['tick']['bidSize']
		price_asks_b_l_arpabtc = data['tick']['ask'] 
		qty_asks_b_l_arpabtc = data['tick']['askSize'] 

		global symbol_b_g_arpabtc 
		global price_bids_b_g_arpabtc 
		global qty_bids_b_g_arpabtc 
		global price_asks_b_g_arpabtc 
		global qty_asks_b_g_arpabtc 

		symbol_b_g_arpabtc = symbol_b_l_arpabtc 
		price_bids_b_g_arpabtc = price_bids_b_l_arpabtc 
		qty_bids_b_g_arpabtc = qty_bids_b_l_arpabtc 
		price_asks_b_g_arpabtc = price_asks_b_l_arpabtc 
		qty_asks_b_g_arpabtc = qty_asks_b_l_arpabtc 


def on_close_arpabtc(ws): 
	print('### closed ###') 

def on_error_arpabtc(ws, message): 
	print(message) 

def on_open_arpabtc(ws): 
	ws.send(json.dumps({'sub': f'market.arpabtc.ticker'})) 

def loop_arpabtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_arpabtc, 
		on_close=on_close_arpabtc, 
		on_error=on_error_arpabtc) 
	ws.on_open = on_open_arpabtc 
	ws.run_forever() 

Thread(target=loop_arpabtc).start() 

def loop_arpausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_arpausdt != 0.0 and qty_bids_a_g_arpausdt != 0.0 and price_asks_a_g_arpausdt != 0.0 and qty_asks_a_g_arpausdt != 0.0 and price_bids_b_g_arpabtc != 0.0 and qty_bids_b_g_arpabtc != 0.0 and price_asks_b_g_arpabtc != 0.0 and qty_asks_b_g_arpabtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_arpausdt) 
			price_b = float(price_bids_b_g_arpabtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_arpabtc, pribil)

Thread(target=loop_arpausdt_Trade).start() 

symbol_a_g_iotxusdt = 'iotxusdt' 
price_bids_a_g_iotxusdt = float(0.0) 
qty_bids_a_g_iotxusdt = float(0.0) 
price_asks_a_g_iotxusdt = float(0.0) 
qty_asks_a_g_iotxusdt = float(0.0) 

def on_message_iotxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_iotxusdt = 'iotxusdt' 
		price_bids_a_l_iotxusdt = data['tick']['bid'] 
		qty_bids_a_l_iotxusdt = data['tick']['bidSize'] 
		price_asks_a_l_iotxusdt = data['tick']['ask'] 
		qty_asks_a_l_iotxusdt = data['tick']['askSize'] 

		global symbol_a_g_iotxusdt 
		global price_bids_a_g_iotxusdt 
		global qty_bids_a_g_iotxusdt 
		global price_asks_a_g_iotxusdt 
		global qty_asks_a_g_iotxusdt 

		symbol_a_g_iotxusdt = symbol_a_l_iotxusdt 
		price_bids_a_g_iotxusdt = price_bids_a_l_iotxusdt 
		qty_bids_a_g_iotxusdt = qty_bids_a_l_iotxusdt 
		price_asks_a_g_iotxusdt = price_asks_a_l_iotxusdt 
		qty_asks_a_g_iotxusdt = qty_asks_a_l_iotxusdt 

def on_close_iotxusdt(ws): 
	print('### closed ###') 

def on_error_iotxusdt(ws, message): 
	print(message) 

def on_open_iotxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.iotxusdt.ticker'})) 

def loop_iotxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_iotxusdt, 
		on_close=on_close_iotxusdt, 
		on_error=on_error_iotxusdt) 
	ws.on_open = on_open_iotxusdt 
	ws.run_forever() 

Thread(target=loop_iotxusdt).start() 

symbol_b_g_iotxbtc = 'iotxbtc' 
price_bids_b_g_iotxbtc = float(0.0) 
qty_bids_b_g_iotxbtc = float(0.0) 
price_asks_b_g_iotxbtc = float(0.0) 
qty_asks_b_g_iotxbtc = float(0.0) 

def on_message_iotxbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_iotxbtc = 'iotxbtc' 
		price_bids_b_l_iotxbtc = data['tick']['bid'] 
		qty_bids_b_l_iotxbtc = data['tick']['bidSize']
		price_asks_b_l_iotxbtc = data['tick']['ask'] 
		qty_asks_b_l_iotxbtc = data['tick']['askSize'] 

		global symbol_b_g_iotxbtc 
		global price_bids_b_g_iotxbtc 
		global qty_bids_b_g_iotxbtc 
		global price_asks_b_g_iotxbtc 
		global qty_asks_b_g_iotxbtc 

		symbol_b_g_iotxbtc = symbol_b_l_iotxbtc 
		price_bids_b_g_iotxbtc = price_bids_b_l_iotxbtc 
		qty_bids_b_g_iotxbtc = qty_bids_b_l_iotxbtc 
		price_asks_b_g_iotxbtc = price_asks_b_l_iotxbtc 
		qty_asks_b_g_iotxbtc = qty_asks_b_l_iotxbtc 


def on_close_iotxbtc(ws): 
	print('### closed ###') 

def on_error_iotxbtc(ws, message): 
	print(message) 

def on_open_iotxbtc(ws): 
	ws.send(json.dumps({'sub': f'market.iotxbtc.ticker'})) 

def loop_iotxbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_iotxbtc, 
		on_close=on_close_iotxbtc, 
		on_error=on_error_iotxbtc) 
	ws.on_open = on_open_iotxbtc 
	ws.run_forever() 

Thread(target=loop_iotxbtc).start() 

def loop_iotxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_iotxusdt != 0.0 and qty_bids_a_g_iotxusdt != 0.0 and price_asks_a_g_iotxusdt != 0.0 and qty_asks_a_g_iotxusdt != 0.0 and price_bids_b_g_iotxbtc != 0.0 and qty_bids_b_g_iotxbtc != 0.0 and price_asks_b_g_iotxbtc != 0.0 and qty_asks_b_g_iotxbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_iotxusdt) 
			price_b = float(price_bids_b_g_iotxbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_iotxbtc, pribil)

Thread(target=loop_iotxusdt_Trade).start() 

symbol_a_g_ruffusdt = 'ruffusdt' 
price_bids_a_g_ruffusdt = float(0.0) 
qty_bids_a_g_ruffusdt = float(0.0) 
price_asks_a_g_ruffusdt = float(0.0) 
qty_asks_a_g_ruffusdt = float(0.0) 

def on_message_ruffusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ruffusdt = 'ruffusdt' 
		price_bids_a_l_ruffusdt = data['tick']['bid'] 
		qty_bids_a_l_ruffusdt = data['tick']['bidSize'] 
		price_asks_a_l_ruffusdt = data['tick']['ask'] 
		qty_asks_a_l_ruffusdt = data['tick']['askSize'] 

		global symbol_a_g_ruffusdt 
		global price_bids_a_g_ruffusdt 
		global qty_bids_a_g_ruffusdt 
		global price_asks_a_g_ruffusdt 
		global qty_asks_a_g_ruffusdt 

		symbol_a_g_ruffusdt = symbol_a_l_ruffusdt 
		price_bids_a_g_ruffusdt = price_bids_a_l_ruffusdt 
		qty_bids_a_g_ruffusdt = qty_bids_a_l_ruffusdt 
		price_asks_a_g_ruffusdt = price_asks_a_l_ruffusdt 
		qty_asks_a_g_ruffusdt = qty_asks_a_l_ruffusdt 

def on_close_ruffusdt(ws): 
	print('### closed ###') 

def on_error_ruffusdt(ws, message): 
	print(message) 

def on_open_ruffusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ruffusdt.ticker'})) 

def loop_ruffusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ruffusdt, 
		on_close=on_close_ruffusdt, 
		on_error=on_error_ruffusdt) 
	ws.on_open = on_open_ruffusdt 
	ws.run_forever() 

Thread(target=loop_ruffusdt).start() 

symbol_b_g_ruffeth = 'ruffeth' 
price_bids_b_g_ruffeth = float(0.0) 
qty_bids_b_g_ruffeth = float(0.0) 
price_asks_b_g_ruffeth = float(0.0) 
qty_asks_b_g_ruffeth = float(0.0) 

def on_message_ruffeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ruffeth = 'ruffeth' 
		price_bids_b_l_ruffeth = data['tick']['bid'] 
		qty_bids_b_l_ruffeth = data['tick']['bidSize']
		price_asks_b_l_ruffeth = data['tick']['ask'] 
		qty_asks_b_l_ruffeth = data['tick']['askSize'] 

		global symbol_b_g_ruffeth 
		global price_bids_b_g_ruffeth 
		global qty_bids_b_g_ruffeth 
		global price_asks_b_g_ruffeth 
		global qty_asks_b_g_ruffeth 

		symbol_b_g_ruffeth = symbol_b_l_ruffeth 
		price_bids_b_g_ruffeth = price_bids_b_l_ruffeth 
		qty_bids_b_g_ruffeth = qty_bids_b_l_ruffeth 
		price_asks_b_g_ruffeth = price_asks_b_l_ruffeth 
		qty_asks_b_g_ruffeth = qty_asks_b_l_ruffeth 


def on_close_ruffeth(ws): 
	print('### closed ###') 

def on_error_ruffeth(ws, message): 
	print(message) 

def on_open_ruffeth(ws): 
	ws.send(json.dumps({'sub': f'market.ruffeth.ticker'})) 

def loop_ruffeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ruffeth, 
		on_close=on_close_ruffeth, 
		on_error=on_error_ruffeth) 
	ws.on_open = on_open_ruffeth 
	ws.run_forever() 

Thread(target=loop_ruffeth).start() 

def loop_ruffusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_ruffusdt != 0.0 and qty_bids_a_g_ruffusdt != 0.0 and price_asks_a_g_ruffusdt != 0.0 and qty_asks_a_g_ruffusdt != 0.0 and price_bids_b_g_ruffeth != 0.0 and qty_bids_b_g_ruffeth != 0.0 and price_asks_b_g_ruffeth != 0.0 and qty_asks_b_g_ruffeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ruffusdt) 
			price_b = float(price_bids_b_g_ruffeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ruffeth, pribil)

Thread(target=loop_ruffusdt_Trade).start() 

symbol_a_g_algousdt = 'algousdt' 
price_bids_a_g_algousdt = float(0.0) 
qty_bids_a_g_algousdt = float(0.0) 
price_asks_a_g_algousdt = float(0.0) 
qty_asks_a_g_algousdt = float(0.0) 

def on_message_algousdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_algousdt = 'algousdt' 
		price_bids_a_l_algousdt = data['tick']['bid'] 
		qty_bids_a_l_algousdt = data['tick']['bidSize'] 
		price_asks_a_l_algousdt = data['tick']['ask'] 
		qty_asks_a_l_algousdt = data['tick']['askSize'] 

		global symbol_a_g_algousdt 
		global price_bids_a_g_algousdt 
		global qty_bids_a_g_algousdt 
		global price_asks_a_g_algousdt 
		global qty_asks_a_g_algousdt 

		symbol_a_g_algousdt = symbol_a_l_algousdt 
		price_bids_a_g_algousdt = price_bids_a_l_algousdt 
		qty_bids_a_g_algousdt = qty_bids_a_l_algousdt 
		price_asks_a_g_algousdt = price_asks_a_l_algousdt 
		qty_asks_a_g_algousdt = qty_asks_a_l_algousdt 

def on_close_algousdt(ws): 
	print('### closed ###') 

def on_error_algousdt(ws, message): 
	print(message) 

def on_open_algousdt(ws): 
	ws.send(json.dumps({'sub': f'market.algousdt.ticker'})) 

def loop_algousdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_algousdt, 
		on_close=on_close_algousdt, 
		on_error=on_error_algousdt) 
	ws.on_open = on_open_algousdt 
	ws.run_forever() 

Thread(target=loop_algousdt).start() 

symbol_b_g_algoeth = 'algoeth' 
price_bids_b_g_algoeth = float(0.0) 
qty_bids_b_g_algoeth = float(0.0) 
price_asks_b_g_algoeth = float(0.0) 
qty_asks_b_g_algoeth = float(0.0) 

def on_message_algoeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_algoeth = 'algoeth' 
		price_bids_b_l_algoeth = data['tick']['bid'] 
		qty_bids_b_l_algoeth = data['tick']['bidSize']
		price_asks_b_l_algoeth = data['tick']['ask'] 
		qty_asks_b_l_algoeth = data['tick']['askSize'] 

		global symbol_b_g_algoeth 
		global price_bids_b_g_algoeth 
		global qty_bids_b_g_algoeth 
		global price_asks_b_g_algoeth 
		global qty_asks_b_g_algoeth 

		symbol_b_g_algoeth = symbol_b_l_algoeth 
		price_bids_b_g_algoeth = price_bids_b_l_algoeth 
		qty_bids_b_g_algoeth = qty_bids_b_l_algoeth 
		price_asks_b_g_algoeth = price_asks_b_l_algoeth 
		qty_asks_b_g_algoeth = qty_asks_b_l_algoeth 


def on_close_algoeth(ws): 
	print('### closed ###') 

def on_error_algoeth(ws, message): 
	print(message) 

def on_open_algoeth(ws): 
	ws.send(json.dumps({'sub': f'market.algoeth.ticker'})) 

def loop_algoeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_algoeth, 
		on_close=on_close_algoeth, 
		on_error=on_error_algoeth) 
	ws.on_open = on_open_algoeth 
	ws.run_forever() 

Thread(target=loop_algoeth).start() 

def loop_algousdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_algousdt != 0.0 and qty_bids_a_g_algousdt != 0.0 and price_asks_a_g_algousdt != 0.0 and qty_asks_a_g_algousdt != 0.0 and price_bids_b_g_algoeth != 0.0 and qty_bids_b_g_algoeth != 0.0 and price_asks_b_g_algoeth != 0.0 and qty_asks_b_g_algoeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_algousdt) 
			price_b = float(price_bids_b_g_algoeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_algoeth, pribil)

Thread(target=loop_algousdt_Trade).start() 

symbol_a_g_scusdt = 'scusdt' 
price_bids_a_g_scusdt = float(0.0) 
qty_bids_a_g_scusdt = float(0.0) 
price_asks_a_g_scusdt = float(0.0) 
qty_asks_a_g_scusdt = float(0.0) 

def on_message_scusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_scusdt = 'scusdt' 
		price_bids_a_l_scusdt = data['tick']['bid'] 
		qty_bids_a_l_scusdt = data['tick']['bidSize'] 
		price_asks_a_l_scusdt = data['tick']['ask'] 
		qty_asks_a_l_scusdt = data['tick']['askSize'] 

		global symbol_a_g_scusdt 
		global price_bids_a_g_scusdt 
		global qty_bids_a_g_scusdt 
		global price_asks_a_g_scusdt 
		global qty_asks_a_g_scusdt 

		symbol_a_g_scusdt = symbol_a_l_scusdt 
		price_bids_a_g_scusdt = price_bids_a_l_scusdt 
		qty_bids_a_g_scusdt = qty_bids_a_l_scusdt 
		price_asks_a_g_scusdt = price_asks_a_l_scusdt 
		qty_asks_a_g_scusdt = qty_asks_a_l_scusdt 

def on_close_scusdt(ws): 
	print('### closed ###') 

def on_error_scusdt(ws, message): 
	print(message) 

def on_open_scusdt(ws): 
	ws.send(json.dumps({'sub': f'market.scusdt.ticker'})) 

def loop_scusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_scusdt, 
		on_close=on_close_scusdt, 
		on_error=on_error_scusdt) 
	ws.on_open = on_open_scusdt 
	ws.run_forever() 

Thread(target=loop_scusdt).start() 

symbol_b_g_scbtc = 'scbtc' 
price_bids_b_g_scbtc = float(0.0) 
qty_bids_b_g_scbtc = float(0.0) 
price_asks_b_g_scbtc = float(0.0) 
qty_asks_b_g_scbtc = float(0.0) 

def on_message_scbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_scbtc = 'scbtc' 
		price_bids_b_l_scbtc = data['tick']['bid'] 
		qty_bids_b_l_scbtc = data['tick']['bidSize']
		price_asks_b_l_scbtc = data['tick']['ask'] 
		qty_asks_b_l_scbtc = data['tick']['askSize'] 

		global symbol_b_g_scbtc 
		global price_bids_b_g_scbtc 
		global qty_bids_b_g_scbtc 
		global price_asks_b_g_scbtc 
		global qty_asks_b_g_scbtc 

		symbol_b_g_scbtc = symbol_b_l_scbtc 
		price_bids_b_g_scbtc = price_bids_b_l_scbtc 
		qty_bids_b_g_scbtc = qty_bids_b_l_scbtc 
		price_asks_b_g_scbtc = price_asks_b_l_scbtc 
		qty_asks_b_g_scbtc = qty_asks_b_l_scbtc 


def on_close_scbtc(ws): 
	print('### closed ###') 

def on_error_scbtc(ws, message): 
	print(message) 

def on_open_scbtc(ws): 
	ws.send(json.dumps({'sub': f'market.scbtc.ticker'})) 

def loop_scbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_scbtc, 
		on_close=on_close_scbtc, 
		on_error=on_error_scbtc) 
	ws.on_open = on_open_scbtc 
	ws.run_forever() 

Thread(target=loop_scbtc).start() 

def loop_scusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_scusdt != 0.0 and qty_bids_a_g_scusdt != 0.0 and price_asks_a_g_scusdt != 0.0 and qty_asks_a_g_scusdt != 0.0 and price_bids_b_g_scbtc != 0.0 and qty_bids_b_g_scbtc != 0.0 and price_asks_b_g_scbtc != 0.0 and qty_asks_b_g_scbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_scusdt) 
			price_b = float(price_bids_b_g_scbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_scbtc, pribil)

Thread(target=loop_scusdt_Trade).start() 

symbol_a_g_rndrusdt = 'rndrusdt' 
price_bids_a_g_rndrusdt = float(0.0) 
qty_bids_a_g_rndrusdt = float(0.0) 
price_asks_a_g_rndrusdt = float(0.0) 
qty_asks_a_g_rndrusdt = float(0.0) 

def on_message_rndrusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_rndrusdt = 'rndrusdt' 
		price_bids_a_l_rndrusdt = data['tick']['bid'] 
		qty_bids_a_l_rndrusdt = data['tick']['bidSize'] 
		price_asks_a_l_rndrusdt = data['tick']['ask'] 
		qty_asks_a_l_rndrusdt = data['tick']['askSize'] 

		global symbol_a_g_rndrusdt 
		global price_bids_a_g_rndrusdt 
		global qty_bids_a_g_rndrusdt 
		global price_asks_a_g_rndrusdt 
		global qty_asks_a_g_rndrusdt 

		symbol_a_g_rndrusdt = symbol_a_l_rndrusdt 
		price_bids_a_g_rndrusdt = price_bids_a_l_rndrusdt 
		qty_bids_a_g_rndrusdt = qty_bids_a_l_rndrusdt 
		price_asks_a_g_rndrusdt = price_asks_a_l_rndrusdt 
		qty_asks_a_g_rndrusdt = qty_asks_a_l_rndrusdt 

def on_close_rndrusdt(ws): 
	print('### closed ###') 

def on_error_rndrusdt(ws, message): 
	print(message) 

def on_open_rndrusdt(ws): 
	ws.send(json.dumps({'sub': f'market.rndrusdt.ticker'})) 

def loop_rndrusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rndrusdt, 
		on_close=on_close_rndrusdt, 
		on_error=on_error_rndrusdt) 
	ws.on_open = on_open_rndrusdt 
	ws.run_forever() 

Thread(target=loop_rndrusdt).start() 

symbol_b_g_rndreth = 'rndreth' 
price_bids_b_g_rndreth = float(0.0) 
qty_bids_b_g_rndreth = float(0.0) 
price_asks_b_g_rndreth = float(0.0) 
qty_asks_b_g_rndreth = float(0.0) 

def on_message_rndreth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_rndreth = 'rndreth' 
		price_bids_b_l_rndreth = data['tick']['bid'] 
		qty_bids_b_l_rndreth = data['tick']['bidSize']
		price_asks_b_l_rndreth = data['tick']['ask'] 
		qty_asks_b_l_rndreth = data['tick']['askSize'] 

		global symbol_b_g_rndreth 
		global price_bids_b_g_rndreth 
		global qty_bids_b_g_rndreth 
		global price_asks_b_g_rndreth 
		global qty_asks_b_g_rndreth 

		symbol_b_g_rndreth = symbol_b_l_rndreth 
		price_bids_b_g_rndreth = price_bids_b_l_rndreth 
		qty_bids_b_g_rndreth = qty_bids_b_l_rndreth 
		price_asks_b_g_rndreth = price_asks_b_l_rndreth 
		qty_asks_b_g_rndreth = qty_asks_b_l_rndreth 


def on_close_rndreth(ws): 
	print('### closed ###') 

def on_error_rndreth(ws, message): 
	print(message) 

def on_open_rndreth(ws): 
	ws.send(json.dumps({'sub': f'market.rndreth.ticker'})) 

def loop_rndreth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rndreth, 
		on_close=on_close_rndreth, 
		on_error=on_error_rndreth) 
	ws.on_open = on_open_rndreth 
	ws.run_forever() 

Thread(target=loop_rndreth).start() 

def loop_rndrusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_rndrusdt != 0.0 and qty_bids_a_g_rndrusdt != 0.0 and price_asks_a_g_rndrusdt != 0.0 and qty_asks_a_g_rndrusdt != 0.0 and price_bids_b_g_rndreth != 0.0 and qty_bids_b_g_rndreth != 0.0 and price_asks_b_g_rndreth != 0.0 and qty_asks_b_g_rndreth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_rndrusdt) 
			price_b = float(price_bids_b_g_rndreth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_rndreth, pribil)

Thread(target=loop_rndrusdt_Trade).start() 

symbol_a_g_glmusdt = 'glmusdt' 
price_bids_a_g_glmusdt = float(0.0) 
qty_bids_a_g_glmusdt = float(0.0) 
price_asks_a_g_glmusdt = float(0.0) 
qty_asks_a_g_glmusdt = float(0.0) 

def on_message_glmusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_glmusdt = 'glmusdt' 
		price_bids_a_l_glmusdt = data['tick']['bid'] 
		qty_bids_a_l_glmusdt = data['tick']['bidSize'] 
		price_asks_a_l_glmusdt = data['tick']['ask'] 
		qty_asks_a_l_glmusdt = data['tick']['askSize'] 

		global symbol_a_g_glmusdt 
		global price_bids_a_g_glmusdt 
		global qty_bids_a_g_glmusdt 
		global price_asks_a_g_glmusdt 
		global qty_asks_a_g_glmusdt 

		symbol_a_g_glmusdt = symbol_a_l_glmusdt 
		price_bids_a_g_glmusdt = price_bids_a_l_glmusdt 
		qty_bids_a_g_glmusdt = qty_bids_a_l_glmusdt 
		price_asks_a_g_glmusdt = price_asks_a_l_glmusdt 
		qty_asks_a_g_glmusdt = qty_asks_a_l_glmusdt 

def on_close_glmusdt(ws): 
	print('### closed ###') 

def on_error_glmusdt(ws, message): 
	print(message) 

def on_open_glmusdt(ws): 
	ws.send(json.dumps({'sub': f'market.glmusdt.ticker'})) 

def loop_glmusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_glmusdt, 
		on_close=on_close_glmusdt, 
		on_error=on_error_glmusdt) 
	ws.on_open = on_open_glmusdt 
	ws.run_forever() 

Thread(target=loop_glmusdt).start() 

symbol_b_g_glmbtc = 'glmbtc' 
price_bids_b_g_glmbtc = float(0.0) 
qty_bids_b_g_glmbtc = float(0.0) 
price_asks_b_g_glmbtc = float(0.0) 
qty_asks_b_g_glmbtc = float(0.0) 

def on_message_glmbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_glmbtc = 'glmbtc' 
		price_bids_b_l_glmbtc = data['tick']['bid'] 
		qty_bids_b_l_glmbtc = data['tick']['bidSize']
		price_asks_b_l_glmbtc = data['tick']['ask'] 
		qty_asks_b_l_glmbtc = data['tick']['askSize'] 

		global symbol_b_g_glmbtc 
		global price_bids_b_g_glmbtc 
		global qty_bids_b_g_glmbtc 
		global price_asks_b_g_glmbtc 
		global qty_asks_b_g_glmbtc 

		symbol_b_g_glmbtc = symbol_b_l_glmbtc 
		price_bids_b_g_glmbtc = price_bids_b_l_glmbtc 
		qty_bids_b_g_glmbtc = qty_bids_b_l_glmbtc 
		price_asks_b_g_glmbtc = price_asks_b_l_glmbtc 
		qty_asks_b_g_glmbtc = qty_asks_b_l_glmbtc 


def on_close_glmbtc(ws): 
	print('### closed ###') 

def on_error_glmbtc(ws, message): 
	print(message) 

def on_open_glmbtc(ws): 
	ws.send(json.dumps({'sub': f'market.glmbtc.ticker'})) 

def loop_glmbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_glmbtc, 
		on_close=on_close_glmbtc, 
		on_error=on_error_glmbtc) 
	ws.on_open = on_open_glmbtc 
	ws.run_forever() 

Thread(target=loop_glmbtc).start() 

def loop_glmusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_glmusdt != 0.0 and qty_bids_a_g_glmusdt != 0.0 and price_asks_a_g_glmusdt != 0.0 and qty_asks_a_g_glmusdt != 0.0 and price_bids_b_g_glmbtc != 0.0 and qty_bids_b_g_glmbtc != 0.0 and price_asks_b_g_glmbtc != 0.0 and qty_asks_b_g_glmbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_glmusdt) 
			price_b = float(price_bids_b_g_glmbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_glmbtc, pribil)

Thread(target=loop_glmusdt_Trade).start() 

symbol_a_g_ognusdt = 'ognusdt' 
price_bids_a_g_ognusdt = float(0.0) 
qty_bids_a_g_ognusdt = float(0.0) 
price_asks_a_g_ognusdt = float(0.0) 
qty_asks_a_g_ognusdt = float(0.0) 

def on_message_ognusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ognusdt = 'ognusdt' 
		price_bids_a_l_ognusdt = data['tick']['bid'] 
		qty_bids_a_l_ognusdt = data['tick']['bidSize'] 
		price_asks_a_l_ognusdt = data['tick']['ask'] 
		qty_asks_a_l_ognusdt = data['tick']['askSize'] 

		global symbol_a_g_ognusdt 
		global price_bids_a_g_ognusdt 
		global qty_bids_a_g_ognusdt 
		global price_asks_a_g_ognusdt 
		global qty_asks_a_g_ognusdt 

		symbol_a_g_ognusdt = symbol_a_l_ognusdt 
		price_bids_a_g_ognusdt = price_bids_a_l_ognusdt 
		qty_bids_a_g_ognusdt = qty_bids_a_l_ognusdt 
		price_asks_a_g_ognusdt = price_asks_a_l_ognusdt 
		qty_asks_a_g_ognusdt = qty_asks_a_l_ognusdt 

def on_close_ognusdt(ws): 
	print('### closed ###') 

def on_error_ognusdt(ws, message): 
	print(message) 

def on_open_ognusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ognusdt.ticker'})) 

def loop_ognusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ognusdt, 
		on_close=on_close_ognusdt, 
		on_error=on_error_ognusdt) 
	ws.on_open = on_open_ognusdt 
	ws.run_forever() 

Thread(target=loop_ognusdt).start() 

symbol_b_g_ognbtc = 'ognbtc' 
price_bids_b_g_ognbtc = float(0.0) 
qty_bids_b_g_ognbtc = float(0.0) 
price_asks_b_g_ognbtc = float(0.0) 
qty_asks_b_g_ognbtc = float(0.0) 

def on_message_ognbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ognbtc = 'ognbtc' 
		price_bids_b_l_ognbtc = data['tick']['bid'] 
		qty_bids_b_l_ognbtc = data['tick']['bidSize']
		price_asks_b_l_ognbtc = data['tick']['ask'] 
		qty_asks_b_l_ognbtc = data['tick']['askSize'] 

		global symbol_b_g_ognbtc 
		global price_bids_b_g_ognbtc 
		global qty_bids_b_g_ognbtc 
		global price_asks_b_g_ognbtc 
		global qty_asks_b_g_ognbtc 

		symbol_b_g_ognbtc = symbol_b_l_ognbtc 
		price_bids_b_g_ognbtc = price_bids_b_l_ognbtc 
		qty_bids_b_g_ognbtc = qty_bids_b_l_ognbtc 
		price_asks_b_g_ognbtc = price_asks_b_l_ognbtc 
		qty_asks_b_g_ognbtc = qty_asks_b_l_ognbtc 


def on_close_ognbtc(ws): 
	print('### closed ###') 

def on_error_ognbtc(ws, message): 
	print(message) 

def on_open_ognbtc(ws): 
	ws.send(json.dumps({'sub': f'market.ognbtc.ticker'})) 

def loop_ognbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ognbtc, 
		on_close=on_close_ognbtc, 
		on_error=on_error_ognbtc) 
	ws.on_open = on_open_ognbtc 
	ws.run_forever() 

Thread(target=loop_ognbtc).start() 

def loop_ognusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_ognusdt != 0.0 and qty_bids_a_g_ognusdt != 0.0 and price_asks_a_g_ognusdt != 0.0 and qty_asks_a_g_ognusdt != 0.0 and price_bids_b_g_ognbtc != 0.0 and qty_bids_b_g_ognbtc != 0.0 and price_asks_b_g_ognbtc != 0.0 and qty_asks_b_g_ognbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ognusdt) 
			price_b = float(price_bids_b_g_ognbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ognbtc, pribil)

Thread(target=loop_ognusdt_Trade).start() 

symbol_a_g_rsrusdt = 'rsrusdt' 
price_bids_a_g_rsrusdt = float(0.0) 
qty_bids_a_g_rsrusdt = float(0.0) 
price_asks_a_g_rsrusdt = float(0.0) 
qty_asks_a_g_rsrusdt = float(0.0) 

def on_message_rsrusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_rsrusdt = 'rsrusdt' 
		price_bids_a_l_rsrusdt = data['tick']['bid'] 
		qty_bids_a_l_rsrusdt = data['tick']['bidSize'] 
		price_asks_a_l_rsrusdt = data['tick']['ask'] 
		qty_asks_a_l_rsrusdt = data['tick']['askSize'] 

		global symbol_a_g_rsrusdt 
		global price_bids_a_g_rsrusdt 
		global qty_bids_a_g_rsrusdt 
		global price_asks_a_g_rsrusdt 
		global qty_asks_a_g_rsrusdt 

		symbol_a_g_rsrusdt = symbol_a_l_rsrusdt 
		price_bids_a_g_rsrusdt = price_bids_a_l_rsrusdt 
		qty_bids_a_g_rsrusdt = qty_bids_a_l_rsrusdt 
		price_asks_a_g_rsrusdt = price_asks_a_l_rsrusdt 
		qty_asks_a_g_rsrusdt = qty_asks_a_l_rsrusdt 

def on_close_rsrusdt(ws): 
	print('### closed ###') 

def on_error_rsrusdt(ws, message): 
	print(message) 

def on_open_rsrusdt(ws): 
	ws.send(json.dumps({'sub': f'market.rsrusdt.ticker'})) 

def loop_rsrusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rsrusdt, 
		on_close=on_close_rsrusdt, 
		on_error=on_error_rsrusdt) 
	ws.on_open = on_open_rsrusdt 
	ws.run_forever() 

Thread(target=loop_rsrusdt).start() 

symbol_b_g_rsrbtc = 'rsrbtc' 
price_bids_b_g_rsrbtc = float(0.0) 
qty_bids_b_g_rsrbtc = float(0.0) 
price_asks_b_g_rsrbtc = float(0.0) 
qty_asks_b_g_rsrbtc = float(0.0) 

def on_message_rsrbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_rsrbtc = 'rsrbtc' 
		price_bids_b_l_rsrbtc = data['tick']['bid'] 
		qty_bids_b_l_rsrbtc = data['tick']['bidSize']
		price_asks_b_l_rsrbtc = data['tick']['ask'] 
		qty_asks_b_l_rsrbtc = data['tick']['askSize'] 

		global symbol_b_g_rsrbtc 
		global price_bids_b_g_rsrbtc 
		global qty_bids_b_g_rsrbtc 
		global price_asks_b_g_rsrbtc 
		global qty_asks_b_g_rsrbtc 

		symbol_b_g_rsrbtc = symbol_b_l_rsrbtc 
		price_bids_b_g_rsrbtc = price_bids_b_l_rsrbtc 
		qty_bids_b_g_rsrbtc = qty_bids_b_l_rsrbtc 
		price_asks_b_g_rsrbtc = price_asks_b_l_rsrbtc 
		qty_asks_b_g_rsrbtc = qty_asks_b_l_rsrbtc 


def on_close_rsrbtc(ws): 
	print('### closed ###') 

def on_error_rsrbtc(ws, message): 
	print(message) 

def on_open_rsrbtc(ws): 
	ws.send(json.dumps({'sub': f'market.rsrbtc.ticker'})) 

def loop_rsrbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rsrbtc, 
		on_close=on_close_rsrbtc, 
		on_error=on_error_rsrbtc) 
	ws.on_open = on_open_rsrbtc 
	ws.run_forever() 

Thread(target=loop_rsrbtc).start() 

def loop_rsrusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_rsrusdt != 0.0 and qty_bids_a_g_rsrusdt != 0.0 and price_asks_a_g_rsrusdt != 0.0 and qty_asks_a_g_rsrusdt != 0.0 and price_bids_b_g_rsrbtc != 0.0 and qty_bids_b_g_rsrbtc != 0.0 and price_asks_b_g_rsrbtc != 0.0 and qty_asks_b_g_rsrbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_rsrusdt) 
			price_b = float(price_bids_b_g_rsrbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_rsrbtc, pribil)

Thread(target=loop_rsrusdt_Trade).start() 

symbol_a_g_qtumusdt = 'qtumusdt' 
price_bids_a_g_qtumusdt = float(0.0) 
qty_bids_a_g_qtumusdt = float(0.0) 
price_asks_a_g_qtumusdt = float(0.0) 
qty_asks_a_g_qtumusdt = float(0.0) 

def on_message_qtumusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_qtumusdt = 'qtumusdt' 
		price_bids_a_l_qtumusdt = data['tick']['bid'] 
		qty_bids_a_l_qtumusdt = data['tick']['bidSize'] 
		price_asks_a_l_qtumusdt = data['tick']['ask'] 
		qty_asks_a_l_qtumusdt = data['tick']['askSize'] 

		global symbol_a_g_qtumusdt 
		global price_bids_a_g_qtumusdt 
		global qty_bids_a_g_qtumusdt 
		global price_asks_a_g_qtumusdt 
		global qty_asks_a_g_qtumusdt 

		symbol_a_g_qtumusdt = symbol_a_l_qtumusdt 
		price_bids_a_g_qtumusdt = price_bids_a_l_qtumusdt 
		qty_bids_a_g_qtumusdt = qty_bids_a_l_qtumusdt 
		price_asks_a_g_qtumusdt = price_asks_a_l_qtumusdt 
		qty_asks_a_g_qtumusdt = qty_asks_a_l_qtumusdt 

def on_close_qtumusdt(ws): 
	print('### closed ###') 

def on_error_qtumusdt(ws, message): 
	print(message) 

def on_open_qtumusdt(ws): 
	ws.send(json.dumps({'sub': f'market.qtumusdt.ticker'})) 

def loop_qtumusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_qtumusdt, 
		on_close=on_close_qtumusdt, 
		on_error=on_error_qtumusdt) 
	ws.on_open = on_open_qtumusdt 
	ws.run_forever() 

Thread(target=loop_qtumusdt).start() 

symbol_b_g_qtumbtc = 'qtumbtc' 
price_bids_b_g_qtumbtc = float(0.0) 
qty_bids_b_g_qtumbtc = float(0.0) 
price_asks_b_g_qtumbtc = float(0.0) 
qty_asks_b_g_qtumbtc = float(0.0) 

def on_message_qtumbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_qtumbtc = 'qtumbtc' 
		price_bids_b_l_qtumbtc = data['tick']['bid'] 
		qty_bids_b_l_qtumbtc = data['tick']['bidSize']
		price_asks_b_l_qtumbtc = data['tick']['ask'] 
		qty_asks_b_l_qtumbtc = data['tick']['askSize'] 

		global symbol_b_g_qtumbtc 
		global price_bids_b_g_qtumbtc 
		global qty_bids_b_g_qtumbtc 
		global price_asks_b_g_qtumbtc 
		global qty_asks_b_g_qtumbtc 

		symbol_b_g_qtumbtc = symbol_b_l_qtumbtc 
		price_bids_b_g_qtumbtc = price_bids_b_l_qtumbtc 
		qty_bids_b_g_qtumbtc = qty_bids_b_l_qtumbtc 
		price_asks_b_g_qtumbtc = price_asks_b_l_qtumbtc 
		qty_asks_b_g_qtumbtc = qty_asks_b_l_qtumbtc 


def on_close_qtumbtc(ws): 
	print('### closed ###') 

def on_error_qtumbtc(ws, message): 
	print(message) 

def on_open_qtumbtc(ws): 
	ws.send(json.dumps({'sub': f'market.qtumbtc.ticker'})) 

def loop_qtumbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_qtumbtc, 
		on_close=on_close_qtumbtc, 
		on_error=on_error_qtumbtc) 
	ws.on_open = on_open_qtumbtc 
	ws.run_forever() 

Thread(target=loop_qtumbtc).start() 

def loop_qtumusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_qtumusdt != 0.0 and qty_bids_a_g_qtumusdt != 0.0 and price_asks_a_g_qtumusdt != 0.0 and qty_asks_a_g_qtumusdt != 0.0 and price_bids_b_g_qtumbtc != 0.0 and qty_bids_b_g_qtumbtc != 0.0 and price_asks_b_g_qtumbtc != 0.0 and qty_asks_b_g_qtumbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_qtumusdt) 
			price_b = float(price_bids_b_g_qtumbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_qtumbtc, pribil)

Thread(target=loop_qtumusdt_Trade).start() 

symbol_a_g_tnbusdt = 'tnbusdt' 
price_bids_a_g_tnbusdt = float(0.0) 
qty_bids_a_g_tnbusdt = float(0.0) 
price_asks_a_g_tnbusdt = float(0.0) 
qty_asks_a_g_tnbusdt = float(0.0) 

def on_message_tnbusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_tnbusdt = 'tnbusdt' 
		price_bids_a_l_tnbusdt = data['tick']['bid'] 
		qty_bids_a_l_tnbusdt = data['tick']['bidSize'] 
		price_asks_a_l_tnbusdt = data['tick']['ask'] 
		qty_asks_a_l_tnbusdt = data['tick']['askSize'] 

		global symbol_a_g_tnbusdt 
		global price_bids_a_g_tnbusdt 
		global qty_bids_a_g_tnbusdt 
		global price_asks_a_g_tnbusdt 
		global qty_asks_a_g_tnbusdt 

		symbol_a_g_tnbusdt = symbol_a_l_tnbusdt 
		price_bids_a_g_tnbusdt = price_bids_a_l_tnbusdt 
		qty_bids_a_g_tnbusdt = qty_bids_a_l_tnbusdt 
		price_asks_a_g_tnbusdt = price_asks_a_l_tnbusdt 
		qty_asks_a_g_tnbusdt = qty_asks_a_l_tnbusdt 

def on_close_tnbusdt(ws): 
	print('### closed ###') 

def on_error_tnbusdt(ws, message): 
	print(message) 

def on_open_tnbusdt(ws): 
	ws.send(json.dumps({'sub': f'market.tnbusdt.ticker'})) 

def loop_tnbusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_tnbusdt, 
		on_close=on_close_tnbusdt, 
		on_error=on_error_tnbusdt) 
	ws.on_open = on_open_tnbusdt 
	ws.run_forever() 

Thread(target=loop_tnbusdt).start() 

symbol_b_g_tnbeth = 'tnbeth' 
price_bids_b_g_tnbeth = float(0.0) 
qty_bids_b_g_tnbeth = float(0.0) 
price_asks_b_g_tnbeth = float(0.0) 
qty_asks_b_g_tnbeth = float(0.0) 

def on_message_tnbeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_tnbeth = 'tnbeth' 
		price_bids_b_l_tnbeth = data['tick']['bid'] 
		qty_bids_b_l_tnbeth = data['tick']['bidSize']
		price_asks_b_l_tnbeth = data['tick']['ask'] 
		qty_asks_b_l_tnbeth = data['tick']['askSize'] 

		global symbol_b_g_tnbeth 
		global price_bids_b_g_tnbeth 
		global qty_bids_b_g_tnbeth 
		global price_asks_b_g_tnbeth 
		global qty_asks_b_g_tnbeth 

		symbol_b_g_tnbeth = symbol_b_l_tnbeth 
		price_bids_b_g_tnbeth = price_bids_b_l_tnbeth 
		qty_bids_b_g_tnbeth = qty_bids_b_l_tnbeth 
		price_asks_b_g_tnbeth = price_asks_b_l_tnbeth 
		qty_asks_b_g_tnbeth = qty_asks_b_l_tnbeth 


def on_close_tnbeth(ws): 
	print('### closed ###') 

def on_error_tnbeth(ws, message): 
	print(message) 

def on_open_tnbeth(ws): 
	ws.send(json.dumps({'sub': f'market.tnbeth.ticker'})) 

def loop_tnbeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_tnbeth, 
		on_close=on_close_tnbeth, 
		on_error=on_error_tnbeth) 
	ws.on_open = on_open_tnbeth 
	ws.run_forever() 

Thread(target=loop_tnbeth).start() 

def loop_tnbusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_tnbusdt != 0.0 and qty_bids_a_g_tnbusdt != 0.0 and price_asks_a_g_tnbusdt != 0.0 and qty_asks_a_g_tnbusdt != 0.0 and price_bids_b_g_tnbeth != 0.0 and qty_bids_b_g_tnbeth != 0.0 and price_asks_b_g_tnbeth != 0.0 and qty_asks_b_g_tnbeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_tnbusdt) 
			price_b = float(price_bids_b_g_tnbeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_tnbeth, pribil)

Thread(target=loop_tnbusdt_Trade).start() 

symbol_a_g_sunusdt = 'sunusdt' 
price_bids_a_g_sunusdt = float(0.0) 
qty_bids_a_g_sunusdt = float(0.0) 
price_asks_a_g_sunusdt = float(0.0) 
qty_asks_a_g_sunusdt = float(0.0) 

def on_message_sunusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_sunusdt = 'sunusdt' 
		price_bids_a_l_sunusdt = data['tick']['bid'] 
		qty_bids_a_l_sunusdt = data['tick']['bidSize'] 
		price_asks_a_l_sunusdt = data['tick']['ask'] 
		qty_asks_a_l_sunusdt = data['tick']['askSize'] 

		global symbol_a_g_sunusdt 
		global price_bids_a_g_sunusdt 
		global qty_bids_a_g_sunusdt 
		global price_asks_a_g_sunusdt 
		global qty_asks_a_g_sunusdt 

		symbol_a_g_sunusdt = symbol_a_l_sunusdt 
		price_bids_a_g_sunusdt = price_bids_a_l_sunusdt 
		qty_bids_a_g_sunusdt = qty_bids_a_l_sunusdt 
		price_asks_a_g_sunusdt = price_asks_a_l_sunusdt 
		qty_asks_a_g_sunusdt = qty_asks_a_l_sunusdt 

def on_close_sunusdt(ws): 
	print('### closed ###') 

def on_error_sunusdt(ws, message): 
	print(message) 

def on_open_sunusdt(ws): 
	ws.send(json.dumps({'sub': f'market.sunusdt.ticker'})) 

def loop_sunusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sunusdt, 
		on_close=on_close_sunusdt, 
		on_error=on_error_sunusdt) 
	ws.on_open = on_open_sunusdt 
	ws.run_forever() 

Thread(target=loop_sunusdt).start() 

symbol_b_g_sunusdd = 'sunusdd' 
price_bids_b_g_sunusdd = float(0.0) 
qty_bids_b_g_sunusdd = float(0.0) 
price_asks_b_g_sunusdd = float(0.0) 
qty_asks_b_g_sunusdd = float(0.0) 

def on_message_sunusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_sunusdd = 'sunusdd' 
		price_bids_b_l_sunusdd = data['tick']['bid'] 
		qty_bids_b_l_sunusdd = data['tick']['bidSize']
		price_asks_b_l_sunusdd = data['tick']['ask'] 
		qty_asks_b_l_sunusdd = data['tick']['askSize'] 

		global symbol_b_g_sunusdd 
		global price_bids_b_g_sunusdd 
		global qty_bids_b_g_sunusdd 
		global price_asks_b_g_sunusdd 
		global qty_asks_b_g_sunusdd 

		symbol_b_g_sunusdd = symbol_b_l_sunusdd 
		price_bids_b_g_sunusdd = price_bids_b_l_sunusdd 
		qty_bids_b_g_sunusdd = qty_bids_b_l_sunusdd 
		price_asks_b_g_sunusdd = price_asks_b_l_sunusdd 
		qty_asks_b_g_sunusdd = qty_asks_b_l_sunusdd 


def on_close_sunusdd(ws): 
	print('### closed ###') 

def on_error_sunusdd(ws, message): 
	print(message) 

def on_open_sunusdd(ws): 
	ws.send(json.dumps({'sub': f'market.sunusdd.ticker'})) 

def loop_sunusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sunusdd, 
		on_close=on_close_sunusdd, 
		on_error=on_error_sunusdd) 
	ws.on_open = on_open_sunusdd 
	ws.run_forever() 

Thread(target=loop_sunusdd).start() 

def loop_sunusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_sunusdt != 0.0 and qty_bids_a_g_sunusdt != 0.0 and price_asks_a_g_sunusdt != 0.0 and qty_asks_a_g_sunusdt != 0.0 and price_bids_b_g_sunusdd != 0.0 and qty_bids_b_g_sunusdd != 0.0 and price_asks_b_g_sunusdd != 0.0 and qty_asks_b_g_sunusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_sunusdt) 
			price_b = float(price_bids_b_g_sunusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_sunusdd, pribil)

Thread(target=loop_sunusdt_Trade).start() 

symbol_a_g_ankrusdt = 'ankrusdt' 
price_bids_a_g_ankrusdt = float(0.0) 
qty_bids_a_g_ankrusdt = float(0.0) 
price_asks_a_g_ankrusdt = float(0.0) 
qty_asks_a_g_ankrusdt = float(0.0) 

def on_message_ankrusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ankrusdt = 'ankrusdt' 
		price_bids_a_l_ankrusdt = data['tick']['bid'] 
		qty_bids_a_l_ankrusdt = data['tick']['bidSize'] 
		price_asks_a_l_ankrusdt = data['tick']['ask'] 
		qty_asks_a_l_ankrusdt = data['tick']['askSize'] 

		global symbol_a_g_ankrusdt 
		global price_bids_a_g_ankrusdt 
		global qty_bids_a_g_ankrusdt 
		global price_asks_a_g_ankrusdt 
		global qty_asks_a_g_ankrusdt 

		symbol_a_g_ankrusdt = symbol_a_l_ankrusdt 
		price_bids_a_g_ankrusdt = price_bids_a_l_ankrusdt 
		qty_bids_a_g_ankrusdt = qty_bids_a_l_ankrusdt 
		price_asks_a_g_ankrusdt = price_asks_a_l_ankrusdt 
		qty_asks_a_g_ankrusdt = qty_asks_a_l_ankrusdt 

def on_close_ankrusdt(ws): 
	print('### closed ###') 

def on_error_ankrusdt(ws, message): 
	print(message) 

def on_open_ankrusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ankrusdt.ticker'})) 

def loop_ankrusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ankrusdt, 
		on_close=on_close_ankrusdt, 
		on_error=on_error_ankrusdt) 
	ws.on_open = on_open_ankrusdt 
	ws.run_forever() 

Thread(target=loop_ankrusdt).start() 

symbol_b_g_ankrbtc = 'ankrbtc' 
price_bids_b_g_ankrbtc = float(0.0) 
qty_bids_b_g_ankrbtc = float(0.0) 
price_asks_b_g_ankrbtc = float(0.0) 
qty_asks_b_g_ankrbtc = float(0.0) 

def on_message_ankrbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ankrbtc = 'ankrbtc' 
		price_bids_b_l_ankrbtc = data['tick']['bid'] 
		qty_bids_b_l_ankrbtc = data['tick']['bidSize']
		price_asks_b_l_ankrbtc = data['tick']['ask'] 
		qty_asks_b_l_ankrbtc = data['tick']['askSize'] 

		global symbol_b_g_ankrbtc 
		global price_bids_b_g_ankrbtc 
		global qty_bids_b_g_ankrbtc 
		global price_asks_b_g_ankrbtc 
		global qty_asks_b_g_ankrbtc 

		symbol_b_g_ankrbtc = symbol_b_l_ankrbtc 
		price_bids_b_g_ankrbtc = price_bids_b_l_ankrbtc 
		qty_bids_b_g_ankrbtc = qty_bids_b_l_ankrbtc 
		price_asks_b_g_ankrbtc = price_asks_b_l_ankrbtc 
		qty_asks_b_g_ankrbtc = qty_asks_b_l_ankrbtc 


def on_close_ankrbtc(ws): 
	print('### closed ###') 

def on_error_ankrbtc(ws, message): 
	print(message) 

def on_open_ankrbtc(ws): 
	ws.send(json.dumps({'sub': f'market.ankrbtc.ticker'})) 

def loop_ankrbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ankrbtc, 
		on_close=on_close_ankrbtc, 
		on_error=on_error_ankrbtc) 
	ws.on_open = on_open_ankrbtc 
	ws.run_forever() 

Thread(target=loop_ankrbtc).start() 

def loop_ankrusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_ankrusdt != 0.0 and qty_bids_a_g_ankrusdt != 0.0 and price_asks_a_g_ankrusdt != 0.0 and qty_asks_a_g_ankrusdt != 0.0 and price_bids_b_g_ankrbtc != 0.0 and qty_bids_b_g_ankrbtc != 0.0 and price_asks_b_g_ankrbtc != 0.0 and qty_asks_b_g_ankrbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ankrusdt) 
			price_b = float(price_bids_b_g_ankrbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ankrbtc, pribil)

Thread(target=loop_ankrusdt_Trade).start() 

symbol_a_g_icpusdt = 'icpusdt' 
price_bids_a_g_icpusdt = float(0.0) 
qty_bids_a_g_icpusdt = float(0.0) 
price_asks_a_g_icpusdt = float(0.0) 
qty_asks_a_g_icpusdt = float(0.0) 

def on_message_icpusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_icpusdt = 'icpusdt' 
		price_bids_a_l_icpusdt = data['tick']['bid'] 
		qty_bids_a_l_icpusdt = data['tick']['bidSize'] 
		price_asks_a_l_icpusdt = data['tick']['ask'] 
		qty_asks_a_l_icpusdt = data['tick']['askSize'] 

		global symbol_a_g_icpusdt 
		global price_bids_a_g_icpusdt 
		global qty_bids_a_g_icpusdt 
		global price_asks_a_g_icpusdt 
		global qty_asks_a_g_icpusdt 

		symbol_a_g_icpusdt = symbol_a_l_icpusdt 
		price_bids_a_g_icpusdt = price_bids_a_l_icpusdt 
		qty_bids_a_g_icpusdt = qty_bids_a_l_icpusdt 
		price_asks_a_g_icpusdt = price_asks_a_l_icpusdt 
		qty_asks_a_g_icpusdt = qty_asks_a_l_icpusdt 

def on_close_icpusdt(ws): 
	print('### closed ###') 

def on_error_icpusdt(ws, message): 
	print(message) 

def on_open_icpusdt(ws): 
	ws.send(json.dumps({'sub': f'market.icpusdt.ticker'})) 

def loop_icpusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_icpusdt, 
		on_close=on_close_icpusdt, 
		on_error=on_error_icpusdt) 
	ws.on_open = on_open_icpusdt 
	ws.run_forever() 

Thread(target=loop_icpusdt).start() 

symbol_b_g_icpbtc = 'icpbtc' 
price_bids_b_g_icpbtc = float(0.0) 
qty_bids_b_g_icpbtc = float(0.0) 
price_asks_b_g_icpbtc = float(0.0) 
qty_asks_b_g_icpbtc = float(0.0) 

def on_message_icpbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_icpbtc = 'icpbtc' 
		price_bids_b_l_icpbtc = data['tick']['bid'] 
		qty_bids_b_l_icpbtc = data['tick']['bidSize']
		price_asks_b_l_icpbtc = data['tick']['ask'] 
		qty_asks_b_l_icpbtc = data['tick']['askSize'] 

		global symbol_b_g_icpbtc 
		global price_bids_b_g_icpbtc 
		global qty_bids_b_g_icpbtc 
		global price_asks_b_g_icpbtc 
		global qty_asks_b_g_icpbtc 

		symbol_b_g_icpbtc = symbol_b_l_icpbtc 
		price_bids_b_g_icpbtc = price_bids_b_l_icpbtc 
		qty_bids_b_g_icpbtc = qty_bids_b_l_icpbtc 
		price_asks_b_g_icpbtc = price_asks_b_l_icpbtc 
		qty_asks_b_g_icpbtc = qty_asks_b_l_icpbtc 


def on_close_icpbtc(ws): 
	print('### closed ###') 

def on_error_icpbtc(ws, message): 
	print(message) 

def on_open_icpbtc(ws): 
	ws.send(json.dumps({'sub': f'market.icpbtc.ticker'})) 

def loop_icpbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_icpbtc, 
		on_close=on_close_icpbtc, 
		on_error=on_error_icpbtc) 
	ws.on_open = on_open_icpbtc 
	ws.run_forever() 

Thread(target=loop_icpbtc).start() 

def loop_icpusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_icpusdt != 0.0 and qty_bids_a_g_icpusdt != 0.0 and price_asks_a_g_icpusdt != 0.0 and qty_asks_a_g_icpusdt != 0.0 and price_bids_b_g_icpbtc != 0.0 and qty_bids_b_g_icpbtc != 0.0 and price_asks_b_g_icpbtc != 0.0 and qty_asks_b_g_icpbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_icpusdt) 
			price_b = float(price_bids_b_g_icpbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_icpbtc, pribil)

Thread(target=loop_icpusdt_Trade).start() 

symbol_a_g_omgusdt = 'omgusdt' 
price_bids_a_g_omgusdt = float(0.0) 
qty_bids_a_g_omgusdt = float(0.0) 
price_asks_a_g_omgusdt = float(0.0) 
qty_asks_a_g_omgusdt = float(0.0) 

def on_message_omgusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_omgusdt = 'omgusdt' 
		price_bids_a_l_omgusdt = data['tick']['bid'] 
		qty_bids_a_l_omgusdt = data['tick']['bidSize'] 
		price_asks_a_l_omgusdt = data['tick']['ask'] 
		qty_asks_a_l_omgusdt = data['tick']['askSize'] 

		global symbol_a_g_omgusdt 
		global price_bids_a_g_omgusdt 
		global qty_bids_a_g_omgusdt 
		global price_asks_a_g_omgusdt 
		global qty_asks_a_g_omgusdt 

		symbol_a_g_omgusdt = symbol_a_l_omgusdt 
		price_bids_a_g_omgusdt = price_bids_a_l_omgusdt 
		qty_bids_a_g_omgusdt = qty_bids_a_l_omgusdt 
		price_asks_a_g_omgusdt = price_asks_a_l_omgusdt 
		qty_asks_a_g_omgusdt = qty_asks_a_l_omgusdt 

def on_close_omgusdt(ws): 
	print('### closed ###') 

def on_error_omgusdt(ws, message): 
	print(message) 

def on_open_omgusdt(ws): 
	ws.send(json.dumps({'sub': f'market.omgusdt.ticker'})) 

def loop_omgusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_omgusdt, 
		on_close=on_close_omgusdt, 
		on_error=on_error_omgusdt) 
	ws.on_open = on_open_omgusdt 
	ws.run_forever() 

Thread(target=loop_omgusdt).start() 

symbol_b_g_omgbtc = 'omgbtc' 
price_bids_b_g_omgbtc = float(0.0) 
qty_bids_b_g_omgbtc = float(0.0) 
price_asks_b_g_omgbtc = float(0.0) 
qty_asks_b_g_omgbtc = float(0.0) 

def on_message_omgbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_omgbtc = 'omgbtc' 
		price_bids_b_l_omgbtc = data['tick']['bid'] 
		qty_bids_b_l_omgbtc = data['tick']['bidSize']
		price_asks_b_l_omgbtc = data['tick']['ask'] 
		qty_asks_b_l_omgbtc = data['tick']['askSize'] 

		global symbol_b_g_omgbtc 
		global price_bids_b_g_omgbtc 
		global qty_bids_b_g_omgbtc 
		global price_asks_b_g_omgbtc 
		global qty_asks_b_g_omgbtc 

		symbol_b_g_omgbtc = symbol_b_l_omgbtc 
		price_bids_b_g_omgbtc = price_bids_b_l_omgbtc 
		qty_bids_b_g_omgbtc = qty_bids_b_l_omgbtc 
		price_asks_b_g_omgbtc = price_asks_b_l_omgbtc 
		qty_asks_b_g_omgbtc = qty_asks_b_l_omgbtc 


def on_close_omgbtc(ws): 
	print('### closed ###') 

def on_error_omgbtc(ws, message): 
	print(message) 

def on_open_omgbtc(ws): 
	ws.send(json.dumps({'sub': f'market.omgbtc.ticker'})) 

def loop_omgbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_omgbtc, 
		on_close=on_close_omgbtc, 
		on_error=on_error_omgbtc) 
	ws.on_open = on_open_omgbtc 
	ws.run_forever() 

Thread(target=loop_omgbtc).start() 

def loop_omgusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_omgusdt != 0.0 and qty_bids_a_g_omgusdt != 0.0 and price_asks_a_g_omgusdt != 0.0 and qty_asks_a_g_omgusdt != 0.0 and price_bids_b_g_omgbtc != 0.0 and qty_bids_b_g_omgbtc != 0.0 and price_asks_b_g_omgbtc != 0.0 and qty_asks_b_g_omgbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_omgusdt) 
			price_b = float(price_bids_b_g_omgbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_omgbtc, pribil)

Thread(target=loop_omgusdt_Trade).start() 

symbol_a_g_oxtusdt = 'oxtusdt' 
price_bids_a_g_oxtusdt = float(0.0) 
qty_bids_a_g_oxtusdt = float(0.0) 
price_asks_a_g_oxtusdt = float(0.0) 
qty_asks_a_g_oxtusdt = float(0.0) 

def on_message_oxtusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_oxtusdt = 'oxtusdt' 
		price_bids_a_l_oxtusdt = data['tick']['bid'] 
		qty_bids_a_l_oxtusdt = data['tick']['bidSize'] 
		price_asks_a_l_oxtusdt = data['tick']['ask'] 
		qty_asks_a_l_oxtusdt = data['tick']['askSize'] 

		global symbol_a_g_oxtusdt 
		global price_bids_a_g_oxtusdt 
		global qty_bids_a_g_oxtusdt 
		global price_asks_a_g_oxtusdt 
		global qty_asks_a_g_oxtusdt 

		symbol_a_g_oxtusdt = symbol_a_l_oxtusdt 
		price_bids_a_g_oxtusdt = price_bids_a_l_oxtusdt 
		qty_bids_a_g_oxtusdt = qty_bids_a_l_oxtusdt 
		price_asks_a_g_oxtusdt = price_asks_a_l_oxtusdt 
		qty_asks_a_g_oxtusdt = qty_asks_a_l_oxtusdt 

def on_close_oxtusdt(ws): 
	print('### closed ###') 

def on_error_oxtusdt(ws, message): 
	print(message) 

def on_open_oxtusdt(ws): 
	ws.send(json.dumps({'sub': f'market.oxtusdt.ticker'})) 

def loop_oxtusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_oxtusdt, 
		on_close=on_close_oxtusdt, 
		on_error=on_error_oxtusdt) 
	ws.on_open = on_open_oxtusdt 
	ws.run_forever() 

Thread(target=loop_oxtusdt).start() 

symbol_b_g_oxteth = 'oxteth' 
price_bids_b_g_oxteth = float(0.0) 
qty_bids_b_g_oxteth = float(0.0) 
price_asks_b_g_oxteth = float(0.0) 
qty_asks_b_g_oxteth = float(0.0) 

def on_message_oxteth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_oxteth = 'oxteth' 
		price_bids_b_l_oxteth = data['tick']['bid'] 
		qty_bids_b_l_oxteth = data['tick']['bidSize']
		price_asks_b_l_oxteth = data['tick']['ask'] 
		qty_asks_b_l_oxteth = data['tick']['askSize'] 

		global symbol_b_g_oxteth 
		global price_bids_b_g_oxteth 
		global qty_bids_b_g_oxteth 
		global price_asks_b_g_oxteth 
		global qty_asks_b_g_oxteth 

		symbol_b_g_oxteth = symbol_b_l_oxteth 
		price_bids_b_g_oxteth = price_bids_b_l_oxteth 
		qty_bids_b_g_oxteth = qty_bids_b_l_oxteth 
		price_asks_b_g_oxteth = price_asks_b_l_oxteth 
		qty_asks_b_g_oxteth = qty_asks_b_l_oxteth 


def on_close_oxteth(ws): 
	print('### closed ###') 

def on_error_oxteth(ws, message): 
	print(message) 

def on_open_oxteth(ws): 
	ws.send(json.dumps({'sub': f'market.oxteth.ticker'})) 

def loop_oxteth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_oxteth, 
		on_close=on_close_oxteth, 
		on_error=on_error_oxteth) 
	ws.on_open = on_open_oxteth 
	ws.run_forever() 

Thread(target=loop_oxteth).start() 

def loop_oxtusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_oxtusdt != 0.0 and qty_bids_a_g_oxtusdt != 0.0 and price_asks_a_g_oxtusdt != 0.0 and qty_asks_a_g_oxtusdt != 0.0 and price_bids_b_g_oxteth != 0.0 and qty_bids_b_g_oxteth != 0.0 and price_asks_b_g_oxteth != 0.0 and qty_asks_b_g_oxteth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_oxtusdt) 
			price_b = float(price_bids_b_g_oxteth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_oxteth, pribil)

Thread(target=loop_oxtusdt_Trade).start() 

symbol_a_g_wxtusdt = 'wxtusdt' 
price_bids_a_g_wxtusdt = float(0.0) 
qty_bids_a_g_wxtusdt = float(0.0) 
price_asks_a_g_wxtusdt = float(0.0) 
qty_asks_a_g_wxtusdt = float(0.0) 

def on_message_wxtusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_wxtusdt = 'wxtusdt' 
		price_bids_a_l_wxtusdt = data['tick']['bid'] 
		qty_bids_a_l_wxtusdt = data['tick']['bidSize'] 
		price_asks_a_l_wxtusdt = data['tick']['ask'] 
		qty_asks_a_l_wxtusdt = data['tick']['askSize'] 

		global symbol_a_g_wxtusdt 
		global price_bids_a_g_wxtusdt 
		global qty_bids_a_g_wxtusdt 
		global price_asks_a_g_wxtusdt 
		global qty_asks_a_g_wxtusdt 

		symbol_a_g_wxtusdt = symbol_a_l_wxtusdt 
		price_bids_a_g_wxtusdt = price_bids_a_l_wxtusdt 
		qty_bids_a_g_wxtusdt = qty_bids_a_l_wxtusdt 
		price_asks_a_g_wxtusdt = price_asks_a_l_wxtusdt 
		qty_asks_a_g_wxtusdt = qty_asks_a_l_wxtusdt 

def on_close_wxtusdt(ws): 
	print('### closed ###') 

def on_error_wxtusdt(ws, message): 
	print(message) 

def on_open_wxtusdt(ws): 
	ws.send(json.dumps({'sub': f'market.wxtusdt.ticker'})) 

def loop_wxtusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wxtusdt, 
		on_close=on_close_wxtusdt, 
		on_error=on_error_wxtusdt) 
	ws.on_open = on_open_wxtusdt 
	ws.run_forever() 

Thread(target=loop_wxtusdt).start() 

symbol_b_g_wxtbtc = 'wxtbtc' 
price_bids_b_g_wxtbtc = float(0.0) 
qty_bids_b_g_wxtbtc = float(0.0) 
price_asks_b_g_wxtbtc = float(0.0) 
qty_asks_b_g_wxtbtc = float(0.0) 

def on_message_wxtbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_wxtbtc = 'wxtbtc' 
		price_bids_b_l_wxtbtc = data['tick']['bid'] 
		qty_bids_b_l_wxtbtc = data['tick']['bidSize']
		price_asks_b_l_wxtbtc = data['tick']['ask'] 
		qty_asks_b_l_wxtbtc = data['tick']['askSize'] 

		global symbol_b_g_wxtbtc 
		global price_bids_b_g_wxtbtc 
		global qty_bids_b_g_wxtbtc 
		global price_asks_b_g_wxtbtc 
		global qty_asks_b_g_wxtbtc 

		symbol_b_g_wxtbtc = symbol_b_l_wxtbtc 
		price_bids_b_g_wxtbtc = price_bids_b_l_wxtbtc 
		qty_bids_b_g_wxtbtc = qty_bids_b_l_wxtbtc 
		price_asks_b_g_wxtbtc = price_asks_b_l_wxtbtc 
		qty_asks_b_g_wxtbtc = qty_asks_b_l_wxtbtc 


def on_close_wxtbtc(ws): 
	print('### closed ###') 

def on_error_wxtbtc(ws, message): 
	print(message) 

def on_open_wxtbtc(ws): 
	ws.send(json.dumps({'sub': f'market.wxtbtc.ticker'})) 

def loop_wxtbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wxtbtc, 
		on_close=on_close_wxtbtc, 
		on_error=on_error_wxtbtc) 
	ws.on_open = on_open_wxtbtc 
	ws.run_forever() 

Thread(target=loop_wxtbtc).start() 

def loop_wxtusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_wxtusdt != 0.0 and qty_bids_a_g_wxtusdt != 0.0 and price_asks_a_g_wxtusdt != 0.0 and qty_asks_a_g_wxtusdt != 0.0 and price_bids_b_g_wxtbtc != 0.0 and qty_bids_b_g_wxtbtc != 0.0 and price_asks_b_g_wxtbtc != 0.0 and qty_asks_b_g_wxtbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_wxtusdt) 
			price_b = float(price_bids_b_g_wxtbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_wxtbtc, pribil)

Thread(target=loop_wxtusdt_Trade).start() 

symbol_a_g_astusdt = 'astusdt' 
price_bids_a_g_astusdt = float(0.0) 
qty_bids_a_g_astusdt = float(0.0) 
price_asks_a_g_astusdt = float(0.0) 
qty_asks_a_g_astusdt = float(0.0) 

def on_message_astusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_astusdt = 'astusdt' 
		price_bids_a_l_astusdt = data['tick']['bid'] 
		qty_bids_a_l_astusdt = data['tick']['bidSize'] 
		price_asks_a_l_astusdt = data['tick']['ask'] 
		qty_asks_a_l_astusdt = data['tick']['askSize'] 

		global symbol_a_g_astusdt 
		global price_bids_a_g_astusdt 
		global qty_bids_a_g_astusdt 
		global price_asks_a_g_astusdt 
		global qty_asks_a_g_astusdt 

		symbol_a_g_astusdt = symbol_a_l_astusdt 
		price_bids_a_g_astusdt = price_bids_a_l_astusdt 
		qty_bids_a_g_astusdt = qty_bids_a_l_astusdt 
		price_asks_a_g_astusdt = price_asks_a_l_astusdt 
		qty_asks_a_g_astusdt = qty_asks_a_l_astusdt 

def on_close_astusdt(ws): 
	print('### closed ###') 

def on_error_astusdt(ws, message): 
	print(message) 

def on_open_astusdt(ws): 
	ws.send(json.dumps({'sub': f'market.astusdt.ticker'})) 

def loop_astusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_astusdt, 
		on_close=on_close_astusdt, 
		on_error=on_error_astusdt) 
	ws.on_open = on_open_astusdt 
	ws.run_forever() 

Thread(target=loop_astusdt).start() 

symbol_b_g_astbtc = 'astbtc' 
price_bids_b_g_astbtc = float(0.0) 
qty_bids_b_g_astbtc = float(0.0) 
price_asks_b_g_astbtc = float(0.0) 
qty_asks_b_g_astbtc = float(0.0) 

def on_message_astbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_astbtc = 'astbtc' 
		price_bids_b_l_astbtc = data['tick']['bid'] 
		qty_bids_b_l_astbtc = data['tick']['bidSize']
		price_asks_b_l_astbtc = data['tick']['ask'] 
		qty_asks_b_l_astbtc = data['tick']['askSize'] 

		global symbol_b_g_astbtc 
		global price_bids_b_g_astbtc 
		global qty_bids_b_g_astbtc 
		global price_asks_b_g_astbtc 
		global qty_asks_b_g_astbtc 

		symbol_b_g_astbtc = symbol_b_l_astbtc 
		price_bids_b_g_astbtc = price_bids_b_l_astbtc 
		qty_bids_b_g_astbtc = qty_bids_b_l_astbtc 
		price_asks_b_g_astbtc = price_asks_b_l_astbtc 
		qty_asks_b_g_astbtc = qty_asks_b_l_astbtc 


def on_close_astbtc(ws): 
	print('### closed ###') 

def on_error_astbtc(ws, message): 
	print(message) 

def on_open_astbtc(ws): 
	ws.send(json.dumps({'sub': f'market.astbtc.ticker'})) 

def loop_astbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_astbtc, 
		on_close=on_close_astbtc, 
		on_error=on_error_astbtc) 
	ws.on_open = on_open_astbtc 
	ws.run_forever() 

Thread(target=loop_astbtc).start() 

def loop_astusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_astusdt != 0.0 and qty_bids_a_g_astusdt != 0.0 and price_asks_a_g_astusdt != 0.0 and qty_asks_a_g_astusdt != 0.0 and price_bids_b_g_astbtc != 0.0 and qty_bids_b_g_astbtc != 0.0 and price_asks_b_g_astbtc != 0.0 and qty_asks_b_g_astbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_astusdt) 
			price_b = float(price_bids_b_g_astbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_astbtc, pribil)

Thread(target=loop_astusdt_Trade).start() 

symbol_a_g_achusdt = 'achusdt' 
price_bids_a_g_achusdt = float(0.0) 
qty_bids_a_g_achusdt = float(0.0) 
price_asks_a_g_achusdt = float(0.0) 
qty_asks_a_g_achusdt = float(0.0) 

def on_message_achusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_achusdt = 'achusdt' 
		price_bids_a_l_achusdt = data['tick']['bid'] 
		qty_bids_a_l_achusdt = data['tick']['bidSize'] 
		price_asks_a_l_achusdt = data['tick']['ask'] 
		qty_asks_a_l_achusdt = data['tick']['askSize'] 

		global symbol_a_g_achusdt 
		global price_bids_a_g_achusdt 
		global qty_bids_a_g_achusdt 
		global price_asks_a_g_achusdt 
		global qty_asks_a_g_achusdt 

		symbol_a_g_achusdt = symbol_a_l_achusdt 
		price_bids_a_g_achusdt = price_bids_a_l_achusdt 
		qty_bids_a_g_achusdt = qty_bids_a_l_achusdt 
		price_asks_a_g_achusdt = price_asks_a_l_achusdt 
		qty_asks_a_g_achusdt = qty_asks_a_l_achusdt 

def on_close_achusdt(ws): 
	print('### closed ###') 

def on_error_achusdt(ws, message): 
	print(message) 

def on_open_achusdt(ws): 
	ws.send(json.dumps({'sub': f'market.achusdt.ticker'})) 

def loop_achusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_achusdt, 
		on_close=on_close_achusdt, 
		on_error=on_error_achusdt) 
	ws.on_open = on_open_achusdt 
	ws.run_forever() 

Thread(target=loop_achusdt).start() 

symbol_b_g_achbtc = 'achbtc' 
price_bids_b_g_achbtc = float(0.0) 
qty_bids_b_g_achbtc = float(0.0) 
price_asks_b_g_achbtc = float(0.0) 
qty_asks_b_g_achbtc = float(0.0) 

def on_message_achbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_achbtc = 'achbtc' 
		price_bids_b_l_achbtc = data['tick']['bid'] 
		qty_bids_b_l_achbtc = data['tick']['bidSize']
		price_asks_b_l_achbtc = data['tick']['ask'] 
		qty_asks_b_l_achbtc = data['tick']['askSize'] 

		global symbol_b_g_achbtc 
		global price_bids_b_g_achbtc 
		global qty_bids_b_g_achbtc 
		global price_asks_b_g_achbtc 
		global qty_asks_b_g_achbtc 

		symbol_b_g_achbtc = symbol_b_l_achbtc 
		price_bids_b_g_achbtc = price_bids_b_l_achbtc 
		qty_bids_b_g_achbtc = qty_bids_b_l_achbtc 
		price_asks_b_g_achbtc = price_asks_b_l_achbtc 
		qty_asks_b_g_achbtc = qty_asks_b_l_achbtc 


def on_close_achbtc(ws): 
	print('### closed ###') 

def on_error_achbtc(ws, message): 
	print(message) 

def on_open_achbtc(ws): 
	ws.send(json.dumps({'sub': f'market.achbtc.ticker'})) 

def loop_achbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_achbtc, 
		on_close=on_close_achbtc, 
		on_error=on_error_achbtc) 
	ws.on_open = on_open_achbtc 
	ws.run_forever() 

Thread(target=loop_achbtc).start() 

def loop_achusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_achusdt != 0.0 and qty_bids_a_g_achusdt != 0.0 and price_asks_a_g_achusdt != 0.0 and qty_asks_a_g_achusdt != 0.0 and price_bids_b_g_achbtc != 0.0 and qty_bids_b_g_achbtc != 0.0 and price_asks_b_g_achbtc != 0.0 and qty_asks_b_g_achbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_achusdt) 
			price_b = float(price_bids_b_g_achbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_achbtc, pribil)

Thread(target=loop_achusdt_Trade).start() 

symbol_a_g_ftmusdt = 'ftmusdt' 
price_bids_a_g_ftmusdt = float(0.0) 
qty_bids_a_g_ftmusdt = float(0.0) 
price_asks_a_g_ftmusdt = float(0.0) 
qty_asks_a_g_ftmusdt = float(0.0) 

def on_message_ftmusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ftmusdt = 'ftmusdt' 
		price_bids_a_l_ftmusdt = data['tick']['bid'] 
		qty_bids_a_l_ftmusdt = data['tick']['bidSize'] 
		price_asks_a_l_ftmusdt = data['tick']['ask'] 
		qty_asks_a_l_ftmusdt = data['tick']['askSize'] 

		global symbol_a_g_ftmusdt 
		global price_bids_a_g_ftmusdt 
		global qty_bids_a_g_ftmusdt 
		global price_asks_a_g_ftmusdt 
		global qty_asks_a_g_ftmusdt 

		symbol_a_g_ftmusdt = symbol_a_l_ftmusdt 
		price_bids_a_g_ftmusdt = price_bids_a_l_ftmusdt 
		qty_bids_a_g_ftmusdt = qty_bids_a_l_ftmusdt 
		price_asks_a_g_ftmusdt = price_asks_a_l_ftmusdt 
		qty_asks_a_g_ftmusdt = qty_asks_a_l_ftmusdt 

def on_close_ftmusdt(ws): 
	print('### closed ###') 

def on_error_ftmusdt(ws, message): 
	print(message) 

def on_open_ftmusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ftmusdt.ticker'})) 

def loop_ftmusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ftmusdt, 
		on_close=on_close_ftmusdt, 
		on_error=on_error_ftmusdt) 
	ws.on_open = on_open_ftmusdt 
	ws.run_forever() 

Thread(target=loop_ftmusdt).start() 

symbol_b_g_ftmusdc = 'ftmusdc' 
price_bids_b_g_ftmusdc = float(0.0) 
qty_bids_b_g_ftmusdc = float(0.0) 
price_asks_b_g_ftmusdc = float(0.0) 
qty_asks_b_g_ftmusdc = float(0.0) 

def on_message_ftmusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ftmusdc = 'ftmusdc' 
		price_bids_b_l_ftmusdc = data['tick']['bid'] 
		qty_bids_b_l_ftmusdc = data['tick']['bidSize']
		price_asks_b_l_ftmusdc = data['tick']['ask'] 
		qty_asks_b_l_ftmusdc = data['tick']['askSize'] 

		global symbol_b_g_ftmusdc 
		global price_bids_b_g_ftmusdc 
		global qty_bids_b_g_ftmusdc 
		global price_asks_b_g_ftmusdc 
		global qty_asks_b_g_ftmusdc 

		symbol_b_g_ftmusdc = symbol_b_l_ftmusdc 
		price_bids_b_g_ftmusdc = price_bids_b_l_ftmusdc 
		qty_bids_b_g_ftmusdc = qty_bids_b_l_ftmusdc 
		price_asks_b_g_ftmusdc = price_asks_b_l_ftmusdc 
		qty_asks_b_g_ftmusdc = qty_asks_b_l_ftmusdc 


def on_close_ftmusdc(ws): 
	print('### closed ###') 

def on_error_ftmusdc(ws, message): 
	print(message) 

def on_open_ftmusdc(ws): 
	ws.send(json.dumps({'sub': f'market.ftmusdc.ticker'})) 

def loop_ftmusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ftmusdc, 
		on_close=on_close_ftmusdc, 
		on_error=on_error_ftmusdc) 
	ws.on_open = on_open_ftmusdc 
	ws.run_forever() 

Thread(target=loop_ftmusdc).start() 

def loop_ftmusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_ftmusdt != 0.0 and qty_bids_a_g_ftmusdt != 0.0 and price_asks_a_g_ftmusdt != 0.0 and qty_asks_a_g_ftmusdt != 0.0 and price_bids_b_g_ftmusdc != 0.0 and qty_bids_b_g_ftmusdc != 0.0 and price_asks_b_g_ftmusdc != 0.0 and qty_asks_b_g_ftmusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ftmusdt) 
			price_b = float(price_bids_b_g_ftmusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ftmusdc, pribil)

Thread(target=loop_ftmusdt_Trade).start() 

symbol_a_g_storjusdt = 'storjusdt' 
price_bids_a_g_storjusdt = float(0.0) 
qty_bids_a_g_storjusdt = float(0.0) 
price_asks_a_g_storjusdt = float(0.0) 
qty_asks_a_g_storjusdt = float(0.0) 

def on_message_storjusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_storjusdt = 'storjusdt' 
		price_bids_a_l_storjusdt = data['tick']['bid'] 
		qty_bids_a_l_storjusdt = data['tick']['bidSize'] 
		price_asks_a_l_storjusdt = data['tick']['ask'] 
		qty_asks_a_l_storjusdt = data['tick']['askSize'] 

		global symbol_a_g_storjusdt 
		global price_bids_a_g_storjusdt 
		global qty_bids_a_g_storjusdt 
		global price_asks_a_g_storjusdt 
		global qty_asks_a_g_storjusdt 

		symbol_a_g_storjusdt = symbol_a_l_storjusdt 
		price_bids_a_g_storjusdt = price_bids_a_l_storjusdt 
		qty_bids_a_g_storjusdt = qty_bids_a_l_storjusdt 
		price_asks_a_g_storjusdt = price_asks_a_l_storjusdt 
		qty_asks_a_g_storjusdt = qty_asks_a_l_storjusdt 

def on_close_storjusdt(ws): 
	print('### closed ###') 

def on_error_storjusdt(ws, message): 
	print(message) 

def on_open_storjusdt(ws): 
	ws.send(json.dumps({'sub': f'market.storjusdt.ticker'})) 

def loop_storjusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_storjusdt, 
		on_close=on_close_storjusdt, 
		on_error=on_error_storjusdt) 
	ws.on_open = on_open_storjusdt 
	ws.run_forever() 

Thread(target=loop_storjusdt).start() 

symbol_b_g_storjbtc = 'storjbtc' 
price_bids_b_g_storjbtc = float(0.0) 
qty_bids_b_g_storjbtc = float(0.0) 
price_asks_b_g_storjbtc = float(0.0) 
qty_asks_b_g_storjbtc = float(0.0) 

def on_message_storjbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_storjbtc = 'storjbtc' 
		price_bids_b_l_storjbtc = data['tick']['bid'] 
		qty_bids_b_l_storjbtc = data['tick']['bidSize']
		price_asks_b_l_storjbtc = data['tick']['ask'] 
		qty_asks_b_l_storjbtc = data['tick']['askSize'] 

		global symbol_b_g_storjbtc 
		global price_bids_b_g_storjbtc 
		global qty_bids_b_g_storjbtc 
		global price_asks_b_g_storjbtc 
		global qty_asks_b_g_storjbtc 

		symbol_b_g_storjbtc = symbol_b_l_storjbtc 
		price_bids_b_g_storjbtc = price_bids_b_l_storjbtc 
		qty_bids_b_g_storjbtc = qty_bids_b_l_storjbtc 
		price_asks_b_g_storjbtc = price_asks_b_l_storjbtc 
		qty_asks_b_g_storjbtc = qty_asks_b_l_storjbtc 


def on_close_storjbtc(ws): 
	print('### closed ###') 

def on_error_storjbtc(ws, message): 
	print(message) 

def on_open_storjbtc(ws): 
	ws.send(json.dumps({'sub': f'market.storjbtc.ticker'})) 

def loop_storjbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_storjbtc, 
		on_close=on_close_storjbtc, 
		on_error=on_error_storjbtc) 
	ws.on_open = on_open_storjbtc 
	ws.run_forever() 

Thread(target=loop_storjbtc).start() 

def loop_storjusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_storjusdt != 0.0 and qty_bids_a_g_storjusdt != 0.0 and price_asks_a_g_storjusdt != 0.0 and qty_asks_a_g_storjusdt != 0.0 and price_bids_b_g_storjbtc != 0.0 and qty_bids_b_g_storjbtc != 0.0 and price_asks_b_g_storjbtc != 0.0 and qty_asks_b_g_storjbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_storjusdt) 
			price_b = float(price_bids_b_g_storjbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_storjbtc, pribil)

Thread(target=loop_storjusdt_Trade).start() 

symbol_a_g_wtcusdt = 'wtcusdt' 
price_bids_a_g_wtcusdt = float(0.0) 
qty_bids_a_g_wtcusdt = float(0.0) 
price_asks_a_g_wtcusdt = float(0.0) 
qty_asks_a_g_wtcusdt = float(0.0) 

def on_message_wtcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_wtcusdt = 'wtcusdt' 
		price_bids_a_l_wtcusdt = data['tick']['bid'] 
		qty_bids_a_l_wtcusdt = data['tick']['bidSize'] 
		price_asks_a_l_wtcusdt = data['tick']['ask'] 
		qty_asks_a_l_wtcusdt = data['tick']['askSize'] 

		global symbol_a_g_wtcusdt 
		global price_bids_a_g_wtcusdt 
		global qty_bids_a_g_wtcusdt 
		global price_asks_a_g_wtcusdt 
		global qty_asks_a_g_wtcusdt 

		symbol_a_g_wtcusdt = symbol_a_l_wtcusdt 
		price_bids_a_g_wtcusdt = price_bids_a_l_wtcusdt 
		qty_bids_a_g_wtcusdt = qty_bids_a_l_wtcusdt 
		price_asks_a_g_wtcusdt = price_asks_a_l_wtcusdt 
		qty_asks_a_g_wtcusdt = qty_asks_a_l_wtcusdt 

def on_close_wtcusdt(ws): 
	print('### closed ###') 

def on_error_wtcusdt(ws, message): 
	print(message) 

def on_open_wtcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.wtcusdt.ticker'})) 

def loop_wtcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wtcusdt, 
		on_close=on_close_wtcusdt, 
		on_error=on_error_wtcusdt) 
	ws.on_open = on_open_wtcusdt 
	ws.run_forever() 

Thread(target=loop_wtcusdt).start() 

symbol_b_g_wtceth = 'wtceth' 
price_bids_b_g_wtceth = float(0.0) 
qty_bids_b_g_wtceth = float(0.0) 
price_asks_b_g_wtceth = float(0.0) 
qty_asks_b_g_wtceth = float(0.0) 

def on_message_wtceth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_wtceth = 'wtceth' 
		price_bids_b_l_wtceth = data['tick']['bid'] 
		qty_bids_b_l_wtceth = data['tick']['bidSize']
		price_asks_b_l_wtceth = data['tick']['ask'] 
		qty_asks_b_l_wtceth = data['tick']['askSize'] 

		global symbol_b_g_wtceth 
		global price_bids_b_g_wtceth 
		global qty_bids_b_g_wtceth 
		global price_asks_b_g_wtceth 
		global qty_asks_b_g_wtceth 

		symbol_b_g_wtceth = symbol_b_l_wtceth 
		price_bids_b_g_wtceth = price_bids_b_l_wtceth 
		qty_bids_b_g_wtceth = qty_bids_b_l_wtceth 
		price_asks_b_g_wtceth = price_asks_b_l_wtceth 
		qty_asks_b_g_wtceth = qty_asks_b_l_wtceth 


def on_close_wtceth(ws): 
	print('### closed ###') 

def on_error_wtceth(ws, message): 
	print(message) 

def on_open_wtceth(ws): 
	ws.send(json.dumps({'sub': f'market.wtceth.ticker'})) 

def loop_wtceth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wtceth, 
		on_close=on_close_wtceth, 
		on_error=on_error_wtceth) 
	ws.on_open = on_open_wtceth 
	ws.run_forever() 

Thread(target=loop_wtceth).start() 

def loop_wtcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_wtcusdt != 0.0 and qty_bids_a_g_wtcusdt != 0.0 and price_asks_a_g_wtcusdt != 0.0 and qty_asks_a_g_wtcusdt != 0.0 and price_bids_b_g_wtceth != 0.0 and qty_bids_b_g_wtceth != 0.0 and price_asks_b_g_wtceth != 0.0 and qty_asks_b_g_wtceth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_wtcusdt) 
			price_b = float(price_bids_b_g_wtceth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_wtceth, pribil)

Thread(target=loop_wtcusdt_Trade).start() 

symbol_a_g_fttusdt = 'fttusdt' 
price_bids_a_g_fttusdt = float(0.0) 
qty_bids_a_g_fttusdt = float(0.0) 
price_asks_a_g_fttusdt = float(0.0) 
qty_asks_a_g_fttusdt = float(0.0) 

def on_message_fttusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_fttusdt = 'fttusdt' 
		price_bids_a_l_fttusdt = data['tick']['bid'] 
		qty_bids_a_l_fttusdt = data['tick']['bidSize'] 
		price_asks_a_l_fttusdt = data['tick']['ask'] 
		qty_asks_a_l_fttusdt = data['tick']['askSize'] 

		global symbol_a_g_fttusdt 
		global price_bids_a_g_fttusdt 
		global qty_bids_a_g_fttusdt 
		global price_asks_a_g_fttusdt 
		global qty_asks_a_g_fttusdt 

		symbol_a_g_fttusdt = symbol_a_l_fttusdt 
		price_bids_a_g_fttusdt = price_bids_a_l_fttusdt 
		qty_bids_a_g_fttusdt = qty_bids_a_l_fttusdt 
		price_asks_a_g_fttusdt = price_asks_a_l_fttusdt 
		qty_asks_a_g_fttusdt = qty_asks_a_l_fttusdt 

def on_close_fttusdt(ws): 
	print('### closed ###') 

def on_error_fttusdt(ws, message): 
	print(message) 

def on_open_fttusdt(ws): 
	ws.send(json.dumps({'sub': f'market.fttusdt.ticker'})) 

def loop_fttusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_fttusdt, 
		on_close=on_close_fttusdt, 
		on_error=on_error_fttusdt) 
	ws.on_open = on_open_fttusdt 
	ws.run_forever() 

Thread(target=loop_fttusdt).start() 

symbol_b_g_fttusdd = 'fttusdd' 
price_bids_b_g_fttusdd = float(0.0) 
qty_bids_b_g_fttusdd = float(0.0) 
price_asks_b_g_fttusdd = float(0.0) 
qty_asks_b_g_fttusdd = float(0.0) 

def on_message_fttusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_fttusdd = 'fttusdd' 
		price_bids_b_l_fttusdd = data['tick']['bid'] 
		qty_bids_b_l_fttusdd = data['tick']['bidSize']
		price_asks_b_l_fttusdd = data['tick']['ask'] 
		qty_asks_b_l_fttusdd = data['tick']['askSize'] 

		global symbol_b_g_fttusdd 
		global price_bids_b_g_fttusdd 
		global qty_bids_b_g_fttusdd 
		global price_asks_b_g_fttusdd 
		global qty_asks_b_g_fttusdd 

		symbol_b_g_fttusdd = symbol_b_l_fttusdd 
		price_bids_b_g_fttusdd = price_bids_b_l_fttusdd 
		qty_bids_b_g_fttusdd = qty_bids_b_l_fttusdd 
		price_asks_b_g_fttusdd = price_asks_b_l_fttusdd 
		qty_asks_b_g_fttusdd = qty_asks_b_l_fttusdd 


def on_close_fttusdd(ws): 
	print('### closed ###') 

def on_error_fttusdd(ws, message): 
	print(message) 

def on_open_fttusdd(ws): 
	ws.send(json.dumps({'sub': f'market.fttusdd.ticker'})) 

def loop_fttusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_fttusdd, 
		on_close=on_close_fttusdd, 
		on_error=on_error_fttusdd) 
	ws.on_open = on_open_fttusdd 
	ws.run_forever() 

Thread(target=loop_fttusdd).start() 

def loop_fttusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_fttusdt != 0.0 and qty_bids_a_g_fttusdt != 0.0 and price_asks_a_g_fttusdt != 0.0 and qty_asks_a_g_fttusdt != 0.0 and price_bids_b_g_fttusdd != 0.0 and qty_bids_b_g_fttusdd != 0.0 and price_asks_b_g_fttusdd != 0.0 and qty_asks_b_g_fttusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_fttusdt) 
			price_b = float(price_bids_b_g_fttusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_fttusdd, pribil)

Thread(target=loop_fttusdt_Trade).start() 

symbol_a_g_trxusdt = 'trxusdt' 
price_bids_a_g_trxusdt = float(0.0) 
qty_bids_a_g_trxusdt = float(0.0) 
price_asks_a_g_trxusdt = float(0.0) 
qty_asks_a_g_trxusdt = float(0.0) 

def on_message_trxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_trxusdt = 'trxusdt' 
		price_bids_a_l_trxusdt = data['tick']['bid'] 
		qty_bids_a_l_trxusdt = data['tick']['bidSize'] 
		price_asks_a_l_trxusdt = data['tick']['ask'] 
		qty_asks_a_l_trxusdt = data['tick']['askSize'] 

		global symbol_a_g_trxusdt 
		global price_bids_a_g_trxusdt 
		global qty_bids_a_g_trxusdt 
		global price_asks_a_g_trxusdt 
		global qty_asks_a_g_trxusdt 

		symbol_a_g_trxusdt = symbol_a_l_trxusdt 
		price_bids_a_g_trxusdt = price_bids_a_l_trxusdt 
		qty_bids_a_g_trxusdt = qty_bids_a_l_trxusdt 
		price_asks_a_g_trxusdt = price_asks_a_l_trxusdt 
		qty_asks_a_g_trxusdt = qty_asks_a_l_trxusdt 

def on_close_trxusdt(ws): 
	print('### closed ###') 

def on_error_trxusdt(ws, message): 
	print(message) 

def on_open_trxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.trxusdt.ticker'})) 

def loop_trxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_trxusdt, 
		on_close=on_close_trxusdt, 
		on_error=on_error_trxusdt) 
	ws.on_open = on_open_trxusdt 
	ws.run_forever() 

Thread(target=loop_trxusdt).start() 

symbol_b_g_trxeth = 'trxeth' 
price_bids_b_g_trxeth = float(0.0) 
qty_bids_b_g_trxeth = float(0.0) 
price_asks_b_g_trxeth = float(0.0) 
qty_asks_b_g_trxeth = float(0.0) 

def on_message_trxeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_trxeth = 'trxeth' 
		price_bids_b_l_trxeth = data['tick']['bid'] 
		qty_bids_b_l_trxeth = data['tick']['bidSize']
		price_asks_b_l_trxeth = data['tick']['ask'] 
		qty_asks_b_l_trxeth = data['tick']['askSize'] 

		global symbol_b_g_trxeth 
		global price_bids_b_g_trxeth 
		global qty_bids_b_g_trxeth 
		global price_asks_b_g_trxeth 
		global qty_asks_b_g_trxeth 

		symbol_b_g_trxeth = symbol_b_l_trxeth 
		price_bids_b_g_trxeth = price_bids_b_l_trxeth 
		qty_bids_b_g_trxeth = qty_bids_b_l_trxeth 
		price_asks_b_g_trxeth = price_asks_b_l_trxeth 
		qty_asks_b_g_trxeth = qty_asks_b_l_trxeth 


def on_close_trxeth(ws): 
	print('### closed ###') 

def on_error_trxeth(ws, message): 
	print(message) 

def on_open_trxeth(ws): 
	ws.send(json.dumps({'sub': f'market.trxeth.ticker'})) 

def loop_trxeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_trxeth, 
		on_close=on_close_trxeth, 
		on_error=on_error_trxeth) 
	ws.on_open = on_open_trxeth 
	ws.run_forever() 

Thread(target=loop_trxeth).start() 

def loop_trxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_trxusdt != 0.0 and qty_bids_a_g_trxusdt != 0.0 and price_asks_a_g_trxusdt != 0.0 and qty_asks_a_g_trxusdt != 0.0 and price_bids_b_g_trxeth != 0.0 and qty_bids_b_g_trxeth != 0.0 and price_asks_b_g_trxeth != 0.0 and qty_asks_b_g_trxeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_trxusdt) 
			price_b = float(price_bids_b_g_trxeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_trxeth, pribil)

Thread(target=loop_trxusdt_Trade).start() 

symbol_a_g_utkusdt = 'utkusdt' 
price_bids_a_g_utkusdt = float(0.0) 
qty_bids_a_g_utkusdt = float(0.0) 
price_asks_a_g_utkusdt = float(0.0) 
qty_asks_a_g_utkusdt = float(0.0) 

def on_message_utkusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_utkusdt = 'utkusdt' 
		price_bids_a_l_utkusdt = data['tick']['bid'] 
		qty_bids_a_l_utkusdt = data['tick']['bidSize'] 
		price_asks_a_l_utkusdt = data['tick']['ask'] 
		qty_asks_a_l_utkusdt = data['tick']['askSize'] 

		global symbol_a_g_utkusdt 
		global price_bids_a_g_utkusdt 
		global qty_bids_a_g_utkusdt 
		global price_asks_a_g_utkusdt 
		global qty_asks_a_g_utkusdt 

		symbol_a_g_utkusdt = symbol_a_l_utkusdt 
		price_bids_a_g_utkusdt = price_bids_a_l_utkusdt 
		qty_bids_a_g_utkusdt = qty_bids_a_l_utkusdt 
		price_asks_a_g_utkusdt = price_asks_a_l_utkusdt 
		qty_asks_a_g_utkusdt = qty_asks_a_l_utkusdt 

def on_close_utkusdt(ws): 
	print('### closed ###') 

def on_error_utkusdt(ws, message): 
	print(message) 

def on_open_utkusdt(ws): 
	ws.send(json.dumps({'sub': f'market.utkusdt.ticker'})) 

def loop_utkusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_utkusdt, 
		on_close=on_close_utkusdt, 
		on_error=on_error_utkusdt) 
	ws.on_open = on_open_utkusdt 
	ws.run_forever() 

Thread(target=loop_utkusdt).start() 

symbol_b_g_utkbtc = 'utkbtc' 
price_bids_b_g_utkbtc = float(0.0) 
qty_bids_b_g_utkbtc = float(0.0) 
price_asks_b_g_utkbtc = float(0.0) 
qty_asks_b_g_utkbtc = float(0.0) 

def on_message_utkbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_utkbtc = 'utkbtc' 
		price_bids_b_l_utkbtc = data['tick']['bid'] 
		qty_bids_b_l_utkbtc = data['tick']['bidSize']
		price_asks_b_l_utkbtc = data['tick']['ask'] 
		qty_asks_b_l_utkbtc = data['tick']['askSize'] 

		global symbol_b_g_utkbtc 
		global price_bids_b_g_utkbtc 
		global qty_bids_b_g_utkbtc 
		global price_asks_b_g_utkbtc 
		global qty_asks_b_g_utkbtc 

		symbol_b_g_utkbtc = symbol_b_l_utkbtc 
		price_bids_b_g_utkbtc = price_bids_b_l_utkbtc 
		qty_bids_b_g_utkbtc = qty_bids_b_l_utkbtc 
		price_asks_b_g_utkbtc = price_asks_b_l_utkbtc 
		qty_asks_b_g_utkbtc = qty_asks_b_l_utkbtc 


def on_close_utkbtc(ws): 
	print('### closed ###') 

def on_error_utkbtc(ws, message): 
	print(message) 

def on_open_utkbtc(ws): 
	ws.send(json.dumps({'sub': f'market.utkbtc.ticker'})) 

def loop_utkbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_utkbtc, 
		on_close=on_close_utkbtc, 
		on_error=on_error_utkbtc) 
	ws.on_open = on_open_utkbtc 
	ws.run_forever() 

Thread(target=loop_utkbtc).start() 

def loop_utkusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_utkusdt != 0.0 and qty_bids_a_g_utkusdt != 0.0 and price_asks_a_g_utkusdt != 0.0 and qty_asks_a_g_utkusdt != 0.0 and price_bids_b_g_utkbtc != 0.0 and qty_bids_b_g_utkbtc != 0.0 and price_asks_b_g_utkbtc != 0.0 and qty_asks_b_g_utkbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_utkusdt) 
			price_b = float(price_bids_b_g_utkbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_utkbtc, pribil)

Thread(target=loop_utkusdt_Trade).start() 

symbol_a_g_icxusdt = 'icxusdt' 
price_bids_a_g_icxusdt = float(0.0) 
qty_bids_a_g_icxusdt = float(0.0) 
price_asks_a_g_icxusdt = float(0.0) 
qty_asks_a_g_icxusdt = float(0.0) 

def on_message_icxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_icxusdt = 'icxusdt' 
		price_bids_a_l_icxusdt = data['tick']['bid'] 
		qty_bids_a_l_icxusdt = data['tick']['bidSize'] 
		price_asks_a_l_icxusdt = data['tick']['ask'] 
		qty_asks_a_l_icxusdt = data['tick']['askSize'] 

		global symbol_a_g_icxusdt 
		global price_bids_a_g_icxusdt 
		global qty_bids_a_g_icxusdt 
		global price_asks_a_g_icxusdt 
		global qty_asks_a_g_icxusdt 

		symbol_a_g_icxusdt = symbol_a_l_icxusdt 
		price_bids_a_g_icxusdt = price_bids_a_l_icxusdt 
		qty_bids_a_g_icxusdt = qty_bids_a_l_icxusdt 
		price_asks_a_g_icxusdt = price_asks_a_l_icxusdt 
		qty_asks_a_g_icxusdt = qty_asks_a_l_icxusdt 

def on_close_icxusdt(ws): 
	print('### closed ###') 

def on_error_icxusdt(ws, message): 
	print(message) 

def on_open_icxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.icxusdt.ticker'})) 

def loop_icxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_icxusdt, 
		on_close=on_close_icxusdt, 
		on_error=on_error_icxusdt) 
	ws.on_open = on_open_icxusdt 
	ws.run_forever() 

Thread(target=loop_icxusdt).start() 

symbol_b_g_icxbtc = 'icxbtc' 
price_bids_b_g_icxbtc = float(0.0) 
qty_bids_b_g_icxbtc = float(0.0) 
price_asks_b_g_icxbtc = float(0.0) 
qty_asks_b_g_icxbtc = float(0.0) 

def on_message_icxbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_icxbtc = 'icxbtc' 
		price_bids_b_l_icxbtc = data['tick']['bid'] 
		qty_bids_b_l_icxbtc = data['tick']['bidSize']
		price_asks_b_l_icxbtc = data['tick']['ask'] 
		qty_asks_b_l_icxbtc = data['tick']['askSize'] 

		global symbol_b_g_icxbtc 
		global price_bids_b_g_icxbtc 
		global qty_bids_b_g_icxbtc 
		global price_asks_b_g_icxbtc 
		global qty_asks_b_g_icxbtc 

		symbol_b_g_icxbtc = symbol_b_l_icxbtc 
		price_bids_b_g_icxbtc = price_bids_b_l_icxbtc 
		qty_bids_b_g_icxbtc = qty_bids_b_l_icxbtc 
		price_asks_b_g_icxbtc = price_asks_b_l_icxbtc 
		qty_asks_b_g_icxbtc = qty_asks_b_l_icxbtc 


def on_close_icxbtc(ws): 
	print('### closed ###') 

def on_error_icxbtc(ws, message): 
	print(message) 

def on_open_icxbtc(ws): 
	ws.send(json.dumps({'sub': f'market.icxbtc.ticker'})) 

def loop_icxbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_icxbtc, 
		on_close=on_close_icxbtc, 
		on_error=on_error_icxbtc) 
	ws.on_open = on_open_icxbtc 
	ws.run_forever() 

Thread(target=loop_icxbtc).start() 

def loop_icxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_icxusdt != 0.0 and qty_bids_a_g_icxusdt != 0.0 and price_asks_a_g_icxusdt != 0.0 and qty_asks_a_g_icxusdt != 0.0 and price_bids_b_g_icxbtc != 0.0 and qty_bids_b_g_icxbtc != 0.0 and price_asks_b_g_icxbtc != 0.0 and qty_asks_b_g_icxbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_icxusdt) 
			price_b = float(price_bids_b_g_icxbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_icxbtc, pribil)

Thread(target=loop_icxusdt_Trade).start() 

symbol_a_g_pundixusdt = 'pundixusdt' 
price_bids_a_g_pundixusdt = float(0.0) 
qty_bids_a_g_pundixusdt = float(0.0) 
price_asks_a_g_pundixusdt = float(0.0) 
qty_asks_a_g_pundixusdt = float(0.0) 

def on_message_pundixusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_pundixusdt = 'pundixusdt' 
		price_bids_a_l_pundixusdt = data['tick']['bid'] 
		qty_bids_a_l_pundixusdt = data['tick']['bidSize'] 
		price_asks_a_l_pundixusdt = data['tick']['ask'] 
		qty_asks_a_l_pundixusdt = data['tick']['askSize'] 

		global symbol_a_g_pundixusdt 
		global price_bids_a_g_pundixusdt 
		global qty_bids_a_g_pundixusdt 
		global price_asks_a_g_pundixusdt 
		global qty_asks_a_g_pundixusdt 

		symbol_a_g_pundixusdt = symbol_a_l_pundixusdt 
		price_bids_a_g_pundixusdt = price_bids_a_l_pundixusdt 
		qty_bids_a_g_pundixusdt = qty_bids_a_l_pundixusdt 
		price_asks_a_g_pundixusdt = price_asks_a_l_pundixusdt 
		qty_asks_a_g_pundixusdt = qty_asks_a_l_pundixusdt 

def on_close_pundixusdt(ws): 
	print('### closed ###') 

def on_error_pundixusdt(ws, message): 
	print(message) 

def on_open_pundixusdt(ws): 
	ws.send(json.dumps({'sub': f'market.pundixusdt.ticker'})) 

def loop_pundixusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_pundixusdt, 
		on_close=on_close_pundixusdt, 
		on_error=on_error_pundixusdt) 
	ws.on_open = on_open_pundixusdt 
	ws.run_forever() 

Thread(target=loop_pundixusdt).start() 

symbol_b_g_pundixbtc = 'pundixbtc' 
price_bids_b_g_pundixbtc = float(0.0) 
qty_bids_b_g_pundixbtc = float(0.0) 
price_asks_b_g_pundixbtc = float(0.0) 
qty_asks_b_g_pundixbtc = float(0.0) 

def on_message_pundixbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_pundixbtc = 'pundixbtc' 
		price_bids_b_l_pundixbtc = data['tick']['bid'] 
		qty_bids_b_l_pundixbtc = data['tick']['bidSize']
		price_asks_b_l_pundixbtc = data['tick']['ask'] 
		qty_asks_b_l_pundixbtc = data['tick']['askSize'] 

		global symbol_b_g_pundixbtc 
		global price_bids_b_g_pundixbtc 
		global qty_bids_b_g_pundixbtc 
		global price_asks_b_g_pundixbtc 
		global qty_asks_b_g_pundixbtc 

		symbol_b_g_pundixbtc = symbol_b_l_pundixbtc 
		price_bids_b_g_pundixbtc = price_bids_b_l_pundixbtc 
		qty_bids_b_g_pundixbtc = qty_bids_b_l_pundixbtc 
		price_asks_b_g_pundixbtc = price_asks_b_l_pundixbtc 
		qty_asks_b_g_pundixbtc = qty_asks_b_l_pundixbtc 


def on_close_pundixbtc(ws): 
	print('### closed ###') 

def on_error_pundixbtc(ws, message): 
	print(message) 

def on_open_pundixbtc(ws): 
	ws.send(json.dumps({'sub': f'market.pundixbtc.ticker'})) 

def loop_pundixbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_pundixbtc, 
		on_close=on_close_pundixbtc, 
		on_error=on_error_pundixbtc) 
	ws.on_open = on_open_pundixbtc 
	ws.run_forever() 

Thread(target=loop_pundixbtc).start() 

def loop_pundixusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_pundixusdt != 0.0 and qty_bids_a_g_pundixusdt != 0.0 and price_asks_a_g_pundixusdt != 0.0 and qty_asks_a_g_pundixusdt != 0.0 and price_bids_b_g_pundixbtc != 0.0 and qty_bids_b_g_pundixbtc != 0.0 and price_asks_b_g_pundixbtc != 0.0 and qty_asks_b_g_pundixbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_pundixusdt) 
			price_b = float(price_bids_b_g_pundixbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_pundixbtc, pribil)

Thread(target=loop_pundixusdt_Trade).start() 

symbol_a_g_chrusdt = 'chrusdt' 
price_bids_a_g_chrusdt = float(0.0) 
qty_bids_a_g_chrusdt = float(0.0) 
price_asks_a_g_chrusdt = float(0.0) 
qty_asks_a_g_chrusdt = float(0.0) 

def on_message_chrusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_chrusdt = 'chrusdt' 
		price_bids_a_l_chrusdt = data['tick']['bid'] 
		qty_bids_a_l_chrusdt = data['tick']['bidSize'] 
		price_asks_a_l_chrusdt = data['tick']['ask'] 
		qty_asks_a_l_chrusdt = data['tick']['askSize'] 

		global symbol_a_g_chrusdt 
		global price_bids_a_g_chrusdt 
		global qty_bids_a_g_chrusdt 
		global price_asks_a_g_chrusdt 
		global qty_asks_a_g_chrusdt 

		symbol_a_g_chrusdt = symbol_a_l_chrusdt 
		price_bids_a_g_chrusdt = price_bids_a_l_chrusdt 
		qty_bids_a_g_chrusdt = qty_bids_a_l_chrusdt 
		price_asks_a_g_chrusdt = price_asks_a_l_chrusdt 
		qty_asks_a_g_chrusdt = qty_asks_a_l_chrusdt 

def on_close_chrusdt(ws): 
	print('### closed ###') 

def on_error_chrusdt(ws, message): 
	print(message) 

def on_open_chrusdt(ws): 
	ws.send(json.dumps({'sub': f'market.chrusdt.ticker'})) 

def loop_chrusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_chrusdt, 
		on_close=on_close_chrusdt, 
		on_error=on_error_chrusdt) 
	ws.on_open = on_open_chrusdt 
	ws.run_forever() 

Thread(target=loop_chrusdt).start() 

symbol_b_g_chrbtc = 'chrbtc' 
price_bids_b_g_chrbtc = float(0.0) 
qty_bids_b_g_chrbtc = float(0.0) 
price_asks_b_g_chrbtc = float(0.0) 
qty_asks_b_g_chrbtc = float(0.0) 

def on_message_chrbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_chrbtc = 'chrbtc' 
		price_bids_b_l_chrbtc = data['tick']['bid'] 
		qty_bids_b_l_chrbtc = data['tick']['bidSize']
		price_asks_b_l_chrbtc = data['tick']['ask'] 
		qty_asks_b_l_chrbtc = data['tick']['askSize'] 

		global symbol_b_g_chrbtc 
		global price_bids_b_g_chrbtc 
		global qty_bids_b_g_chrbtc 
		global price_asks_b_g_chrbtc 
		global qty_asks_b_g_chrbtc 

		symbol_b_g_chrbtc = symbol_b_l_chrbtc 
		price_bids_b_g_chrbtc = price_bids_b_l_chrbtc 
		qty_bids_b_g_chrbtc = qty_bids_b_l_chrbtc 
		price_asks_b_g_chrbtc = price_asks_b_l_chrbtc 
		qty_asks_b_g_chrbtc = qty_asks_b_l_chrbtc 


def on_close_chrbtc(ws): 
	print('### closed ###') 

def on_error_chrbtc(ws, message): 
	print(message) 

def on_open_chrbtc(ws): 
	ws.send(json.dumps({'sub': f'market.chrbtc.ticker'})) 

def loop_chrbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_chrbtc, 
		on_close=on_close_chrbtc, 
		on_error=on_error_chrbtc) 
	ws.on_open = on_open_chrbtc 
	ws.run_forever() 

Thread(target=loop_chrbtc).start() 

def loop_chrusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_chrusdt != 0.0 and qty_bids_a_g_chrusdt != 0.0 and price_asks_a_g_chrusdt != 0.0 and qty_asks_a_g_chrusdt != 0.0 and price_bids_b_g_chrbtc != 0.0 and qty_bids_b_g_chrbtc != 0.0 and price_asks_b_g_chrbtc != 0.0 and qty_asks_b_g_chrbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_chrusdt) 
			price_b = float(price_bids_b_g_chrbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_chrbtc, pribil)

Thread(target=loop_chrusdt_Trade).start() 

symbol_a_g_linausdt = 'linausdt' 
price_bids_a_g_linausdt = float(0.0) 
qty_bids_a_g_linausdt = float(0.0) 
price_asks_a_g_linausdt = float(0.0) 
qty_asks_a_g_linausdt = float(0.0) 

def on_message_linausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_linausdt = 'linausdt' 
		price_bids_a_l_linausdt = data['tick']['bid'] 
		qty_bids_a_l_linausdt = data['tick']['bidSize'] 
		price_asks_a_l_linausdt = data['tick']['ask'] 
		qty_asks_a_l_linausdt = data['tick']['askSize'] 

		global symbol_a_g_linausdt 
		global price_bids_a_g_linausdt 
		global qty_bids_a_g_linausdt 
		global price_asks_a_g_linausdt 
		global qty_asks_a_g_linausdt 

		symbol_a_g_linausdt = symbol_a_l_linausdt 
		price_bids_a_g_linausdt = price_bids_a_l_linausdt 
		qty_bids_a_g_linausdt = qty_bids_a_l_linausdt 
		price_asks_a_g_linausdt = price_asks_a_l_linausdt 
		qty_asks_a_g_linausdt = qty_asks_a_l_linausdt 

def on_close_linausdt(ws): 
	print('### closed ###') 

def on_error_linausdt(ws, message): 
	print(message) 

def on_open_linausdt(ws): 
	ws.send(json.dumps({'sub': f'market.linausdt.ticker'})) 

def loop_linausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_linausdt, 
		on_close=on_close_linausdt, 
		on_error=on_error_linausdt) 
	ws.on_open = on_open_linausdt 
	ws.run_forever() 

Thread(target=loop_linausdt).start() 

symbol_b_g_linabtc = 'linabtc' 
price_bids_b_g_linabtc = float(0.0) 
qty_bids_b_g_linabtc = float(0.0) 
price_asks_b_g_linabtc = float(0.0) 
qty_asks_b_g_linabtc = float(0.0) 

def on_message_linabtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_linabtc = 'linabtc' 
		price_bids_b_l_linabtc = data['tick']['bid'] 
		qty_bids_b_l_linabtc = data['tick']['bidSize']
		price_asks_b_l_linabtc = data['tick']['ask'] 
		qty_asks_b_l_linabtc = data['tick']['askSize'] 

		global symbol_b_g_linabtc 
		global price_bids_b_g_linabtc 
		global qty_bids_b_g_linabtc 
		global price_asks_b_g_linabtc 
		global qty_asks_b_g_linabtc 

		symbol_b_g_linabtc = symbol_b_l_linabtc 
		price_bids_b_g_linabtc = price_bids_b_l_linabtc 
		qty_bids_b_g_linabtc = qty_bids_b_l_linabtc 
		price_asks_b_g_linabtc = price_asks_b_l_linabtc 
		qty_asks_b_g_linabtc = qty_asks_b_l_linabtc 


def on_close_linabtc(ws): 
	print('### closed ###') 

def on_error_linabtc(ws, message): 
	print(message) 

def on_open_linabtc(ws): 
	ws.send(json.dumps({'sub': f'market.linabtc.ticker'})) 

def loop_linabtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_linabtc, 
		on_close=on_close_linabtc, 
		on_error=on_error_linabtc) 
	ws.on_open = on_open_linabtc 
	ws.run_forever() 

Thread(target=loop_linabtc).start() 

def loop_linausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_linausdt != 0.0 and qty_bids_a_g_linausdt != 0.0 and price_asks_a_g_linausdt != 0.0 and qty_asks_a_g_linausdt != 0.0 and price_bids_b_g_linabtc != 0.0 and qty_bids_b_g_linabtc != 0.0 and price_asks_b_g_linabtc != 0.0 and qty_asks_b_g_linabtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_linausdt) 
			price_b = float(price_bids_b_g_linabtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_linabtc, pribil)

Thread(target=loop_linausdt_Trade).start() 

symbol_a_g_hftusdt = 'hftusdt' 
price_bids_a_g_hftusdt = float(0.0) 
qty_bids_a_g_hftusdt = float(0.0) 
price_asks_a_g_hftusdt = float(0.0) 
qty_asks_a_g_hftusdt = float(0.0) 

def on_message_hftusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_hftusdt = 'hftusdt' 
		price_bids_a_l_hftusdt = data['tick']['bid'] 
		qty_bids_a_l_hftusdt = data['tick']['bidSize'] 
		price_asks_a_l_hftusdt = data['tick']['ask'] 
		qty_asks_a_l_hftusdt = data['tick']['askSize'] 

		global symbol_a_g_hftusdt 
		global price_bids_a_g_hftusdt 
		global qty_bids_a_g_hftusdt 
		global price_asks_a_g_hftusdt 
		global qty_asks_a_g_hftusdt 

		symbol_a_g_hftusdt = symbol_a_l_hftusdt 
		price_bids_a_g_hftusdt = price_bids_a_l_hftusdt 
		qty_bids_a_g_hftusdt = qty_bids_a_l_hftusdt 
		price_asks_a_g_hftusdt = price_asks_a_l_hftusdt 
		qty_asks_a_g_hftusdt = qty_asks_a_l_hftusdt 

def on_close_hftusdt(ws): 
	print('### closed ###') 

def on_error_hftusdt(ws, message): 
	print(message) 

def on_open_hftusdt(ws): 
	ws.send(json.dumps({'sub': f'market.hftusdt.ticker'})) 

def loop_hftusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_hftusdt, 
		on_close=on_close_hftusdt, 
		on_error=on_error_hftusdt) 
	ws.on_open = on_open_hftusdt 
	ws.run_forever() 

Thread(target=loop_hftusdt).start() 

symbol_b_g_hftusdd = 'hftusdd' 
price_bids_b_g_hftusdd = float(0.0) 
qty_bids_b_g_hftusdd = float(0.0) 
price_asks_b_g_hftusdd = float(0.0) 
qty_asks_b_g_hftusdd = float(0.0) 

def on_message_hftusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_hftusdd = 'hftusdd' 
		price_bids_b_l_hftusdd = data['tick']['bid'] 
		qty_bids_b_l_hftusdd = data['tick']['bidSize']
		price_asks_b_l_hftusdd = data['tick']['ask'] 
		qty_asks_b_l_hftusdd = data['tick']['askSize'] 

		global symbol_b_g_hftusdd 
		global price_bids_b_g_hftusdd 
		global qty_bids_b_g_hftusdd 
		global price_asks_b_g_hftusdd 
		global qty_asks_b_g_hftusdd 

		symbol_b_g_hftusdd = symbol_b_l_hftusdd 
		price_bids_b_g_hftusdd = price_bids_b_l_hftusdd 
		qty_bids_b_g_hftusdd = qty_bids_b_l_hftusdd 
		price_asks_b_g_hftusdd = price_asks_b_l_hftusdd 
		qty_asks_b_g_hftusdd = qty_asks_b_l_hftusdd 


def on_close_hftusdd(ws): 
	print('### closed ###') 

def on_error_hftusdd(ws, message): 
	print(message) 

def on_open_hftusdd(ws): 
	ws.send(json.dumps({'sub': f'market.hftusdd.ticker'})) 

def loop_hftusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_hftusdd, 
		on_close=on_close_hftusdd, 
		on_error=on_error_hftusdd) 
	ws.on_open = on_open_hftusdd 
	ws.run_forever() 

Thread(target=loop_hftusdd).start() 

def loop_hftusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_hftusdt != 0.0 and qty_bids_a_g_hftusdt != 0.0 and price_asks_a_g_hftusdt != 0.0 and qty_asks_a_g_hftusdt != 0.0 and price_bids_b_g_hftusdd != 0.0 and qty_bids_b_g_hftusdd != 0.0 and price_asks_b_g_hftusdd != 0.0 and qty_asks_b_g_hftusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_hftusdt) 
			price_b = float(price_bids_b_g_hftusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_hftusdd, pribil)

Thread(target=loop_hftusdt_Trade).start() 

symbol_a_g_compusdt = 'compusdt' 
price_bids_a_g_compusdt = float(0.0) 
qty_bids_a_g_compusdt = float(0.0) 
price_asks_a_g_compusdt = float(0.0) 
qty_asks_a_g_compusdt = float(0.0) 

def on_message_compusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_compusdt = 'compusdt' 
		price_bids_a_l_compusdt = data['tick']['bid'] 
		qty_bids_a_l_compusdt = data['tick']['bidSize'] 
		price_asks_a_l_compusdt = data['tick']['ask'] 
		qty_asks_a_l_compusdt = data['tick']['askSize'] 

		global symbol_a_g_compusdt 
		global price_bids_a_g_compusdt 
		global qty_bids_a_g_compusdt 
		global price_asks_a_g_compusdt 
		global qty_asks_a_g_compusdt 

		symbol_a_g_compusdt = symbol_a_l_compusdt 
		price_bids_a_g_compusdt = price_bids_a_l_compusdt 
		qty_bids_a_g_compusdt = qty_bids_a_l_compusdt 
		price_asks_a_g_compusdt = price_asks_a_l_compusdt 
		qty_asks_a_g_compusdt = qty_asks_a_l_compusdt 

def on_close_compusdt(ws): 
	print('### closed ###') 

def on_error_compusdt(ws, message): 
	print(message) 

def on_open_compusdt(ws): 
	ws.send(json.dumps({'sub': f'market.compusdt.ticker'})) 

def loop_compusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_compusdt, 
		on_close=on_close_compusdt, 
		on_error=on_error_compusdt) 
	ws.on_open = on_open_compusdt 
	ws.run_forever() 

Thread(target=loop_compusdt).start() 

symbol_b_g_compbtc = 'compbtc' 
price_bids_b_g_compbtc = float(0.0) 
qty_bids_b_g_compbtc = float(0.0) 
price_asks_b_g_compbtc = float(0.0) 
qty_asks_b_g_compbtc = float(0.0) 

def on_message_compbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_compbtc = 'compbtc' 
		price_bids_b_l_compbtc = data['tick']['bid'] 
		qty_bids_b_l_compbtc = data['tick']['bidSize']
		price_asks_b_l_compbtc = data['tick']['ask'] 
		qty_asks_b_l_compbtc = data['tick']['askSize'] 

		global symbol_b_g_compbtc 
		global price_bids_b_g_compbtc 
		global qty_bids_b_g_compbtc 
		global price_asks_b_g_compbtc 
		global qty_asks_b_g_compbtc 

		symbol_b_g_compbtc = symbol_b_l_compbtc 
		price_bids_b_g_compbtc = price_bids_b_l_compbtc 
		qty_bids_b_g_compbtc = qty_bids_b_l_compbtc 
		price_asks_b_g_compbtc = price_asks_b_l_compbtc 
		qty_asks_b_g_compbtc = qty_asks_b_l_compbtc 


def on_close_compbtc(ws): 
	print('### closed ###') 

def on_error_compbtc(ws, message): 
	print(message) 

def on_open_compbtc(ws): 
	ws.send(json.dumps({'sub': f'market.compbtc.ticker'})) 

def loop_compbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_compbtc, 
		on_close=on_close_compbtc, 
		on_error=on_error_compbtc) 
	ws.on_open = on_open_compbtc 
	ws.run_forever() 

Thread(target=loop_compbtc).start() 

def loop_compusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_compusdt != 0.0 and qty_bids_a_g_compusdt != 0.0 and price_asks_a_g_compusdt != 0.0 and qty_asks_a_g_compusdt != 0.0 and price_bids_b_g_compbtc != 0.0 and qty_bids_b_g_compbtc != 0.0 and price_asks_b_g_compbtc != 0.0 and qty_asks_b_g_compbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_compusdt) 
			price_b = float(price_bids_b_g_compbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_compbtc, pribil)

Thread(target=loop_compusdt_Trade).start() 

symbol_a_g_sandusdt = 'sandusdt' 
price_bids_a_g_sandusdt = float(0.0) 
qty_bids_a_g_sandusdt = float(0.0) 
price_asks_a_g_sandusdt = float(0.0) 
qty_asks_a_g_sandusdt = float(0.0) 

def on_message_sandusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_sandusdt = 'sandusdt' 
		price_bids_a_l_sandusdt = data['tick']['bid'] 
		qty_bids_a_l_sandusdt = data['tick']['bidSize'] 
		price_asks_a_l_sandusdt = data['tick']['ask'] 
		qty_asks_a_l_sandusdt = data['tick']['askSize'] 

		global symbol_a_g_sandusdt 
		global price_bids_a_g_sandusdt 
		global qty_bids_a_g_sandusdt 
		global price_asks_a_g_sandusdt 
		global qty_asks_a_g_sandusdt 

		symbol_a_g_sandusdt = symbol_a_l_sandusdt 
		price_bids_a_g_sandusdt = price_bids_a_l_sandusdt 
		qty_bids_a_g_sandusdt = qty_bids_a_l_sandusdt 
		price_asks_a_g_sandusdt = price_asks_a_l_sandusdt 
		qty_asks_a_g_sandusdt = qty_asks_a_l_sandusdt 

def on_close_sandusdt(ws): 
	print('### closed ###') 

def on_error_sandusdt(ws, message): 
	print(message) 

def on_open_sandusdt(ws): 
	ws.send(json.dumps({'sub': f'market.sandusdt.ticker'})) 

def loop_sandusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sandusdt, 
		on_close=on_close_sandusdt, 
		on_error=on_error_sandusdt) 
	ws.on_open = on_open_sandusdt 
	ws.run_forever() 

Thread(target=loop_sandusdt).start() 

symbol_b_g_sandusdc = 'sandusdc' 
price_bids_b_g_sandusdc = float(0.0) 
qty_bids_b_g_sandusdc = float(0.0) 
price_asks_b_g_sandusdc = float(0.0) 
qty_asks_b_g_sandusdc = float(0.0) 

def on_message_sandusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_sandusdc = 'sandusdc' 
		price_bids_b_l_sandusdc = data['tick']['bid'] 
		qty_bids_b_l_sandusdc = data['tick']['bidSize']
		price_asks_b_l_sandusdc = data['tick']['ask'] 
		qty_asks_b_l_sandusdc = data['tick']['askSize'] 

		global symbol_b_g_sandusdc 
		global price_bids_b_g_sandusdc 
		global qty_bids_b_g_sandusdc 
		global price_asks_b_g_sandusdc 
		global qty_asks_b_g_sandusdc 

		symbol_b_g_sandusdc = symbol_b_l_sandusdc 
		price_bids_b_g_sandusdc = price_bids_b_l_sandusdc 
		qty_bids_b_g_sandusdc = qty_bids_b_l_sandusdc 
		price_asks_b_g_sandusdc = price_asks_b_l_sandusdc 
		qty_asks_b_g_sandusdc = qty_asks_b_l_sandusdc 


def on_close_sandusdc(ws): 
	print('### closed ###') 

def on_error_sandusdc(ws, message): 
	print(message) 

def on_open_sandusdc(ws): 
	ws.send(json.dumps({'sub': f'market.sandusdc.ticker'})) 

def loop_sandusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sandusdc, 
		on_close=on_close_sandusdc, 
		on_error=on_error_sandusdc) 
	ws.on_open = on_open_sandusdc 
	ws.run_forever() 

Thread(target=loop_sandusdc).start() 

def loop_sandusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_sandusdt != 0.0 and qty_bids_a_g_sandusdt != 0.0 and price_asks_a_g_sandusdt != 0.0 and qty_asks_a_g_sandusdt != 0.0 and price_bids_b_g_sandusdc != 0.0 and qty_bids_b_g_sandusdc != 0.0 and price_asks_b_g_sandusdc != 0.0 and qty_asks_b_g_sandusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_sandusdt) 
			price_b = float(price_bids_b_g_sandusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_sandusdc, pribil)

Thread(target=loop_sandusdt_Trade).start() 

symbol_a_g_dockusdt = 'dockusdt' 
price_bids_a_g_dockusdt = float(0.0) 
qty_bids_a_g_dockusdt = float(0.0) 
price_asks_a_g_dockusdt = float(0.0) 
qty_asks_a_g_dockusdt = float(0.0) 

def on_message_dockusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_dockusdt = 'dockusdt' 
		price_bids_a_l_dockusdt = data['tick']['bid'] 
		qty_bids_a_l_dockusdt = data['tick']['bidSize'] 
		price_asks_a_l_dockusdt = data['tick']['ask'] 
		qty_asks_a_l_dockusdt = data['tick']['askSize'] 

		global symbol_a_g_dockusdt 
		global price_bids_a_g_dockusdt 
		global qty_bids_a_g_dockusdt 
		global price_asks_a_g_dockusdt 
		global qty_asks_a_g_dockusdt 

		symbol_a_g_dockusdt = symbol_a_l_dockusdt 
		price_bids_a_g_dockusdt = price_bids_a_l_dockusdt 
		qty_bids_a_g_dockusdt = qty_bids_a_l_dockusdt 
		price_asks_a_g_dockusdt = price_asks_a_l_dockusdt 
		qty_asks_a_g_dockusdt = qty_asks_a_l_dockusdt 

def on_close_dockusdt(ws): 
	print('### closed ###') 

def on_error_dockusdt(ws, message): 
	print(message) 

def on_open_dockusdt(ws): 
	ws.send(json.dumps({'sub': f'market.dockusdt.ticker'})) 

def loop_dockusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dockusdt, 
		on_close=on_close_dockusdt, 
		on_error=on_error_dockusdt) 
	ws.on_open = on_open_dockusdt 
	ws.run_forever() 

Thread(target=loop_dockusdt).start() 

symbol_b_g_dockbtc = 'dockbtc' 
price_bids_b_g_dockbtc = float(0.0) 
qty_bids_b_g_dockbtc = float(0.0) 
price_asks_b_g_dockbtc = float(0.0) 
qty_asks_b_g_dockbtc = float(0.0) 

def on_message_dockbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_dockbtc = 'dockbtc' 
		price_bids_b_l_dockbtc = data['tick']['bid'] 
		qty_bids_b_l_dockbtc = data['tick']['bidSize']
		price_asks_b_l_dockbtc = data['tick']['ask'] 
		qty_asks_b_l_dockbtc = data['tick']['askSize'] 

		global symbol_b_g_dockbtc 
		global price_bids_b_g_dockbtc 
		global qty_bids_b_g_dockbtc 
		global price_asks_b_g_dockbtc 
		global qty_asks_b_g_dockbtc 

		symbol_b_g_dockbtc = symbol_b_l_dockbtc 
		price_bids_b_g_dockbtc = price_bids_b_l_dockbtc 
		qty_bids_b_g_dockbtc = qty_bids_b_l_dockbtc 
		price_asks_b_g_dockbtc = price_asks_b_l_dockbtc 
		qty_asks_b_g_dockbtc = qty_asks_b_l_dockbtc 


def on_close_dockbtc(ws): 
	print('### closed ###') 

def on_error_dockbtc(ws, message): 
	print(message) 

def on_open_dockbtc(ws): 
	ws.send(json.dumps({'sub': f'market.dockbtc.ticker'})) 

def loop_dockbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dockbtc, 
		on_close=on_close_dockbtc, 
		on_error=on_error_dockbtc) 
	ws.on_open = on_open_dockbtc 
	ws.run_forever() 

Thread(target=loop_dockbtc).start() 

def loop_dockusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_dockusdt != 0.0 and qty_bids_a_g_dockusdt != 0.0 and price_asks_a_g_dockusdt != 0.0 and qty_asks_a_g_dockusdt != 0.0 and price_bids_b_g_dockbtc != 0.0 and qty_bids_b_g_dockbtc != 0.0 and price_asks_b_g_dockbtc != 0.0 and qty_asks_b_g_dockbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_dockusdt) 
			price_b = float(price_bids_b_g_dockbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_dockbtc, pribil)

Thread(target=loop_dockusdt_Trade).start() 

symbol_a_g_nearusdt = 'nearusdt' 
price_bids_a_g_nearusdt = float(0.0) 
qty_bids_a_g_nearusdt = float(0.0) 
price_asks_a_g_nearusdt = float(0.0) 
qty_asks_a_g_nearusdt = float(0.0) 

def on_message_nearusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_nearusdt = 'nearusdt' 
		price_bids_a_l_nearusdt = data['tick']['bid'] 
		qty_bids_a_l_nearusdt = data['tick']['bidSize'] 
		price_asks_a_l_nearusdt = data['tick']['ask'] 
		qty_asks_a_l_nearusdt = data['tick']['askSize'] 

		global symbol_a_g_nearusdt 
		global price_bids_a_g_nearusdt 
		global qty_bids_a_g_nearusdt 
		global price_asks_a_g_nearusdt 
		global qty_asks_a_g_nearusdt 

		symbol_a_g_nearusdt = symbol_a_l_nearusdt 
		price_bids_a_g_nearusdt = price_bids_a_l_nearusdt 
		qty_bids_a_g_nearusdt = qty_bids_a_l_nearusdt 
		price_asks_a_g_nearusdt = price_asks_a_l_nearusdt 
		qty_asks_a_g_nearusdt = qty_asks_a_l_nearusdt 

def on_close_nearusdt(ws): 
	print('### closed ###') 

def on_error_nearusdt(ws, message): 
	print(message) 

def on_open_nearusdt(ws): 
	ws.send(json.dumps({'sub': f'market.nearusdt.ticker'})) 

def loop_nearusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nearusdt, 
		on_close=on_close_nearusdt, 
		on_error=on_error_nearusdt) 
	ws.on_open = on_open_nearusdt 
	ws.run_forever() 

Thread(target=loop_nearusdt).start() 

symbol_b_g_nearbtc = 'nearbtc' 
price_bids_b_g_nearbtc = float(0.0) 
qty_bids_b_g_nearbtc = float(0.0) 
price_asks_b_g_nearbtc = float(0.0) 
qty_asks_b_g_nearbtc = float(0.0) 

def on_message_nearbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_nearbtc = 'nearbtc' 
		price_bids_b_l_nearbtc = data['tick']['bid'] 
		qty_bids_b_l_nearbtc = data['tick']['bidSize']
		price_asks_b_l_nearbtc = data['tick']['ask'] 
		qty_asks_b_l_nearbtc = data['tick']['askSize'] 

		global symbol_b_g_nearbtc 
		global price_bids_b_g_nearbtc 
		global qty_bids_b_g_nearbtc 
		global price_asks_b_g_nearbtc 
		global qty_asks_b_g_nearbtc 

		symbol_b_g_nearbtc = symbol_b_l_nearbtc 
		price_bids_b_g_nearbtc = price_bids_b_l_nearbtc 
		qty_bids_b_g_nearbtc = qty_bids_b_l_nearbtc 
		price_asks_b_g_nearbtc = price_asks_b_l_nearbtc 
		qty_asks_b_g_nearbtc = qty_asks_b_l_nearbtc 


def on_close_nearbtc(ws): 
	print('### closed ###') 

def on_error_nearbtc(ws, message): 
	print(message) 

def on_open_nearbtc(ws): 
	ws.send(json.dumps({'sub': f'market.nearbtc.ticker'})) 

def loop_nearbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nearbtc, 
		on_close=on_close_nearbtc, 
		on_error=on_error_nearbtc) 
	ws.on_open = on_open_nearbtc 
	ws.run_forever() 

Thread(target=loop_nearbtc).start() 

def loop_nearusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_nearusdt != 0.0 and qty_bids_a_g_nearusdt != 0.0 and price_asks_a_g_nearusdt != 0.0 and qty_asks_a_g_nearusdt != 0.0 and price_bids_b_g_nearbtc != 0.0 and qty_bids_b_g_nearbtc != 0.0 and price_asks_b_g_nearbtc != 0.0 and qty_asks_b_g_nearbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_nearusdt) 
			price_b = float(price_bids_b_g_nearbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_nearbtc, pribil)

Thread(target=loop_nearusdt_Trade).start() 

symbol_a_g_kanusdt = 'kanusdt' 
price_bids_a_g_kanusdt = float(0.0) 
qty_bids_a_g_kanusdt = float(0.0) 
price_asks_a_g_kanusdt = float(0.0) 
qty_asks_a_g_kanusdt = float(0.0) 

def on_message_kanusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_kanusdt = 'kanusdt' 
		price_bids_a_l_kanusdt = data['tick']['bid'] 
		qty_bids_a_l_kanusdt = data['tick']['bidSize'] 
		price_asks_a_l_kanusdt = data['tick']['ask'] 
		qty_asks_a_l_kanusdt = data['tick']['askSize'] 

		global symbol_a_g_kanusdt 
		global price_bids_a_g_kanusdt 
		global qty_bids_a_g_kanusdt 
		global price_asks_a_g_kanusdt 
		global qty_asks_a_g_kanusdt 

		symbol_a_g_kanusdt = symbol_a_l_kanusdt 
		price_bids_a_g_kanusdt = price_bids_a_l_kanusdt 
		qty_bids_a_g_kanusdt = qty_bids_a_l_kanusdt 
		price_asks_a_g_kanusdt = price_asks_a_l_kanusdt 
		qty_asks_a_g_kanusdt = qty_asks_a_l_kanusdt 

def on_close_kanusdt(ws): 
	print('### closed ###') 

def on_error_kanusdt(ws, message): 
	print(message) 

def on_open_kanusdt(ws): 
	ws.send(json.dumps({'sub': f'market.kanusdt.ticker'})) 

def loop_kanusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kanusdt, 
		on_close=on_close_kanusdt, 
		on_error=on_error_kanusdt) 
	ws.on_open = on_open_kanusdt 
	ws.run_forever() 

Thread(target=loop_kanusdt).start() 

symbol_b_g_kaneth = 'kaneth' 
price_bids_b_g_kaneth = float(0.0) 
qty_bids_b_g_kaneth = float(0.0) 
price_asks_b_g_kaneth = float(0.0) 
qty_asks_b_g_kaneth = float(0.0) 

def on_message_kaneth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_kaneth = 'kaneth' 
		price_bids_b_l_kaneth = data['tick']['bid'] 
		qty_bids_b_l_kaneth = data['tick']['bidSize']
		price_asks_b_l_kaneth = data['tick']['ask'] 
		qty_asks_b_l_kaneth = data['tick']['askSize'] 

		global symbol_b_g_kaneth 
		global price_bids_b_g_kaneth 
		global qty_bids_b_g_kaneth 
		global price_asks_b_g_kaneth 
		global qty_asks_b_g_kaneth 

		symbol_b_g_kaneth = symbol_b_l_kaneth 
		price_bids_b_g_kaneth = price_bids_b_l_kaneth 
		qty_bids_b_g_kaneth = qty_bids_b_l_kaneth 
		price_asks_b_g_kaneth = price_asks_b_l_kaneth 
		qty_asks_b_g_kaneth = qty_asks_b_l_kaneth 


def on_close_kaneth(ws): 
	print('### closed ###') 

def on_error_kaneth(ws, message): 
	print(message) 

def on_open_kaneth(ws): 
	ws.send(json.dumps({'sub': f'market.kaneth.ticker'})) 

def loop_kaneth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kaneth, 
		on_close=on_close_kaneth, 
		on_error=on_error_kaneth) 
	ws.on_open = on_open_kaneth 
	ws.run_forever() 

Thread(target=loop_kaneth).start() 

def loop_kanusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_kanusdt != 0.0 and qty_bids_a_g_kanusdt != 0.0 and price_asks_a_g_kanusdt != 0.0 and qty_asks_a_g_kanusdt != 0.0 and price_bids_b_g_kaneth != 0.0 and qty_bids_b_g_kaneth != 0.0 and price_asks_b_g_kaneth != 0.0 and qty_asks_b_g_kaneth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_kanusdt) 
			price_b = float(price_bids_b_g_kaneth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_kaneth, pribil)

Thread(target=loop_kanusdt_Trade).start() 

symbol_a_g_snxusdt = 'snxusdt' 
price_bids_a_g_snxusdt = float(0.0) 
qty_bids_a_g_snxusdt = float(0.0) 
price_asks_a_g_snxusdt = float(0.0) 
qty_asks_a_g_snxusdt = float(0.0) 

def on_message_snxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_snxusdt = 'snxusdt' 
		price_bids_a_l_snxusdt = data['tick']['bid'] 
		qty_bids_a_l_snxusdt = data['tick']['bidSize'] 
		price_asks_a_l_snxusdt = data['tick']['ask'] 
		qty_asks_a_l_snxusdt = data['tick']['askSize'] 

		global symbol_a_g_snxusdt 
		global price_bids_a_g_snxusdt 
		global qty_bids_a_g_snxusdt 
		global price_asks_a_g_snxusdt 
		global qty_asks_a_g_snxusdt 

		symbol_a_g_snxusdt = symbol_a_l_snxusdt 
		price_bids_a_g_snxusdt = price_bids_a_l_snxusdt 
		qty_bids_a_g_snxusdt = qty_bids_a_l_snxusdt 
		price_asks_a_g_snxusdt = price_asks_a_l_snxusdt 
		qty_asks_a_g_snxusdt = qty_asks_a_l_snxusdt 

def on_close_snxusdt(ws): 
	print('### closed ###') 

def on_error_snxusdt(ws, message): 
	print(message) 

def on_open_snxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.snxusdt.ticker'})) 

def loop_snxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_snxusdt, 
		on_close=on_close_snxusdt, 
		on_error=on_error_snxusdt) 
	ws.on_open = on_open_snxusdt 
	ws.run_forever() 

Thread(target=loop_snxusdt).start() 

symbol_b_g_snxbtc = 'snxbtc' 
price_bids_b_g_snxbtc = float(0.0) 
qty_bids_b_g_snxbtc = float(0.0) 
price_asks_b_g_snxbtc = float(0.0) 
qty_asks_b_g_snxbtc = float(0.0) 

def on_message_snxbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_snxbtc = 'snxbtc' 
		price_bids_b_l_snxbtc = data['tick']['bid'] 
		qty_bids_b_l_snxbtc = data['tick']['bidSize']
		price_asks_b_l_snxbtc = data['tick']['ask'] 
		qty_asks_b_l_snxbtc = data['tick']['askSize'] 

		global symbol_b_g_snxbtc 
		global price_bids_b_g_snxbtc 
		global qty_bids_b_g_snxbtc 
		global price_asks_b_g_snxbtc 
		global qty_asks_b_g_snxbtc 

		symbol_b_g_snxbtc = symbol_b_l_snxbtc 
		price_bids_b_g_snxbtc = price_bids_b_l_snxbtc 
		qty_bids_b_g_snxbtc = qty_bids_b_l_snxbtc 
		price_asks_b_g_snxbtc = price_asks_b_l_snxbtc 
		qty_asks_b_g_snxbtc = qty_asks_b_l_snxbtc 


def on_close_snxbtc(ws): 
	print('### closed ###') 

def on_error_snxbtc(ws, message): 
	print(message) 

def on_open_snxbtc(ws): 
	ws.send(json.dumps({'sub': f'market.snxbtc.ticker'})) 

def loop_snxbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_snxbtc, 
		on_close=on_close_snxbtc, 
		on_error=on_error_snxbtc) 
	ws.on_open = on_open_snxbtc 
	ws.run_forever() 

Thread(target=loop_snxbtc).start() 

def loop_snxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_snxusdt != 0.0 and qty_bids_a_g_snxusdt != 0.0 and price_asks_a_g_snxusdt != 0.0 and qty_asks_a_g_snxusdt != 0.0 and price_bids_b_g_snxbtc != 0.0 and qty_bids_b_g_snxbtc != 0.0 and price_asks_b_g_snxbtc != 0.0 and qty_asks_b_g_snxbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_snxusdt) 
			price_b = float(price_bids_b_g_snxbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_snxbtc, pribil)

Thread(target=loop_snxusdt_Trade).start() 

symbol_a_g_thetausdt = 'thetausdt' 
price_bids_a_g_thetausdt = float(0.0) 
qty_bids_a_g_thetausdt = float(0.0) 
price_asks_a_g_thetausdt = float(0.0) 
qty_asks_a_g_thetausdt = float(0.0) 

def on_message_thetausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_thetausdt = 'thetausdt' 
		price_bids_a_l_thetausdt = data['tick']['bid'] 
		qty_bids_a_l_thetausdt = data['tick']['bidSize'] 
		price_asks_a_l_thetausdt = data['tick']['ask'] 
		qty_asks_a_l_thetausdt = data['tick']['askSize'] 

		global symbol_a_g_thetausdt 
		global price_bids_a_g_thetausdt 
		global qty_bids_a_g_thetausdt 
		global price_asks_a_g_thetausdt 
		global qty_asks_a_g_thetausdt 

		symbol_a_g_thetausdt = symbol_a_l_thetausdt 
		price_bids_a_g_thetausdt = price_bids_a_l_thetausdt 
		qty_bids_a_g_thetausdt = qty_bids_a_l_thetausdt 
		price_asks_a_g_thetausdt = price_asks_a_l_thetausdt 
		qty_asks_a_g_thetausdt = qty_asks_a_l_thetausdt 

def on_close_thetausdt(ws): 
	print('### closed ###') 

def on_error_thetausdt(ws, message): 
	print(message) 

def on_open_thetausdt(ws): 
	ws.send(json.dumps({'sub': f'market.thetausdt.ticker'})) 

def loop_thetausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_thetausdt, 
		on_close=on_close_thetausdt, 
		on_error=on_error_thetausdt) 
	ws.on_open = on_open_thetausdt 
	ws.run_forever() 

Thread(target=loop_thetausdt).start() 

symbol_b_g_thetaeth = 'thetaeth' 
price_bids_b_g_thetaeth = float(0.0) 
qty_bids_b_g_thetaeth = float(0.0) 
price_asks_b_g_thetaeth = float(0.0) 
qty_asks_b_g_thetaeth = float(0.0) 

def on_message_thetaeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_thetaeth = 'thetaeth' 
		price_bids_b_l_thetaeth = data['tick']['bid'] 
		qty_bids_b_l_thetaeth = data['tick']['bidSize']
		price_asks_b_l_thetaeth = data['tick']['ask'] 
		qty_asks_b_l_thetaeth = data['tick']['askSize'] 

		global symbol_b_g_thetaeth 
		global price_bids_b_g_thetaeth 
		global qty_bids_b_g_thetaeth 
		global price_asks_b_g_thetaeth 
		global qty_asks_b_g_thetaeth 

		symbol_b_g_thetaeth = symbol_b_l_thetaeth 
		price_bids_b_g_thetaeth = price_bids_b_l_thetaeth 
		qty_bids_b_g_thetaeth = qty_bids_b_l_thetaeth 
		price_asks_b_g_thetaeth = price_asks_b_l_thetaeth 
		qty_asks_b_g_thetaeth = qty_asks_b_l_thetaeth 


def on_close_thetaeth(ws): 
	print('### closed ###') 

def on_error_thetaeth(ws, message): 
	print(message) 

def on_open_thetaeth(ws): 
	ws.send(json.dumps({'sub': f'market.thetaeth.ticker'})) 

def loop_thetaeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_thetaeth, 
		on_close=on_close_thetaeth, 
		on_error=on_error_thetaeth) 
	ws.on_open = on_open_thetaeth 
	ws.run_forever() 

Thread(target=loop_thetaeth).start() 

def loop_thetausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_thetausdt != 0.0 and qty_bids_a_g_thetausdt != 0.0 and price_asks_a_g_thetausdt != 0.0 and qty_asks_a_g_thetausdt != 0.0 and price_bids_b_g_thetaeth != 0.0 and qty_bids_b_g_thetaeth != 0.0 and price_asks_b_g_thetaeth != 0.0 and qty_asks_b_g_thetaeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_thetausdt) 
			price_b = float(price_bids_b_g_thetaeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_thetaeth, pribil)

Thread(target=loop_thetausdt_Trade).start() 

symbol_a_g_aptusdt = 'aptusdt' 
price_bids_a_g_aptusdt = float(0.0) 
qty_bids_a_g_aptusdt = float(0.0) 
price_asks_a_g_aptusdt = float(0.0) 
qty_asks_a_g_aptusdt = float(0.0) 

def on_message_aptusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_aptusdt = 'aptusdt' 
		price_bids_a_l_aptusdt = data['tick']['bid'] 
		qty_bids_a_l_aptusdt = data['tick']['bidSize'] 
		price_asks_a_l_aptusdt = data['tick']['ask'] 
		qty_asks_a_l_aptusdt = data['tick']['askSize'] 

		global symbol_a_g_aptusdt 
		global price_bids_a_g_aptusdt 
		global qty_bids_a_g_aptusdt 
		global price_asks_a_g_aptusdt 
		global qty_asks_a_g_aptusdt 

		symbol_a_g_aptusdt = symbol_a_l_aptusdt 
		price_bids_a_g_aptusdt = price_bids_a_l_aptusdt 
		qty_bids_a_g_aptusdt = qty_bids_a_l_aptusdt 
		price_asks_a_g_aptusdt = price_asks_a_l_aptusdt 
		qty_asks_a_g_aptusdt = qty_asks_a_l_aptusdt 

def on_close_aptusdt(ws): 
	print('### closed ###') 

def on_error_aptusdt(ws, message): 
	print(message) 

def on_open_aptusdt(ws): 
	ws.send(json.dumps({'sub': f'market.aptusdt.ticker'})) 

def loop_aptusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_aptusdt, 
		on_close=on_close_aptusdt, 
		on_error=on_error_aptusdt) 
	ws.on_open = on_open_aptusdt 
	ws.run_forever() 

Thread(target=loop_aptusdt).start() 

symbol_b_g_aptusdc = 'aptusdc' 
price_bids_b_g_aptusdc = float(0.0) 
qty_bids_b_g_aptusdc = float(0.0) 
price_asks_b_g_aptusdc = float(0.0) 
qty_asks_b_g_aptusdc = float(0.0) 

def on_message_aptusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_aptusdc = 'aptusdc' 
		price_bids_b_l_aptusdc = data['tick']['bid'] 
		qty_bids_b_l_aptusdc = data['tick']['bidSize']
		price_asks_b_l_aptusdc = data['tick']['ask'] 
		qty_asks_b_l_aptusdc = data['tick']['askSize'] 

		global symbol_b_g_aptusdc 
		global price_bids_b_g_aptusdc 
		global qty_bids_b_g_aptusdc 
		global price_asks_b_g_aptusdc 
		global qty_asks_b_g_aptusdc 

		symbol_b_g_aptusdc = symbol_b_l_aptusdc 
		price_bids_b_g_aptusdc = price_bids_b_l_aptusdc 
		qty_bids_b_g_aptusdc = qty_bids_b_l_aptusdc 
		price_asks_b_g_aptusdc = price_asks_b_l_aptusdc 
		qty_asks_b_g_aptusdc = qty_asks_b_l_aptusdc 


def on_close_aptusdc(ws): 
	print('### closed ###') 

def on_error_aptusdc(ws, message): 
	print(message) 

def on_open_aptusdc(ws): 
	ws.send(json.dumps({'sub': f'market.aptusdc.ticker'})) 

def loop_aptusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_aptusdc, 
		on_close=on_close_aptusdc, 
		on_error=on_error_aptusdc) 
	ws.on_open = on_open_aptusdc 
	ws.run_forever() 

Thread(target=loop_aptusdc).start() 

def loop_aptusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_aptusdt != 0.0 and qty_bids_a_g_aptusdt != 0.0 and price_asks_a_g_aptusdt != 0.0 and qty_asks_a_g_aptusdt != 0.0 and price_bids_b_g_aptusdc != 0.0 and qty_bids_b_g_aptusdc != 0.0 and price_asks_b_g_aptusdc != 0.0 and qty_asks_b_g_aptusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_aptusdt) 
			price_b = float(price_bids_b_g_aptusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_aptusdc, pribil)

Thread(target=loop_aptusdt_Trade).start() 

symbol_a_g_1inchusdt = '1inchusdt' 
price_bids_a_g_1inchusdt = float(0.0) 
qty_bids_a_g_1inchusdt = float(0.0) 
price_asks_a_g_1inchusdt = float(0.0) 
qty_asks_a_g_1inchusdt = float(0.0) 

def on_message_1inchusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_1inchusdt = '1inchusdt' 
		price_bids_a_l_1inchusdt = data['tick']['bid'] 
		qty_bids_a_l_1inchusdt = data['tick']['bidSize'] 
		price_asks_a_l_1inchusdt = data['tick']['ask'] 
		qty_asks_a_l_1inchusdt = data['tick']['askSize'] 

		global symbol_a_g_1inchusdt 
		global price_bids_a_g_1inchusdt 
		global qty_bids_a_g_1inchusdt 
		global price_asks_a_g_1inchusdt 
		global qty_asks_a_g_1inchusdt 

		symbol_a_g_1inchusdt = symbol_a_l_1inchusdt 
		price_bids_a_g_1inchusdt = price_bids_a_l_1inchusdt 
		qty_bids_a_g_1inchusdt = qty_bids_a_l_1inchusdt 
		price_asks_a_g_1inchusdt = price_asks_a_l_1inchusdt 
		qty_asks_a_g_1inchusdt = qty_asks_a_l_1inchusdt 

def on_close_1inchusdt(ws): 
	print('### closed ###') 

def on_error_1inchusdt(ws, message): 
	print(message) 

def on_open_1inchusdt(ws): 
	ws.send(json.dumps({'sub': f'market.1inchusdt.ticker'})) 

def loop_1inchusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_1inchusdt, 
		on_close=on_close_1inchusdt, 
		on_error=on_error_1inchusdt) 
	ws.on_open = on_open_1inchusdt 
	ws.run_forever() 

Thread(target=loop_1inchusdt).start() 

symbol_b_g_1inchbtc = '1inchbtc' 
price_bids_b_g_1inchbtc = float(0.0) 
qty_bids_b_g_1inchbtc = float(0.0) 
price_asks_b_g_1inchbtc = float(0.0) 
qty_asks_b_g_1inchbtc = float(0.0) 

def on_message_1inchbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_1inchbtc = '1inchbtc' 
		price_bids_b_l_1inchbtc = data['tick']['bid'] 
		qty_bids_b_l_1inchbtc = data['tick']['bidSize']
		price_asks_b_l_1inchbtc = data['tick']['ask'] 
		qty_asks_b_l_1inchbtc = data['tick']['askSize'] 

		global symbol_b_g_1inchbtc 
		global price_bids_b_g_1inchbtc 
		global qty_bids_b_g_1inchbtc 
		global price_asks_b_g_1inchbtc 
		global qty_asks_b_g_1inchbtc 

		symbol_b_g_1inchbtc = symbol_b_l_1inchbtc 
		price_bids_b_g_1inchbtc = price_bids_b_l_1inchbtc 
		qty_bids_b_g_1inchbtc = qty_bids_b_l_1inchbtc 
		price_asks_b_g_1inchbtc = price_asks_b_l_1inchbtc 
		qty_asks_b_g_1inchbtc = qty_asks_b_l_1inchbtc 


def on_close_1inchbtc(ws): 
	print('### closed ###') 

def on_error_1inchbtc(ws, message): 
	print(message) 

def on_open_1inchbtc(ws): 
	ws.send(json.dumps({'sub': f'market.1inchbtc.ticker'})) 

def loop_1inchbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_1inchbtc, 
		on_close=on_close_1inchbtc, 
		on_error=on_error_1inchbtc) 
	ws.on_open = on_open_1inchbtc 
	ws.run_forever() 

Thread(target=loop_1inchbtc).start() 

def loop_1inchusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_1inchusdt != 0.0 and qty_bids_a_g_1inchusdt != 0.0 and price_asks_a_g_1inchusdt != 0.0 and qty_asks_a_g_1inchusdt != 0.0 and price_bids_b_g_1inchbtc != 0.0 and qty_bids_b_g_1inchbtc != 0.0 and price_asks_b_g_1inchbtc != 0.0 and qty_asks_b_g_1inchbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_1inchusdt) 
			price_b = float(price_bids_b_g_1inchbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_1inchbtc, pribil)

Thread(target=loop_1inchusdt_Trade).start() 

symbol_a_g_nestusdt = 'nestusdt' 
price_bids_a_g_nestusdt = float(0.0) 
qty_bids_a_g_nestusdt = float(0.0) 
price_asks_a_g_nestusdt = float(0.0) 
qty_asks_a_g_nestusdt = float(0.0) 

def on_message_nestusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_nestusdt = 'nestusdt' 
		price_bids_a_l_nestusdt = data['tick']['bid'] 
		qty_bids_a_l_nestusdt = data['tick']['bidSize'] 
		price_asks_a_l_nestusdt = data['tick']['ask'] 
		qty_asks_a_l_nestusdt = data['tick']['askSize'] 

		global symbol_a_g_nestusdt 
		global price_bids_a_g_nestusdt 
		global qty_bids_a_g_nestusdt 
		global price_asks_a_g_nestusdt 
		global qty_asks_a_g_nestusdt 

		symbol_a_g_nestusdt = symbol_a_l_nestusdt 
		price_bids_a_g_nestusdt = price_bids_a_l_nestusdt 
		qty_bids_a_g_nestusdt = qty_bids_a_l_nestusdt 
		price_asks_a_g_nestusdt = price_asks_a_l_nestusdt 
		qty_asks_a_g_nestusdt = qty_asks_a_l_nestusdt 

def on_close_nestusdt(ws): 
	print('### closed ###') 

def on_error_nestusdt(ws, message): 
	print(message) 

def on_open_nestusdt(ws): 
	ws.send(json.dumps({'sub': f'market.nestusdt.ticker'})) 

def loop_nestusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nestusdt, 
		on_close=on_close_nestusdt, 
		on_error=on_error_nestusdt) 
	ws.on_open = on_open_nestusdt 
	ws.run_forever() 

Thread(target=loop_nestusdt).start() 

symbol_b_g_nestbtc = 'nestbtc' 
price_bids_b_g_nestbtc = float(0.0) 
qty_bids_b_g_nestbtc = float(0.0) 
price_asks_b_g_nestbtc = float(0.0) 
qty_asks_b_g_nestbtc = float(0.0) 

def on_message_nestbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_nestbtc = 'nestbtc' 
		price_bids_b_l_nestbtc = data['tick']['bid'] 
		qty_bids_b_l_nestbtc = data['tick']['bidSize']
		price_asks_b_l_nestbtc = data['tick']['ask'] 
		qty_asks_b_l_nestbtc = data['tick']['askSize'] 

		global symbol_b_g_nestbtc 
		global price_bids_b_g_nestbtc 
		global qty_bids_b_g_nestbtc 
		global price_asks_b_g_nestbtc 
		global qty_asks_b_g_nestbtc 

		symbol_b_g_nestbtc = symbol_b_l_nestbtc 
		price_bids_b_g_nestbtc = price_bids_b_l_nestbtc 
		qty_bids_b_g_nestbtc = qty_bids_b_l_nestbtc 
		price_asks_b_g_nestbtc = price_asks_b_l_nestbtc 
		qty_asks_b_g_nestbtc = qty_asks_b_l_nestbtc 


def on_close_nestbtc(ws): 
	print('### closed ###') 

def on_error_nestbtc(ws, message): 
	print(message) 

def on_open_nestbtc(ws): 
	ws.send(json.dumps({'sub': f'market.nestbtc.ticker'})) 

def loop_nestbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nestbtc, 
		on_close=on_close_nestbtc, 
		on_error=on_error_nestbtc) 
	ws.on_open = on_open_nestbtc 
	ws.run_forever() 

Thread(target=loop_nestbtc).start() 

def loop_nestusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_nestusdt != 0.0 and qty_bids_a_g_nestusdt != 0.0 and price_asks_a_g_nestusdt != 0.0 and qty_asks_a_g_nestusdt != 0.0 and price_bids_b_g_nestbtc != 0.0 and qty_bids_b_g_nestbtc != 0.0 and price_asks_b_g_nestbtc != 0.0 and qty_asks_b_g_nestbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_nestusdt) 
			price_b = float(price_bids_b_g_nestbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_nestbtc, pribil)

Thread(target=loop_nestusdt_Trade).start() 

symbol_a_g_manausdt = 'manausdt' 
price_bids_a_g_manausdt = float(0.0) 
qty_bids_a_g_manausdt = float(0.0) 
price_asks_a_g_manausdt = float(0.0) 
qty_asks_a_g_manausdt = float(0.0) 

def on_message_manausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_manausdt = 'manausdt' 
		price_bids_a_l_manausdt = data['tick']['bid'] 
		qty_bids_a_l_manausdt = data['tick']['bidSize'] 
		price_asks_a_l_manausdt = data['tick']['ask'] 
		qty_asks_a_l_manausdt = data['tick']['askSize'] 

		global symbol_a_g_manausdt 
		global price_bids_a_g_manausdt 
		global qty_bids_a_g_manausdt 
		global price_asks_a_g_manausdt 
		global qty_asks_a_g_manausdt 

		symbol_a_g_manausdt = symbol_a_l_manausdt 
		price_bids_a_g_manausdt = price_bids_a_l_manausdt 
		qty_bids_a_g_manausdt = qty_bids_a_l_manausdt 
		price_asks_a_g_manausdt = price_asks_a_l_manausdt 
		qty_asks_a_g_manausdt = qty_asks_a_l_manausdt 

def on_close_manausdt(ws): 
	print('### closed ###') 

def on_error_manausdt(ws, message): 
	print(message) 

def on_open_manausdt(ws): 
	ws.send(json.dumps({'sub': f'market.manausdt.ticker'})) 

def loop_manausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_manausdt, 
		on_close=on_close_manausdt, 
		on_error=on_error_manausdt) 
	ws.on_open = on_open_manausdt 
	ws.run_forever() 

Thread(target=loop_manausdt).start() 

symbol_b_g_manausdc = 'manausdc' 
price_bids_b_g_manausdc = float(0.0) 
qty_bids_b_g_manausdc = float(0.0) 
price_asks_b_g_manausdc = float(0.0) 
qty_asks_b_g_manausdc = float(0.0) 

def on_message_manausdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_manausdc = 'manausdc' 
		price_bids_b_l_manausdc = data['tick']['bid'] 
		qty_bids_b_l_manausdc = data['tick']['bidSize']
		price_asks_b_l_manausdc = data['tick']['ask'] 
		qty_asks_b_l_manausdc = data['tick']['askSize'] 

		global symbol_b_g_manausdc 
		global price_bids_b_g_manausdc 
		global qty_bids_b_g_manausdc 
		global price_asks_b_g_manausdc 
		global qty_asks_b_g_manausdc 

		symbol_b_g_manausdc = symbol_b_l_manausdc 
		price_bids_b_g_manausdc = price_bids_b_l_manausdc 
		qty_bids_b_g_manausdc = qty_bids_b_l_manausdc 
		price_asks_b_g_manausdc = price_asks_b_l_manausdc 
		qty_asks_b_g_manausdc = qty_asks_b_l_manausdc 


def on_close_manausdc(ws): 
	print('### closed ###') 

def on_error_manausdc(ws, message): 
	print(message) 

def on_open_manausdc(ws): 
	ws.send(json.dumps({'sub': f'market.manausdc.ticker'})) 

def loop_manausdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_manausdc, 
		on_close=on_close_manausdc, 
		on_error=on_error_manausdc) 
	ws.on_open = on_open_manausdc 
	ws.run_forever() 

Thread(target=loop_manausdc).start() 

def loop_manausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_manausdt != 0.0 and qty_bids_a_g_manausdt != 0.0 and price_asks_a_g_manausdt != 0.0 and qty_asks_a_g_manausdt != 0.0 and price_bids_b_g_manausdc != 0.0 and qty_bids_b_g_manausdc != 0.0 and price_asks_b_g_manausdc != 0.0 and qty_asks_b_g_manausdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_manausdt) 
			price_b = float(price_bids_b_g_manausdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_manausdc, pribil)

Thread(target=loop_manausdt_Trade).start() 

symbol_a_g_cruusdt = 'cruusdt' 
price_bids_a_g_cruusdt = float(0.0) 
qty_bids_a_g_cruusdt = float(0.0) 
price_asks_a_g_cruusdt = float(0.0) 
qty_asks_a_g_cruusdt = float(0.0) 

def on_message_cruusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_cruusdt = 'cruusdt' 
		price_bids_a_l_cruusdt = data['tick']['bid'] 
		qty_bids_a_l_cruusdt = data['tick']['bidSize'] 
		price_asks_a_l_cruusdt = data['tick']['ask'] 
		qty_asks_a_l_cruusdt = data['tick']['askSize'] 

		global symbol_a_g_cruusdt 
		global price_bids_a_g_cruusdt 
		global qty_bids_a_g_cruusdt 
		global price_asks_a_g_cruusdt 
		global qty_asks_a_g_cruusdt 

		symbol_a_g_cruusdt = symbol_a_l_cruusdt 
		price_bids_a_g_cruusdt = price_bids_a_l_cruusdt 
		qty_bids_a_g_cruusdt = qty_bids_a_l_cruusdt 
		price_asks_a_g_cruusdt = price_asks_a_l_cruusdt 
		qty_asks_a_g_cruusdt = qty_asks_a_l_cruusdt 

def on_close_cruusdt(ws): 
	print('### closed ###') 

def on_error_cruusdt(ws, message): 
	print(message) 

def on_open_cruusdt(ws): 
	ws.send(json.dumps({'sub': f'market.cruusdt.ticker'})) 

def loop_cruusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_cruusdt, 
		on_close=on_close_cruusdt, 
		on_error=on_error_cruusdt) 
	ws.on_open = on_open_cruusdt 
	ws.run_forever() 

Thread(target=loop_cruusdt).start() 

symbol_b_g_crubtc = 'crubtc' 
price_bids_b_g_crubtc = float(0.0) 
qty_bids_b_g_crubtc = float(0.0) 
price_asks_b_g_crubtc = float(0.0) 
qty_asks_b_g_crubtc = float(0.0) 

def on_message_crubtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_crubtc = 'crubtc' 
		price_bids_b_l_crubtc = data['tick']['bid'] 
		qty_bids_b_l_crubtc = data['tick']['bidSize']
		price_asks_b_l_crubtc = data['tick']['ask'] 
		qty_asks_b_l_crubtc = data['tick']['askSize'] 

		global symbol_b_g_crubtc 
		global price_bids_b_g_crubtc 
		global qty_bids_b_g_crubtc 
		global price_asks_b_g_crubtc 
		global qty_asks_b_g_crubtc 

		symbol_b_g_crubtc = symbol_b_l_crubtc 
		price_bids_b_g_crubtc = price_bids_b_l_crubtc 
		qty_bids_b_g_crubtc = qty_bids_b_l_crubtc 
		price_asks_b_g_crubtc = price_asks_b_l_crubtc 
		qty_asks_b_g_crubtc = qty_asks_b_l_crubtc 


def on_close_crubtc(ws): 
	print('### closed ###') 

def on_error_crubtc(ws, message): 
	print(message) 

def on_open_crubtc(ws): 
	ws.send(json.dumps({'sub': f'market.crubtc.ticker'})) 

def loop_crubtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_crubtc, 
		on_close=on_close_crubtc, 
		on_error=on_error_crubtc) 
	ws.on_open = on_open_crubtc 
	ws.run_forever() 

Thread(target=loop_crubtc).start() 

def loop_cruusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_cruusdt != 0.0 and qty_bids_a_g_cruusdt != 0.0 and price_asks_a_g_cruusdt != 0.0 and qty_asks_a_g_cruusdt != 0.0 and price_bids_b_g_crubtc != 0.0 and qty_bids_b_g_crubtc != 0.0 and price_asks_b_g_crubtc != 0.0 and qty_asks_b_g_crubtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_cruusdt) 
			price_b = float(price_bids_b_g_crubtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_crubtc, pribil)

Thread(target=loop_cruusdt_Trade).start() 

symbol_a_g_flowusdt = 'flowusdt' 
price_bids_a_g_flowusdt = float(0.0) 
qty_bids_a_g_flowusdt = float(0.0) 
price_asks_a_g_flowusdt = float(0.0) 
qty_asks_a_g_flowusdt = float(0.0) 

def on_message_flowusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_flowusdt = 'flowusdt' 
		price_bids_a_l_flowusdt = data['tick']['bid'] 
		qty_bids_a_l_flowusdt = data['tick']['bidSize'] 
		price_asks_a_l_flowusdt = data['tick']['ask'] 
		qty_asks_a_l_flowusdt = data['tick']['askSize'] 

		global symbol_a_g_flowusdt 
		global price_bids_a_g_flowusdt 
		global qty_bids_a_g_flowusdt 
		global price_asks_a_g_flowusdt 
		global qty_asks_a_g_flowusdt 

		symbol_a_g_flowusdt = symbol_a_l_flowusdt 
		price_bids_a_g_flowusdt = price_bids_a_l_flowusdt 
		qty_bids_a_g_flowusdt = qty_bids_a_l_flowusdt 
		price_asks_a_g_flowusdt = price_asks_a_l_flowusdt 
		qty_asks_a_g_flowusdt = qty_asks_a_l_flowusdt 

def on_close_flowusdt(ws): 
	print('### closed ###') 

def on_error_flowusdt(ws, message): 
	print(message) 

def on_open_flowusdt(ws): 
	ws.send(json.dumps({'sub': f'market.flowusdt.ticker'})) 

def loop_flowusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_flowusdt, 
		on_close=on_close_flowusdt, 
		on_error=on_error_flowusdt) 
	ws.on_open = on_open_flowusdt 
	ws.run_forever() 

Thread(target=loop_flowusdt).start() 

symbol_b_g_floweth = 'floweth' 
price_bids_b_g_floweth = float(0.0) 
qty_bids_b_g_floweth = float(0.0) 
price_asks_b_g_floweth = float(0.0) 
qty_asks_b_g_floweth = float(0.0) 

def on_message_floweth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_floweth = 'floweth' 
		price_bids_b_l_floweth = data['tick']['bid'] 
		qty_bids_b_l_floweth = data['tick']['bidSize']
		price_asks_b_l_floweth = data['tick']['ask'] 
		qty_asks_b_l_floweth = data['tick']['askSize'] 

		global symbol_b_g_floweth 
		global price_bids_b_g_floweth 
		global qty_bids_b_g_floweth 
		global price_asks_b_g_floweth 
		global qty_asks_b_g_floweth 

		symbol_b_g_floweth = symbol_b_l_floweth 
		price_bids_b_g_floweth = price_bids_b_l_floweth 
		qty_bids_b_g_floweth = qty_bids_b_l_floweth 
		price_asks_b_g_floweth = price_asks_b_l_floweth 
		qty_asks_b_g_floweth = qty_asks_b_l_floweth 


def on_close_floweth(ws): 
	print('### closed ###') 

def on_error_floweth(ws, message): 
	print(message) 

def on_open_floweth(ws): 
	ws.send(json.dumps({'sub': f'market.floweth.ticker'})) 

def loop_floweth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_floweth, 
		on_close=on_close_floweth, 
		on_error=on_error_floweth) 
	ws.on_open = on_open_floweth 
	ws.run_forever() 

Thread(target=loop_floweth).start() 

def loop_flowusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_flowusdt != 0.0 and qty_bids_a_g_flowusdt != 0.0 and price_asks_a_g_flowusdt != 0.0 and qty_asks_a_g_flowusdt != 0.0 and price_bids_b_g_floweth != 0.0 and qty_bids_b_g_floweth != 0.0 and price_asks_b_g_floweth != 0.0 and qty_asks_b_g_floweth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_flowusdt) 
			price_b = float(price_bids_b_g_floweth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_floweth, pribil)

Thread(target=loop_flowusdt_Trade).start() 

symbol_a_g_zrxusdt = 'zrxusdt' 
price_bids_a_g_zrxusdt = float(0.0) 
qty_bids_a_g_zrxusdt = float(0.0) 
price_asks_a_g_zrxusdt = float(0.0) 
qty_asks_a_g_zrxusdt = float(0.0) 

def on_message_zrxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_zrxusdt = 'zrxusdt' 
		price_bids_a_l_zrxusdt = data['tick']['bid'] 
		qty_bids_a_l_zrxusdt = data['tick']['bidSize'] 
		price_asks_a_l_zrxusdt = data['tick']['ask'] 
		qty_asks_a_l_zrxusdt = data['tick']['askSize'] 

		global symbol_a_g_zrxusdt 
		global price_bids_a_g_zrxusdt 
		global qty_bids_a_g_zrxusdt 
		global price_asks_a_g_zrxusdt 
		global qty_asks_a_g_zrxusdt 

		symbol_a_g_zrxusdt = symbol_a_l_zrxusdt 
		price_bids_a_g_zrxusdt = price_bids_a_l_zrxusdt 
		qty_bids_a_g_zrxusdt = qty_bids_a_l_zrxusdt 
		price_asks_a_g_zrxusdt = price_asks_a_l_zrxusdt 
		qty_asks_a_g_zrxusdt = qty_asks_a_l_zrxusdt 

def on_close_zrxusdt(ws): 
	print('### closed ###') 

def on_error_zrxusdt(ws, message): 
	print(message) 

def on_open_zrxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.zrxusdt.ticker'})) 

def loop_zrxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_zrxusdt, 
		on_close=on_close_zrxusdt, 
		on_error=on_error_zrxusdt) 
	ws.on_open = on_open_zrxusdt 
	ws.run_forever() 

Thread(target=loop_zrxusdt).start() 

symbol_b_g_zrxbtc = 'zrxbtc' 
price_bids_b_g_zrxbtc = float(0.0) 
qty_bids_b_g_zrxbtc = float(0.0) 
price_asks_b_g_zrxbtc = float(0.0) 
qty_asks_b_g_zrxbtc = float(0.0) 

def on_message_zrxbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_zrxbtc = 'zrxbtc' 
		price_bids_b_l_zrxbtc = data['tick']['bid'] 
		qty_bids_b_l_zrxbtc = data['tick']['bidSize']
		price_asks_b_l_zrxbtc = data['tick']['ask'] 
		qty_asks_b_l_zrxbtc = data['tick']['askSize'] 

		global symbol_b_g_zrxbtc 
		global price_bids_b_g_zrxbtc 
		global qty_bids_b_g_zrxbtc 
		global price_asks_b_g_zrxbtc 
		global qty_asks_b_g_zrxbtc 

		symbol_b_g_zrxbtc = symbol_b_l_zrxbtc 
		price_bids_b_g_zrxbtc = price_bids_b_l_zrxbtc 
		qty_bids_b_g_zrxbtc = qty_bids_b_l_zrxbtc 
		price_asks_b_g_zrxbtc = price_asks_b_l_zrxbtc 
		qty_asks_b_g_zrxbtc = qty_asks_b_l_zrxbtc 


def on_close_zrxbtc(ws): 
	print('### closed ###') 

def on_error_zrxbtc(ws, message): 
	print(message) 

def on_open_zrxbtc(ws): 
	ws.send(json.dumps({'sub': f'market.zrxbtc.ticker'})) 

def loop_zrxbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_zrxbtc, 
		on_close=on_close_zrxbtc, 
		on_error=on_error_zrxbtc) 
	ws.on_open = on_open_zrxbtc 
	ws.run_forever() 

Thread(target=loop_zrxbtc).start() 

def loop_zrxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_zrxusdt != 0.0 and qty_bids_a_g_zrxusdt != 0.0 and price_asks_a_g_zrxusdt != 0.0 and qty_asks_a_g_zrxusdt != 0.0 and price_bids_b_g_zrxbtc != 0.0 and qty_bids_b_g_zrxbtc != 0.0 and price_asks_b_g_zrxbtc != 0.0 and qty_asks_b_g_zrxbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_zrxusdt) 
			price_b = float(price_bids_b_g_zrxbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_zrxbtc, pribil)

Thread(target=loop_zrxusdt_Trade).start() 

symbol_a_g_ttusdt = 'ttusdt' 
price_bids_a_g_ttusdt = float(0.0) 
qty_bids_a_g_ttusdt = float(0.0) 
price_asks_a_g_ttusdt = float(0.0) 
qty_asks_a_g_ttusdt = float(0.0) 

def on_message_ttusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ttusdt = 'ttusdt' 
		price_bids_a_l_ttusdt = data['tick']['bid'] 
		qty_bids_a_l_ttusdt = data['tick']['bidSize'] 
		price_asks_a_l_ttusdt = data['tick']['ask'] 
		qty_asks_a_l_ttusdt = data['tick']['askSize'] 

		global symbol_a_g_ttusdt 
		global price_bids_a_g_ttusdt 
		global qty_bids_a_g_ttusdt 
		global price_asks_a_g_ttusdt 
		global qty_asks_a_g_ttusdt 

		symbol_a_g_ttusdt = symbol_a_l_ttusdt 
		price_bids_a_g_ttusdt = price_bids_a_l_ttusdt 
		qty_bids_a_g_ttusdt = qty_bids_a_l_ttusdt 
		price_asks_a_g_ttusdt = price_asks_a_l_ttusdt 
		qty_asks_a_g_ttusdt = qty_asks_a_l_ttusdt 

def on_close_ttusdt(ws): 
	print('### closed ###') 

def on_error_ttusdt(ws, message): 
	print(message) 

def on_open_ttusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ttusdt.ticker'})) 

def loop_ttusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ttusdt, 
		on_close=on_close_ttusdt, 
		on_error=on_error_ttusdt) 
	ws.on_open = on_open_ttusdt 
	ws.run_forever() 

Thread(target=loop_ttusdt).start() 

symbol_b_g_ttbtc = 'ttbtc' 
price_bids_b_g_ttbtc = float(0.0) 
qty_bids_b_g_ttbtc = float(0.0) 
price_asks_b_g_ttbtc = float(0.0) 
qty_asks_b_g_ttbtc = float(0.0) 

def on_message_ttbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ttbtc = 'ttbtc' 
		price_bids_b_l_ttbtc = data['tick']['bid'] 
		qty_bids_b_l_ttbtc = data['tick']['bidSize']
		price_asks_b_l_ttbtc = data['tick']['ask'] 
		qty_asks_b_l_ttbtc = data['tick']['askSize'] 

		global symbol_b_g_ttbtc 
		global price_bids_b_g_ttbtc 
		global qty_bids_b_g_ttbtc 
		global price_asks_b_g_ttbtc 
		global qty_asks_b_g_ttbtc 

		symbol_b_g_ttbtc = symbol_b_l_ttbtc 
		price_bids_b_g_ttbtc = price_bids_b_l_ttbtc 
		qty_bids_b_g_ttbtc = qty_bids_b_l_ttbtc 
		price_asks_b_g_ttbtc = price_asks_b_l_ttbtc 
		qty_asks_b_g_ttbtc = qty_asks_b_l_ttbtc 


def on_close_ttbtc(ws): 
	print('### closed ###') 

def on_error_ttbtc(ws, message): 
	print(message) 

def on_open_ttbtc(ws): 
	ws.send(json.dumps({'sub': f'market.ttbtc.ticker'})) 

def loop_ttbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ttbtc, 
		on_close=on_close_ttbtc, 
		on_error=on_error_ttbtc) 
	ws.on_open = on_open_ttbtc 
	ws.run_forever() 

Thread(target=loop_ttbtc).start() 

def loop_ttusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_ttusdt != 0.0 and qty_bids_a_g_ttusdt != 0.0 and price_asks_a_g_ttusdt != 0.0 and qty_asks_a_g_ttusdt != 0.0 and price_bids_b_g_ttbtc != 0.0 and qty_bids_b_g_ttbtc != 0.0 and price_asks_b_g_ttbtc != 0.0 and qty_asks_b_g_ttbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ttusdt) 
			price_b = float(price_bids_b_g_ttbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ttbtc, pribil)

Thread(target=loop_ttusdt_Trade).start() 

symbol_a_g_bsvusdt = 'bsvusdt' 
price_bids_a_g_bsvusdt = float(0.0) 
qty_bids_a_g_bsvusdt = float(0.0) 
price_asks_a_g_bsvusdt = float(0.0) 
qty_asks_a_g_bsvusdt = float(0.0) 

def on_message_bsvusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_bsvusdt = 'bsvusdt' 
		price_bids_a_l_bsvusdt = data['tick']['bid'] 
		qty_bids_a_l_bsvusdt = data['tick']['bidSize'] 
		price_asks_a_l_bsvusdt = data['tick']['ask'] 
		qty_asks_a_l_bsvusdt = data['tick']['askSize'] 

		global symbol_a_g_bsvusdt 
		global price_bids_a_g_bsvusdt 
		global qty_bids_a_g_bsvusdt 
		global price_asks_a_g_bsvusdt 
		global qty_asks_a_g_bsvusdt 

		symbol_a_g_bsvusdt = symbol_a_l_bsvusdt 
		price_bids_a_g_bsvusdt = price_bids_a_l_bsvusdt 
		qty_bids_a_g_bsvusdt = qty_bids_a_l_bsvusdt 
		price_asks_a_g_bsvusdt = price_asks_a_l_bsvusdt 
		qty_asks_a_g_bsvusdt = qty_asks_a_l_bsvusdt 

def on_close_bsvusdt(ws): 
	print('### closed ###') 

def on_error_bsvusdt(ws, message): 
	print(message) 

def on_open_bsvusdt(ws): 
	ws.send(json.dumps({'sub': f'market.bsvusdt.ticker'})) 

def loop_bsvusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bsvusdt, 
		on_close=on_close_bsvusdt, 
		on_error=on_error_bsvusdt) 
	ws.on_open = on_open_bsvusdt 
	ws.run_forever() 

Thread(target=loop_bsvusdt).start() 

symbol_b_g_bsvbtc = 'bsvbtc' 
price_bids_b_g_bsvbtc = float(0.0) 
qty_bids_b_g_bsvbtc = float(0.0) 
price_asks_b_g_bsvbtc = float(0.0) 
qty_asks_b_g_bsvbtc = float(0.0) 

def on_message_bsvbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_bsvbtc = 'bsvbtc' 
		price_bids_b_l_bsvbtc = data['tick']['bid'] 
		qty_bids_b_l_bsvbtc = data['tick']['bidSize']
		price_asks_b_l_bsvbtc = data['tick']['ask'] 
		qty_asks_b_l_bsvbtc = data['tick']['askSize'] 

		global symbol_b_g_bsvbtc 
		global price_bids_b_g_bsvbtc 
		global qty_bids_b_g_bsvbtc 
		global price_asks_b_g_bsvbtc 
		global qty_asks_b_g_bsvbtc 

		symbol_b_g_bsvbtc = symbol_b_l_bsvbtc 
		price_bids_b_g_bsvbtc = price_bids_b_l_bsvbtc 
		qty_bids_b_g_bsvbtc = qty_bids_b_l_bsvbtc 
		price_asks_b_g_bsvbtc = price_asks_b_l_bsvbtc 
		qty_asks_b_g_bsvbtc = qty_asks_b_l_bsvbtc 


def on_close_bsvbtc(ws): 
	print('### closed ###') 

def on_error_bsvbtc(ws, message): 
	print(message) 

def on_open_bsvbtc(ws): 
	ws.send(json.dumps({'sub': f'market.bsvbtc.ticker'})) 

def loop_bsvbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bsvbtc, 
		on_close=on_close_bsvbtc, 
		on_error=on_error_bsvbtc) 
	ws.on_open = on_open_bsvbtc 
	ws.run_forever() 

Thread(target=loop_bsvbtc).start() 

def loop_bsvusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_bsvusdt != 0.0 and qty_bids_a_g_bsvusdt != 0.0 and price_asks_a_g_bsvusdt != 0.0 and qty_asks_a_g_bsvusdt != 0.0 and price_bids_b_g_bsvbtc != 0.0 and qty_bids_b_g_bsvbtc != 0.0 and price_asks_b_g_bsvbtc != 0.0 and qty_asks_b_g_bsvbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_bsvusdt) 
			price_b = float(price_bids_b_g_bsvbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_bsvbtc, pribil)

Thread(target=loop_bsvusdt_Trade).start() 

symbol_a_g_polsusdt = 'polsusdt' 
price_bids_a_g_polsusdt = float(0.0) 
qty_bids_a_g_polsusdt = float(0.0) 
price_asks_a_g_polsusdt = float(0.0) 
qty_asks_a_g_polsusdt = float(0.0) 

def on_message_polsusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_polsusdt = 'polsusdt' 
		price_bids_a_l_polsusdt = data['tick']['bid'] 
		qty_bids_a_l_polsusdt = data['tick']['bidSize'] 
		price_asks_a_l_polsusdt = data['tick']['ask'] 
		qty_asks_a_l_polsusdt = data['tick']['askSize'] 

		global symbol_a_g_polsusdt 
		global price_bids_a_g_polsusdt 
		global qty_bids_a_g_polsusdt 
		global price_asks_a_g_polsusdt 
		global qty_asks_a_g_polsusdt 

		symbol_a_g_polsusdt = symbol_a_l_polsusdt 
		price_bids_a_g_polsusdt = price_bids_a_l_polsusdt 
		qty_bids_a_g_polsusdt = qty_bids_a_l_polsusdt 
		price_asks_a_g_polsusdt = price_asks_a_l_polsusdt 
		qty_asks_a_g_polsusdt = qty_asks_a_l_polsusdt 

def on_close_polsusdt(ws): 
	print('### closed ###') 

def on_error_polsusdt(ws, message): 
	print(message) 

def on_open_polsusdt(ws): 
	ws.send(json.dumps({'sub': f'market.polsusdt.ticker'})) 

def loop_polsusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_polsusdt, 
		on_close=on_close_polsusdt, 
		on_error=on_error_polsusdt) 
	ws.on_open = on_open_polsusdt 
	ws.run_forever() 

Thread(target=loop_polsusdt).start() 

symbol_b_g_polsbtc = 'polsbtc' 
price_bids_b_g_polsbtc = float(0.0) 
qty_bids_b_g_polsbtc = float(0.0) 
price_asks_b_g_polsbtc = float(0.0) 
qty_asks_b_g_polsbtc = float(0.0) 

def on_message_polsbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_polsbtc = 'polsbtc' 
		price_bids_b_l_polsbtc = data['tick']['bid'] 
		qty_bids_b_l_polsbtc = data['tick']['bidSize']
		price_asks_b_l_polsbtc = data['tick']['ask'] 
		qty_asks_b_l_polsbtc = data['tick']['askSize'] 

		global symbol_b_g_polsbtc 
		global price_bids_b_g_polsbtc 
		global qty_bids_b_g_polsbtc 
		global price_asks_b_g_polsbtc 
		global qty_asks_b_g_polsbtc 

		symbol_b_g_polsbtc = symbol_b_l_polsbtc 
		price_bids_b_g_polsbtc = price_bids_b_l_polsbtc 
		qty_bids_b_g_polsbtc = qty_bids_b_l_polsbtc 
		price_asks_b_g_polsbtc = price_asks_b_l_polsbtc 
		qty_asks_b_g_polsbtc = qty_asks_b_l_polsbtc 


def on_close_polsbtc(ws): 
	print('### closed ###') 

def on_error_polsbtc(ws, message): 
	print(message) 

def on_open_polsbtc(ws): 
	ws.send(json.dumps({'sub': f'market.polsbtc.ticker'})) 

def loop_polsbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_polsbtc, 
		on_close=on_close_polsbtc, 
		on_error=on_error_polsbtc) 
	ws.on_open = on_open_polsbtc 
	ws.run_forever() 

Thread(target=loop_polsbtc).start() 

def loop_polsusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_polsusdt != 0.0 and qty_bids_a_g_polsusdt != 0.0 and price_asks_a_g_polsusdt != 0.0 and qty_asks_a_g_polsusdt != 0.0 and price_bids_b_g_polsbtc != 0.0 and qty_bids_b_g_polsbtc != 0.0 and price_asks_b_g_polsbtc != 0.0 and qty_asks_b_g_polsbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_polsusdt) 
			price_b = float(price_bids_b_g_polsbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_polsbtc, pribil)

Thread(target=loop_polsusdt_Trade).start() 

symbol_a_g_wbtcusdt = 'wbtcusdt' 
price_bids_a_g_wbtcusdt = float(0.0) 
qty_bids_a_g_wbtcusdt = float(0.0) 
price_asks_a_g_wbtcusdt = float(0.0) 
qty_asks_a_g_wbtcusdt = float(0.0) 

def on_message_wbtcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_wbtcusdt = 'wbtcusdt' 
		price_bids_a_l_wbtcusdt = data['tick']['bid'] 
		qty_bids_a_l_wbtcusdt = data['tick']['bidSize'] 
		price_asks_a_l_wbtcusdt = data['tick']['ask'] 
		qty_asks_a_l_wbtcusdt = data['tick']['askSize'] 

		global symbol_a_g_wbtcusdt 
		global price_bids_a_g_wbtcusdt 
		global qty_bids_a_g_wbtcusdt 
		global price_asks_a_g_wbtcusdt 
		global qty_asks_a_g_wbtcusdt 

		symbol_a_g_wbtcusdt = symbol_a_l_wbtcusdt 
		price_bids_a_g_wbtcusdt = price_bids_a_l_wbtcusdt 
		qty_bids_a_g_wbtcusdt = qty_bids_a_l_wbtcusdt 
		price_asks_a_g_wbtcusdt = price_asks_a_l_wbtcusdt 
		qty_asks_a_g_wbtcusdt = qty_asks_a_l_wbtcusdt 

def on_close_wbtcusdt(ws): 
	print('### closed ###') 

def on_error_wbtcusdt(ws, message): 
	print(message) 

def on_open_wbtcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.wbtcusdt.ticker'})) 

def loop_wbtcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wbtcusdt, 
		on_close=on_close_wbtcusdt, 
		on_error=on_error_wbtcusdt) 
	ws.on_open = on_open_wbtcusdt 
	ws.run_forever() 

Thread(target=loop_wbtcusdt).start() 

symbol_b_g_wbtcbtc = 'wbtcbtc' 
price_bids_b_g_wbtcbtc = float(0.0) 
qty_bids_b_g_wbtcbtc = float(0.0) 
price_asks_b_g_wbtcbtc = float(0.0) 
qty_asks_b_g_wbtcbtc = float(0.0) 

def on_message_wbtcbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_wbtcbtc = 'wbtcbtc' 
		price_bids_b_l_wbtcbtc = data['tick']['bid'] 
		qty_bids_b_l_wbtcbtc = data['tick']['bidSize']
		price_asks_b_l_wbtcbtc = data['tick']['ask'] 
		qty_asks_b_l_wbtcbtc = data['tick']['askSize'] 

		global symbol_b_g_wbtcbtc 
		global price_bids_b_g_wbtcbtc 
		global qty_bids_b_g_wbtcbtc 
		global price_asks_b_g_wbtcbtc 
		global qty_asks_b_g_wbtcbtc 

		symbol_b_g_wbtcbtc = symbol_b_l_wbtcbtc 
		price_bids_b_g_wbtcbtc = price_bids_b_l_wbtcbtc 
		qty_bids_b_g_wbtcbtc = qty_bids_b_l_wbtcbtc 
		price_asks_b_g_wbtcbtc = price_asks_b_l_wbtcbtc 
		qty_asks_b_g_wbtcbtc = qty_asks_b_l_wbtcbtc 


def on_close_wbtcbtc(ws): 
	print('### closed ###') 

def on_error_wbtcbtc(ws, message): 
	print(message) 

def on_open_wbtcbtc(ws): 
	ws.send(json.dumps({'sub': f'market.wbtcbtc.ticker'})) 

def loop_wbtcbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wbtcbtc, 
		on_close=on_close_wbtcbtc, 
		on_error=on_error_wbtcbtc) 
	ws.on_open = on_open_wbtcbtc 
	ws.run_forever() 

Thread(target=loop_wbtcbtc).start() 

def loop_wbtcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_wbtcusdt != 0.0 and qty_bids_a_g_wbtcusdt != 0.0 and price_asks_a_g_wbtcusdt != 0.0 and qty_asks_a_g_wbtcusdt != 0.0 and price_bids_b_g_wbtcbtc != 0.0 and qty_bids_b_g_wbtcbtc != 0.0 and price_asks_b_g_wbtcbtc != 0.0 and qty_asks_b_g_wbtcbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_wbtcusdt) 
			price_b = float(price_bids_b_g_wbtcbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_wbtcbtc, pribil)

Thread(target=loop_wbtcusdt_Trade).start() 

symbol_a_g_mdxusdt = 'mdxusdt' 
price_bids_a_g_mdxusdt = float(0.0) 
qty_bids_a_g_mdxusdt = float(0.0) 
price_asks_a_g_mdxusdt = float(0.0) 
qty_asks_a_g_mdxusdt = float(0.0) 

def on_message_mdxusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_mdxusdt = 'mdxusdt' 
		price_bids_a_l_mdxusdt = data['tick']['bid'] 
		qty_bids_a_l_mdxusdt = data['tick']['bidSize'] 
		price_asks_a_l_mdxusdt = data['tick']['ask'] 
		qty_asks_a_l_mdxusdt = data['tick']['askSize'] 

		global symbol_a_g_mdxusdt 
		global price_bids_a_g_mdxusdt 
		global qty_bids_a_g_mdxusdt 
		global price_asks_a_g_mdxusdt 
		global qty_asks_a_g_mdxusdt 

		symbol_a_g_mdxusdt = symbol_a_l_mdxusdt 
		price_bids_a_g_mdxusdt = price_bids_a_l_mdxusdt 
		qty_bids_a_g_mdxusdt = qty_bids_a_l_mdxusdt 
		price_asks_a_g_mdxusdt = price_asks_a_l_mdxusdt 
		qty_asks_a_g_mdxusdt = qty_asks_a_l_mdxusdt 

def on_close_mdxusdt(ws): 
	print('### closed ###') 

def on_error_mdxusdt(ws, message): 
	print(message) 

def on_open_mdxusdt(ws): 
	ws.send(json.dumps({'sub': f'market.mdxusdt.ticker'})) 

def loop_mdxusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_mdxusdt, 
		on_close=on_close_mdxusdt, 
		on_error=on_error_mdxusdt) 
	ws.on_open = on_open_mdxusdt 
	ws.run_forever() 

Thread(target=loop_mdxusdt).start() 

symbol_b_g_mdxbtc = 'mdxbtc' 
price_bids_b_g_mdxbtc = float(0.0) 
qty_bids_b_g_mdxbtc = float(0.0) 
price_asks_b_g_mdxbtc = float(0.0) 
qty_asks_b_g_mdxbtc = float(0.0) 

def on_message_mdxbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_mdxbtc = 'mdxbtc' 
		price_bids_b_l_mdxbtc = data['tick']['bid'] 
		qty_bids_b_l_mdxbtc = data['tick']['bidSize']
		price_asks_b_l_mdxbtc = data['tick']['ask'] 
		qty_asks_b_l_mdxbtc = data['tick']['askSize'] 

		global symbol_b_g_mdxbtc 
		global price_bids_b_g_mdxbtc 
		global qty_bids_b_g_mdxbtc 
		global price_asks_b_g_mdxbtc 
		global qty_asks_b_g_mdxbtc 

		symbol_b_g_mdxbtc = symbol_b_l_mdxbtc 
		price_bids_b_g_mdxbtc = price_bids_b_l_mdxbtc 
		qty_bids_b_g_mdxbtc = qty_bids_b_l_mdxbtc 
		price_asks_b_g_mdxbtc = price_asks_b_l_mdxbtc 
		qty_asks_b_g_mdxbtc = qty_asks_b_l_mdxbtc 


def on_close_mdxbtc(ws): 
	print('### closed ###') 

def on_error_mdxbtc(ws, message): 
	print(message) 

def on_open_mdxbtc(ws): 
	ws.send(json.dumps({'sub': f'market.mdxbtc.ticker'})) 

def loop_mdxbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_mdxbtc, 
		on_close=on_close_mdxbtc, 
		on_error=on_error_mdxbtc) 
	ws.on_open = on_open_mdxbtc 
	ws.run_forever() 

Thread(target=loop_mdxbtc).start() 

def loop_mdxusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_mdxusdt != 0.0 and qty_bids_a_g_mdxusdt != 0.0 and price_asks_a_g_mdxusdt != 0.0 and qty_asks_a_g_mdxusdt != 0.0 and price_bids_b_g_mdxbtc != 0.0 and qty_bids_b_g_mdxbtc != 0.0 and price_asks_b_g_mdxbtc != 0.0 and qty_asks_b_g_mdxbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_mdxusdt) 
			price_b = float(price_bids_b_g_mdxbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_mdxbtc, pribil)

Thread(target=loop_mdxusdt_Trade).start() 

symbol_a_g_opusdt = 'opusdt' 
price_bids_a_g_opusdt = float(0.0) 
qty_bids_a_g_opusdt = float(0.0) 
price_asks_a_g_opusdt = float(0.0) 
qty_asks_a_g_opusdt = float(0.0) 

def on_message_opusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_opusdt = 'opusdt' 
		price_bids_a_l_opusdt = data['tick']['bid'] 
		qty_bids_a_l_opusdt = data['tick']['bidSize'] 
		price_asks_a_l_opusdt = data['tick']['ask'] 
		qty_asks_a_l_opusdt = data['tick']['askSize'] 

		global symbol_a_g_opusdt 
		global price_bids_a_g_opusdt 
		global qty_bids_a_g_opusdt 
		global price_asks_a_g_opusdt 
		global qty_asks_a_g_opusdt 

		symbol_a_g_opusdt = symbol_a_l_opusdt 
		price_bids_a_g_opusdt = price_bids_a_l_opusdt 
		qty_bids_a_g_opusdt = qty_bids_a_l_opusdt 
		price_asks_a_g_opusdt = price_asks_a_l_opusdt 
		qty_asks_a_g_opusdt = qty_asks_a_l_opusdt 

def on_close_opusdt(ws): 
	print('### closed ###') 

def on_error_opusdt(ws, message): 
	print(message) 

def on_open_opusdt(ws): 
	ws.send(json.dumps({'sub': f'market.opusdt.ticker'})) 

def loop_opusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_opusdt, 
		on_close=on_close_opusdt, 
		on_error=on_error_opusdt) 
	ws.on_open = on_open_opusdt 
	ws.run_forever() 

Thread(target=loop_opusdt).start() 

symbol_b_g_opusdc = 'opusdc' 
price_bids_b_g_opusdc = float(0.0) 
qty_bids_b_g_opusdc = float(0.0) 
price_asks_b_g_opusdc = float(0.0) 
qty_asks_b_g_opusdc = float(0.0) 

def on_message_opusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_opusdc = 'opusdc' 
		price_bids_b_l_opusdc = data['tick']['bid'] 
		qty_bids_b_l_opusdc = data['tick']['bidSize']
		price_asks_b_l_opusdc = data['tick']['ask'] 
		qty_asks_b_l_opusdc = data['tick']['askSize'] 

		global symbol_b_g_opusdc 
		global price_bids_b_g_opusdc 
		global qty_bids_b_g_opusdc 
		global price_asks_b_g_opusdc 
		global qty_asks_b_g_opusdc 

		symbol_b_g_opusdc = symbol_b_l_opusdc 
		price_bids_b_g_opusdc = price_bids_b_l_opusdc 
		qty_bids_b_g_opusdc = qty_bids_b_l_opusdc 
		price_asks_b_g_opusdc = price_asks_b_l_opusdc 
		qty_asks_b_g_opusdc = qty_asks_b_l_opusdc 


def on_close_opusdc(ws): 
	print('### closed ###') 

def on_error_opusdc(ws, message): 
	print(message) 

def on_open_opusdc(ws): 
	ws.send(json.dumps({'sub': f'market.opusdc.ticker'})) 

def loop_opusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_opusdc, 
		on_close=on_close_opusdc, 
		on_error=on_error_opusdc) 
	ws.on_open = on_open_opusdc 
	ws.run_forever() 

Thread(target=loop_opusdc).start() 

def loop_opusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_opusdt != 0.0 and qty_bids_a_g_opusdt != 0.0 and price_asks_a_g_opusdt != 0.0 and qty_asks_a_g_opusdt != 0.0 and price_bids_b_g_opusdc != 0.0 and qty_bids_b_g_opusdc != 0.0 and price_asks_b_g_opusdc != 0.0 and qty_asks_b_g_opusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_opusdt) 
			price_b = float(price_bids_b_g_opusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_opusdc, pribil)

Thread(target=loop_opusdt_Trade).start() 

symbol_a_g_crvusdt = 'crvusdt' 
price_bids_a_g_crvusdt = float(0.0) 
qty_bids_a_g_crvusdt = float(0.0) 
price_asks_a_g_crvusdt = float(0.0) 
qty_asks_a_g_crvusdt = float(0.0) 

def on_message_crvusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_crvusdt = 'crvusdt' 
		price_bids_a_l_crvusdt = data['tick']['bid'] 
		qty_bids_a_l_crvusdt = data['tick']['bidSize'] 
		price_asks_a_l_crvusdt = data['tick']['ask'] 
		qty_asks_a_l_crvusdt = data['tick']['askSize'] 

		global symbol_a_g_crvusdt 
		global price_bids_a_g_crvusdt 
		global qty_bids_a_g_crvusdt 
		global price_asks_a_g_crvusdt 
		global qty_asks_a_g_crvusdt 

		symbol_a_g_crvusdt = symbol_a_l_crvusdt 
		price_bids_a_g_crvusdt = price_bids_a_l_crvusdt 
		qty_bids_a_g_crvusdt = qty_bids_a_l_crvusdt 
		price_asks_a_g_crvusdt = price_asks_a_l_crvusdt 
		qty_asks_a_g_crvusdt = qty_asks_a_l_crvusdt 

def on_close_crvusdt(ws): 
	print('### closed ###') 

def on_error_crvusdt(ws, message): 
	print(message) 

def on_open_crvusdt(ws): 
	ws.send(json.dumps({'sub': f'market.crvusdt.ticker'})) 

def loop_crvusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_crvusdt, 
		on_close=on_close_crvusdt, 
		on_error=on_error_crvusdt) 
	ws.on_open = on_open_crvusdt 
	ws.run_forever() 

Thread(target=loop_crvusdt).start() 

symbol_b_g_crvbtc = 'crvbtc' 
price_bids_b_g_crvbtc = float(0.0) 
qty_bids_b_g_crvbtc = float(0.0) 
price_asks_b_g_crvbtc = float(0.0) 
qty_asks_b_g_crvbtc = float(0.0) 

def on_message_crvbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_crvbtc = 'crvbtc' 
		price_bids_b_l_crvbtc = data['tick']['bid'] 
		qty_bids_b_l_crvbtc = data['tick']['bidSize']
		price_asks_b_l_crvbtc = data['tick']['ask'] 
		qty_asks_b_l_crvbtc = data['tick']['askSize'] 

		global symbol_b_g_crvbtc 
		global price_bids_b_g_crvbtc 
		global qty_bids_b_g_crvbtc 
		global price_asks_b_g_crvbtc 
		global qty_asks_b_g_crvbtc 

		symbol_b_g_crvbtc = symbol_b_l_crvbtc 
		price_bids_b_g_crvbtc = price_bids_b_l_crvbtc 
		qty_bids_b_g_crvbtc = qty_bids_b_l_crvbtc 
		price_asks_b_g_crvbtc = price_asks_b_l_crvbtc 
		qty_asks_b_g_crvbtc = qty_asks_b_l_crvbtc 


def on_close_crvbtc(ws): 
	print('### closed ###') 

def on_error_crvbtc(ws, message): 
	print(message) 

def on_open_crvbtc(ws): 
	ws.send(json.dumps({'sub': f'market.crvbtc.ticker'})) 

def loop_crvbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_crvbtc, 
		on_close=on_close_crvbtc, 
		on_error=on_error_crvbtc) 
	ws.on_open = on_open_crvbtc 
	ws.run_forever() 

Thread(target=loop_crvbtc).start() 

def loop_crvusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_crvusdt != 0.0 and qty_bids_a_g_crvusdt != 0.0 and price_asks_a_g_crvusdt != 0.0 and qty_asks_a_g_crvusdt != 0.0 and price_bids_b_g_crvbtc != 0.0 and qty_bids_b_g_crvbtc != 0.0 and price_asks_b_g_crvbtc != 0.0 and qty_asks_b_g_crvbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_crvusdt) 
			price_b = float(price_bids_b_g_crvbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_crvbtc, pribil)

Thread(target=loop_crvusdt_Trade).start() 

symbol_a_g_zilusdt = 'zilusdt' 
price_bids_a_g_zilusdt = float(0.0) 
qty_bids_a_g_zilusdt = float(0.0) 
price_asks_a_g_zilusdt = float(0.0) 
qty_asks_a_g_zilusdt = float(0.0) 

def on_message_zilusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_zilusdt = 'zilusdt' 
		price_bids_a_l_zilusdt = data['tick']['bid'] 
		qty_bids_a_l_zilusdt = data['tick']['bidSize'] 
		price_asks_a_l_zilusdt = data['tick']['ask'] 
		qty_asks_a_l_zilusdt = data['tick']['askSize'] 

		global symbol_a_g_zilusdt 
		global price_bids_a_g_zilusdt 
		global qty_bids_a_g_zilusdt 
		global price_asks_a_g_zilusdt 
		global qty_asks_a_g_zilusdt 

		symbol_a_g_zilusdt = symbol_a_l_zilusdt 
		price_bids_a_g_zilusdt = price_bids_a_l_zilusdt 
		qty_bids_a_g_zilusdt = qty_bids_a_l_zilusdt 
		price_asks_a_g_zilusdt = price_asks_a_l_zilusdt 
		qty_asks_a_g_zilusdt = qty_asks_a_l_zilusdt 

def on_close_zilusdt(ws): 
	print('### closed ###') 

def on_error_zilusdt(ws, message): 
	print(message) 

def on_open_zilusdt(ws): 
	ws.send(json.dumps({'sub': f'market.zilusdt.ticker'})) 

def loop_zilusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_zilusdt, 
		on_close=on_close_zilusdt, 
		on_error=on_error_zilusdt) 
	ws.on_open = on_open_zilusdt 
	ws.run_forever() 

Thread(target=loop_zilusdt).start() 

symbol_b_g_zilbtc = 'zilbtc' 
price_bids_b_g_zilbtc = float(0.0) 
qty_bids_b_g_zilbtc = float(0.0) 
price_asks_b_g_zilbtc = float(0.0) 
qty_asks_b_g_zilbtc = float(0.0) 

def on_message_zilbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_zilbtc = 'zilbtc' 
		price_bids_b_l_zilbtc = data['tick']['bid'] 
		qty_bids_b_l_zilbtc = data['tick']['bidSize']
		price_asks_b_l_zilbtc = data['tick']['ask'] 
		qty_asks_b_l_zilbtc = data['tick']['askSize'] 

		global symbol_b_g_zilbtc 
		global price_bids_b_g_zilbtc 
		global qty_bids_b_g_zilbtc 
		global price_asks_b_g_zilbtc 
		global qty_asks_b_g_zilbtc 

		symbol_b_g_zilbtc = symbol_b_l_zilbtc 
		price_bids_b_g_zilbtc = price_bids_b_l_zilbtc 
		qty_bids_b_g_zilbtc = qty_bids_b_l_zilbtc 
		price_asks_b_g_zilbtc = price_asks_b_l_zilbtc 
		qty_asks_b_g_zilbtc = qty_asks_b_l_zilbtc 


def on_close_zilbtc(ws): 
	print('### closed ###') 

def on_error_zilbtc(ws, message): 
	print(message) 

def on_open_zilbtc(ws): 
	ws.send(json.dumps({'sub': f'market.zilbtc.ticker'})) 

def loop_zilbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_zilbtc, 
		on_close=on_close_zilbtc, 
		on_error=on_error_zilbtc) 
	ws.on_open = on_open_zilbtc 
	ws.run_forever() 

Thread(target=loop_zilbtc).start() 

def loop_zilusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_zilusdt != 0.0 and qty_bids_a_g_zilusdt != 0.0 and price_asks_a_g_zilusdt != 0.0 and qty_asks_a_g_zilusdt != 0.0 and price_bids_b_g_zilbtc != 0.0 and qty_bids_b_g_zilbtc != 0.0 and price_asks_b_g_zilbtc != 0.0 and qty_asks_b_g_zilbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_zilusdt) 
			price_b = float(price_bids_b_g_zilbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_zilbtc, pribil)

Thread(target=loop_zilusdt_Trade).start() 

symbol_a_g_ltcusdt = 'ltcusdt' 
price_bids_a_g_ltcusdt = float(0.0) 
qty_bids_a_g_ltcusdt = float(0.0) 
price_asks_a_g_ltcusdt = float(0.0) 
qty_asks_a_g_ltcusdt = float(0.0) 

def on_message_ltcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_ltcusdt = 'ltcusdt' 
		price_bids_a_l_ltcusdt = data['tick']['bid'] 
		qty_bids_a_l_ltcusdt = data['tick']['bidSize'] 
		price_asks_a_l_ltcusdt = data['tick']['ask'] 
		qty_asks_a_l_ltcusdt = data['tick']['askSize'] 

		global symbol_a_g_ltcusdt 
		global price_bids_a_g_ltcusdt 
		global qty_bids_a_g_ltcusdt 
		global price_asks_a_g_ltcusdt 
		global qty_asks_a_g_ltcusdt 

		symbol_a_g_ltcusdt = symbol_a_l_ltcusdt 
		price_bids_a_g_ltcusdt = price_bids_a_l_ltcusdt 
		qty_bids_a_g_ltcusdt = qty_bids_a_l_ltcusdt 
		price_asks_a_g_ltcusdt = price_asks_a_l_ltcusdt 
		qty_asks_a_g_ltcusdt = qty_asks_a_l_ltcusdt 

def on_close_ltcusdt(ws): 
	print('### closed ###') 

def on_error_ltcusdt(ws, message): 
	print(message) 

def on_open_ltcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.ltcusdt.ticker'})) 

def loop_ltcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ltcusdt, 
		on_close=on_close_ltcusdt, 
		on_error=on_error_ltcusdt) 
	ws.on_open = on_open_ltcusdt 
	ws.run_forever() 

Thread(target=loop_ltcusdt).start() 

symbol_b_g_ltcbtc = 'ltcbtc' 
price_bids_b_g_ltcbtc = float(0.0) 
qty_bids_b_g_ltcbtc = float(0.0) 
price_asks_b_g_ltcbtc = float(0.0) 
qty_asks_b_g_ltcbtc = float(0.0) 

def on_message_ltcbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_ltcbtc = 'ltcbtc' 
		price_bids_b_l_ltcbtc = data['tick']['bid'] 
		qty_bids_b_l_ltcbtc = data['tick']['bidSize']
		price_asks_b_l_ltcbtc = data['tick']['ask'] 
		qty_asks_b_l_ltcbtc = data['tick']['askSize'] 

		global symbol_b_g_ltcbtc 
		global price_bids_b_g_ltcbtc 
		global qty_bids_b_g_ltcbtc 
		global price_asks_b_g_ltcbtc 
		global qty_asks_b_g_ltcbtc 

		symbol_b_g_ltcbtc = symbol_b_l_ltcbtc 
		price_bids_b_g_ltcbtc = price_bids_b_l_ltcbtc 
		qty_bids_b_g_ltcbtc = qty_bids_b_l_ltcbtc 
		price_asks_b_g_ltcbtc = price_asks_b_l_ltcbtc 
		qty_asks_b_g_ltcbtc = qty_asks_b_l_ltcbtc 


def on_close_ltcbtc(ws): 
	print('### closed ###') 

def on_error_ltcbtc(ws, message): 
	print(message) 

def on_open_ltcbtc(ws): 
	ws.send(json.dumps({'sub': f'market.ltcbtc.ticker'})) 

def loop_ltcbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_ltcbtc, 
		on_close=on_close_ltcbtc, 
		on_error=on_error_ltcbtc) 
	ws.on_open = on_open_ltcbtc 
	ws.run_forever() 

Thread(target=loop_ltcbtc).start() 

def loop_ltcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_ltcusdt != 0.0 and qty_bids_a_g_ltcusdt != 0.0 and price_asks_a_g_ltcusdt != 0.0 and qty_asks_a_g_ltcusdt != 0.0 and price_bids_b_g_ltcbtc != 0.0 and qty_bids_b_g_ltcbtc != 0.0 and price_asks_b_g_ltcbtc != 0.0 and qty_asks_b_g_ltcbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_ltcusdt) 
			price_b = float(price_bids_b_g_ltcbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_ltcbtc, pribil)

Thread(target=loop_ltcusdt_Trade).start() 

symbol_a_g_nftusdt = 'nftusdt' 
price_bids_a_g_nftusdt = float(0.0) 
qty_bids_a_g_nftusdt = float(0.0) 
price_asks_a_g_nftusdt = float(0.0) 
qty_asks_a_g_nftusdt = float(0.0) 

def on_message_nftusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_nftusdt = 'nftusdt' 
		price_bids_a_l_nftusdt = data['tick']['bid'] 
		qty_bids_a_l_nftusdt = data['tick']['bidSize'] 
		price_asks_a_l_nftusdt = data['tick']['ask'] 
		qty_asks_a_l_nftusdt = data['tick']['askSize'] 

		global symbol_a_g_nftusdt 
		global price_bids_a_g_nftusdt 
		global qty_bids_a_g_nftusdt 
		global price_asks_a_g_nftusdt 
		global qty_asks_a_g_nftusdt 

		symbol_a_g_nftusdt = symbol_a_l_nftusdt 
		price_bids_a_g_nftusdt = price_bids_a_l_nftusdt 
		qty_bids_a_g_nftusdt = qty_bids_a_l_nftusdt 
		price_asks_a_g_nftusdt = price_asks_a_l_nftusdt 
		qty_asks_a_g_nftusdt = qty_asks_a_l_nftusdt 

def on_close_nftusdt(ws): 
	print('### closed ###') 

def on_error_nftusdt(ws, message): 
	print(message) 

def on_open_nftusdt(ws): 
	ws.send(json.dumps({'sub': f'market.nftusdt.ticker'})) 

def loop_nftusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nftusdt, 
		on_close=on_close_nftusdt, 
		on_error=on_error_nftusdt) 
	ws.on_open = on_open_nftusdt 
	ws.run_forever() 

Thread(target=loop_nftusdt).start() 

symbol_b_g_nftusdd = 'nftusdd' 
price_bids_b_g_nftusdd = float(0.0) 
qty_bids_b_g_nftusdd = float(0.0) 
price_asks_b_g_nftusdd = float(0.0) 
qty_asks_b_g_nftusdd = float(0.0) 

def on_message_nftusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_nftusdd = 'nftusdd' 
		price_bids_b_l_nftusdd = data['tick']['bid'] 
		qty_bids_b_l_nftusdd = data['tick']['bidSize']
		price_asks_b_l_nftusdd = data['tick']['ask'] 
		qty_asks_b_l_nftusdd = data['tick']['askSize'] 

		global symbol_b_g_nftusdd 
		global price_bids_b_g_nftusdd 
		global qty_bids_b_g_nftusdd 
		global price_asks_b_g_nftusdd 
		global qty_asks_b_g_nftusdd 

		symbol_b_g_nftusdd = symbol_b_l_nftusdd 
		price_bids_b_g_nftusdd = price_bids_b_l_nftusdd 
		qty_bids_b_g_nftusdd = qty_bids_b_l_nftusdd 
		price_asks_b_g_nftusdd = price_asks_b_l_nftusdd 
		qty_asks_b_g_nftusdd = qty_asks_b_l_nftusdd 


def on_close_nftusdd(ws): 
	print('### closed ###') 

def on_error_nftusdd(ws, message): 
	print(message) 

def on_open_nftusdd(ws): 
	ws.send(json.dumps({'sub': f'market.nftusdd.ticker'})) 

def loop_nftusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nftusdd, 
		on_close=on_close_nftusdd, 
		on_error=on_error_nftusdd) 
	ws.on_open = on_open_nftusdd 
	ws.run_forever() 

Thread(target=loop_nftusdd).start() 

def loop_nftusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_nftusdt != 0.0 and qty_bids_a_g_nftusdt != 0.0 and price_asks_a_g_nftusdt != 0.0 and qty_asks_a_g_nftusdt != 0.0 and price_bids_b_g_nftusdd != 0.0 and qty_bids_b_g_nftusdd != 0.0 and price_asks_b_g_nftusdd != 0.0 and qty_asks_b_g_nftusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_nftusdt) 
			price_b = float(price_bids_b_g_nftusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_nftusdd, pribil)

Thread(target=loop_nftusdt_Trade).start() 

symbol_a_g_umausdt = 'umausdt' 
price_bids_a_g_umausdt = float(0.0) 
qty_bids_a_g_umausdt = float(0.0) 
price_asks_a_g_umausdt = float(0.0) 
qty_asks_a_g_umausdt = float(0.0) 

def on_message_umausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_umausdt = 'umausdt' 
		price_bids_a_l_umausdt = data['tick']['bid'] 
		qty_bids_a_l_umausdt = data['tick']['bidSize'] 
		price_asks_a_l_umausdt = data['tick']['ask'] 
		qty_asks_a_l_umausdt = data['tick']['askSize'] 

		global symbol_a_g_umausdt 
		global price_bids_a_g_umausdt 
		global qty_bids_a_g_umausdt 
		global price_asks_a_g_umausdt 
		global qty_asks_a_g_umausdt 

		symbol_a_g_umausdt = symbol_a_l_umausdt 
		price_bids_a_g_umausdt = price_bids_a_l_umausdt 
		qty_bids_a_g_umausdt = qty_bids_a_l_umausdt 
		price_asks_a_g_umausdt = price_asks_a_l_umausdt 
		qty_asks_a_g_umausdt = qty_asks_a_l_umausdt 

def on_close_umausdt(ws): 
	print('### closed ###') 

def on_error_umausdt(ws, message): 
	print(message) 

def on_open_umausdt(ws): 
	ws.send(json.dumps({'sub': f'market.umausdt.ticker'})) 

def loop_umausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_umausdt, 
		on_close=on_close_umausdt, 
		on_error=on_error_umausdt) 
	ws.on_open = on_open_umausdt 
	ws.run_forever() 

Thread(target=loop_umausdt).start() 

symbol_b_g_umabtc = 'umabtc' 
price_bids_b_g_umabtc = float(0.0) 
qty_bids_b_g_umabtc = float(0.0) 
price_asks_b_g_umabtc = float(0.0) 
qty_asks_b_g_umabtc = float(0.0) 

def on_message_umabtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_umabtc = 'umabtc' 
		price_bids_b_l_umabtc = data['tick']['bid'] 
		qty_bids_b_l_umabtc = data['tick']['bidSize']
		price_asks_b_l_umabtc = data['tick']['ask'] 
		qty_asks_b_l_umabtc = data['tick']['askSize'] 

		global symbol_b_g_umabtc 
		global price_bids_b_g_umabtc 
		global qty_bids_b_g_umabtc 
		global price_asks_b_g_umabtc 
		global qty_asks_b_g_umabtc 

		symbol_b_g_umabtc = symbol_b_l_umabtc 
		price_bids_b_g_umabtc = price_bids_b_l_umabtc 
		qty_bids_b_g_umabtc = qty_bids_b_l_umabtc 
		price_asks_b_g_umabtc = price_asks_b_l_umabtc 
		qty_asks_b_g_umabtc = qty_asks_b_l_umabtc 


def on_close_umabtc(ws): 
	print('### closed ###') 

def on_error_umabtc(ws, message): 
	print(message) 

def on_open_umabtc(ws): 
	ws.send(json.dumps({'sub': f'market.umabtc.ticker'})) 

def loop_umabtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_umabtc, 
		on_close=on_close_umabtc, 
		on_error=on_error_umabtc) 
	ws.on_open = on_open_umabtc 
	ws.run_forever() 

Thread(target=loop_umabtc).start() 

def loop_umausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_umausdt != 0.0 and qty_bids_a_g_umausdt != 0.0 and price_asks_a_g_umausdt != 0.0 and qty_asks_a_g_umausdt != 0.0 and price_bids_b_g_umabtc != 0.0 and qty_bids_b_g_umabtc != 0.0 and price_asks_b_g_umabtc != 0.0 and qty_asks_b_g_umabtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_umausdt) 
			price_b = float(price_bids_b_g_umabtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_umabtc, pribil)

Thread(target=loop_umausdt_Trade).start() 

symbol_a_g_kcalusdt = 'kcalusdt' 
price_bids_a_g_kcalusdt = float(0.0) 
qty_bids_a_g_kcalusdt = float(0.0) 
price_asks_a_g_kcalusdt = float(0.0) 
qty_asks_a_g_kcalusdt = float(0.0) 

def on_message_kcalusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_kcalusdt = 'kcalusdt' 
		price_bids_a_l_kcalusdt = data['tick']['bid'] 
		qty_bids_a_l_kcalusdt = data['tick']['bidSize'] 
		price_asks_a_l_kcalusdt = data['tick']['ask'] 
		qty_asks_a_l_kcalusdt = data['tick']['askSize'] 

		global symbol_a_g_kcalusdt 
		global price_bids_a_g_kcalusdt 
		global qty_bids_a_g_kcalusdt 
		global price_asks_a_g_kcalusdt 
		global qty_asks_a_g_kcalusdt 

		symbol_a_g_kcalusdt = symbol_a_l_kcalusdt 
		price_bids_a_g_kcalusdt = price_bids_a_l_kcalusdt 
		qty_bids_a_g_kcalusdt = qty_bids_a_l_kcalusdt 
		price_asks_a_g_kcalusdt = price_asks_a_l_kcalusdt 
		qty_asks_a_g_kcalusdt = qty_asks_a_l_kcalusdt 

def on_close_kcalusdt(ws): 
	print('### closed ###') 

def on_error_kcalusdt(ws, message): 
	print(message) 

def on_open_kcalusdt(ws): 
	ws.send(json.dumps({'sub': f'market.kcalusdt.ticker'})) 

def loop_kcalusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kcalusdt, 
		on_close=on_close_kcalusdt, 
		on_error=on_error_kcalusdt) 
	ws.on_open = on_open_kcalusdt 
	ws.run_forever() 

Thread(target=loop_kcalusdt).start() 

symbol_b_g_kcalusdd = 'kcalusdd' 
price_bids_b_g_kcalusdd = float(0.0) 
qty_bids_b_g_kcalusdd = float(0.0) 
price_asks_b_g_kcalusdd = float(0.0) 
qty_asks_b_g_kcalusdd = float(0.0) 

def on_message_kcalusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_kcalusdd = 'kcalusdd' 
		price_bids_b_l_kcalusdd = data['tick']['bid'] 
		qty_bids_b_l_kcalusdd = data['tick']['bidSize']
		price_asks_b_l_kcalusdd = data['tick']['ask'] 
		qty_asks_b_l_kcalusdd = data['tick']['askSize'] 

		global symbol_b_g_kcalusdd 
		global price_bids_b_g_kcalusdd 
		global qty_bids_b_g_kcalusdd 
		global price_asks_b_g_kcalusdd 
		global qty_asks_b_g_kcalusdd 

		symbol_b_g_kcalusdd = symbol_b_l_kcalusdd 
		price_bids_b_g_kcalusdd = price_bids_b_l_kcalusdd 
		qty_bids_b_g_kcalusdd = qty_bids_b_l_kcalusdd 
		price_asks_b_g_kcalusdd = price_asks_b_l_kcalusdd 
		qty_asks_b_g_kcalusdd = qty_asks_b_l_kcalusdd 


def on_close_kcalusdd(ws): 
	print('### closed ###') 

def on_error_kcalusdd(ws, message): 
	print(message) 

def on_open_kcalusdd(ws): 
	ws.send(json.dumps({'sub': f'market.kcalusdd.ticker'})) 

def loop_kcalusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kcalusdd, 
		on_close=on_close_kcalusdd, 
		on_error=on_error_kcalusdd) 
	ws.on_open = on_open_kcalusdd 
	ws.run_forever() 

Thread(target=loop_kcalusdd).start() 

def loop_kcalusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_kcalusdt != 0.0 and qty_bids_a_g_kcalusdt != 0.0 and price_asks_a_g_kcalusdt != 0.0 and qty_asks_a_g_kcalusdt != 0.0 and price_bids_b_g_kcalusdd != 0.0 and qty_bids_b_g_kcalusdd != 0.0 and price_asks_b_g_kcalusdd != 0.0 and qty_asks_b_g_kcalusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_kcalusdt) 
			price_b = float(price_bids_b_g_kcalusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_kcalusdd, pribil)

Thread(target=loop_kcalusdt_Trade).start() 

symbol_a_g_api3usdt = 'api3usdt' 
price_bids_a_g_api3usdt = float(0.0) 
qty_bids_a_g_api3usdt = float(0.0) 
price_asks_a_g_api3usdt = float(0.0) 
qty_asks_a_g_api3usdt = float(0.0) 

def on_message_api3usdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_api3usdt = 'api3usdt' 
		price_bids_a_l_api3usdt = data['tick']['bid'] 
		qty_bids_a_l_api3usdt = data['tick']['bidSize'] 
		price_asks_a_l_api3usdt = data['tick']['ask'] 
		qty_asks_a_l_api3usdt = data['tick']['askSize'] 

		global symbol_a_g_api3usdt 
		global price_bids_a_g_api3usdt 
		global qty_bids_a_g_api3usdt 
		global price_asks_a_g_api3usdt 
		global qty_asks_a_g_api3usdt 

		symbol_a_g_api3usdt = symbol_a_l_api3usdt 
		price_bids_a_g_api3usdt = price_bids_a_l_api3usdt 
		qty_bids_a_g_api3usdt = qty_bids_a_l_api3usdt 
		price_asks_a_g_api3usdt = price_asks_a_l_api3usdt 
		qty_asks_a_g_api3usdt = qty_asks_a_l_api3usdt 

def on_close_api3usdt(ws): 
	print('### closed ###') 

def on_error_api3usdt(ws, message): 
	print(message) 

def on_open_api3usdt(ws): 
	ws.send(json.dumps({'sub': f'market.api3usdt.ticker'})) 

def loop_api3usdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_api3usdt, 
		on_close=on_close_api3usdt, 
		on_error=on_error_api3usdt) 
	ws.on_open = on_open_api3usdt 
	ws.run_forever() 

Thread(target=loop_api3usdt).start() 

symbol_b_g_api3btc = 'api3btc' 
price_bids_b_g_api3btc = float(0.0) 
qty_bids_b_g_api3btc = float(0.0) 
price_asks_b_g_api3btc = float(0.0) 
qty_asks_b_g_api3btc = float(0.0) 

def on_message_api3btc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_api3btc = 'api3btc' 
		price_bids_b_l_api3btc = data['tick']['bid'] 
		qty_bids_b_l_api3btc = data['tick']['bidSize']
		price_asks_b_l_api3btc = data['tick']['ask'] 
		qty_asks_b_l_api3btc = data['tick']['askSize'] 

		global symbol_b_g_api3btc 
		global price_bids_b_g_api3btc 
		global qty_bids_b_g_api3btc 
		global price_asks_b_g_api3btc 
		global qty_asks_b_g_api3btc 

		symbol_b_g_api3btc = symbol_b_l_api3btc 
		price_bids_b_g_api3btc = price_bids_b_l_api3btc 
		qty_bids_b_g_api3btc = qty_bids_b_l_api3btc 
		price_asks_b_g_api3btc = price_asks_b_l_api3btc 
		qty_asks_b_g_api3btc = qty_asks_b_l_api3btc 


def on_close_api3btc(ws): 
	print('### closed ###') 

def on_error_api3btc(ws, message): 
	print(message) 

def on_open_api3btc(ws): 
	ws.send(json.dumps({'sub': f'market.api3btc.ticker'})) 

def loop_api3btc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_api3btc, 
		on_close=on_close_api3btc, 
		on_error=on_error_api3btc) 
	ws.on_open = on_open_api3btc 
	ws.run_forever() 

Thread(target=loop_api3btc).start() 

def loop_api3usdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_api3usdt != 0.0 and qty_bids_a_g_api3usdt != 0.0 and price_asks_a_g_api3usdt != 0.0 and qty_asks_a_g_api3usdt != 0.0 and price_bids_b_g_api3btc != 0.0 and qty_bids_b_g_api3btc != 0.0 and price_asks_b_g_api3btc != 0.0 and qty_asks_b_g_api3btc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_api3usdt) 
			price_b = float(price_bids_b_g_api3btc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_api3btc, pribil)

Thread(target=loop_api3usdt_Trade).start() 

symbol_a_g_vsysusdt = 'vsysusdt' 
price_bids_a_g_vsysusdt = float(0.0) 
qty_bids_a_g_vsysusdt = float(0.0) 
price_asks_a_g_vsysusdt = float(0.0) 
qty_asks_a_g_vsysusdt = float(0.0) 

def on_message_vsysusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_vsysusdt = 'vsysusdt' 
		price_bids_a_l_vsysusdt = data['tick']['bid'] 
		qty_bids_a_l_vsysusdt = data['tick']['bidSize'] 
		price_asks_a_l_vsysusdt = data['tick']['ask'] 
		qty_asks_a_l_vsysusdt = data['tick']['askSize'] 

		global symbol_a_g_vsysusdt 
		global price_bids_a_g_vsysusdt 
		global qty_bids_a_g_vsysusdt 
		global price_asks_a_g_vsysusdt 
		global qty_asks_a_g_vsysusdt 

		symbol_a_g_vsysusdt = symbol_a_l_vsysusdt 
		price_bids_a_g_vsysusdt = price_bids_a_l_vsysusdt 
		qty_bids_a_g_vsysusdt = qty_bids_a_l_vsysusdt 
		price_asks_a_g_vsysusdt = price_asks_a_l_vsysusdt 
		qty_asks_a_g_vsysusdt = qty_asks_a_l_vsysusdt 

def on_close_vsysusdt(ws): 
	print('### closed ###') 

def on_error_vsysusdt(ws, message): 
	print(message) 

def on_open_vsysusdt(ws): 
	ws.send(json.dumps({'sub': f'market.vsysusdt.ticker'})) 

def loop_vsysusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_vsysusdt, 
		on_close=on_close_vsysusdt, 
		on_error=on_error_vsysusdt) 
	ws.on_open = on_open_vsysusdt 
	ws.run_forever() 

Thread(target=loop_vsysusdt).start() 

symbol_b_g_vsysbtc = 'vsysbtc' 
price_bids_b_g_vsysbtc = float(0.0) 
qty_bids_b_g_vsysbtc = float(0.0) 
price_asks_b_g_vsysbtc = float(0.0) 
qty_asks_b_g_vsysbtc = float(0.0) 

def on_message_vsysbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_vsysbtc = 'vsysbtc' 
		price_bids_b_l_vsysbtc = data['tick']['bid'] 
		qty_bids_b_l_vsysbtc = data['tick']['bidSize']
		price_asks_b_l_vsysbtc = data['tick']['ask'] 
		qty_asks_b_l_vsysbtc = data['tick']['askSize'] 

		global symbol_b_g_vsysbtc 
		global price_bids_b_g_vsysbtc 
		global qty_bids_b_g_vsysbtc 
		global price_asks_b_g_vsysbtc 
		global qty_asks_b_g_vsysbtc 

		symbol_b_g_vsysbtc = symbol_b_l_vsysbtc 
		price_bids_b_g_vsysbtc = price_bids_b_l_vsysbtc 
		qty_bids_b_g_vsysbtc = qty_bids_b_l_vsysbtc 
		price_asks_b_g_vsysbtc = price_asks_b_l_vsysbtc 
		qty_asks_b_g_vsysbtc = qty_asks_b_l_vsysbtc 


def on_close_vsysbtc(ws): 
	print('### closed ###') 

def on_error_vsysbtc(ws, message): 
	print(message) 

def on_open_vsysbtc(ws): 
	ws.send(json.dumps({'sub': f'market.vsysbtc.ticker'})) 

def loop_vsysbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_vsysbtc, 
		on_close=on_close_vsysbtc, 
		on_error=on_error_vsysbtc) 
	ws.on_open = on_open_vsysbtc 
	ws.run_forever() 

Thread(target=loop_vsysbtc).start() 

def loop_vsysusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_vsysusdt != 0.0 and qty_bids_a_g_vsysusdt != 0.0 and price_asks_a_g_vsysusdt != 0.0 and qty_asks_a_g_vsysusdt != 0.0 and price_bids_b_g_vsysbtc != 0.0 and qty_bids_b_g_vsysbtc != 0.0 and price_asks_b_g_vsysbtc != 0.0 and qty_asks_b_g_vsysbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_vsysusdt) 
			price_b = float(price_bids_b_g_vsysbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_vsysbtc, pribil)

Thread(target=loop_vsysusdt_Trade).start() 

symbol_a_g_iotausdt = 'iotausdt' 
price_bids_a_g_iotausdt = float(0.0) 
qty_bids_a_g_iotausdt = float(0.0) 
price_asks_a_g_iotausdt = float(0.0) 
qty_asks_a_g_iotausdt = float(0.0) 

def on_message_iotausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_iotausdt = 'iotausdt' 
		price_bids_a_l_iotausdt = data['tick']['bid'] 
		qty_bids_a_l_iotausdt = data['tick']['bidSize'] 
		price_asks_a_l_iotausdt = data['tick']['ask'] 
		qty_asks_a_l_iotausdt = data['tick']['askSize'] 

		global symbol_a_g_iotausdt 
		global price_bids_a_g_iotausdt 
		global qty_bids_a_g_iotausdt 
		global price_asks_a_g_iotausdt 
		global qty_asks_a_g_iotausdt 

		symbol_a_g_iotausdt = symbol_a_l_iotausdt 
		price_bids_a_g_iotausdt = price_bids_a_l_iotausdt 
		qty_bids_a_g_iotausdt = qty_bids_a_l_iotausdt 
		price_asks_a_g_iotausdt = price_asks_a_l_iotausdt 
		qty_asks_a_g_iotausdt = qty_asks_a_l_iotausdt 

def on_close_iotausdt(ws): 
	print('### closed ###') 

def on_error_iotausdt(ws, message): 
	print(message) 

def on_open_iotausdt(ws): 
	ws.send(json.dumps({'sub': f'market.iotausdt.ticker'})) 

def loop_iotausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_iotausdt, 
		on_close=on_close_iotausdt, 
		on_error=on_error_iotausdt) 
	ws.on_open = on_open_iotausdt 
	ws.run_forever() 

Thread(target=loop_iotausdt).start() 

symbol_b_g_iotabtc = 'iotabtc' 
price_bids_b_g_iotabtc = float(0.0) 
qty_bids_b_g_iotabtc = float(0.0) 
price_asks_b_g_iotabtc = float(0.0) 
qty_asks_b_g_iotabtc = float(0.0) 

def on_message_iotabtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_iotabtc = 'iotabtc' 
		price_bids_b_l_iotabtc = data['tick']['bid'] 
		qty_bids_b_l_iotabtc = data['tick']['bidSize']
		price_asks_b_l_iotabtc = data['tick']['ask'] 
		qty_asks_b_l_iotabtc = data['tick']['askSize'] 

		global symbol_b_g_iotabtc 
		global price_bids_b_g_iotabtc 
		global qty_bids_b_g_iotabtc 
		global price_asks_b_g_iotabtc 
		global qty_asks_b_g_iotabtc 

		symbol_b_g_iotabtc = symbol_b_l_iotabtc 
		price_bids_b_g_iotabtc = price_bids_b_l_iotabtc 
		qty_bids_b_g_iotabtc = qty_bids_b_l_iotabtc 
		price_asks_b_g_iotabtc = price_asks_b_l_iotabtc 
		qty_asks_b_g_iotabtc = qty_asks_b_l_iotabtc 


def on_close_iotabtc(ws): 
	print('### closed ###') 

def on_error_iotabtc(ws, message): 
	print(message) 

def on_open_iotabtc(ws): 
	ws.send(json.dumps({'sub': f'market.iotabtc.ticker'})) 

def loop_iotabtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_iotabtc, 
		on_close=on_close_iotabtc, 
		on_error=on_error_iotabtc) 
	ws.on_open = on_open_iotabtc 
	ws.run_forever() 

Thread(target=loop_iotabtc).start() 

def loop_iotausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_iotausdt != 0.0 and qty_bids_a_g_iotausdt != 0.0 and price_asks_a_g_iotausdt != 0.0 and qty_asks_a_g_iotausdt != 0.0 and price_bids_b_g_iotabtc != 0.0 and qty_bids_b_g_iotabtc != 0.0 and price_asks_b_g_iotabtc != 0.0 and qty_asks_b_g_iotabtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_iotausdt) 
			price_b = float(price_bids_b_g_iotabtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_iotabtc, pribil)

Thread(target=loop_iotausdt_Trade).start() 

symbol_a_g_swftcusdt = 'swftcusdt' 
price_bids_a_g_swftcusdt = float(0.0) 
qty_bids_a_g_swftcusdt = float(0.0) 
price_asks_a_g_swftcusdt = float(0.0) 
qty_asks_a_g_swftcusdt = float(0.0) 

def on_message_swftcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_swftcusdt = 'swftcusdt' 
		price_bids_a_l_swftcusdt = data['tick']['bid'] 
		qty_bids_a_l_swftcusdt = data['tick']['bidSize'] 
		price_asks_a_l_swftcusdt = data['tick']['ask'] 
		qty_asks_a_l_swftcusdt = data['tick']['askSize'] 

		global symbol_a_g_swftcusdt 
		global price_bids_a_g_swftcusdt 
		global qty_bids_a_g_swftcusdt 
		global price_asks_a_g_swftcusdt 
		global qty_asks_a_g_swftcusdt 

		symbol_a_g_swftcusdt = symbol_a_l_swftcusdt 
		price_bids_a_g_swftcusdt = price_bids_a_l_swftcusdt 
		qty_bids_a_g_swftcusdt = qty_bids_a_l_swftcusdt 
		price_asks_a_g_swftcusdt = price_asks_a_l_swftcusdt 
		qty_asks_a_g_swftcusdt = qty_asks_a_l_swftcusdt 

def on_close_swftcusdt(ws): 
	print('### closed ###') 

def on_error_swftcusdt(ws, message): 
	print(message) 

def on_open_swftcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.swftcusdt.ticker'})) 

def loop_swftcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_swftcusdt, 
		on_close=on_close_swftcusdt, 
		on_error=on_error_swftcusdt) 
	ws.on_open = on_open_swftcusdt 
	ws.run_forever() 

Thread(target=loop_swftcusdt).start() 

symbol_b_g_swftcbtc = 'swftcbtc' 
price_bids_b_g_swftcbtc = float(0.0) 
qty_bids_b_g_swftcbtc = float(0.0) 
price_asks_b_g_swftcbtc = float(0.0) 
qty_asks_b_g_swftcbtc = float(0.0) 

def on_message_swftcbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_swftcbtc = 'swftcbtc' 
		price_bids_b_l_swftcbtc = data['tick']['bid'] 
		qty_bids_b_l_swftcbtc = data['tick']['bidSize']
		price_asks_b_l_swftcbtc = data['tick']['ask'] 
		qty_asks_b_l_swftcbtc = data['tick']['askSize'] 

		global symbol_b_g_swftcbtc 
		global price_bids_b_g_swftcbtc 
		global qty_bids_b_g_swftcbtc 
		global price_asks_b_g_swftcbtc 
		global qty_asks_b_g_swftcbtc 

		symbol_b_g_swftcbtc = symbol_b_l_swftcbtc 
		price_bids_b_g_swftcbtc = price_bids_b_l_swftcbtc 
		qty_bids_b_g_swftcbtc = qty_bids_b_l_swftcbtc 
		price_asks_b_g_swftcbtc = price_asks_b_l_swftcbtc 
		qty_asks_b_g_swftcbtc = qty_asks_b_l_swftcbtc 


def on_close_swftcbtc(ws): 
	print('### closed ###') 

def on_error_swftcbtc(ws, message): 
	print(message) 

def on_open_swftcbtc(ws): 
	ws.send(json.dumps({'sub': f'market.swftcbtc.ticker'})) 

def loop_swftcbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_swftcbtc, 
		on_close=on_close_swftcbtc, 
		on_error=on_error_swftcbtc) 
	ws.on_open = on_open_swftcbtc 
	ws.run_forever() 

Thread(target=loop_swftcbtc).start() 

def loop_swftcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_swftcusdt != 0.0 and qty_bids_a_g_swftcusdt != 0.0 and price_asks_a_g_swftcusdt != 0.0 and qty_asks_a_g_swftcusdt != 0.0 and price_bids_b_g_swftcbtc != 0.0 and qty_bids_b_g_swftcbtc != 0.0 and price_asks_b_g_swftcbtc != 0.0 and qty_asks_b_g_swftcbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_swftcusdt) 
			price_b = float(price_bids_b_g_swftcbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_swftcbtc, pribil)

Thread(target=loop_swftcusdt_Trade).start() 

symbol_a_g_sklusdt = 'sklusdt' 
price_bids_a_g_sklusdt = float(0.0) 
qty_bids_a_g_sklusdt = float(0.0) 
price_asks_a_g_sklusdt = float(0.0) 
qty_asks_a_g_sklusdt = float(0.0) 

def on_message_sklusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_sklusdt = 'sklusdt' 
		price_bids_a_l_sklusdt = data['tick']['bid'] 
		qty_bids_a_l_sklusdt = data['tick']['bidSize'] 
		price_asks_a_l_sklusdt = data['tick']['ask'] 
		qty_asks_a_l_sklusdt = data['tick']['askSize'] 

		global symbol_a_g_sklusdt 
		global price_bids_a_g_sklusdt 
		global qty_bids_a_g_sklusdt 
		global price_asks_a_g_sklusdt 
		global qty_asks_a_g_sklusdt 

		symbol_a_g_sklusdt = symbol_a_l_sklusdt 
		price_bids_a_g_sklusdt = price_bids_a_l_sklusdt 
		qty_bids_a_g_sklusdt = qty_bids_a_l_sklusdt 
		price_asks_a_g_sklusdt = price_asks_a_l_sklusdt 
		qty_asks_a_g_sklusdt = qty_asks_a_l_sklusdt 

def on_close_sklusdt(ws): 
	print('### closed ###') 

def on_error_sklusdt(ws, message): 
	print(message) 

def on_open_sklusdt(ws): 
	ws.send(json.dumps({'sub': f'market.sklusdt.ticker'})) 

def loop_sklusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sklusdt, 
		on_close=on_close_sklusdt, 
		on_error=on_error_sklusdt) 
	ws.on_open = on_open_sklusdt 
	ws.run_forever() 

Thread(target=loop_sklusdt).start() 

symbol_b_g_skleth = 'skleth' 
price_bids_b_g_skleth = float(0.0) 
qty_bids_b_g_skleth = float(0.0) 
price_asks_b_g_skleth = float(0.0) 
qty_asks_b_g_skleth = float(0.0) 

def on_message_skleth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_skleth = 'skleth' 
		price_bids_b_l_skleth = data['tick']['bid'] 
		qty_bids_b_l_skleth = data['tick']['bidSize']
		price_asks_b_l_skleth = data['tick']['ask'] 
		qty_asks_b_l_skleth = data['tick']['askSize'] 

		global symbol_b_g_skleth 
		global price_bids_b_g_skleth 
		global qty_bids_b_g_skleth 
		global price_asks_b_g_skleth 
		global qty_asks_b_g_skleth 

		symbol_b_g_skleth = symbol_b_l_skleth 
		price_bids_b_g_skleth = price_bids_b_l_skleth 
		qty_bids_b_g_skleth = qty_bids_b_l_skleth 
		price_asks_b_g_skleth = price_asks_b_l_skleth 
		qty_asks_b_g_skleth = qty_asks_b_l_skleth 


def on_close_skleth(ws): 
	print('### closed ###') 

def on_error_skleth(ws, message): 
	print(message) 

def on_open_skleth(ws): 
	ws.send(json.dumps({'sub': f'market.skleth.ticker'})) 

def loop_skleth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_skleth, 
		on_close=on_close_skleth, 
		on_error=on_error_skleth) 
	ws.on_open = on_open_skleth 
	ws.run_forever() 

Thread(target=loop_skleth).start() 

def loop_sklusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_sklusdt != 0.0 and qty_bids_a_g_sklusdt != 0.0 and price_asks_a_g_sklusdt != 0.0 and qty_asks_a_g_sklusdt != 0.0 and price_bids_b_g_skleth != 0.0 and qty_bids_b_g_skleth != 0.0 and price_asks_b_g_skleth != 0.0 and qty_asks_b_g_skleth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_sklusdt) 
			price_b = float(price_bids_b_g_skleth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_skleth, pribil)

Thread(target=loop_sklusdt_Trade).start() 

symbol_a_g_rvnusdt = 'rvnusdt' 
price_bids_a_g_rvnusdt = float(0.0) 
qty_bids_a_g_rvnusdt = float(0.0) 
price_asks_a_g_rvnusdt = float(0.0) 
qty_asks_a_g_rvnusdt = float(0.0) 

def on_message_rvnusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_rvnusdt = 'rvnusdt' 
		price_bids_a_l_rvnusdt = data['tick']['bid'] 
		qty_bids_a_l_rvnusdt = data['tick']['bidSize'] 
		price_asks_a_l_rvnusdt = data['tick']['ask'] 
		qty_asks_a_l_rvnusdt = data['tick']['askSize'] 

		global symbol_a_g_rvnusdt 
		global price_bids_a_g_rvnusdt 
		global qty_bids_a_g_rvnusdt 
		global price_asks_a_g_rvnusdt 
		global qty_asks_a_g_rvnusdt 

		symbol_a_g_rvnusdt = symbol_a_l_rvnusdt 
		price_bids_a_g_rvnusdt = price_bids_a_l_rvnusdt 
		qty_bids_a_g_rvnusdt = qty_bids_a_l_rvnusdt 
		price_asks_a_g_rvnusdt = price_asks_a_l_rvnusdt 
		qty_asks_a_g_rvnusdt = qty_asks_a_l_rvnusdt 

def on_close_rvnusdt(ws): 
	print('### closed ###') 

def on_error_rvnusdt(ws, message): 
	print(message) 

def on_open_rvnusdt(ws): 
	ws.send(json.dumps({'sub': f'market.rvnusdt.ticker'})) 

def loop_rvnusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rvnusdt, 
		on_close=on_close_rvnusdt, 
		on_error=on_error_rvnusdt) 
	ws.on_open = on_open_rvnusdt 
	ws.run_forever() 

Thread(target=loop_rvnusdt).start() 

symbol_b_g_rvnbtc = 'rvnbtc' 
price_bids_b_g_rvnbtc = float(0.0) 
qty_bids_b_g_rvnbtc = float(0.0) 
price_asks_b_g_rvnbtc = float(0.0) 
qty_asks_b_g_rvnbtc = float(0.0) 

def on_message_rvnbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_rvnbtc = 'rvnbtc' 
		price_bids_b_l_rvnbtc = data['tick']['bid'] 
		qty_bids_b_l_rvnbtc = data['tick']['bidSize']
		price_asks_b_l_rvnbtc = data['tick']['ask'] 
		qty_asks_b_l_rvnbtc = data['tick']['askSize'] 

		global symbol_b_g_rvnbtc 
		global price_bids_b_g_rvnbtc 
		global qty_bids_b_g_rvnbtc 
		global price_asks_b_g_rvnbtc 
		global qty_asks_b_g_rvnbtc 

		symbol_b_g_rvnbtc = symbol_b_l_rvnbtc 
		price_bids_b_g_rvnbtc = price_bids_b_l_rvnbtc 
		qty_bids_b_g_rvnbtc = qty_bids_b_l_rvnbtc 
		price_asks_b_g_rvnbtc = price_asks_b_l_rvnbtc 
		qty_asks_b_g_rvnbtc = qty_asks_b_l_rvnbtc 


def on_close_rvnbtc(ws): 
	print('### closed ###') 

def on_error_rvnbtc(ws, message): 
	print(message) 

def on_open_rvnbtc(ws): 
	ws.send(json.dumps({'sub': f'market.rvnbtc.ticker'})) 

def loop_rvnbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rvnbtc, 
		on_close=on_close_rvnbtc, 
		on_error=on_error_rvnbtc) 
	ws.on_open = on_open_rvnbtc 
	ws.run_forever() 

Thread(target=loop_rvnbtc).start() 

def loop_rvnusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_rvnusdt != 0.0 and qty_bids_a_g_rvnusdt != 0.0 and price_asks_a_g_rvnusdt != 0.0 and qty_asks_a_g_rvnusdt != 0.0 and price_bids_b_g_rvnbtc != 0.0 and qty_bids_b_g_rvnbtc != 0.0 and price_asks_b_g_rvnbtc != 0.0 and qty_asks_b_g_rvnbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_rvnusdt) 
			price_b = float(price_bids_b_g_rvnbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_rvnbtc, pribil)

Thread(target=loop_rvnusdt_Trade).start() 

symbol_a_g_cotiusdt = 'cotiusdt' 
price_bids_a_g_cotiusdt = float(0.0) 
qty_bids_a_g_cotiusdt = float(0.0) 
price_asks_a_g_cotiusdt = float(0.0) 
qty_asks_a_g_cotiusdt = float(0.0) 

def on_message_cotiusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_cotiusdt = 'cotiusdt' 
		price_bids_a_l_cotiusdt = data['tick']['bid'] 
		qty_bids_a_l_cotiusdt = data['tick']['bidSize'] 
		price_asks_a_l_cotiusdt = data['tick']['ask'] 
		qty_asks_a_l_cotiusdt = data['tick']['askSize'] 

		global symbol_a_g_cotiusdt 
		global price_bids_a_g_cotiusdt 
		global qty_bids_a_g_cotiusdt 
		global price_asks_a_g_cotiusdt 
		global qty_asks_a_g_cotiusdt 

		symbol_a_g_cotiusdt = symbol_a_l_cotiusdt 
		price_bids_a_g_cotiusdt = price_bids_a_l_cotiusdt 
		qty_bids_a_g_cotiusdt = qty_bids_a_l_cotiusdt 
		price_asks_a_g_cotiusdt = price_asks_a_l_cotiusdt 
		qty_asks_a_g_cotiusdt = qty_asks_a_l_cotiusdt 

def on_close_cotiusdt(ws): 
	print('### closed ###') 

def on_error_cotiusdt(ws, message): 
	print(message) 

def on_open_cotiusdt(ws): 
	ws.send(json.dumps({'sub': f'market.cotiusdt.ticker'})) 

def loop_cotiusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_cotiusdt, 
		on_close=on_close_cotiusdt, 
		on_error=on_error_cotiusdt) 
	ws.on_open = on_open_cotiusdt 
	ws.run_forever() 

Thread(target=loop_cotiusdt).start() 

symbol_b_g_cotibtc = 'cotibtc' 
price_bids_b_g_cotibtc = float(0.0) 
qty_bids_b_g_cotibtc = float(0.0) 
price_asks_b_g_cotibtc = float(0.0) 
qty_asks_b_g_cotibtc = float(0.0) 

def on_message_cotibtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_cotibtc = 'cotibtc' 
		price_bids_b_l_cotibtc = data['tick']['bid'] 
		qty_bids_b_l_cotibtc = data['tick']['bidSize']
		price_asks_b_l_cotibtc = data['tick']['ask'] 
		qty_asks_b_l_cotibtc = data['tick']['askSize'] 

		global symbol_b_g_cotibtc 
		global price_bids_b_g_cotibtc 
		global qty_bids_b_g_cotibtc 
		global price_asks_b_g_cotibtc 
		global qty_asks_b_g_cotibtc 

		symbol_b_g_cotibtc = symbol_b_l_cotibtc 
		price_bids_b_g_cotibtc = price_bids_b_l_cotibtc 
		qty_bids_b_g_cotibtc = qty_bids_b_l_cotibtc 
		price_asks_b_g_cotibtc = price_asks_b_l_cotibtc 
		qty_asks_b_g_cotibtc = qty_asks_b_l_cotibtc 


def on_close_cotibtc(ws): 
	print('### closed ###') 

def on_error_cotibtc(ws, message): 
	print(message) 

def on_open_cotibtc(ws): 
	ws.send(json.dumps({'sub': f'market.cotibtc.ticker'})) 

def loop_cotibtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_cotibtc, 
		on_close=on_close_cotibtc, 
		on_error=on_error_cotibtc) 
	ws.on_open = on_open_cotibtc 
	ws.run_forever() 

Thread(target=loop_cotibtc).start() 

def loop_cotiusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_cotiusdt != 0.0 and qty_bids_a_g_cotiusdt != 0.0 and price_asks_a_g_cotiusdt != 0.0 and qty_asks_a_g_cotiusdt != 0.0 and price_bids_b_g_cotibtc != 0.0 and qty_bids_b_g_cotibtc != 0.0 and price_asks_b_g_cotibtc != 0.0 and qty_asks_b_g_cotibtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_cotiusdt) 
			price_b = float(price_bids_b_g_cotibtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_cotibtc, pribil)

Thread(target=loop_cotiusdt_Trade).start() 

symbol_a_g_lambusdt = 'lambusdt' 
price_bids_a_g_lambusdt = float(0.0) 
qty_bids_a_g_lambusdt = float(0.0) 
price_asks_a_g_lambusdt = float(0.0) 
qty_asks_a_g_lambusdt = float(0.0) 

def on_message_lambusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_lambusdt = 'lambusdt' 
		price_bids_a_l_lambusdt = data['tick']['bid'] 
		qty_bids_a_l_lambusdt = data['tick']['bidSize'] 
		price_asks_a_l_lambusdt = data['tick']['ask'] 
		qty_asks_a_l_lambusdt = data['tick']['askSize'] 

		global symbol_a_g_lambusdt 
		global price_bids_a_g_lambusdt 
		global qty_bids_a_g_lambusdt 
		global price_asks_a_g_lambusdt 
		global qty_asks_a_g_lambusdt 

		symbol_a_g_lambusdt = symbol_a_l_lambusdt 
		price_bids_a_g_lambusdt = price_bids_a_l_lambusdt 
		qty_bids_a_g_lambusdt = qty_bids_a_l_lambusdt 
		price_asks_a_g_lambusdt = price_asks_a_l_lambusdt 
		qty_asks_a_g_lambusdt = qty_asks_a_l_lambusdt 

def on_close_lambusdt(ws): 
	print('### closed ###') 

def on_error_lambusdt(ws, message): 
	print(message) 

def on_open_lambusdt(ws): 
	ws.send(json.dumps({'sub': f'market.lambusdt.ticker'})) 

def loop_lambusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_lambusdt, 
		on_close=on_close_lambusdt, 
		on_error=on_error_lambusdt) 
	ws.on_open = on_open_lambusdt 
	ws.run_forever() 

Thread(target=loop_lambusdt).start() 

symbol_b_g_lambbtc = 'lambbtc' 
price_bids_b_g_lambbtc = float(0.0) 
qty_bids_b_g_lambbtc = float(0.0) 
price_asks_b_g_lambbtc = float(0.0) 
qty_asks_b_g_lambbtc = float(0.0) 

def on_message_lambbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_lambbtc = 'lambbtc' 
		price_bids_b_l_lambbtc = data['tick']['bid'] 
		qty_bids_b_l_lambbtc = data['tick']['bidSize']
		price_asks_b_l_lambbtc = data['tick']['ask'] 
		qty_asks_b_l_lambbtc = data['tick']['askSize'] 

		global symbol_b_g_lambbtc 
		global price_bids_b_g_lambbtc 
		global qty_bids_b_g_lambbtc 
		global price_asks_b_g_lambbtc 
		global qty_asks_b_g_lambbtc 

		symbol_b_g_lambbtc = symbol_b_l_lambbtc 
		price_bids_b_g_lambbtc = price_bids_b_l_lambbtc 
		qty_bids_b_g_lambbtc = qty_bids_b_l_lambbtc 
		price_asks_b_g_lambbtc = price_asks_b_l_lambbtc 
		qty_asks_b_g_lambbtc = qty_asks_b_l_lambbtc 


def on_close_lambbtc(ws): 
	print('### closed ###') 

def on_error_lambbtc(ws, message): 
	print(message) 

def on_open_lambbtc(ws): 
	ws.send(json.dumps({'sub': f'market.lambbtc.ticker'})) 

def loop_lambbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_lambbtc, 
		on_close=on_close_lambbtc, 
		on_error=on_error_lambbtc) 
	ws.on_open = on_open_lambbtc 
	ws.run_forever() 

Thread(target=loop_lambbtc).start() 

def loop_lambusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_lambusdt != 0.0 and qty_bids_a_g_lambusdt != 0.0 and price_asks_a_g_lambusdt != 0.0 and qty_asks_a_g_lambusdt != 0.0 and price_bids_b_g_lambbtc != 0.0 and qty_bids_b_g_lambbtc != 0.0 and price_asks_b_g_lambbtc != 0.0 and qty_asks_b_g_lambbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_lambusdt) 
			price_b = float(price_bids_b_g_lambbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_lambbtc, pribil)

Thread(target=loop_lambusdt_Trade).start() 

symbol_a_g_xtzusdt = 'xtzusdt' 
price_bids_a_g_xtzusdt = float(0.0) 
qty_bids_a_g_xtzusdt = float(0.0) 
price_asks_a_g_xtzusdt = float(0.0) 
qty_asks_a_g_xtzusdt = float(0.0) 

def on_message_xtzusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_xtzusdt = 'xtzusdt' 
		price_bids_a_l_xtzusdt = data['tick']['bid'] 
		qty_bids_a_l_xtzusdt = data['tick']['bidSize'] 
		price_asks_a_l_xtzusdt = data['tick']['ask'] 
		qty_asks_a_l_xtzusdt = data['tick']['askSize'] 

		global symbol_a_g_xtzusdt 
		global price_bids_a_g_xtzusdt 
		global qty_bids_a_g_xtzusdt 
		global price_asks_a_g_xtzusdt 
		global qty_asks_a_g_xtzusdt 

		symbol_a_g_xtzusdt = symbol_a_l_xtzusdt 
		price_bids_a_g_xtzusdt = price_bids_a_l_xtzusdt 
		qty_bids_a_g_xtzusdt = qty_bids_a_l_xtzusdt 
		price_asks_a_g_xtzusdt = price_asks_a_l_xtzusdt 
		qty_asks_a_g_xtzusdt = qty_asks_a_l_xtzusdt 

def on_close_xtzusdt(ws): 
	print('### closed ###') 

def on_error_xtzusdt(ws, message): 
	print(message) 

def on_open_xtzusdt(ws): 
	ws.send(json.dumps({'sub': f'market.xtzusdt.ticker'})) 

def loop_xtzusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xtzusdt, 
		on_close=on_close_xtzusdt, 
		on_error=on_error_xtzusdt) 
	ws.on_open = on_open_xtzusdt 
	ws.run_forever() 

Thread(target=loop_xtzusdt).start() 

symbol_b_g_xtzusdc = 'xtzusdc' 
price_bids_b_g_xtzusdc = float(0.0) 
qty_bids_b_g_xtzusdc = float(0.0) 
price_asks_b_g_xtzusdc = float(0.0) 
qty_asks_b_g_xtzusdc = float(0.0) 

def on_message_xtzusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_xtzusdc = 'xtzusdc' 
		price_bids_b_l_xtzusdc = data['tick']['bid'] 
		qty_bids_b_l_xtzusdc = data['tick']['bidSize']
		price_asks_b_l_xtzusdc = data['tick']['ask'] 
		qty_asks_b_l_xtzusdc = data['tick']['askSize'] 

		global symbol_b_g_xtzusdc 
		global price_bids_b_g_xtzusdc 
		global qty_bids_b_g_xtzusdc 
		global price_asks_b_g_xtzusdc 
		global qty_asks_b_g_xtzusdc 

		symbol_b_g_xtzusdc = symbol_b_l_xtzusdc 
		price_bids_b_g_xtzusdc = price_bids_b_l_xtzusdc 
		qty_bids_b_g_xtzusdc = qty_bids_b_l_xtzusdc 
		price_asks_b_g_xtzusdc = price_asks_b_l_xtzusdc 
		qty_asks_b_g_xtzusdc = qty_asks_b_l_xtzusdc 


def on_close_xtzusdc(ws): 
	print('### closed ###') 

def on_error_xtzusdc(ws, message): 
	print(message) 

def on_open_xtzusdc(ws): 
	ws.send(json.dumps({'sub': f'market.xtzusdc.ticker'})) 

def loop_xtzusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xtzusdc, 
		on_close=on_close_xtzusdc, 
		on_error=on_error_xtzusdc) 
	ws.on_open = on_open_xtzusdc 
	ws.run_forever() 

Thread(target=loop_xtzusdc).start() 

def loop_xtzusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_xtzusdt != 0.0 and qty_bids_a_g_xtzusdt != 0.0 and price_asks_a_g_xtzusdt != 0.0 and qty_asks_a_g_xtzusdt != 0.0 and price_bids_b_g_xtzusdc != 0.0 and qty_bids_b_g_xtzusdc != 0.0 and price_asks_b_g_xtzusdc != 0.0 and qty_asks_b_g_xtzusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_xtzusdt) 
			price_b = float(price_bids_b_g_xtzusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_xtzusdc, pribil)

Thread(target=loop_xtzusdt_Trade).start() 

symbol_a_g_csprusdt = 'csprusdt' 
price_bids_a_g_csprusdt = float(0.0) 
qty_bids_a_g_csprusdt = float(0.0) 
price_asks_a_g_csprusdt = float(0.0) 
qty_asks_a_g_csprusdt = float(0.0) 

def on_message_csprusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_csprusdt = 'csprusdt' 
		price_bids_a_l_csprusdt = data['tick']['bid'] 
		qty_bids_a_l_csprusdt = data['tick']['bidSize'] 
		price_asks_a_l_csprusdt = data['tick']['ask'] 
		qty_asks_a_l_csprusdt = data['tick']['askSize'] 

		global symbol_a_g_csprusdt 
		global price_bids_a_g_csprusdt 
		global qty_bids_a_g_csprusdt 
		global price_asks_a_g_csprusdt 
		global qty_asks_a_g_csprusdt 

		symbol_a_g_csprusdt = symbol_a_l_csprusdt 
		price_bids_a_g_csprusdt = price_bids_a_l_csprusdt 
		qty_bids_a_g_csprusdt = qty_bids_a_l_csprusdt 
		price_asks_a_g_csprusdt = price_asks_a_l_csprusdt 
		qty_asks_a_g_csprusdt = qty_asks_a_l_csprusdt 

def on_close_csprusdt(ws): 
	print('### closed ###') 

def on_error_csprusdt(ws, message): 
	print(message) 

def on_open_csprusdt(ws): 
	ws.send(json.dumps({'sub': f'market.csprusdt.ticker'})) 

def loop_csprusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_csprusdt, 
		on_close=on_close_csprusdt, 
		on_error=on_error_csprusdt) 
	ws.on_open = on_open_csprusdt 
	ws.run_forever() 

Thread(target=loop_csprusdt).start() 

symbol_b_g_csprbtc = 'csprbtc' 
price_bids_b_g_csprbtc = float(0.0) 
qty_bids_b_g_csprbtc = float(0.0) 
price_asks_b_g_csprbtc = float(0.0) 
qty_asks_b_g_csprbtc = float(0.0) 

def on_message_csprbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_csprbtc = 'csprbtc' 
		price_bids_b_l_csprbtc = data['tick']['bid'] 
		qty_bids_b_l_csprbtc = data['tick']['bidSize']
		price_asks_b_l_csprbtc = data['tick']['ask'] 
		qty_asks_b_l_csprbtc = data['tick']['askSize'] 

		global symbol_b_g_csprbtc 
		global price_bids_b_g_csprbtc 
		global qty_bids_b_g_csprbtc 
		global price_asks_b_g_csprbtc 
		global qty_asks_b_g_csprbtc 

		symbol_b_g_csprbtc = symbol_b_l_csprbtc 
		price_bids_b_g_csprbtc = price_bids_b_l_csprbtc 
		qty_bids_b_g_csprbtc = qty_bids_b_l_csprbtc 
		price_asks_b_g_csprbtc = price_asks_b_l_csprbtc 
		qty_asks_b_g_csprbtc = qty_asks_b_l_csprbtc 


def on_close_csprbtc(ws): 
	print('### closed ###') 

def on_error_csprbtc(ws, message): 
	print(message) 

def on_open_csprbtc(ws): 
	ws.send(json.dumps({'sub': f'market.csprbtc.ticker'})) 

def loop_csprbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_csprbtc, 
		on_close=on_close_csprbtc, 
		on_error=on_error_csprbtc) 
	ws.on_open = on_open_csprbtc 
	ws.run_forever() 

Thread(target=loop_csprbtc).start() 

def loop_csprusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_csprusdt != 0.0 and qty_bids_a_g_csprusdt != 0.0 and price_asks_a_g_csprusdt != 0.0 and qty_asks_a_g_csprusdt != 0.0 and price_bids_b_g_csprbtc != 0.0 and qty_bids_b_g_csprbtc != 0.0 and price_asks_b_g_csprbtc != 0.0 and qty_asks_b_g_csprbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_csprusdt) 
			price_b = float(price_bids_b_g_csprbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_csprbtc, pribil)

Thread(target=loop_csprusdt_Trade).start() 

symbol_a_g_iostusdt = 'iostusdt' 
price_bids_a_g_iostusdt = float(0.0) 
qty_bids_a_g_iostusdt = float(0.0) 
price_asks_a_g_iostusdt = float(0.0) 
qty_asks_a_g_iostusdt = float(0.0) 

def on_message_iostusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_iostusdt = 'iostusdt' 
		price_bids_a_l_iostusdt = data['tick']['bid'] 
		qty_bids_a_l_iostusdt = data['tick']['bidSize'] 
		price_asks_a_l_iostusdt = data['tick']['ask'] 
		qty_asks_a_l_iostusdt = data['tick']['askSize'] 

		global symbol_a_g_iostusdt 
		global price_bids_a_g_iostusdt 
		global qty_bids_a_g_iostusdt 
		global price_asks_a_g_iostusdt 
		global qty_asks_a_g_iostusdt 

		symbol_a_g_iostusdt = symbol_a_l_iostusdt 
		price_bids_a_g_iostusdt = price_bids_a_l_iostusdt 
		qty_bids_a_g_iostusdt = qty_bids_a_l_iostusdt 
		price_asks_a_g_iostusdt = price_asks_a_l_iostusdt 
		qty_asks_a_g_iostusdt = qty_asks_a_l_iostusdt 

def on_close_iostusdt(ws): 
	print('### closed ###') 

def on_error_iostusdt(ws, message): 
	print(message) 

def on_open_iostusdt(ws): 
	ws.send(json.dumps({'sub': f'market.iostusdt.ticker'})) 

def loop_iostusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_iostusdt, 
		on_close=on_close_iostusdt, 
		on_error=on_error_iostusdt) 
	ws.on_open = on_open_iostusdt 
	ws.run_forever() 

Thread(target=loop_iostusdt).start() 

symbol_b_g_iosteth = 'iosteth' 
price_bids_b_g_iosteth = float(0.0) 
qty_bids_b_g_iosteth = float(0.0) 
price_asks_b_g_iosteth = float(0.0) 
qty_asks_b_g_iosteth = float(0.0) 

def on_message_iosteth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_iosteth = 'iosteth' 
		price_bids_b_l_iosteth = data['tick']['bid'] 
		qty_bids_b_l_iosteth = data['tick']['bidSize']
		price_asks_b_l_iosteth = data['tick']['ask'] 
		qty_asks_b_l_iosteth = data['tick']['askSize'] 

		global symbol_b_g_iosteth 
		global price_bids_b_g_iosteth 
		global qty_bids_b_g_iosteth 
		global price_asks_b_g_iosteth 
		global qty_asks_b_g_iosteth 

		symbol_b_g_iosteth = symbol_b_l_iosteth 
		price_bids_b_g_iosteth = price_bids_b_l_iosteth 
		qty_bids_b_g_iosteth = qty_bids_b_l_iosteth 
		price_asks_b_g_iosteth = price_asks_b_l_iosteth 
		qty_asks_b_g_iosteth = qty_asks_b_l_iosteth 


def on_close_iosteth(ws): 
	print('### closed ###') 

def on_error_iosteth(ws, message): 
	print(message) 

def on_open_iosteth(ws): 
	ws.send(json.dumps({'sub': f'market.iosteth.ticker'})) 

def loop_iosteth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_iosteth, 
		on_close=on_close_iosteth, 
		on_error=on_error_iosteth) 
	ws.on_open = on_open_iosteth 
	ws.run_forever() 

Thread(target=loop_iosteth).start() 

def loop_iostusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_iostusdt != 0.0 and qty_bids_a_g_iostusdt != 0.0 and price_asks_a_g_iostusdt != 0.0 and qty_asks_a_g_iostusdt != 0.0 and price_bids_b_g_iosteth != 0.0 and qty_bids_b_g_iosteth != 0.0 and price_asks_b_g_iosteth != 0.0 and qty_asks_b_g_iosteth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_iostusdt) 
			price_b = float(price_bids_b_g_iosteth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_iosteth, pribil)

Thread(target=loop_iostusdt_Trade).start() 

symbol_a_g_antusdt = 'antusdt' 
price_bids_a_g_antusdt = float(0.0) 
qty_bids_a_g_antusdt = float(0.0) 
price_asks_a_g_antusdt = float(0.0) 
qty_asks_a_g_antusdt = float(0.0) 

def on_message_antusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_antusdt = 'antusdt' 
		price_bids_a_l_antusdt = data['tick']['bid'] 
		qty_bids_a_l_antusdt = data['tick']['bidSize'] 
		price_asks_a_l_antusdt = data['tick']['ask'] 
		qty_asks_a_l_antusdt = data['tick']['askSize'] 

		global symbol_a_g_antusdt 
		global price_bids_a_g_antusdt 
		global qty_bids_a_g_antusdt 
		global price_asks_a_g_antusdt 
		global qty_asks_a_g_antusdt 

		symbol_a_g_antusdt = symbol_a_l_antusdt 
		price_bids_a_g_antusdt = price_bids_a_l_antusdt 
		qty_bids_a_g_antusdt = qty_bids_a_l_antusdt 
		price_asks_a_g_antusdt = price_asks_a_l_antusdt 
		qty_asks_a_g_antusdt = qty_asks_a_l_antusdt 

def on_close_antusdt(ws): 
	print('### closed ###') 

def on_error_antusdt(ws, message): 
	print(message) 

def on_open_antusdt(ws): 
	ws.send(json.dumps({'sub': f'market.antusdt.ticker'})) 

def loop_antusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_antusdt, 
		on_close=on_close_antusdt, 
		on_error=on_error_antusdt) 
	ws.on_open = on_open_antusdt 
	ws.run_forever() 

Thread(target=loop_antusdt).start() 

symbol_b_g_antbtc = 'antbtc' 
price_bids_b_g_antbtc = float(0.0) 
qty_bids_b_g_antbtc = float(0.0) 
price_asks_b_g_antbtc = float(0.0) 
qty_asks_b_g_antbtc = float(0.0) 

def on_message_antbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_antbtc = 'antbtc' 
		price_bids_b_l_antbtc = data['tick']['bid'] 
		qty_bids_b_l_antbtc = data['tick']['bidSize']
		price_asks_b_l_antbtc = data['tick']['ask'] 
		qty_asks_b_l_antbtc = data['tick']['askSize'] 

		global symbol_b_g_antbtc 
		global price_bids_b_g_antbtc 
		global qty_bids_b_g_antbtc 
		global price_asks_b_g_antbtc 
		global qty_asks_b_g_antbtc 

		symbol_b_g_antbtc = symbol_b_l_antbtc 
		price_bids_b_g_antbtc = price_bids_b_l_antbtc 
		qty_bids_b_g_antbtc = qty_bids_b_l_antbtc 
		price_asks_b_g_antbtc = price_asks_b_l_antbtc 
		qty_asks_b_g_antbtc = qty_asks_b_l_antbtc 


def on_close_antbtc(ws): 
	print('### closed ###') 

def on_error_antbtc(ws, message): 
	print(message) 

def on_open_antbtc(ws): 
	ws.send(json.dumps({'sub': f'market.antbtc.ticker'})) 

def loop_antbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_antbtc, 
		on_close=on_close_antbtc, 
		on_error=on_error_antbtc) 
	ws.on_open = on_open_antbtc 
	ws.run_forever() 

Thread(target=loop_antbtc).start() 

def loop_antusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_antusdt != 0.0 and qty_bids_a_g_antusdt != 0.0 and price_asks_a_g_antusdt != 0.0 and qty_asks_a_g_antusdt != 0.0 and price_bids_b_g_antbtc != 0.0 and qty_bids_b_g_antbtc != 0.0 and price_asks_b_g_antbtc != 0.0 and qty_asks_b_g_antbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_antusdt) 
			price_b = float(price_bids_b_g_antbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_antbtc, pribil)

Thread(target=loop_antusdt_Trade).start() 

symbol_a_g_xemusdt = 'xemusdt' 
price_bids_a_g_xemusdt = float(0.0) 
qty_bids_a_g_xemusdt = float(0.0) 
price_asks_a_g_xemusdt = float(0.0) 
qty_asks_a_g_xemusdt = float(0.0) 

def on_message_xemusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_xemusdt = 'xemusdt' 
		price_bids_a_l_xemusdt = data['tick']['bid'] 
		qty_bids_a_l_xemusdt = data['tick']['bidSize'] 
		price_asks_a_l_xemusdt = data['tick']['ask'] 
		qty_asks_a_l_xemusdt = data['tick']['askSize'] 

		global symbol_a_g_xemusdt 
		global price_bids_a_g_xemusdt 
		global qty_bids_a_g_xemusdt 
		global price_asks_a_g_xemusdt 
		global qty_asks_a_g_xemusdt 

		symbol_a_g_xemusdt = symbol_a_l_xemusdt 
		price_bids_a_g_xemusdt = price_bids_a_l_xemusdt 
		qty_bids_a_g_xemusdt = qty_bids_a_l_xemusdt 
		price_asks_a_g_xemusdt = price_asks_a_l_xemusdt 
		qty_asks_a_g_xemusdt = qty_asks_a_l_xemusdt 

def on_close_xemusdt(ws): 
	print('### closed ###') 

def on_error_xemusdt(ws, message): 
	print(message) 

def on_open_xemusdt(ws): 
	ws.send(json.dumps({'sub': f'market.xemusdt.ticker'})) 

def loop_xemusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xemusdt, 
		on_close=on_close_xemusdt, 
		on_error=on_error_xemusdt) 
	ws.on_open = on_open_xemusdt 
	ws.run_forever() 

Thread(target=loop_xemusdt).start() 

symbol_b_g_xembtc = 'xembtc' 
price_bids_b_g_xembtc = float(0.0) 
qty_bids_b_g_xembtc = float(0.0) 
price_asks_b_g_xembtc = float(0.0) 
qty_asks_b_g_xembtc = float(0.0) 

def on_message_xembtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_xembtc = 'xembtc' 
		price_bids_b_l_xembtc = data['tick']['bid'] 
		qty_bids_b_l_xembtc = data['tick']['bidSize']
		price_asks_b_l_xembtc = data['tick']['ask'] 
		qty_asks_b_l_xembtc = data['tick']['askSize'] 

		global symbol_b_g_xembtc 
		global price_bids_b_g_xembtc 
		global qty_bids_b_g_xembtc 
		global price_asks_b_g_xembtc 
		global qty_asks_b_g_xembtc 

		symbol_b_g_xembtc = symbol_b_l_xembtc 
		price_bids_b_g_xembtc = price_bids_b_l_xembtc 
		qty_bids_b_g_xembtc = qty_bids_b_l_xembtc 
		price_asks_b_g_xembtc = price_asks_b_l_xembtc 
		qty_asks_b_g_xembtc = qty_asks_b_l_xembtc 


def on_close_xembtc(ws): 
	print('### closed ###') 

def on_error_xembtc(ws, message): 
	print(message) 

def on_open_xembtc(ws): 
	ws.send(json.dumps({'sub': f'market.xembtc.ticker'})) 

def loop_xembtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xembtc, 
		on_close=on_close_xembtc, 
		on_error=on_error_xembtc) 
	ws.on_open = on_open_xembtc 
	ws.run_forever() 

Thread(target=loop_xembtc).start() 

def loop_xemusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_xemusdt != 0.0 and qty_bids_a_g_xemusdt != 0.0 and price_asks_a_g_xemusdt != 0.0 and qty_asks_a_g_xemusdt != 0.0 and price_bids_b_g_xembtc != 0.0 and qty_bids_b_g_xembtc != 0.0 and price_asks_b_g_xembtc != 0.0 and qty_asks_b_g_xembtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_xemusdt) 
			price_b = float(price_bids_b_g_xembtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_xembtc, pribil)

Thread(target=loop_xemusdt_Trade).start() 

symbol_a_g_etcusdt = 'etcusdt' 
price_bids_a_g_etcusdt = float(0.0) 
qty_bids_a_g_etcusdt = float(0.0) 
price_asks_a_g_etcusdt = float(0.0) 
qty_asks_a_g_etcusdt = float(0.0) 

def on_message_etcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_etcusdt = 'etcusdt' 
		price_bids_a_l_etcusdt = data['tick']['bid'] 
		qty_bids_a_l_etcusdt = data['tick']['bidSize'] 
		price_asks_a_l_etcusdt = data['tick']['ask'] 
		qty_asks_a_l_etcusdt = data['tick']['askSize'] 

		global symbol_a_g_etcusdt 
		global price_bids_a_g_etcusdt 
		global qty_bids_a_g_etcusdt 
		global price_asks_a_g_etcusdt 
		global qty_asks_a_g_etcusdt 

		symbol_a_g_etcusdt = symbol_a_l_etcusdt 
		price_bids_a_g_etcusdt = price_bids_a_l_etcusdt 
		qty_bids_a_g_etcusdt = qty_bids_a_l_etcusdt 
		price_asks_a_g_etcusdt = price_asks_a_l_etcusdt 
		qty_asks_a_g_etcusdt = qty_asks_a_l_etcusdt 

def on_close_etcusdt(ws): 
	print('### closed ###') 

def on_error_etcusdt(ws, message): 
	print(message) 

def on_open_etcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.etcusdt.ticker'})) 

def loop_etcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_etcusdt, 
		on_close=on_close_etcusdt, 
		on_error=on_error_etcusdt) 
	ws.on_open = on_open_etcusdt 
	ws.run_forever() 

Thread(target=loop_etcusdt).start() 

symbol_b_g_etcbtc = 'etcbtc' 
price_bids_b_g_etcbtc = float(0.0) 
qty_bids_b_g_etcbtc = float(0.0) 
price_asks_b_g_etcbtc = float(0.0) 
qty_asks_b_g_etcbtc = float(0.0) 

def on_message_etcbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_etcbtc = 'etcbtc' 
		price_bids_b_l_etcbtc = data['tick']['bid'] 
		qty_bids_b_l_etcbtc = data['tick']['bidSize']
		price_asks_b_l_etcbtc = data['tick']['ask'] 
		qty_asks_b_l_etcbtc = data['tick']['askSize'] 

		global symbol_b_g_etcbtc 
		global price_bids_b_g_etcbtc 
		global qty_bids_b_g_etcbtc 
		global price_asks_b_g_etcbtc 
		global qty_asks_b_g_etcbtc 

		symbol_b_g_etcbtc = symbol_b_l_etcbtc 
		price_bids_b_g_etcbtc = price_bids_b_l_etcbtc 
		qty_bids_b_g_etcbtc = qty_bids_b_l_etcbtc 
		price_asks_b_g_etcbtc = price_asks_b_l_etcbtc 
		qty_asks_b_g_etcbtc = qty_asks_b_l_etcbtc 


def on_close_etcbtc(ws): 
	print('### closed ###') 

def on_error_etcbtc(ws, message): 
	print(message) 

def on_open_etcbtc(ws): 
	ws.send(json.dumps({'sub': f'market.etcbtc.ticker'})) 

def loop_etcbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_etcbtc, 
		on_close=on_close_etcbtc, 
		on_error=on_error_etcbtc) 
	ws.on_open = on_open_etcbtc 
	ws.run_forever() 

Thread(target=loop_etcbtc).start() 

def loop_etcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_etcusdt != 0.0 and qty_bids_a_g_etcusdt != 0.0 and price_asks_a_g_etcusdt != 0.0 and qty_asks_a_g_etcusdt != 0.0 and price_bids_b_g_etcbtc != 0.0 and qty_bids_b_g_etcbtc != 0.0 and price_asks_b_g_etcbtc != 0.0 and qty_asks_b_g_etcbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_etcusdt) 
			price_b = float(price_bids_b_g_etcbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_etcbtc, pribil)

Thread(target=loop_etcusdt_Trade).start() 

symbol_a_g_stethusdt = 'stethusdt' 
price_bids_a_g_stethusdt = float(0.0) 
qty_bids_a_g_stethusdt = float(0.0) 
price_asks_a_g_stethusdt = float(0.0) 
qty_asks_a_g_stethusdt = float(0.0) 

def on_message_stethusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_stethusdt = 'stethusdt' 
		price_bids_a_l_stethusdt = data['tick']['bid'] 
		qty_bids_a_l_stethusdt = data['tick']['bidSize'] 
		price_asks_a_l_stethusdt = data['tick']['ask'] 
		qty_asks_a_l_stethusdt = data['tick']['askSize'] 

		global symbol_a_g_stethusdt 
		global price_bids_a_g_stethusdt 
		global qty_bids_a_g_stethusdt 
		global price_asks_a_g_stethusdt 
		global qty_asks_a_g_stethusdt 

		symbol_a_g_stethusdt = symbol_a_l_stethusdt 
		price_bids_a_g_stethusdt = price_bids_a_l_stethusdt 
		qty_bids_a_g_stethusdt = qty_bids_a_l_stethusdt 
		price_asks_a_g_stethusdt = price_asks_a_l_stethusdt 
		qty_asks_a_g_stethusdt = qty_asks_a_l_stethusdt 

def on_close_stethusdt(ws): 
	print('### closed ###') 

def on_error_stethusdt(ws, message): 
	print(message) 

def on_open_stethusdt(ws): 
	ws.send(json.dumps({'sub': f'market.stethusdt.ticker'})) 

def loop_stethusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_stethusdt, 
		on_close=on_close_stethusdt, 
		on_error=on_error_stethusdt) 
	ws.on_open = on_open_stethusdt 
	ws.run_forever() 

Thread(target=loop_stethusdt).start() 

symbol_b_g_stetheth = 'stetheth' 
price_bids_b_g_stetheth = float(0.0) 
qty_bids_b_g_stetheth = float(0.0) 
price_asks_b_g_stetheth = float(0.0) 
qty_asks_b_g_stetheth = float(0.0) 

def on_message_stetheth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_stetheth = 'stetheth' 
		price_bids_b_l_stetheth = data['tick']['bid'] 
		qty_bids_b_l_stetheth = data['tick']['bidSize']
		price_asks_b_l_stetheth = data['tick']['ask'] 
		qty_asks_b_l_stetheth = data['tick']['askSize'] 

		global symbol_b_g_stetheth 
		global price_bids_b_g_stetheth 
		global qty_bids_b_g_stetheth 
		global price_asks_b_g_stetheth 
		global qty_asks_b_g_stetheth 

		symbol_b_g_stetheth = symbol_b_l_stetheth 
		price_bids_b_g_stetheth = price_bids_b_l_stetheth 
		qty_bids_b_g_stetheth = qty_bids_b_l_stetheth 
		price_asks_b_g_stetheth = price_asks_b_l_stetheth 
		qty_asks_b_g_stetheth = qty_asks_b_l_stetheth 


def on_close_stetheth(ws): 
	print('### closed ###') 

def on_error_stetheth(ws, message): 
	print(message) 

def on_open_stetheth(ws): 
	ws.send(json.dumps({'sub': f'market.stetheth.ticker'})) 

def loop_stetheth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_stetheth, 
		on_close=on_close_stetheth, 
		on_error=on_error_stetheth) 
	ws.on_open = on_open_stetheth 
	ws.run_forever() 

Thread(target=loop_stetheth).start() 

def loop_stethusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_stethusdt != 0.0 and qty_bids_a_g_stethusdt != 0.0 and price_asks_a_g_stethusdt != 0.0 and qty_asks_a_g_stethusdt != 0.0 and price_bids_b_g_stetheth != 0.0 and qty_bids_b_g_stetheth != 0.0 and price_asks_b_g_stetheth != 0.0 and qty_asks_b_g_stetheth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_stethusdt) 
			price_b = float(price_bids_b_g_stetheth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_stetheth, pribil)

Thread(target=loop_stethusdt_Trade).start() 

symbol_a_g_grtusdt = 'grtusdt' 
price_bids_a_g_grtusdt = float(0.0) 
qty_bids_a_g_grtusdt = float(0.0) 
price_asks_a_g_grtusdt = float(0.0) 
qty_asks_a_g_grtusdt = float(0.0) 

def on_message_grtusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_grtusdt = 'grtusdt' 
		price_bids_a_l_grtusdt = data['tick']['bid'] 
		qty_bids_a_l_grtusdt = data['tick']['bidSize'] 
		price_asks_a_l_grtusdt = data['tick']['ask'] 
		qty_asks_a_l_grtusdt = data['tick']['askSize'] 

		global symbol_a_g_grtusdt 
		global price_bids_a_g_grtusdt 
		global qty_bids_a_g_grtusdt 
		global price_asks_a_g_grtusdt 
		global qty_asks_a_g_grtusdt 

		symbol_a_g_grtusdt = symbol_a_l_grtusdt 
		price_bids_a_g_grtusdt = price_bids_a_l_grtusdt 
		qty_bids_a_g_grtusdt = qty_bids_a_l_grtusdt 
		price_asks_a_g_grtusdt = price_asks_a_l_grtusdt 
		qty_asks_a_g_grtusdt = qty_asks_a_l_grtusdt 

def on_close_grtusdt(ws): 
	print('### closed ###') 

def on_error_grtusdt(ws, message): 
	print(message) 

def on_open_grtusdt(ws): 
	ws.send(json.dumps({'sub': f'market.grtusdt.ticker'})) 

def loop_grtusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_grtusdt, 
		on_close=on_close_grtusdt, 
		on_error=on_error_grtusdt) 
	ws.on_open = on_open_grtusdt 
	ws.run_forever() 

Thread(target=loop_grtusdt).start() 

symbol_b_g_grtbtc = 'grtbtc' 
price_bids_b_g_grtbtc = float(0.0) 
qty_bids_b_g_grtbtc = float(0.0) 
price_asks_b_g_grtbtc = float(0.0) 
qty_asks_b_g_grtbtc = float(0.0) 

def on_message_grtbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_grtbtc = 'grtbtc' 
		price_bids_b_l_grtbtc = data['tick']['bid'] 
		qty_bids_b_l_grtbtc = data['tick']['bidSize']
		price_asks_b_l_grtbtc = data['tick']['ask'] 
		qty_asks_b_l_grtbtc = data['tick']['askSize'] 

		global symbol_b_g_grtbtc 
		global price_bids_b_g_grtbtc 
		global qty_bids_b_g_grtbtc 
		global price_asks_b_g_grtbtc 
		global qty_asks_b_g_grtbtc 

		symbol_b_g_grtbtc = symbol_b_l_grtbtc 
		price_bids_b_g_grtbtc = price_bids_b_l_grtbtc 
		qty_bids_b_g_grtbtc = qty_bids_b_l_grtbtc 
		price_asks_b_g_grtbtc = price_asks_b_l_grtbtc 
		qty_asks_b_g_grtbtc = qty_asks_b_l_grtbtc 


def on_close_grtbtc(ws): 
	print('### closed ###') 

def on_error_grtbtc(ws, message): 
	print(message) 

def on_open_grtbtc(ws): 
	ws.send(json.dumps({'sub': f'market.grtbtc.ticker'})) 

def loop_grtbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_grtbtc, 
		on_close=on_close_grtbtc, 
		on_error=on_error_grtbtc) 
	ws.on_open = on_open_grtbtc 
	ws.run_forever() 

Thread(target=loop_grtbtc).start() 

def loop_grtusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_grtusdt != 0.0 and qty_bids_a_g_grtusdt != 0.0 and price_asks_a_g_grtusdt != 0.0 and qty_asks_a_g_grtusdt != 0.0 and price_bids_b_g_grtbtc != 0.0 and qty_bids_b_g_grtbtc != 0.0 and price_asks_b_g_grtbtc != 0.0 and qty_asks_b_g_grtbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_grtusdt) 
			price_b = float(price_bids_b_g_grtbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_grtbtc, pribil)

Thread(target=loop_grtusdt_Trade).start() 

symbol_a_g_flzusdt = 'flzusdt' 
price_bids_a_g_flzusdt = float(0.0) 
qty_bids_a_g_flzusdt = float(0.0) 
price_asks_a_g_flzusdt = float(0.0) 
qty_asks_a_g_flzusdt = float(0.0) 

def on_message_flzusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_flzusdt = 'flzusdt' 
		price_bids_a_l_flzusdt = data['tick']['bid'] 
		qty_bids_a_l_flzusdt = data['tick']['bidSize'] 
		price_asks_a_l_flzusdt = data['tick']['ask'] 
		qty_asks_a_l_flzusdt = data['tick']['askSize'] 

		global symbol_a_g_flzusdt 
		global price_bids_a_g_flzusdt 
		global qty_bids_a_g_flzusdt 
		global price_asks_a_g_flzusdt 
		global qty_asks_a_g_flzusdt 

		symbol_a_g_flzusdt = symbol_a_l_flzusdt 
		price_bids_a_g_flzusdt = price_bids_a_l_flzusdt 
		qty_bids_a_g_flzusdt = qty_bids_a_l_flzusdt 
		price_asks_a_g_flzusdt = price_asks_a_l_flzusdt 
		qty_asks_a_g_flzusdt = qty_asks_a_l_flzusdt 

def on_close_flzusdt(ws): 
	print('### closed ###') 

def on_error_flzusdt(ws, message): 
	print(message) 

def on_open_flzusdt(ws): 
	ws.send(json.dumps({'sub': f'market.flzusdt.ticker'})) 

def loop_flzusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_flzusdt, 
		on_close=on_close_flzusdt, 
		on_error=on_error_flzusdt) 
	ws.on_open = on_open_flzusdt 
	ws.run_forever() 

Thread(target=loop_flzusdt).start() 

symbol_b_g_flzusdc = 'flzusdc' 
price_bids_b_g_flzusdc = float(0.0) 
qty_bids_b_g_flzusdc = float(0.0) 
price_asks_b_g_flzusdc = float(0.0) 
qty_asks_b_g_flzusdc = float(0.0) 

def on_message_flzusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_flzusdc = 'flzusdc' 
		price_bids_b_l_flzusdc = data['tick']['bid'] 
		qty_bids_b_l_flzusdc = data['tick']['bidSize']
		price_asks_b_l_flzusdc = data['tick']['ask'] 
		qty_asks_b_l_flzusdc = data['tick']['askSize'] 

		global symbol_b_g_flzusdc 
		global price_bids_b_g_flzusdc 
		global qty_bids_b_g_flzusdc 
		global price_asks_b_g_flzusdc 
		global qty_asks_b_g_flzusdc 

		symbol_b_g_flzusdc = symbol_b_l_flzusdc 
		price_bids_b_g_flzusdc = price_bids_b_l_flzusdc 
		qty_bids_b_g_flzusdc = qty_bids_b_l_flzusdc 
		price_asks_b_g_flzusdc = price_asks_b_l_flzusdc 
		qty_asks_b_g_flzusdc = qty_asks_b_l_flzusdc 


def on_close_flzusdc(ws): 
	print('### closed ###') 

def on_error_flzusdc(ws, message): 
	print(message) 

def on_open_flzusdc(ws): 
	ws.send(json.dumps({'sub': f'market.flzusdc.ticker'})) 

def loop_flzusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_flzusdc, 
		on_close=on_close_flzusdc, 
		on_error=on_error_flzusdc) 
	ws.on_open = on_open_flzusdc 
	ws.run_forever() 

Thread(target=loop_flzusdc).start() 

def loop_flzusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_flzusdt != 0.0 and qty_bids_a_g_flzusdt != 0.0 and price_asks_a_g_flzusdt != 0.0 and qty_asks_a_g_flzusdt != 0.0 and price_bids_b_g_flzusdc != 0.0 and qty_bids_b_g_flzusdc != 0.0 and price_asks_b_g_flzusdc != 0.0 and qty_asks_b_g_flzusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_flzusdt) 
			price_b = float(price_bids_b_g_flzusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_flzusdc, pribil)

Thread(target=loop_flzusdt_Trade).start() 

symbol_a_g_sushiusdt = 'sushiusdt' 
price_bids_a_g_sushiusdt = float(0.0) 
qty_bids_a_g_sushiusdt = float(0.0) 
price_asks_a_g_sushiusdt = float(0.0) 
qty_asks_a_g_sushiusdt = float(0.0) 

def on_message_sushiusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_sushiusdt = 'sushiusdt' 
		price_bids_a_l_sushiusdt = data['tick']['bid'] 
		qty_bids_a_l_sushiusdt = data['tick']['bidSize'] 
		price_asks_a_l_sushiusdt = data['tick']['ask'] 
		qty_asks_a_l_sushiusdt = data['tick']['askSize'] 

		global symbol_a_g_sushiusdt 
		global price_bids_a_g_sushiusdt 
		global qty_bids_a_g_sushiusdt 
		global price_asks_a_g_sushiusdt 
		global qty_asks_a_g_sushiusdt 

		symbol_a_g_sushiusdt = symbol_a_l_sushiusdt 
		price_bids_a_g_sushiusdt = price_bids_a_l_sushiusdt 
		qty_bids_a_g_sushiusdt = qty_bids_a_l_sushiusdt 
		price_asks_a_g_sushiusdt = price_asks_a_l_sushiusdt 
		qty_asks_a_g_sushiusdt = qty_asks_a_l_sushiusdt 

def on_close_sushiusdt(ws): 
	print('### closed ###') 

def on_error_sushiusdt(ws, message): 
	print(message) 

def on_open_sushiusdt(ws): 
	ws.send(json.dumps({'sub': f'market.sushiusdt.ticker'})) 

def loop_sushiusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sushiusdt, 
		on_close=on_close_sushiusdt, 
		on_error=on_error_sushiusdt) 
	ws.on_open = on_open_sushiusdt 
	ws.run_forever() 

Thread(target=loop_sushiusdt).start() 

symbol_b_g_sushieth = 'sushieth' 
price_bids_b_g_sushieth = float(0.0) 
qty_bids_b_g_sushieth = float(0.0) 
price_asks_b_g_sushieth = float(0.0) 
qty_asks_b_g_sushieth = float(0.0) 

def on_message_sushieth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_sushieth = 'sushieth' 
		price_bids_b_l_sushieth = data['tick']['bid'] 
		qty_bids_b_l_sushieth = data['tick']['bidSize']
		price_asks_b_l_sushieth = data['tick']['ask'] 
		qty_asks_b_l_sushieth = data['tick']['askSize'] 

		global symbol_b_g_sushieth 
		global price_bids_b_g_sushieth 
		global qty_bids_b_g_sushieth 
		global price_asks_b_g_sushieth 
		global qty_asks_b_g_sushieth 

		symbol_b_g_sushieth = symbol_b_l_sushieth 
		price_bids_b_g_sushieth = price_bids_b_l_sushieth 
		qty_bids_b_g_sushieth = qty_bids_b_l_sushieth 
		price_asks_b_g_sushieth = price_asks_b_l_sushieth 
		qty_asks_b_g_sushieth = qty_asks_b_l_sushieth 


def on_close_sushieth(ws): 
	print('### closed ###') 

def on_error_sushieth(ws, message): 
	print(message) 

def on_open_sushieth(ws): 
	ws.send(json.dumps({'sub': f'market.sushieth.ticker'})) 

def loop_sushieth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_sushieth, 
		on_close=on_close_sushieth, 
		on_error=on_error_sushieth) 
	ws.on_open = on_open_sushieth 
	ws.run_forever() 

Thread(target=loop_sushieth).start() 

def loop_sushiusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_sushiusdt != 0.0 and qty_bids_a_g_sushiusdt != 0.0 and price_asks_a_g_sushiusdt != 0.0 and qty_asks_a_g_sushiusdt != 0.0 and price_bids_b_g_sushieth != 0.0 and qty_bids_b_g_sushieth != 0.0 and price_asks_b_g_sushieth != 0.0 and qty_asks_b_g_sushieth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_sushiusdt) 
			price_b = float(price_bids_b_g_sushieth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_sushieth, pribil)

Thread(target=loop_sushiusdt_Trade).start() 

symbol_a_g_dogeusdt = 'dogeusdt' 
price_bids_a_g_dogeusdt = float(0.0) 
qty_bids_a_g_dogeusdt = float(0.0) 
price_asks_a_g_dogeusdt = float(0.0) 
qty_asks_a_g_dogeusdt = float(0.0) 

def on_message_dogeusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_dogeusdt = 'dogeusdt' 
		price_bids_a_l_dogeusdt = data['tick']['bid'] 
		qty_bids_a_l_dogeusdt = data['tick']['bidSize'] 
		price_asks_a_l_dogeusdt = data['tick']['ask'] 
		qty_asks_a_l_dogeusdt = data['tick']['askSize'] 

		global symbol_a_g_dogeusdt 
		global price_bids_a_g_dogeusdt 
		global qty_bids_a_g_dogeusdt 
		global price_asks_a_g_dogeusdt 
		global qty_asks_a_g_dogeusdt 

		symbol_a_g_dogeusdt = symbol_a_l_dogeusdt 
		price_bids_a_g_dogeusdt = price_bids_a_l_dogeusdt 
		qty_bids_a_g_dogeusdt = qty_bids_a_l_dogeusdt 
		price_asks_a_g_dogeusdt = price_asks_a_l_dogeusdt 
		qty_asks_a_g_dogeusdt = qty_asks_a_l_dogeusdt 

def on_close_dogeusdt(ws): 
	print('### closed ###') 

def on_error_dogeusdt(ws, message): 
	print(message) 

def on_open_dogeusdt(ws): 
	ws.send(json.dumps({'sub': f'market.dogeusdt.ticker'})) 

def loop_dogeusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dogeusdt, 
		on_close=on_close_dogeusdt, 
		on_error=on_error_dogeusdt) 
	ws.on_open = on_open_dogeusdt 
	ws.run_forever() 

Thread(target=loop_dogeusdt).start() 

symbol_b_g_dogeusdc = 'dogeusdc' 
price_bids_b_g_dogeusdc = float(0.0) 
qty_bids_b_g_dogeusdc = float(0.0) 
price_asks_b_g_dogeusdc = float(0.0) 
qty_asks_b_g_dogeusdc = float(0.0) 

def on_message_dogeusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_dogeusdc = 'dogeusdc' 
		price_bids_b_l_dogeusdc = data['tick']['bid'] 
		qty_bids_b_l_dogeusdc = data['tick']['bidSize']
		price_asks_b_l_dogeusdc = data['tick']['ask'] 
		qty_asks_b_l_dogeusdc = data['tick']['askSize'] 

		global symbol_b_g_dogeusdc 
		global price_bids_b_g_dogeusdc 
		global qty_bids_b_g_dogeusdc 
		global price_asks_b_g_dogeusdc 
		global qty_asks_b_g_dogeusdc 

		symbol_b_g_dogeusdc = symbol_b_l_dogeusdc 
		price_bids_b_g_dogeusdc = price_bids_b_l_dogeusdc 
		qty_bids_b_g_dogeusdc = qty_bids_b_l_dogeusdc 
		price_asks_b_g_dogeusdc = price_asks_b_l_dogeusdc 
		qty_asks_b_g_dogeusdc = qty_asks_b_l_dogeusdc 


def on_close_dogeusdc(ws): 
	print('### closed ###') 

def on_error_dogeusdc(ws, message): 
	print(message) 

def on_open_dogeusdc(ws): 
	ws.send(json.dumps({'sub': f'market.dogeusdc.ticker'})) 

def loop_dogeusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dogeusdc, 
		on_close=on_close_dogeusdc, 
		on_error=on_error_dogeusdc) 
	ws.on_open = on_open_dogeusdc 
	ws.run_forever() 

Thread(target=loop_dogeusdc).start() 

def loop_dogeusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_dogeusdt != 0.0 and qty_bids_a_g_dogeusdt != 0.0 and price_asks_a_g_dogeusdt != 0.0 and qty_asks_a_g_dogeusdt != 0.0 and price_bids_b_g_dogeusdc != 0.0 and qty_bids_b_g_dogeusdc != 0.0 and price_asks_b_g_dogeusdc != 0.0 and qty_asks_b_g_dogeusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_dogeusdt) 
			price_b = float(price_bids_b_g_dogeusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_dogeusdc, pribil)

Thread(target=loop_dogeusdt_Trade).start() 

symbol_a_g_usddusdt = 'usddusdt' 
price_bids_a_g_usddusdt = float(0.0) 
qty_bids_a_g_usddusdt = float(0.0) 
price_asks_a_g_usddusdt = float(0.0) 
qty_asks_a_g_usddusdt = float(0.0) 

def on_message_usddusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_usddusdt = 'usddusdt' 
		price_bids_a_l_usddusdt = data['tick']['bid'] 
		qty_bids_a_l_usddusdt = data['tick']['bidSize'] 
		price_asks_a_l_usddusdt = data['tick']['ask'] 
		qty_asks_a_l_usddusdt = data['tick']['askSize'] 

		global symbol_a_g_usddusdt 
		global price_bids_a_g_usddusdt 
		global qty_bids_a_g_usddusdt 
		global price_asks_a_g_usddusdt 
		global qty_asks_a_g_usddusdt 

		symbol_a_g_usddusdt = symbol_a_l_usddusdt 
		price_bids_a_g_usddusdt = price_bids_a_l_usddusdt 
		qty_bids_a_g_usddusdt = qty_bids_a_l_usddusdt 
		price_asks_a_g_usddusdt = price_asks_a_l_usddusdt 
		qty_asks_a_g_usddusdt = qty_asks_a_l_usddusdt 

def on_close_usddusdt(ws): 
	print('### closed ###') 

def on_error_usddusdt(ws, message): 
	print(message) 

def on_open_usddusdt(ws): 
	ws.send(json.dumps({'sub': f'market.usddusdt.ticker'})) 

def loop_usddusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_usddusdt, 
		on_close=on_close_usddusdt, 
		on_error=on_error_usddusdt) 
	ws.on_open = on_open_usddusdt 
	ws.run_forever() 

Thread(target=loop_usddusdt).start() 

symbol_b_g_usddusdc = 'usddusdc' 
price_bids_b_g_usddusdc = float(0.0) 
qty_bids_b_g_usddusdc = float(0.0) 
price_asks_b_g_usddusdc = float(0.0) 
qty_asks_b_g_usddusdc = float(0.0) 

def on_message_usddusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_usddusdc = 'usddusdc' 
		price_bids_b_l_usddusdc = data['tick']['bid'] 
		qty_bids_b_l_usddusdc = data['tick']['bidSize']
		price_asks_b_l_usddusdc = data['tick']['ask'] 
		qty_asks_b_l_usddusdc = data['tick']['askSize'] 

		global symbol_b_g_usddusdc 
		global price_bids_b_g_usddusdc 
		global qty_bids_b_g_usddusdc 
		global price_asks_b_g_usddusdc 
		global qty_asks_b_g_usddusdc 

		symbol_b_g_usddusdc = symbol_b_l_usddusdc 
		price_bids_b_g_usddusdc = price_bids_b_l_usddusdc 
		qty_bids_b_g_usddusdc = qty_bids_b_l_usddusdc 
		price_asks_b_g_usddusdc = price_asks_b_l_usddusdc 
		qty_asks_b_g_usddusdc = qty_asks_b_l_usddusdc 


def on_close_usddusdc(ws): 
	print('### closed ###') 

def on_error_usddusdc(ws, message): 
	print(message) 

def on_open_usddusdc(ws): 
	ws.send(json.dumps({'sub': f'market.usddusdc.ticker'})) 

def loop_usddusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_usddusdc, 
		on_close=on_close_usddusdc, 
		on_error=on_error_usddusdc) 
	ws.on_open = on_open_usddusdc 
	ws.run_forever() 

Thread(target=loop_usddusdc).start() 

def loop_usddusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_usddusdt != 0.0 and qty_bids_a_g_usddusdt != 0.0 and price_asks_a_g_usddusdt != 0.0 and qty_asks_a_g_usddusdt != 0.0 and price_bids_b_g_usddusdc != 0.0 and qty_bids_b_g_usddusdc != 0.0 and price_asks_b_g_usddusdc != 0.0 and qty_asks_b_g_usddusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_usddusdt) 
			price_b = float(price_bids_b_g_usddusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_usddusdc, pribil)

Thread(target=loop_usddusdt_Trade).start() 

symbol_a_g_neousdt = 'neousdt' 
price_bids_a_g_neousdt = float(0.0) 
qty_bids_a_g_neousdt = float(0.0) 
price_asks_a_g_neousdt = float(0.0) 
qty_asks_a_g_neousdt = float(0.0) 

def on_message_neousdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_neousdt = 'neousdt' 
		price_bids_a_l_neousdt = data['tick']['bid'] 
		qty_bids_a_l_neousdt = data['tick']['bidSize'] 
		price_asks_a_l_neousdt = data['tick']['ask'] 
		qty_asks_a_l_neousdt = data['tick']['askSize'] 

		global symbol_a_g_neousdt 
		global price_bids_a_g_neousdt 
		global qty_bids_a_g_neousdt 
		global price_asks_a_g_neousdt 
		global qty_asks_a_g_neousdt 

		symbol_a_g_neousdt = symbol_a_l_neousdt 
		price_bids_a_g_neousdt = price_bids_a_l_neousdt 
		qty_bids_a_g_neousdt = qty_bids_a_l_neousdt 
		price_asks_a_g_neousdt = price_asks_a_l_neousdt 
		qty_asks_a_g_neousdt = qty_asks_a_l_neousdt 

def on_close_neousdt(ws): 
	print('### closed ###') 

def on_error_neousdt(ws, message): 
	print(message) 

def on_open_neousdt(ws): 
	ws.send(json.dumps({'sub': f'market.neousdt.ticker'})) 

def loop_neousdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_neousdt, 
		on_close=on_close_neousdt, 
		on_error=on_error_neousdt) 
	ws.on_open = on_open_neousdt 
	ws.run_forever() 

Thread(target=loop_neousdt).start() 

symbol_b_g_neobtc = 'neobtc' 
price_bids_b_g_neobtc = float(0.0) 
qty_bids_b_g_neobtc = float(0.0) 
price_asks_b_g_neobtc = float(0.0) 
qty_asks_b_g_neobtc = float(0.0) 

def on_message_neobtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_neobtc = 'neobtc' 
		price_bids_b_l_neobtc = data['tick']['bid'] 
		qty_bids_b_l_neobtc = data['tick']['bidSize']
		price_asks_b_l_neobtc = data['tick']['ask'] 
		qty_asks_b_l_neobtc = data['tick']['askSize'] 

		global symbol_b_g_neobtc 
		global price_bids_b_g_neobtc 
		global qty_bids_b_g_neobtc 
		global price_asks_b_g_neobtc 
		global qty_asks_b_g_neobtc 

		symbol_b_g_neobtc = symbol_b_l_neobtc 
		price_bids_b_g_neobtc = price_bids_b_l_neobtc 
		qty_bids_b_g_neobtc = qty_bids_b_l_neobtc 
		price_asks_b_g_neobtc = price_asks_b_l_neobtc 
		qty_asks_b_g_neobtc = qty_asks_b_l_neobtc 


def on_close_neobtc(ws): 
	print('### closed ###') 

def on_error_neobtc(ws, message): 
	print(message) 

def on_open_neobtc(ws): 
	ws.send(json.dumps({'sub': f'market.neobtc.ticker'})) 

def loop_neobtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_neobtc, 
		on_close=on_close_neobtc, 
		on_error=on_error_neobtc) 
	ws.on_open = on_open_neobtc 
	ws.run_forever() 

Thread(target=loop_neobtc).start() 

def loop_neousdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_neousdt != 0.0 and qty_bids_a_g_neousdt != 0.0 and price_asks_a_g_neousdt != 0.0 and qty_asks_a_g_neousdt != 0.0 and price_bids_b_g_neobtc != 0.0 and qty_bids_b_g_neobtc != 0.0 and price_asks_b_g_neobtc != 0.0 and qty_asks_b_g_neobtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_neousdt) 
			price_b = float(price_bids_b_g_neobtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_neobtc, pribil)

Thread(target=loop_neousdt_Trade).start() 

symbol_a_g_steemusdt = 'steemusdt' 
price_bids_a_g_steemusdt = float(0.0) 
qty_bids_a_g_steemusdt = float(0.0) 
price_asks_a_g_steemusdt = float(0.0) 
qty_asks_a_g_steemusdt = float(0.0) 

def on_message_steemusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_steemusdt = 'steemusdt' 
		price_bids_a_l_steemusdt = data['tick']['bid'] 
		qty_bids_a_l_steemusdt = data['tick']['bidSize'] 
		price_asks_a_l_steemusdt = data['tick']['ask'] 
		qty_asks_a_l_steemusdt = data['tick']['askSize'] 

		global symbol_a_g_steemusdt 
		global price_bids_a_g_steemusdt 
		global qty_bids_a_g_steemusdt 
		global price_asks_a_g_steemusdt 
		global qty_asks_a_g_steemusdt 

		symbol_a_g_steemusdt = symbol_a_l_steemusdt 
		price_bids_a_g_steemusdt = price_bids_a_l_steemusdt 
		qty_bids_a_g_steemusdt = qty_bids_a_l_steemusdt 
		price_asks_a_g_steemusdt = price_asks_a_l_steemusdt 
		qty_asks_a_g_steemusdt = qty_asks_a_l_steemusdt 

def on_close_steemusdt(ws): 
	print('### closed ###') 

def on_error_steemusdt(ws, message): 
	print(message) 

def on_open_steemusdt(ws): 
	ws.send(json.dumps({'sub': f'market.steemusdt.ticker'})) 

def loop_steemusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_steemusdt, 
		on_close=on_close_steemusdt, 
		on_error=on_error_steemusdt) 
	ws.on_open = on_open_steemusdt 
	ws.run_forever() 

Thread(target=loop_steemusdt).start() 

symbol_b_g_steembtc = 'steembtc' 
price_bids_b_g_steembtc = float(0.0) 
qty_bids_b_g_steembtc = float(0.0) 
price_asks_b_g_steembtc = float(0.0) 
qty_asks_b_g_steembtc = float(0.0) 

def on_message_steembtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_steembtc = 'steembtc' 
		price_bids_b_l_steembtc = data['tick']['bid'] 
		qty_bids_b_l_steembtc = data['tick']['bidSize']
		price_asks_b_l_steembtc = data['tick']['ask'] 
		qty_asks_b_l_steembtc = data['tick']['askSize'] 

		global symbol_b_g_steembtc 
		global price_bids_b_g_steembtc 
		global qty_bids_b_g_steembtc 
		global price_asks_b_g_steembtc 
		global qty_asks_b_g_steembtc 

		symbol_b_g_steembtc = symbol_b_l_steembtc 
		price_bids_b_g_steembtc = price_bids_b_l_steembtc 
		qty_bids_b_g_steembtc = qty_bids_b_l_steembtc 
		price_asks_b_g_steembtc = price_asks_b_l_steembtc 
		qty_asks_b_g_steembtc = qty_asks_b_l_steembtc 


def on_close_steembtc(ws): 
	print('### closed ###') 

def on_error_steembtc(ws, message): 
	print(message) 

def on_open_steembtc(ws): 
	ws.send(json.dumps({'sub': f'market.steembtc.ticker'})) 

def loop_steembtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_steembtc, 
		on_close=on_close_steembtc, 
		on_error=on_error_steembtc) 
	ws.on_open = on_open_steembtc 
	ws.run_forever() 

Thread(target=loop_steembtc).start() 

def loop_steemusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_steemusdt != 0.0 and qty_bids_a_g_steemusdt != 0.0 and price_asks_a_g_steemusdt != 0.0 and qty_asks_a_g_steemusdt != 0.0 and price_bids_b_g_steembtc != 0.0 and qty_bids_b_g_steembtc != 0.0 and price_asks_b_g_steembtc != 0.0 and qty_asks_b_g_steembtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_steemusdt) 
			price_b = float(price_bids_b_g_steembtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_steembtc, pribil)

Thread(target=loop_steemusdt_Trade).start() 

symbol_a_g_filusdt = 'filusdt' 
price_bids_a_g_filusdt = float(0.0) 
qty_bids_a_g_filusdt = float(0.0) 
price_asks_a_g_filusdt = float(0.0) 
qty_asks_a_g_filusdt = float(0.0) 

def on_message_filusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_filusdt = 'filusdt' 
		price_bids_a_l_filusdt = data['tick']['bid'] 
		qty_bids_a_l_filusdt = data['tick']['bidSize'] 
		price_asks_a_l_filusdt = data['tick']['ask'] 
		qty_asks_a_l_filusdt = data['tick']['askSize'] 

		global symbol_a_g_filusdt 
		global price_bids_a_g_filusdt 
		global qty_bids_a_g_filusdt 
		global price_asks_a_g_filusdt 
		global qty_asks_a_g_filusdt 

		symbol_a_g_filusdt = symbol_a_l_filusdt 
		price_bids_a_g_filusdt = price_bids_a_l_filusdt 
		qty_bids_a_g_filusdt = qty_bids_a_l_filusdt 
		price_asks_a_g_filusdt = price_asks_a_l_filusdt 
		qty_asks_a_g_filusdt = qty_asks_a_l_filusdt 

def on_close_filusdt(ws): 
	print('### closed ###') 

def on_error_filusdt(ws, message): 
	print(message) 

def on_open_filusdt(ws): 
	ws.send(json.dumps({'sub': f'market.filusdt.ticker'})) 

def loop_filusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_filusdt, 
		on_close=on_close_filusdt, 
		on_error=on_error_filusdt) 
	ws.on_open = on_open_filusdt 
	ws.run_forever() 

Thread(target=loop_filusdt).start() 

symbol_b_g_filusdd = 'filusdd' 
price_bids_b_g_filusdd = float(0.0) 
qty_bids_b_g_filusdd = float(0.0) 
price_asks_b_g_filusdd = float(0.0) 
qty_asks_b_g_filusdd = float(0.0) 

def on_message_filusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_filusdd = 'filusdd' 
		price_bids_b_l_filusdd = data['tick']['bid'] 
		qty_bids_b_l_filusdd = data['tick']['bidSize']
		price_asks_b_l_filusdd = data['tick']['ask'] 
		qty_asks_b_l_filusdd = data['tick']['askSize'] 

		global symbol_b_g_filusdd 
		global price_bids_b_g_filusdd 
		global qty_bids_b_g_filusdd 
		global price_asks_b_g_filusdd 
		global qty_asks_b_g_filusdd 

		symbol_b_g_filusdd = symbol_b_l_filusdd 
		price_bids_b_g_filusdd = price_bids_b_l_filusdd 
		qty_bids_b_g_filusdd = qty_bids_b_l_filusdd 
		price_asks_b_g_filusdd = price_asks_b_l_filusdd 
		qty_asks_b_g_filusdd = qty_asks_b_l_filusdd 


def on_close_filusdd(ws): 
	print('### closed ###') 

def on_error_filusdd(ws, message): 
	print(message) 

def on_open_filusdd(ws): 
	ws.send(json.dumps({'sub': f'market.filusdd.ticker'})) 

def loop_filusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_filusdd, 
		on_close=on_close_filusdd, 
		on_error=on_error_filusdd) 
	ws.on_open = on_open_filusdd 
	ws.run_forever() 

Thread(target=loop_filusdd).start() 

def loop_filusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_filusdt != 0.0 and qty_bids_a_g_filusdt != 0.0 and price_asks_a_g_filusdt != 0.0 and qty_asks_a_g_filusdt != 0.0 and price_bids_b_g_filusdd != 0.0 and qty_bids_b_g_filusdd != 0.0 and price_asks_b_g_filusdd != 0.0 and qty_asks_b_g_filusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_filusdt) 
			price_b = float(price_bids_b_g_filusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_filusdd, pribil)

Thread(target=loop_filusdt_Trade).start() 

symbol_a_g_rcccusdt = 'rcccusdt' 
price_bids_a_g_rcccusdt = float(0.0) 
qty_bids_a_g_rcccusdt = float(0.0) 
price_asks_a_g_rcccusdt = float(0.0) 
qty_asks_a_g_rcccusdt = float(0.0) 

def on_message_rcccusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_rcccusdt = 'rcccusdt' 
		price_bids_a_l_rcccusdt = data['tick']['bid'] 
		qty_bids_a_l_rcccusdt = data['tick']['bidSize'] 
		price_asks_a_l_rcccusdt = data['tick']['ask'] 
		qty_asks_a_l_rcccusdt = data['tick']['askSize'] 

		global symbol_a_g_rcccusdt 
		global price_bids_a_g_rcccusdt 
		global qty_bids_a_g_rcccusdt 
		global price_asks_a_g_rcccusdt 
		global qty_asks_a_g_rcccusdt 

		symbol_a_g_rcccusdt = symbol_a_l_rcccusdt 
		price_bids_a_g_rcccusdt = price_bids_a_l_rcccusdt 
		qty_bids_a_g_rcccusdt = qty_bids_a_l_rcccusdt 
		price_asks_a_g_rcccusdt = price_asks_a_l_rcccusdt 
		qty_asks_a_g_rcccusdt = qty_asks_a_l_rcccusdt 

def on_close_rcccusdt(ws): 
	print('### closed ###') 

def on_error_rcccusdt(ws, message): 
	print(message) 

def on_open_rcccusdt(ws): 
	ws.send(json.dumps({'sub': f'market.rcccusdt.ticker'})) 

def loop_rcccusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rcccusdt, 
		on_close=on_close_rcccusdt, 
		on_error=on_error_rcccusdt) 
	ws.on_open = on_open_rcccusdt 
	ws.run_forever() 

Thread(target=loop_rcccusdt).start() 

symbol_b_g_rcccbtc = 'rcccbtc' 
price_bids_b_g_rcccbtc = float(0.0) 
qty_bids_b_g_rcccbtc = float(0.0) 
price_asks_b_g_rcccbtc = float(0.0) 
qty_asks_b_g_rcccbtc = float(0.0) 

def on_message_rcccbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_rcccbtc = 'rcccbtc' 
		price_bids_b_l_rcccbtc = data['tick']['bid'] 
		qty_bids_b_l_rcccbtc = data['tick']['bidSize']
		price_asks_b_l_rcccbtc = data['tick']['ask'] 
		qty_asks_b_l_rcccbtc = data['tick']['askSize'] 

		global symbol_b_g_rcccbtc 
		global price_bids_b_g_rcccbtc 
		global qty_bids_b_g_rcccbtc 
		global price_asks_b_g_rcccbtc 
		global qty_asks_b_g_rcccbtc 

		symbol_b_g_rcccbtc = symbol_b_l_rcccbtc 
		price_bids_b_g_rcccbtc = price_bids_b_l_rcccbtc 
		qty_bids_b_g_rcccbtc = qty_bids_b_l_rcccbtc 
		price_asks_b_g_rcccbtc = price_asks_b_l_rcccbtc 
		qty_asks_b_g_rcccbtc = qty_asks_b_l_rcccbtc 


def on_close_rcccbtc(ws): 
	print('### closed ###') 

def on_error_rcccbtc(ws, message): 
	print(message) 

def on_open_rcccbtc(ws): 
	ws.send(json.dumps({'sub': f'market.rcccbtc.ticker'})) 

def loop_rcccbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_rcccbtc, 
		on_close=on_close_rcccbtc, 
		on_error=on_error_rcccbtc) 
	ws.on_open = on_open_rcccbtc 
	ws.run_forever() 

Thread(target=loop_rcccbtc).start() 

def loop_rcccusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_rcccusdt != 0.0 and qty_bids_a_g_rcccusdt != 0.0 and price_asks_a_g_rcccusdt != 0.0 and qty_asks_a_g_rcccusdt != 0.0 and price_bids_b_g_rcccbtc != 0.0 and qty_bids_b_g_rcccbtc != 0.0 and price_asks_b_g_rcccbtc != 0.0 and qty_asks_b_g_rcccbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_rcccusdt) 
			price_b = float(price_bids_b_g_rcccbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_rcccbtc, pribil)

Thread(target=loop_rcccusdt_Trade).start() 

symbol_a_g_xrtusdt = 'xrtusdt' 
price_bids_a_g_xrtusdt = float(0.0) 
qty_bids_a_g_xrtusdt = float(0.0) 
price_asks_a_g_xrtusdt = float(0.0) 
qty_asks_a_g_xrtusdt = float(0.0) 

def on_message_xrtusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_xrtusdt = 'xrtusdt' 
		price_bids_a_l_xrtusdt = data['tick']['bid'] 
		qty_bids_a_l_xrtusdt = data['tick']['bidSize'] 
		price_asks_a_l_xrtusdt = data['tick']['ask'] 
		qty_asks_a_l_xrtusdt = data['tick']['askSize'] 

		global symbol_a_g_xrtusdt 
		global price_bids_a_g_xrtusdt 
		global qty_bids_a_g_xrtusdt 
		global price_asks_a_g_xrtusdt 
		global qty_asks_a_g_xrtusdt 

		symbol_a_g_xrtusdt = symbol_a_l_xrtusdt 
		price_bids_a_g_xrtusdt = price_bids_a_l_xrtusdt 
		qty_bids_a_g_xrtusdt = qty_bids_a_l_xrtusdt 
		price_asks_a_g_xrtusdt = price_asks_a_l_xrtusdt 
		qty_asks_a_g_xrtusdt = qty_asks_a_l_xrtusdt 

def on_close_xrtusdt(ws): 
	print('### closed ###') 

def on_error_xrtusdt(ws, message): 
	print(message) 

def on_open_xrtusdt(ws): 
	ws.send(json.dumps({'sub': f'market.xrtusdt.ticker'})) 

def loop_xrtusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xrtusdt, 
		on_close=on_close_xrtusdt, 
		on_error=on_error_xrtusdt) 
	ws.on_open = on_open_xrtusdt 
	ws.run_forever() 

Thread(target=loop_xrtusdt).start() 

symbol_b_g_xrteth = 'xrteth' 
price_bids_b_g_xrteth = float(0.0) 
qty_bids_b_g_xrteth = float(0.0) 
price_asks_b_g_xrteth = float(0.0) 
qty_asks_b_g_xrteth = float(0.0) 

def on_message_xrteth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_xrteth = 'xrteth' 
		price_bids_b_l_xrteth = data['tick']['bid'] 
		qty_bids_b_l_xrteth = data['tick']['bidSize']
		price_asks_b_l_xrteth = data['tick']['ask'] 
		qty_asks_b_l_xrteth = data['tick']['askSize'] 

		global symbol_b_g_xrteth 
		global price_bids_b_g_xrteth 
		global qty_bids_b_g_xrteth 
		global price_asks_b_g_xrteth 
		global qty_asks_b_g_xrteth 

		symbol_b_g_xrteth = symbol_b_l_xrteth 
		price_bids_b_g_xrteth = price_bids_b_l_xrteth 
		qty_bids_b_g_xrteth = qty_bids_b_l_xrteth 
		price_asks_b_g_xrteth = price_asks_b_l_xrteth 
		qty_asks_b_g_xrteth = qty_asks_b_l_xrteth 


def on_close_xrteth(ws): 
	print('### closed ###') 

def on_error_xrteth(ws, message): 
	print(message) 

def on_open_xrteth(ws): 
	ws.send(json.dumps({'sub': f'market.xrteth.ticker'})) 

def loop_xrteth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xrteth, 
		on_close=on_close_xrteth, 
		on_error=on_error_xrteth) 
	ws.on_open = on_open_xrteth 
	ws.run_forever() 

Thread(target=loop_xrteth).start() 

def loop_xrtusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_xrtusdt != 0.0 and qty_bids_a_g_xrtusdt != 0.0 and price_asks_a_g_xrtusdt != 0.0 and qty_asks_a_g_xrtusdt != 0.0 and price_bids_b_g_xrteth != 0.0 and qty_bids_b_g_xrteth != 0.0 and price_asks_b_g_xrteth != 0.0 and qty_asks_b_g_xrteth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_xrtusdt) 
			price_b = float(price_bids_b_g_xrteth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_xrteth, pribil)

Thread(target=loop_xrtusdt_Trade).start() 

symbol_a_g_yggusdt = 'yggusdt' 
price_bids_a_g_yggusdt = float(0.0) 
qty_bids_a_g_yggusdt = float(0.0) 
price_asks_a_g_yggusdt = float(0.0) 
qty_asks_a_g_yggusdt = float(0.0) 

def on_message_yggusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_yggusdt = 'yggusdt' 
		price_bids_a_l_yggusdt = data['tick']['bid'] 
		qty_bids_a_l_yggusdt = data['tick']['bidSize'] 
		price_asks_a_l_yggusdt = data['tick']['ask'] 
		qty_asks_a_l_yggusdt = data['tick']['askSize'] 

		global symbol_a_g_yggusdt 
		global price_bids_a_g_yggusdt 
		global qty_bids_a_g_yggusdt 
		global price_asks_a_g_yggusdt 
		global qty_asks_a_g_yggusdt 

		symbol_a_g_yggusdt = symbol_a_l_yggusdt 
		price_bids_a_g_yggusdt = price_bids_a_l_yggusdt 
		qty_bids_a_g_yggusdt = qty_bids_a_l_yggusdt 
		price_asks_a_g_yggusdt = price_asks_a_l_yggusdt 
		qty_asks_a_g_yggusdt = qty_asks_a_l_yggusdt 

def on_close_yggusdt(ws): 
	print('### closed ###') 

def on_error_yggusdt(ws, message): 
	print(message) 

def on_open_yggusdt(ws): 
	ws.send(json.dumps({'sub': f'market.yggusdt.ticker'})) 

def loop_yggusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_yggusdt, 
		on_close=on_close_yggusdt, 
		on_error=on_error_yggusdt) 
	ws.on_open = on_open_yggusdt 
	ws.run_forever() 

Thread(target=loop_yggusdt).start() 

symbol_b_g_yggbtc = 'yggbtc' 
price_bids_b_g_yggbtc = float(0.0) 
qty_bids_b_g_yggbtc = float(0.0) 
price_asks_b_g_yggbtc = float(0.0) 
qty_asks_b_g_yggbtc = float(0.0) 

def on_message_yggbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_yggbtc = 'yggbtc' 
		price_bids_b_l_yggbtc = data['tick']['bid'] 
		qty_bids_b_l_yggbtc = data['tick']['bidSize']
		price_asks_b_l_yggbtc = data['tick']['ask'] 
		qty_asks_b_l_yggbtc = data['tick']['askSize'] 

		global symbol_b_g_yggbtc 
		global price_bids_b_g_yggbtc 
		global qty_bids_b_g_yggbtc 
		global price_asks_b_g_yggbtc 
		global qty_asks_b_g_yggbtc 

		symbol_b_g_yggbtc = symbol_b_l_yggbtc 
		price_bids_b_g_yggbtc = price_bids_b_l_yggbtc 
		qty_bids_b_g_yggbtc = qty_bids_b_l_yggbtc 
		price_asks_b_g_yggbtc = price_asks_b_l_yggbtc 
		qty_asks_b_g_yggbtc = qty_asks_b_l_yggbtc 


def on_close_yggbtc(ws): 
	print('### closed ###') 

def on_error_yggbtc(ws, message): 
	print(message) 

def on_open_yggbtc(ws): 
	ws.send(json.dumps({'sub': f'market.yggbtc.ticker'})) 

def loop_yggbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_yggbtc, 
		on_close=on_close_yggbtc, 
		on_error=on_error_yggbtc) 
	ws.on_open = on_open_yggbtc 
	ws.run_forever() 

Thread(target=loop_yggbtc).start() 

def loop_yggusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_yggusdt != 0.0 and qty_bids_a_g_yggusdt != 0.0 and price_asks_a_g_yggusdt != 0.0 and qty_asks_a_g_yggusdt != 0.0 and price_bids_b_g_yggbtc != 0.0 and qty_bids_b_g_yggbtc != 0.0 and price_asks_b_g_yggbtc != 0.0 and qty_asks_b_g_yggbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_yggusdt) 
			price_b = float(price_bids_b_g_yggbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_yggbtc, pribil)

Thread(target=loop_yggusdt_Trade).start() 

symbol_a_g_wiccusdt = 'wiccusdt' 
price_bids_a_g_wiccusdt = float(0.0) 
qty_bids_a_g_wiccusdt = float(0.0) 
price_asks_a_g_wiccusdt = float(0.0) 
qty_asks_a_g_wiccusdt = float(0.0) 

def on_message_wiccusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_wiccusdt = 'wiccusdt' 
		price_bids_a_l_wiccusdt = data['tick']['bid'] 
		qty_bids_a_l_wiccusdt = data['tick']['bidSize'] 
		price_asks_a_l_wiccusdt = data['tick']['ask'] 
		qty_asks_a_l_wiccusdt = data['tick']['askSize'] 

		global symbol_a_g_wiccusdt 
		global price_bids_a_g_wiccusdt 
		global qty_bids_a_g_wiccusdt 
		global price_asks_a_g_wiccusdt 
		global qty_asks_a_g_wiccusdt 

		symbol_a_g_wiccusdt = symbol_a_l_wiccusdt 
		price_bids_a_g_wiccusdt = price_bids_a_l_wiccusdt 
		qty_bids_a_g_wiccusdt = qty_bids_a_l_wiccusdt 
		price_asks_a_g_wiccusdt = price_asks_a_l_wiccusdt 
		qty_asks_a_g_wiccusdt = qty_asks_a_l_wiccusdt 

def on_close_wiccusdt(ws): 
	print('### closed ###') 

def on_error_wiccusdt(ws, message): 
	print(message) 

def on_open_wiccusdt(ws): 
	ws.send(json.dumps({'sub': f'market.wiccusdt.ticker'})) 

def loop_wiccusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wiccusdt, 
		on_close=on_close_wiccusdt, 
		on_error=on_error_wiccusdt) 
	ws.on_open = on_open_wiccusdt 
	ws.run_forever() 

Thread(target=loop_wiccusdt).start() 

symbol_b_g_wiccbtc = 'wiccbtc' 
price_bids_b_g_wiccbtc = float(0.0) 
qty_bids_b_g_wiccbtc = float(0.0) 
price_asks_b_g_wiccbtc = float(0.0) 
qty_asks_b_g_wiccbtc = float(0.0) 

def on_message_wiccbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_wiccbtc = 'wiccbtc' 
		price_bids_b_l_wiccbtc = data['tick']['bid'] 
		qty_bids_b_l_wiccbtc = data['tick']['bidSize']
		price_asks_b_l_wiccbtc = data['tick']['ask'] 
		qty_asks_b_l_wiccbtc = data['tick']['askSize'] 

		global symbol_b_g_wiccbtc 
		global price_bids_b_g_wiccbtc 
		global qty_bids_b_g_wiccbtc 
		global price_asks_b_g_wiccbtc 
		global qty_asks_b_g_wiccbtc 

		symbol_b_g_wiccbtc = symbol_b_l_wiccbtc 
		price_bids_b_g_wiccbtc = price_bids_b_l_wiccbtc 
		qty_bids_b_g_wiccbtc = qty_bids_b_l_wiccbtc 
		price_asks_b_g_wiccbtc = price_asks_b_l_wiccbtc 
		qty_asks_b_g_wiccbtc = qty_asks_b_l_wiccbtc 


def on_close_wiccbtc(ws): 
	print('### closed ###') 

def on_error_wiccbtc(ws, message): 
	print(message) 

def on_open_wiccbtc(ws): 
	ws.send(json.dumps({'sub': f'market.wiccbtc.ticker'})) 

def loop_wiccbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wiccbtc, 
		on_close=on_close_wiccbtc, 
		on_error=on_error_wiccbtc) 
	ws.on_open = on_open_wiccbtc 
	ws.run_forever() 

Thread(target=loop_wiccbtc).start() 

def loop_wiccusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_wiccusdt != 0.0 and qty_bids_a_g_wiccusdt != 0.0 and price_asks_a_g_wiccusdt != 0.0 and qty_asks_a_g_wiccusdt != 0.0 and price_bids_b_g_wiccbtc != 0.0 and qty_bids_b_g_wiccbtc != 0.0 and price_asks_b_g_wiccbtc != 0.0 and qty_asks_b_g_wiccbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_wiccusdt) 
			price_b = float(price_bids_b_g_wiccbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_wiccbtc, pribil)

Thread(target=loop_wiccusdt_Trade).start() 

symbol_a_g_seeleusdt = 'seeleusdt' 
price_bids_a_g_seeleusdt = float(0.0) 
qty_bids_a_g_seeleusdt = float(0.0) 
price_asks_a_g_seeleusdt = float(0.0) 
qty_asks_a_g_seeleusdt = float(0.0) 

def on_message_seeleusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_seeleusdt = 'seeleusdt' 
		price_bids_a_l_seeleusdt = data['tick']['bid'] 
		qty_bids_a_l_seeleusdt = data['tick']['bidSize'] 
		price_asks_a_l_seeleusdt = data['tick']['ask'] 
		qty_asks_a_l_seeleusdt = data['tick']['askSize'] 

		global symbol_a_g_seeleusdt 
		global price_bids_a_g_seeleusdt 
		global qty_bids_a_g_seeleusdt 
		global price_asks_a_g_seeleusdt 
		global qty_asks_a_g_seeleusdt 

		symbol_a_g_seeleusdt = symbol_a_l_seeleusdt 
		price_bids_a_g_seeleusdt = price_bids_a_l_seeleusdt 
		qty_bids_a_g_seeleusdt = qty_bids_a_l_seeleusdt 
		price_asks_a_g_seeleusdt = price_asks_a_l_seeleusdt 
		qty_asks_a_g_seeleusdt = qty_asks_a_l_seeleusdt 

def on_close_seeleusdt(ws): 
	print('### closed ###') 

def on_error_seeleusdt(ws, message): 
	print(message) 

def on_open_seeleusdt(ws): 
	ws.send(json.dumps({'sub': f'market.seeleusdt.ticker'})) 

def loop_seeleusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_seeleusdt, 
		on_close=on_close_seeleusdt, 
		on_error=on_error_seeleusdt) 
	ws.on_open = on_open_seeleusdt 
	ws.run_forever() 

Thread(target=loop_seeleusdt).start() 

symbol_b_g_seeleeth = 'seeleeth' 
price_bids_b_g_seeleeth = float(0.0) 
qty_bids_b_g_seeleeth = float(0.0) 
price_asks_b_g_seeleeth = float(0.0) 
qty_asks_b_g_seeleeth = float(0.0) 

def on_message_seeleeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_seeleeth = 'seeleeth' 
		price_bids_b_l_seeleeth = data['tick']['bid'] 
		qty_bids_b_l_seeleeth = data['tick']['bidSize']
		price_asks_b_l_seeleeth = data['tick']['ask'] 
		qty_asks_b_l_seeleeth = data['tick']['askSize'] 

		global symbol_b_g_seeleeth 
		global price_bids_b_g_seeleeth 
		global qty_bids_b_g_seeleeth 
		global price_asks_b_g_seeleeth 
		global qty_asks_b_g_seeleeth 

		symbol_b_g_seeleeth = symbol_b_l_seeleeth 
		price_bids_b_g_seeleeth = price_bids_b_l_seeleeth 
		qty_bids_b_g_seeleeth = qty_bids_b_l_seeleeth 
		price_asks_b_g_seeleeth = price_asks_b_l_seeleeth 
		qty_asks_b_g_seeleeth = qty_asks_b_l_seeleeth 


def on_close_seeleeth(ws): 
	print('### closed ###') 

def on_error_seeleeth(ws, message): 
	print(message) 

def on_open_seeleeth(ws): 
	ws.send(json.dumps({'sub': f'market.seeleeth.ticker'})) 

def loop_seeleeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_seeleeth, 
		on_close=on_close_seeleeth, 
		on_error=on_error_seeleeth) 
	ws.on_open = on_open_seeleeth 
	ws.run_forever() 

Thread(target=loop_seeleeth).start() 

def loop_seeleusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_seeleusdt != 0.0 and qty_bids_a_g_seeleusdt != 0.0 and price_asks_a_g_seeleusdt != 0.0 and qty_asks_a_g_seeleusdt != 0.0 and price_bids_b_g_seeleeth != 0.0 and qty_bids_b_g_seeleeth != 0.0 and price_asks_b_g_seeleeth != 0.0 and qty_asks_b_g_seeleeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_seeleusdt) 
			price_b = float(price_bids_b_g_seeleeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_seeleeth, pribil)

Thread(target=loop_seeleusdt_Trade).start() 

symbol_a_g_yfiusdt = 'yfiusdt' 
price_bids_a_g_yfiusdt = float(0.0) 
qty_bids_a_g_yfiusdt = float(0.0) 
price_asks_a_g_yfiusdt = float(0.0) 
qty_asks_a_g_yfiusdt = float(0.0) 

def on_message_yfiusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_yfiusdt = 'yfiusdt' 
		price_bids_a_l_yfiusdt = data['tick']['bid'] 
		qty_bids_a_l_yfiusdt = data['tick']['bidSize'] 
		price_asks_a_l_yfiusdt = data['tick']['ask'] 
		qty_asks_a_l_yfiusdt = data['tick']['askSize'] 

		global symbol_a_g_yfiusdt 
		global price_bids_a_g_yfiusdt 
		global qty_bids_a_g_yfiusdt 
		global price_asks_a_g_yfiusdt 
		global qty_asks_a_g_yfiusdt 

		symbol_a_g_yfiusdt = symbol_a_l_yfiusdt 
		price_bids_a_g_yfiusdt = price_bids_a_l_yfiusdt 
		qty_bids_a_g_yfiusdt = qty_bids_a_l_yfiusdt 
		price_asks_a_g_yfiusdt = price_asks_a_l_yfiusdt 
		qty_asks_a_g_yfiusdt = qty_asks_a_l_yfiusdt 

def on_close_yfiusdt(ws): 
	print('### closed ###') 

def on_error_yfiusdt(ws, message): 
	print(message) 

def on_open_yfiusdt(ws): 
	ws.send(json.dumps({'sub': f'market.yfiusdt.ticker'})) 

def loop_yfiusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_yfiusdt, 
		on_close=on_close_yfiusdt, 
		on_error=on_error_yfiusdt) 
	ws.on_open = on_open_yfiusdt 
	ws.run_forever() 

Thread(target=loop_yfiusdt).start() 

symbol_b_g_yfibtc = 'yfibtc' 
price_bids_b_g_yfibtc = float(0.0) 
qty_bids_b_g_yfibtc = float(0.0) 
price_asks_b_g_yfibtc = float(0.0) 
qty_asks_b_g_yfibtc = float(0.0) 

def on_message_yfibtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_yfibtc = 'yfibtc' 
		price_bids_b_l_yfibtc = data['tick']['bid'] 
		qty_bids_b_l_yfibtc = data['tick']['bidSize']
		price_asks_b_l_yfibtc = data['tick']['ask'] 
		qty_asks_b_l_yfibtc = data['tick']['askSize'] 

		global symbol_b_g_yfibtc 
		global price_bids_b_g_yfibtc 
		global qty_bids_b_g_yfibtc 
		global price_asks_b_g_yfibtc 
		global qty_asks_b_g_yfibtc 

		symbol_b_g_yfibtc = symbol_b_l_yfibtc 
		price_bids_b_g_yfibtc = price_bids_b_l_yfibtc 
		qty_bids_b_g_yfibtc = qty_bids_b_l_yfibtc 
		price_asks_b_g_yfibtc = price_asks_b_l_yfibtc 
		qty_asks_b_g_yfibtc = qty_asks_b_l_yfibtc 


def on_close_yfibtc(ws): 
	print('### closed ###') 

def on_error_yfibtc(ws, message): 
	print(message) 

def on_open_yfibtc(ws): 
	ws.send(json.dumps({'sub': f'market.yfibtc.ticker'})) 

def loop_yfibtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_yfibtc, 
		on_close=on_close_yfibtc, 
		on_error=on_error_yfibtc) 
	ws.on_open = on_open_yfibtc 
	ws.run_forever() 

Thread(target=loop_yfibtc).start() 

def loop_yfiusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_yfiusdt != 0.0 and qty_bids_a_g_yfiusdt != 0.0 and price_asks_a_g_yfiusdt != 0.0 and qty_asks_a_g_yfiusdt != 0.0 and price_bids_b_g_yfibtc != 0.0 and qty_bids_b_g_yfibtc != 0.0 and price_asks_b_g_yfibtc != 0.0 and qty_asks_b_g_yfibtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_yfiusdt) 
			price_b = float(price_bids_b_g_yfibtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_yfibtc, pribil)

Thread(target=loop_yfiusdt_Trade).start() 

symbol_a_g_injusdt = 'injusdt' 
price_bids_a_g_injusdt = float(0.0) 
qty_bids_a_g_injusdt = float(0.0) 
price_asks_a_g_injusdt = float(0.0) 
qty_asks_a_g_injusdt = float(0.0) 

def on_message_injusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_injusdt = 'injusdt' 
		price_bids_a_l_injusdt = data['tick']['bid'] 
		qty_bids_a_l_injusdt = data['tick']['bidSize'] 
		price_asks_a_l_injusdt = data['tick']['ask'] 
		qty_asks_a_l_injusdt = data['tick']['askSize'] 

		global symbol_a_g_injusdt 
		global price_bids_a_g_injusdt 
		global qty_bids_a_g_injusdt 
		global price_asks_a_g_injusdt 
		global qty_asks_a_g_injusdt 

		symbol_a_g_injusdt = symbol_a_l_injusdt 
		price_bids_a_g_injusdt = price_bids_a_l_injusdt 
		qty_bids_a_g_injusdt = qty_bids_a_l_injusdt 
		price_asks_a_g_injusdt = price_asks_a_l_injusdt 
		qty_asks_a_g_injusdt = qty_asks_a_l_injusdt 

def on_close_injusdt(ws): 
	print('### closed ###') 

def on_error_injusdt(ws, message): 
	print(message) 

def on_open_injusdt(ws): 
	ws.send(json.dumps({'sub': f'market.injusdt.ticker'})) 

def loop_injusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_injusdt, 
		on_close=on_close_injusdt, 
		on_error=on_error_injusdt) 
	ws.on_open = on_open_injusdt 
	ws.run_forever() 

Thread(target=loop_injusdt).start() 

symbol_b_g_injbtc = 'injbtc' 
price_bids_b_g_injbtc = float(0.0) 
qty_bids_b_g_injbtc = float(0.0) 
price_asks_b_g_injbtc = float(0.0) 
qty_asks_b_g_injbtc = float(0.0) 

def on_message_injbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_injbtc = 'injbtc' 
		price_bids_b_l_injbtc = data['tick']['bid'] 
		qty_bids_b_l_injbtc = data['tick']['bidSize']
		price_asks_b_l_injbtc = data['tick']['ask'] 
		qty_asks_b_l_injbtc = data['tick']['askSize'] 

		global symbol_b_g_injbtc 
		global price_bids_b_g_injbtc 
		global qty_bids_b_g_injbtc 
		global price_asks_b_g_injbtc 
		global qty_asks_b_g_injbtc 

		symbol_b_g_injbtc = symbol_b_l_injbtc 
		price_bids_b_g_injbtc = price_bids_b_l_injbtc 
		qty_bids_b_g_injbtc = qty_bids_b_l_injbtc 
		price_asks_b_g_injbtc = price_asks_b_l_injbtc 
		qty_asks_b_g_injbtc = qty_asks_b_l_injbtc 


def on_close_injbtc(ws): 
	print('### closed ###') 

def on_error_injbtc(ws, message): 
	print(message) 

def on_open_injbtc(ws): 
	ws.send(json.dumps({'sub': f'market.injbtc.ticker'})) 

def loop_injbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_injbtc, 
		on_close=on_close_injbtc, 
		on_error=on_error_injbtc) 
	ws.on_open = on_open_injbtc 
	ws.run_forever() 

Thread(target=loop_injbtc).start() 

def loop_injusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_injusdt != 0.0 and qty_bids_a_g_injusdt != 0.0 and price_asks_a_g_injusdt != 0.0 and qty_asks_a_g_injusdt != 0.0 and price_bids_b_g_injbtc != 0.0 and qty_bids_b_g_injbtc != 0.0 and price_asks_b_g_injbtc != 0.0 and qty_asks_b_g_injbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_injusdt) 
			price_b = float(price_bids_b_g_injbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_injbtc, pribil)

Thread(target=loop_injusdt_Trade).start() 

symbol_a_g_wavesusdt = 'wavesusdt' 
price_bids_a_g_wavesusdt = float(0.0) 
qty_bids_a_g_wavesusdt = float(0.0) 
price_asks_a_g_wavesusdt = float(0.0) 
qty_asks_a_g_wavesusdt = float(0.0) 

def on_message_wavesusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_wavesusdt = 'wavesusdt' 
		price_bids_a_l_wavesusdt = data['tick']['bid'] 
		qty_bids_a_l_wavesusdt = data['tick']['bidSize'] 
		price_asks_a_l_wavesusdt = data['tick']['ask'] 
		qty_asks_a_l_wavesusdt = data['tick']['askSize'] 

		global symbol_a_g_wavesusdt 
		global price_bids_a_g_wavesusdt 
		global qty_bids_a_g_wavesusdt 
		global price_asks_a_g_wavesusdt 
		global qty_asks_a_g_wavesusdt 

		symbol_a_g_wavesusdt = symbol_a_l_wavesusdt 
		price_bids_a_g_wavesusdt = price_bids_a_l_wavesusdt 
		qty_bids_a_g_wavesusdt = qty_bids_a_l_wavesusdt 
		price_asks_a_g_wavesusdt = price_asks_a_l_wavesusdt 
		qty_asks_a_g_wavesusdt = qty_asks_a_l_wavesusdt 

def on_close_wavesusdt(ws): 
	print('### closed ###') 

def on_error_wavesusdt(ws, message): 
	print(message) 

def on_open_wavesusdt(ws): 
	ws.send(json.dumps({'sub': f'market.wavesusdt.ticker'})) 

def loop_wavesusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wavesusdt, 
		on_close=on_close_wavesusdt, 
		on_error=on_error_wavesusdt) 
	ws.on_open = on_open_wavesusdt 
	ws.run_forever() 

Thread(target=loop_wavesusdt).start() 

symbol_b_g_wavesbtc = 'wavesbtc' 
price_bids_b_g_wavesbtc = float(0.0) 
qty_bids_b_g_wavesbtc = float(0.0) 
price_asks_b_g_wavesbtc = float(0.0) 
qty_asks_b_g_wavesbtc = float(0.0) 

def on_message_wavesbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_wavesbtc = 'wavesbtc' 
		price_bids_b_l_wavesbtc = data['tick']['bid'] 
		qty_bids_b_l_wavesbtc = data['tick']['bidSize']
		price_asks_b_l_wavesbtc = data['tick']['ask'] 
		qty_asks_b_l_wavesbtc = data['tick']['askSize'] 

		global symbol_b_g_wavesbtc 
		global price_bids_b_g_wavesbtc 
		global qty_bids_b_g_wavesbtc 
		global price_asks_b_g_wavesbtc 
		global qty_asks_b_g_wavesbtc 

		symbol_b_g_wavesbtc = symbol_b_l_wavesbtc 
		price_bids_b_g_wavesbtc = price_bids_b_l_wavesbtc 
		qty_bids_b_g_wavesbtc = qty_bids_b_l_wavesbtc 
		price_asks_b_g_wavesbtc = price_asks_b_l_wavesbtc 
		qty_asks_b_g_wavesbtc = qty_asks_b_l_wavesbtc 


def on_close_wavesbtc(ws): 
	print('### closed ###') 

def on_error_wavesbtc(ws, message): 
	print(message) 

def on_open_wavesbtc(ws): 
	ws.send(json.dumps({'sub': f'market.wavesbtc.ticker'})) 

def loop_wavesbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_wavesbtc, 
		on_close=on_close_wavesbtc, 
		on_error=on_error_wavesbtc) 
	ws.on_open = on_open_wavesbtc 
	ws.run_forever() 

Thread(target=loop_wavesbtc).start() 

def loop_wavesusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_wavesusdt != 0.0 and qty_bids_a_g_wavesusdt != 0.0 and price_asks_a_g_wavesusdt != 0.0 and qty_asks_a_g_wavesusdt != 0.0 and price_bids_b_g_wavesbtc != 0.0 and qty_bids_b_g_wavesbtc != 0.0 and price_asks_b_g_wavesbtc != 0.0 and qty_asks_b_g_wavesbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_wavesusdt) 
			price_b = float(price_bids_b_g_wavesbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_wavesbtc, pribil)

Thread(target=loop_wavesusdt_Trade).start() 

symbol_a_g_frontusdt = 'frontusdt' 
price_bids_a_g_frontusdt = float(0.0) 
qty_bids_a_g_frontusdt = float(0.0) 
price_asks_a_g_frontusdt = float(0.0) 
qty_asks_a_g_frontusdt = float(0.0) 

def on_message_frontusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_frontusdt = 'frontusdt' 
		price_bids_a_l_frontusdt = data['tick']['bid'] 
		qty_bids_a_l_frontusdt = data['tick']['bidSize'] 
		price_asks_a_l_frontusdt = data['tick']['ask'] 
		qty_asks_a_l_frontusdt = data['tick']['askSize'] 

		global symbol_a_g_frontusdt 
		global price_bids_a_g_frontusdt 
		global qty_bids_a_g_frontusdt 
		global price_asks_a_g_frontusdt 
		global qty_asks_a_g_frontusdt 

		symbol_a_g_frontusdt = symbol_a_l_frontusdt 
		price_bids_a_g_frontusdt = price_bids_a_l_frontusdt 
		qty_bids_a_g_frontusdt = qty_bids_a_l_frontusdt 
		price_asks_a_g_frontusdt = price_asks_a_l_frontusdt 
		qty_asks_a_g_frontusdt = qty_asks_a_l_frontusdt 

def on_close_frontusdt(ws): 
	print('### closed ###') 

def on_error_frontusdt(ws, message): 
	print(message) 

def on_open_frontusdt(ws): 
	ws.send(json.dumps({'sub': f'market.frontusdt.ticker'})) 

def loop_frontusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_frontusdt, 
		on_close=on_close_frontusdt, 
		on_error=on_error_frontusdt) 
	ws.on_open = on_open_frontusdt 
	ws.run_forever() 

Thread(target=loop_frontusdt).start() 

symbol_b_g_frontbtc = 'frontbtc' 
price_bids_b_g_frontbtc = float(0.0) 
qty_bids_b_g_frontbtc = float(0.0) 
price_asks_b_g_frontbtc = float(0.0) 
qty_asks_b_g_frontbtc = float(0.0) 

def on_message_frontbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_frontbtc = 'frontbtc' 
		price_bids_b_l_frontbtc = data['tick']['bid'] 
		qty_bids_b_l_frontbtc = data['tick']['bidSize']
		price_asks_b_l_frontbtc = data['tick']['ask'] 
		qty_asks_b_l_frontbtc = data['tick']['askSize'] 

		global symbol_b_g_frontbtc 
		global price_bids_b_g_frontbtc 
		global qty_bids_b_g_frontbtc 
		global price_asks_b_g_frontbtc 
		global qty_asks_b_g_frontbtc 

		symbol_b_g_frontbtc = symbol_b_l_frontbtc 
		price_bids_b_g_frontbtc = price_bids_b_l_frontbtc 
		qty_bids_b_g_frontbtc = qty_bids_b_l_frontbtc 
		price_asks_b_g_frontbtc = price_asks_b_l_frontbtc 
		qty_asks_b_g_frontbtc = qty_asks_b_l_frontbtc 


def on_close_frontbtc(ws): 
	print('### closed ###') 

def on_error_frontbtc(ws, message): 
	print(message) 

def on_open_frontbtc(ws): 
	ws.send(json.dumps({'sub': f'market.frontbtc.ticker'})) 

def loop_frontbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_frontbtc, 
		on_close=on_close_frontbtc, 
		on_error=on_error_frontbtc) 
	ws.on_open = on_open_frontbtc 
	ws.run_forever() 

Thread(target=loop_frontbtc).start() 

def loop_frontusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_frontusdt != 0.0 and qty_bids_a_g_frontusdt != 0.0 and price_asks_a_g_frontusdt != 0.0 and qty_asks_a_g_frontusdt != 0.0 and price_bids_b_g_frontbtc != 0.0 and qty_bids_b_g_frontbtc != 0.0 and price_asks_b_g_frontbtc != 0.0 and qty_asks_b_g_frontbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_frontusdt) 
			price_b = float(price_bids_b_g_frontbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_frontbtc, pribil)

Thread(target=loop_frontusdt_Trade).start() 

symbol_a_g_jstusdt = 'jstusdt' 
price_bids_a_g_jstusdt = float(0.0) 
qty_bids_a_g_jstusdt = float(0.0) 
price_asks_a_g_jstusdt = float(0.0) 
qty_asks_a_g_jstusdt = float(0.0) 

def on_message_jstusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_jstusdt = 'jstusdt' 
		price_bids_a_l_jstusdt = data['tick']['bid'] 
		qty_bids_a_l_jstusdt = data['tick']['bidSize'] 
		price_asks_a_l_jstusdt = data['tick']['ask'] 
		qty_asks_a_l_jstusdt = data['tick']['askSize'] 

		global symbol_a_g_jstusdt 
		global price_bids_a_g_jstusdt 
		global qty_bids_a_g_jstusdt 
		global price_asks_a_g_jstusdt 
		global qty_asks_a_g_jstusdt 

		symbol_a_g_jstusdt = symbol_a_l_jstusdt 
		price_bids_a_g_jstusdt = price_bids_a_l_jstusdt 
		qty_bids_a_g_jstusdt = qty_bids_a_l_jstusdt 
		price_asks_a_g_jstusdt = price_asks_a_l_jstusdt 
		qty_asks_a_g_jstusdt = qty_asks_a_l_jstusdt 

def on_close_jstusdt(ws): 
	print('### closed ###') 

def on_error_jstusdt(ws, message): 
	print(message) 

def on_open_jstusdt(ws): 
	ws.send(json.dumps({'sub': f'market.jstusdt.ticker'})) 

def loop_jstusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_jstusdt, 
		on_close=on_close_jstusdt, 
		on_error=on_error_jstusdt) 
	ws.on_open = on_open_jstusdt 
	ws.run_forever() 

Thread(target=loop_jstusdt).start() 

symbol_b_g_jstusdd = 'jstusdd' 
price_bids_b_g_jstusdd = float(0.0) 
qty_bids_b_g_jstusdd = float(0.0) 
price_asks_b_g_jstusdd = float(0.0) 
qty_asks_b_g_jstusdd = float(0.0) 

def on_message_jstusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_jstusdd = 'jstusdd' 
		price_bids_b_l_jstusdd = data['tick']['bid'] 
		qty_bids_b_l_jstusdd = data['tick']['bidSize']
		price_asks_b_l_jstusdd = data['tick']['ask'] 
		qty_asks_b_l_jstusdd = data['tick']['askSize'] 

		global symbol_b_g_jstusdd 
		global price_bids_b_g_jstusdd 
		global qty_bids_b_g_jstusdd 
		global price_asks_b_g_jstusdd 
		global qty_asks_b_g_jstusdd 

		symbol_b_g_jstusdd = symbol_b_l_jstusdd 
		price_bids_b_g_jstusdd = price_bids_b_l_jstusdd 
		qty_bids_b_g_jstusdd = qty_bids_b_l_jstusdd 
		price_asks_b_g_jstusdd = price_asks_b_l_jstusdd 
		qty_asks_b_g_jstusdd = qty_asks_b_l_jstusdd 


def on_close_jstusdd(ws): 
	print('### closed ###') 

def on_error_jstusdd(ws, message): 
	print(message) 

def on_open_jstusdd(ws): 
	ws.send(json.dumps({'sub': f'market.jstusdd.ticker'})) 

def loop_jstusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_jstusdd, 
		on_close=on_close_jstusdd, 
		on_error=on_error_jstusdd) 
	ws.on_open = on_open_jstusdd 
	ws.run_forever() 

Thread(target=loop_jstusdd).start() 

def loop_jstusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_jstusdt != 0.0 and qty_bids_a_g_jstusdt != 0.0 and price_asks_a_g_jstusdt != 0.0 and qty_asks_a_g_jstusdt != 0.0 and price_bids_b_g_jstusdd != 0.0 and qty_bids_b_g_jstusdd != 0.0 and price_asks_b_g_jstusdd != 0.0 and qty_asks_b_g_jstusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_jstusdt) 
			price_b = float(price_bids_b_g_jstusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_jstusdd, pribil)

Thread(target=loop_jstusdt_Trade).start() 

symbol_a_g_nexousdt = 'nexousdt' 
price_bids_a_g_nexousdt = float(0.0) 
qty_bids_a_g_nexousdt = float(0.0) 
price_asks_a_g_nexousdt = float(0.0) 
qty_asks_a_g_nexousdt = float(0.0) 

def on_message_nexousdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_nexousdt = 'nexousdt' 
		price_bids_a_l_nexousdt = data['tick']['bid'] 
		qty_bids_a_l_nexousdt = data['tick']['bidSize'] 
		price_asks_a_l_nexousdt = data['tick']['ask'] 
		qty_asks_a_l_nexousdt = data['tick']['askSize'] 

		global symbol_a_g_nexousdt 
		global price_bids_a_g_nexousdt 
		global qty_bids_a_g_nexousdt 
		global price_asks_a_g_nexousdt 
		global qty_asks_a_g_nexousdt 

		symbol_a_g_nexousdt = symbol_a_l_nexousdt 
		price_bids_a_g_nexousdt = price_bids_a_l_nexousdt 
		qty_bids_a_g_nexousdt = qty_bids_a_l_nexousdt 
		price_asks_a_g_nexousdt = price_asks_a_l_nexousdt 
		qty_asks_a_g_nexousdt = qty_asks_a_l_nexousdt 

def on_close_nexousdt(ws): 
	print('### closed ###') 

def on_error_nexousdt(ws, message): 
	print(message) 

def on_open_nexousdt(ws): 
	ws.send(json.dumps({'sub': f'market.nexousdt.ticker'})) 

def loop_nexousdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nexousdt, 
		on_close=on_close_nexousdt, 
		on_error=on_error_nexousdt) 
	ws.on_open = on_open_nexousdt 
	ws.run_forever() 

Thread(target=loop_nexousdt).start() 

symbol_b_g_nexobtc = 'nexobtc' 
price_bids_b_g_nexobtc = float(0.0) 
qty_bids_b_g_nexobtc = float(0.0) 
price_asks_b_g_nexobtc = float(0.0) 
qty_asks_b_g_nexobtc = float(0.0) 

def on_message_nexobtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_nexobtc = 'nexobtc' 
		price_bids_b_l_nexobtc = data['tick']['bid'] 
		qty_bids_b_l_nexobtc = data['tick']['bidSize']
		price_asks_b_l_nexobtc = data['tick']['ask'] 
		qty_asks_b_l_nexobtc = data['tick']['askSize'] 

		global symbol_b_g_nexobtc 
		global price_bids_b_g_nexobtc 
		global qty_bids_b_g_nexobtc 
		global price_asks_b_g_nexobtc 
		global qty_asks_b_g_nexobtc 

		symbol_b_g_nexobtc = symbol_b_l_nexobtc 
		price_bids_b_g_nexobtc = price_bids_b_l_nexobtc 
		qty_bids_b_g_nexobtc = qty_bids_b_l_nexobtc 
		price_asks_b_g_nexobtc = price_asks_b_l_nexobtc 
		qty_asks_b_g_nexobtc = qty_asks_b_l_nexobtc 


def on_close_nexobtc(ws): 
	print('### closed ###') 

def on_error_nexobtc(ws, message): 
	print(message) 

def on_open_nexobtc(ws): 
	ws.send(json.dumps({'sub': f'market.nexobtc.ticker'})) 

def loop_nexobtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nexobtc, 
		on_close=on_close_nexobtc, 
		on_error=on_error_nexobtc) 
	ws.on_open = on_open_nexobtc 
	ws.run_forever() 

Thread(target=loop_nexobtc).start() 

def loop_nexousdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_nexousdt != 0.0 and qty_bids_a_g_nexousdt != 0.0 and price_asks_a_g_nexousdt != 0.0 and qty_asks_a_g_nexousdt != 0.0 and price_bids_b_g_nexobtc != 0.0 and qty_bids_b_g_nexobtc != 0.0 and price_asks_b_g_nexobtc != 0.0 and qty_asks_b_g_nexobtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_nexousdt) 
			price_b = float(price_bids_b_g_nexobtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_nexobtc, pribil)

Thread(target=loop_nexousdt_Trade).start() 

symbol_a_g_bchusdt = 'bchusdt' 
price_bids_a_g_bchusdt = float(0.0) 
qty_bids_a_g_bchusdt = float(0.0) 
price_asks_a_g_bchusdt = float(0.0) 
qty_asks_a_g_bchusdt = float(0.0) 

def on_message_bchusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_bchusdt = 'bchusdt' 
		price_bids_a_l_bchusdt = data['tick']['bid'] 
		qty_bids_a_l_bchusdt = data['tick']['bidSize'] 
		price_asks_a_l_bchusdt = data['tick']['ask'] 
		qty_asks_a_l_bchusdt = data['tick']['askSize'] 

		global symbol_a_g_bchusdt 
		global price_bids_a_g_bchusdt 
		global qty_bids_a_g_bchusdt 
		global price_asks_a_g_bchusdt 
		global qty_asks_a_g_bchusdt 

		symbol_a_g_bchusdt = symbol_a_l_bchusdt 
		price_bids_a_g_bchusdt = price_bids_a_l_bchusdt 
		qty_bids_a_g_bchusdt = qty_bids_a_l_bchusdt 
		price_asks_a_g_bchusdt = price_asks_a_l_bchusdt 
		qty_asks_a_g_bchusdt = qty_asks_a_l_bchusdt 

def on_close_bchusdt(ws): 
	print('### closed ###') 

def on_error_bchusdt(ws, message): 
	print(message) 

def on_open_bchusdt(ws): 
	ws.send(json.dumps({'sub': f'market.bchusdt.ticker'})) 

def loop_bchusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bchusdt, 
		on_close=on_close_bchusdt, 
		on_error=on_error_bchusdt) 
	ws.on_open = on_open_bchusdt 
	ws.run_forever() 

Thread(target=loop_bchusdt).start() 

symbol_b_g_bchht = 'bchht' 
price_bids_b_g_bchht = float(0.0) 
qty_bids_b_g_bchht = float(0.0) 
price_asks_b_g_bchht = float(0.0) 
qty_asks_b_g_bchht = float(0.0) 

def on_message_bchht(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_bchht = 'bchht' 
		price_bids_b_l_bchht = data['tick']['bid'] 
		qty_bids_b_l_bchht = data['tick']['bidSize']
		price_asks_b_l_bchht = data['tick']['ask'] 
		qty_asks_b_l_bchht = data['tick']['askSize'] 

		global symbol_b_g_bchht 
		global price_bids_b_g_bchht 
		global qty_bids_b_g_bchht 
		global price_asks_b_g_bchht 
		global qty_asks_b_g_bchht 

		symbol_b_g_bchht = symbol_b_l_bchht 
		price_bids_b_g_bchht = price_bids_b_l_bchht 
		qty_bids_b_g_bchht = qty_bids_b_l_bchht 
		price_asks_b_g_bchht = price_asks_b_l_bchht 
		qty_asks_b_g_bchht = qty_asks_b_l_bchht 


def on_close_bchht(ws): 
	print('### closed ###') 

def on_error_bchht(ws, message): 
	print(message) 

def on_open_bchht(ws): 
	ws.send(json.dumps({'sub': f'market.bchht.ticker'})) 

def loop_bchht(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_bchht, 
		on_close=on_close_bchht, 
		on_error=on_error_bchht) 
	ws.on_open = on_open_bchht 
	ws.run_forever() 

Thread(target=loop_bchht).start() 

def loop_bchusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_HTUSDT != 0.0 and qty_bids_c_g_HTUSDT != 0.0 and price_asks_c_g_HTUSDT != 0.0 and qty_asks_c_g_HTUSDT != 0.0 and price_bids_a_g_bchusdt != 0.0 and qty_bids_a_g_bchusdt != 0.0 and price_asks_a_g_bchusdt != 0.0 and qty_asks_a_g_bchusdt != 0.0 and price_bids_b_g_bchht != 0.0 and qty_bids_b_g_bchht != 0.0 and price_asks_b_g_bchht != 0.0 and qty_asks_b_g_bchht != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_bchusdt) 
			price_b = float(price_bids_b_g_bchht) * price_a 
			price_c = float(price_bids_c_g_HTUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_bchht, pribil)

Thread(target=loop_bchusdt_Trade).start() 

symbol_a_g_xchusdt = 'xchusdt' 
price_bids_a_g_xchusdt = float(0.0) 
qty_bids_a_g_xchusdt = float(0.0) 
price_asks_a_g_xchusdt = float(0.0) 
qty_asks_a_g_xchusdt = float(0.0) 

def on_message_xchusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_xchusdt = 'xchusdt' 
		price_bids_a_l_xchusdt = data['tick']['bid'] 
		qty_bids_a_l_xchusdt = data['tick']['bidSize'] 
		price_asks_a_l_xchusdt = data['tick']['ask'] 
		qty_asks_a_l_xchusdt = data['tick']['askSize'] 

		global symbol_a_g_xchusdt 
		global price_bids_a_g_xchusdt 
		global qty_bids_a_g_xchusdt 
		global price_asks_a_g_xchusdt 
		global qty_asks_a_g_xchusdt 

		symbol_a_g_xchusdt = symbol_a_l_xchusdt 
		price_bids_a_g_xchusdt = price_bids_a_l_xchusdt 
		qty_bids_a_g_xchusdt = qty_bids_a_l_xchusdt 
		price_asks_a_g_xchusdt = price_asks_a_l_xchusdt 
		qty_asks_a_g_xchusdt = qty_asks_a_l_xchusdt 

def on_close_xchusdt(ws): 
	print('### closed ###') 

def on_error_xchusdt(ws, message): 
	print(message) 

def on_open_xchusdt(ws): 
	ws.send(json.dumps({'sub': f'market.xchusdt.ticker'})) 

def loop_xchusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xchusdt, 
		on_close=on_close_xchusdt, 
		on_error=on_error_xchusdt) 
	ws.on_open = on_open_xchusdt 
	ws.run_forever() 

Thread(target=loop_xchusdt).start() 

symbol_b_g_xchbtc = 'xchbtc' 
price_bids_b_g_xchbtc = float(0.0) 
qty_bids_b_g_xchbtc = float(0.0) 
price_asks_b_g_xchbtc = float(0.0) 
qty_asks_b_g_xchbtc = float(0.0) 

def on_message_xchbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_xchbtc = 'xchbtc' 
		price_bids_b_l_xchbtc = data['tick']['bid'] 
		qty_bids_b_l_xchbtc = data['tick']['bidSize']
		price_asks_b_l_xchbtc = data['tick']['ask'] 
		qty_asks_b_l_xchbtc = data['tick']['askSize'] 

		global symbol_b_g_xchbtc 
		global price_bids_b_g_xchbtc 
		global qty_bids_b_g_xchbtc 
		global price_asks_b_g_xchbtc 
		global qty_asks_b_g_xchbtc 

		symbol_b_g_xchbtc = symbol_b_l_xchbtc 
		price_bids_b_g_xchbtc = price_bids_b_l_xchbtc 
		qty_bids_b_g_xchbtc = qty_bids_b_l_xchbtc 
		price_asks_b_g_xchbtc = price_asks_b_l_xchbtc 
		qty_asks_b_g_xchbtc = qty_asks_b_l_xchbtc 


def on_close_xchbtc(ws): 
	print('### closed ###') 

def on_error_xchbtc(ws, message): 
	print(message) 

def on_open_xchbtc(ws): 
	ws.send(json.dumps({'sub': f'market.xchbtc.ticker'})) 

def loop_xchbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_xchbtc, 
		on_close=on_close_xchbtc, 
		on_error=on_error_xchbtc) 
	ws.on_open = on_open_xchbtc 
	ws.run_forever() 

Thread(target=loop_xchbtc).start() 

def loop_xchusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_xchusdt != 0.0 and qty_bids_a_g_xchusdt != 0.0 and price_asks_a_g_xchusdt != 0.0 and qty_asks_a_g_xchusdt != 0.0 and price_bids_b_g_xchbtc != 0.0 and qty_bids_b_g_xchbtc != 0.0 and price_asks_b_g_xchbtc != 0.0 and qty_asks_b_g_xchbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_xchusdt) 
			price_b = float(price_bids_b_g_xchbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_xchbtc, pribil)

Thread(target=loop_xchusdt_Trade).start() 

symbol_a_g_kncusdt = 'kncusdt' 
price_bids_a_g_kncusdt = float(0.0) 
qty_bids_a_g_kncusdt = float(0.0) 
price_asks_a_g_kncusdt = float(0.0) 
qty_asks_a_g_kncusdt = float(0.0) 

def on_message_kncusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_kncusdt = 'kncusdt' 
		price_bids_a_l_kncusdt = data['tick']['bid'] 
		qty_bids_a_l_kncusdt = data['tick']['bidSize'] 
		price_asks_a_l_kncusdt = data['tick']['ask'] 
		qty_asks_a_l_kncusdt = data['tick']['askSize'] 

		global symbol_a_g_kncusdt 
		global price_bids_a_g_kncusdt 
		global qty_bids_a_g_kncusdt 
		global price_asks_a_g_kncusdt 
		global qty_asks_a_g_kncusdt 

		symbol_a_g_kncusdt = symbol_a_l_kncusdt 
		price_bids_a_g_kncusdt = price_bids_a_l_kncusdt 
		qty_bids_a_g_kncusdt = qty_bids_a_l_kncusdt 
		price_asks_a_g_kncusdt = price_asks_a_l_kncusdt 
		qty_asks_a_g_kncusdt = qty_asks_a_l_kncusdt 

def on_close_kncusdt(ws): 
	print('### closed ###') 

def on_error_kncusdt(ws, message): 
	print(message) 

def on_open_kncusdt(ws): 
	ws.send(json.dumps({'sub': f'market.kncusdt.ticker'})) 

def loop_kncusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kncusdt, 
		on_close=on_close_kncusdt, 
		on_error=on_error_kncusdt) 
	ws.on_open = on_open_kncusdt 
	ws.run_forever() 

Thread(target=loop_kncusdt).start() 

symbol_b_g_kncbtc = 'kncbtc' 
price_bids_b_g_kncbtc = float(0.0) 
qty_bids_b_g_kncbtc = float(0.0) 
price_asks_b_g_kncbtc = float(0.0) 
qty_asks_b_g_kncbtc = float(0.0) 

def on_message_kncbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_kncbtc = 'kncbtc' 
		price_bids_b_l_kncbtc = data['tick']['bid'] 
		qty_bids_b_l_kncbtc = data['tick']['bidSize']
		price_asks_b_l_kncbtc = data['tick']['ask'] 
		qty_asks_b_l_kncbtc = data['tick']['askSize'] 

		global symbol_b_g_kncbtc 
		global price_bids_b_g_kncbtc 
		global qty_bids_b_g_kncbtc 
		global price_asks_b_g_kncbtc 
		global qty_asks_b_g_kncbtc 

		symbol_b_g_kncbtc = symbol_b_l_kncbtc 
		price_bids_b_g_kncbtc = price_bids_b_l_kncbtc 
		qty_bids_b_g_kncbtc = qty_bids_b_l_kncbtc 
		price_asks_b_g_kncbtc = price_asks_b_l_kncbtc 
		qty_asks_b_g_kncbtc = qty_asks_b_l_kncbtc 


def on_close_kncbtc(ws): 
	print('### closed ###') 

def on_error_kncbtc(ws, message): 
	print(message) 

def on_open_kncbtc(ws): 
	ws.send(json.dumps({'sub': f'market.kncbtc.ticker'})) 

def loop_kncbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kncbtc, 
		on_close=on_close_kncbtc, 
		on_error=on_error_kncbtc) 
	ws.on_open = on_open_kncbtc 
	ws.run_forever() 

Thread(target=loop_kncbtc).start() 

def loop_kncusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_kncusdt != 0.0 and qty_bids_a_g_kncusdt != 0.0 and price_asks_a_g_kncusdt != 0.0 and qty_asks_a_g_kncusdt != 0.0 and price_bids_b_g_kncbtc != 0.0 and qty_bids_b_g_kncbtc != 0.0 and price_asks_b_g_kncbtc != 0.0 and qty_asks_b_g_kncbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_kncusdt) 
			price_b = float(price_bids_b_g_kncbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_kncbtc, pribil)

Thread(target=loop_kncusdt_Trade).start() 

symbol_a_g_kavausdt = 'kavausdt' 
price_bids_a_g_kavausdt = float(0.0) 
qty_bids_a_g_kavausdt = float(0.0) 
price_asks_a_g_kavausdt = float(0.0) 
qty_asks_a_g_kavausdt = float(0.0) 

def on_message_kavausdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_kavausdt = 'kavausdt' 
		price_bids_a_l_kavausdt = data['tick']['bid'] 
		qty_bids_a_l_kavausdt = data['tick']['bidSize'] 
		price_asks_a_l_kavausdt = data['tick']['ask'] 
		qty_asks_a_l_kavausdt = data['tick']['askSize'] 

		global symbol_a_g_kavausdt 
		global price_bids_a_g_kavausdt 
		global qty_bids_a_g_kavausdt 
		global price_asks_a_g_kavausdt 
		global qty_asks_a_g_kavausdt 

		symbol_a_g_kavausdt = symbol_a_l_kavausdt 
		price_bids_a_g_kavausdt = price_bids_a_l_kavausdt 
		qty_bids_a_g_kavausdt = qty_bids_a_l_kavausdt 
		price_asks_a_g_kavausdt = price_asks_a_l_kavausdt 
		qty_asks_a_g_kavausdt = qty_asks_a_l_kavausdt 

def on_close_kavausdt(ws): 
	print('### closed ###') 

def on_error_kavausdt(ws, message): 
	print(message) 

def on_open_kavausdt(ws): 
	ws.send(json.dumps({'sub': f'market.kavausdt.ticker'})) 

def loop_kavausdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kavausdt, 
		on_close=on_close_kavausdt, 
		on_error=on_error_kavausdt) 
	ws.on_open = on_open_kavausdt 
	ws.run_forever() 

Thread(target=loop_kavausdt).start() 

symbol_b_g_kavabtc = 'kavabtc' 
price_bids_b_g_kavabtc = float(0.0) 
qty_bids_b_g_kavabtc = float(0.0) 
price_asks_b_g_kavabtc = float(0.0) 
qty_asks_b_g_kavabtc = float(0.0) 

def on_message_kavabtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_kavabtc = 'kavabtc' 
		price_bids_b_l_kavabtc = data['tick']['bid'] 
		qty_bids_b_l_kavabtc = data['tick']['bidSize']
		price_asks_b_l_kavabtc = data['tick']['ask'] 
		qty_asks_b_l_kavabtc = data['tick']['askSize'] 

		global symbol_b_g_kavabtc 
		global price_bids_b_g_kavabtc 
		global qty_bids_b_g_kavabtc 
		global price_asks_b_g_kavabtc 
		global qty_asks_b_g_kavabtc 

		symbol_b_g_kavabtc = symbol_b_l_kavabtc 
		price_bids_b_g_kavabtc = price_bids_b_l_kavabtc 
		qty_bids_b_g_kavabtc = qty_bids_b_l_kavabtc 
		price_asks_b_g_kavabtc = price_asks_b_l_kavabtc 
		qty_asks_b_g_kavabtc = qty_asks_b_l_kavabtc 


def on_close_kavabtc(ws): 
	print('### closed ###') 

def on_error_kavabtc(ws, message): 
	print(message) 

def on_open_kavabtc(ws): 
	ws.send(json.dumps({'sub': f'market.kavabtc.ticker'})) 

def loop_kavabtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_kavabtc, 
		on_close=on_close_kavabtc, 
		on_error=on_error_kavabtc) 
	ws.on_open = on_open_kavabtc 
	ws.run_forever() 

Thread(target=loop_kavabtc).start() 

def loop_kavausdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_kavausdt != 0.0 and qty_bids_a_g_kavausdt != 0.0 and price_asks_a_g_kavausdt != 0.0 and qty_asks_a_g_kavausdt != 0.0 and price_bids_b_g_kavabtc != 0.0 and qty_bids_b_g_kavabtc != 0.0 and price_asks_b_g_kavabtc != 0.0 and qty_asks_b_g_kavabtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_kavausdt) 
			price_b = float(price_bids_b_g_kavabtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_kavabtc, pribil)

Thread(target=loop_kavausdt_Trade).start() 

symbol_a_g_hptusdt = 'hptusdt' 
price_bids_a_g_hptusdt = float(0.0) 
qty_bids_a_g_hptusdt = float(0.0) 
price_asks_a_g_hptusdt = float(0.0) 
qty_asks_a_g_hptusdt = float(0.0) 

def on_message_hptusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_hptusdt = 'hptusdt' 
		price_bids_a_l_hptusdt = data['tick']['bid'] 
		qty_bids_a_l_hptusdt = data['tick']['bidSize'] 
		price_asks_a_l_hptusdt = data['tick']['ask'] 
		qty_asks_a_l_hptusdt = data['tick']['askSize'] 

		global symbol_a_g_hptusdt 
		global price_bids_a_g_hptusdt 
		global qty_bids_a_g_hptusdt 
		global price_asks_a_g_hptusdt 
		global qty_asks_a_g_hptusdt 

		symbol_a_g_hptusdt = symbol_a_l_hptusdt 
		price_bids_a_g_hptusdt = price_bids_a_l_hptusdt 
		qty_bids_a_g_hptusdt = qty_bids_a_l_hptusdt 
		price_asks_a_g_hptusdt = price_asks_a_l_hptusdt 
		qty_asks_a_g_hptusdt = qty_asks_a_l_hptusdt 

def on_close_hptusdt(ws): 
	print('### closed ###') 

def on_error_hptusdt(ws, message): 
	print(message) 

def on_open_hptusdt(ws): 
	ws.send(json.dumps({'sub': f'market.hptusdt.ticker'})) 

def loop_hptusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_hptusdt, 
		on_close=on_close_hptusdt, 
		on_error=on_error_hptusdt) 
	ws.on_open = on_open_hptusdt 
	ws.run_forever() 

Thread(target=loop_hptusdt).start() 

symbol_b_g_hptbtc = 'hptbtc' 
price_bids_b_g_hptbtc = float(0.0) 
qty_bids_b_g_hptbtc = float(0.0) 
price_asks_b_g_hptbtc = float(0.0) 
qty_asks_b_g_hptbtc = float(0.0) 

def on_message_hptbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_hptbtc = 'hptbtc' 
		price_bids_b_l_hptbtc = data['tick']['bid'] 
		qty_bids_b_l_hptbtc = data['tick']['bidSize']
		price_asks_b_l_hptbtc = data['tick']['ask'] 
		qty_asks_b_l_hptbtc = data['tick']['askSize'] 

		global symbol_b_g_hptbtc 
		global price_bids_b_g_hptbtc 
		global qty_bids_b_g_hptbtc 
		global price_asks_b_g_hptbtc 
		global qty_asks_b_g_hptbtc 

		symbol_b_g_hptbtc = symbol_b_l_hptbtc 
		price_bids_b_g_hptbtc = price_bids_b_l_hptbtc 
		qty_bids_b_g_hptbtc = qty_bids_b_l_hptbtc 
		price_asks_b_g_hptbtc = price_asks_b_l_hptbtc 
		qty_asks_b_g_hptbtc = qty_asks_b_l_hptbtc 


def on_close_hptbtc(ws): 
	print('### closed ###') 

def on_error_hptbtc(ws, message): 
	print(message) 

def on_open_hptbtc(ws): 
	ws.send(json.dumps({'sub': f'market.hptbtc.ticker'})) 

def loop_hptbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_hptbtc, 
		on_close=on_close_hptbtc, 
		on_error=on_error_hptbtc) 
	ws.on_open = on_open_hptbtc 
	ws.run_forever() 

Thread(target=loop_hptbtc).start() 

def loop_hptusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_hptusdt != 0.0 and qty_bids_a_g_hptusdt != 0.0 and price_asks_a_g_hptusdt != 0.0 and qty_asks_a_g_hptusdt != 0.0 and price_bids_b_g_hptbtc != 0.0 and qty_bids_b_g_hptbtc != 0.0 and price_asks_b_g_hptbtc != 0.0 and qty_asks_b_g_hptbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_hptusdt) 
			price_b = float(price_bids_b_g_hptbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_hptbtc, pribil)

Thread(target=loop_hptusdt_Trade).start() 

symbol_a_g_winusdt = 'winusdt' 
price_bids_a_g_winusdt = float(0.0) 
qty_bids_a_g_winusdt = float(0.0) 
price_asks_a_g_winusdt = float(0.0) 
qty_asks_a_g_winusdt = float(0.0) 

def on_message_winusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_winusdt = 'winusdt' 
		price_bids_a_l_winusdt = data['tick']['bid'] 
		qty_bids_a_l_winusdt = data['tick']['bidSize'] 
		price_asks_a_l_winusdt = data['tick']['ask'] 
		qty_asks_a_l_winusdt = data['tick']['askSize'] 

		global symbol_a_g_winusdt 
		global price_bids_a_g_winusdt 
		global qty_bids_a_g_winusdt 
		global price_asks_a_g_winusdt 
		global qty_asks_a_g_winusdt 

		symbol_a_g_winusdt = symbol_a_l_winusdt 
		price_bids_a_g_winusdt = price_bids_a_l_winusdt 
		qty_bids_a_g_winusdt = qty_bids_a_l_winusdt 
		price_asks_a_g_winusdt = price_asks_a_l_winusdt 
		qty_asks_a_g_winusdt = qty_asks_a_l_winusdt 

def on_close_winusdt(ws): 
	print('### closed ###') 

def on_error_winusdt(ws, message): 
	print(message) 

def on_open_winusdt(ws): 
	ws.send(json.dumps({'sub': f'market.winusdt.ticker'})) 

def loop_winusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_winusdt, 
		on_close=on_close_winusdt, 
		on_error=on_error_winusdt) 
	ws.on_open = on_open_winusdt 
	ws.run_forever() 

Thread(target=loop_winusdt).start() 

symbol_b_g_winusdd = 'winusdd' 
price_bids_b_g_winusdd = float(0.0) 
qty_bids_b_g_winusdd = float(0.0) 
price_asks_b_g_winusdd = float(0.0) 
qty_asks_b_g_winusdd = float(0.0) 

def on_message_winusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_winusdd = 'winusdd' 
		price_bids_b_l_winusdd = data['tick']['bid'] 
		qty_bids_b_l_winusdd = data['tick']['bidSize']
		price_asks_b_l_winusdd = data['tick']['ask'] 
		qty_asks_b_l_winusdd = data['tick']['askSize'] 

		global symbol_b_g_winusdd 
		global price_bids_b_g_winusdd 
		global qty_bids_b_g_winusdd 
		global price_asks_b_g_winusdd 
		global qty_asks_b_g_winusdd 

		symbol_b_g_winusdd = symbol_b_l_winusdd 
		price_bids_b_g_winusdd = price_bids_b_l_winusdd 
		qty_bids_b_g_winusdd = qty_bids_b_l_winusdd 
		price_asks_b_g_winusdd = price_asks_b_l_winusdd 
		qty_asks_b_g_winusdd = qty_asks_b_l_winusdd 


def on_close_winusdd(ws): 
	print('### closed ###') 

def on_error_winusdd(ws, message): 
	print(message) 

def on_open_winusdd(ws): 
	ws.send(json.dumps({'sub': f'market.winusdd.ticker'})) 

def loop_winusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_winusdd, 
		on_close=on_close_winusdd, 
		on_error=on_error_winusdd) 
	ws.on_open = on_open_winusdd 
	ws.run_forever() 

Thread(target=loop_winusdd).start() 

def loop_winusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_winusdt != 0.0 and qty_bids_a_g_winusdt != 0.0 and price_asks_a_g_winusdt != 0.0 and qty_asks_a_g_winusdt != 0.0 and price_bids_b_g_winusdd != 0.0 and qty_bids_b_g_winusdd != 0.0 and price_asks_b_g_winusdd != 0.0 and qty_asks_b_g_winusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_winusdt) 
			price_b = float(price_bids_b_g_winusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_winusdd, pribil)

Thread(target=loop_winusdt_Trade).start() 

symbol_a_g_arusdt = 'arusdt' 
price_bids_a_g_arusdt = float(0.0) 
qty_bids_a_g_arusdt = float(0.0) 
price_asks_a_g_arusdt = float(0.0) 
qty_asks_a_g_arusdt = float(0.0) 

def on_message_arusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_arusdt = 'arusdt' 
		price_bids_a_l_arusdt = data['tick']['bid'] 
		qty_bids_a_l_arusdt = data['tick']['bidSize'] 
		price_asks_a_l_arusdt = data['tick']['ask'] 
		qty_asks_a_l_arusdt = data['tick']['askSize'] 

		global symbol_a_g_arusdt 
		global price_bids_a_g_arusdt 
		global qty_bids_a_g_arusdt 
		global price_asks_a_g_arusdt 
		global qty_asks_a_g_arusdt 

		symbol_a_g_arusdt = symbol_a_l_arusdt 
		price_bids_a_g_arusdt = price_bids_a_l_arusdt 
		qty_bids_a_g_arusdt = qty_bids_a_l_arusdt 
		price_asks_a_g_arusdt = price_asks_a_l_arusdt 
		qty_asks_a_g_arusdt = qty_asks_a_l_arusdt 

def on_close_arusdt(ws): 
	print('### closed ###') 

def on_error_arusdt(ws, message): 
	print(message) 

def on_open_arusdt(ws): 
	ws.send(json.dumps({'sub': f'market.arusdt.ticker'})) 

def loop_arusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_arusdt, 
		on_close=on_close_arusdt, 
		on_error=on_error_arusdt) 
	ws.on_open = on_open_arusdt 
	ws.run_forever() 

Thread(target=loop_arusdt).start() 

symbol_b_g_arbtc = 'arbtc' 
price_bids_b_g_arbtc = float(0.0) 
qty_bids_b_g_arbtc = float(0.0) 
price_asks_b_g_arbtc = float(0.0) 
qty_asks_b_g_arbtc = float(0.0) 

def on_message_arbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_arbtc = 'arbtc' 
		price_bids_b_l_arbtc = data['tick']['bid'] 
		qty_bids_b_l_arbtc = data['tick']['bidSize']
		price_asks_b_l_arbtc = data['tick']['ask'] 
		qty_asks_b_l_arbtc = data['tick']['askSize'] 

		global symbol_b_g_arbtc 
		global price_bids_b_g_arbtc 
		global qty_bids_b_g_arbtc 
		global price_asks_b_g_arbtc 
		global qty_asks_b_g_arbtc 

		symbol_b_g_arbtc = symbol_b_l_arbtc 
		price_bids_b_g_arbtc = price_bids_b_l_arbtc 
		qty_bids_b_g_arbtc = qty_bids_b_l_arbtc 
		price_asks_b_g_arbtc = price_asks_b_l_arbtc 
		qty_asks_b_g_arbtc = qty_asks_b_l_arbtc 


def on_close_arbtc(ws): 
	print('### closed ###') 

def on_error_arbtc(ws, message): 
	print(message) 

def on_open_arbtc(ws): 
	ws.send(json.dumps({'sub': f'market.arbtc.ticker'})) 

def loop_arbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_arbtc, 
		on_close=on_close_arbtc, 
		on_error=on_error_arbtc) 
	ws.on_open = on_open_arbtc 
	ws.run_forever() 

Thread(target=loop_arbtc).start() 

def loop_arusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_arusdt != 0.0 and qty_bids_a_g_arusdt != 0.0 and price_asks_a_g_arusdt != 0.0 and qty_asks_a_g_arusdt != 0.0 and price_bids_b_g_arbtc != 0.0 and qty_bids_b_g_arbtc != 0.0 and price_asks_b_g_arbtc != 0.0 and qty_asks_b_g_arbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_arusdt) 
			price_b = float(price_bids_b_g_arbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_arbtc, pribil)

Thread(target=loop_arusdt_Trade).start() 

symbol_a_g_dfusdt = 'dfusdt' 
price_bids_a_g_dfusdt = float(0.0) 
qty_bids_a_g_dfusdt = float(0.0) 
price_asks_a_g_dfusdt = float(0.0) 
qty_asks_a_g_dfusdt = float(0.0) 

def on_message_dfusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_dfusdt = 'dfusdt' 
		price_bids_a_l_dfusdt = data['tick']['bid'] 
		qty_bids_a_l_dfusdt = data['tick']['bidSize'] 
		price_asks_a_l_dfusdt = data['tick']['ask'] 
		qty_asks_a_l_dfusdt = data['tick']['askSize'] 

		global symbol_a_g_dfusdt 
		global price_bids_a_g_dfusdt 
		global qty_bids_a_g_dfusdt 
		global price_asks_a_g_dfusdt 
		global qty_asks_a_g_dfusdt 

		symbol_a_g_dfusdt = symbol_a_l_dfusdt 
		price_bids_a_g_dfusdt = price_bids_a_l_dfusdt 
		qty_bids_a_g_dfusdt = qty_bids_a_l_dfusdt 
		price_asks_a_g_dfusdt = price_asks_a_l_dfusdt 
		qty_asks_a_g_dfusdt = qty_asks_a_l_dfusdt 

def on_close_dfusdt(ws): 
	print('### closed ###') 

def on_error_dfusdt(ws, message): 
	print(message) 

def on_open_dfusdt(ws): 
	ws.send(json.dumps({'sub': f'market.dfusdt.ticker'})) 

def loop_dfusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dfusdt, 
		on_close=on_close_dfusdt, 
		on_error=on_error_dfusdt) 
	ws.on_open = on_open_dfusdt 
	ws.run_forever() 

Thread(target=loop_dfusdt).start() 

symbol_b_g_dfbtc = 'dfbtc' 
price_bids_b_g_dfbtc = float(0.0) 
qty_bids_b_g_dfbtc = float(0.0) 
price_asks_b_g_dfbtc = float(0.0) 
qty_asks_b_g_dfbtc = float(0.0) 

def on_message_dfbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_dfbtc = 'dfbtc' 
		price_bids_b_l_dfbtc = data['tick']['bid'] 
		qty_bids_b_l_dfbtc = data['tick']['bidSize']
		price_asks_b_l_dfbtc = data['tick']['ask'] 
		qty_asks_b_l_dfbtc = data['tick']['askSize'] 

		global symbol_b_g_dfbtc 
		global price_bids_b_g_dfbtc 
		global qty_bids_b_g_dfbtc 
		global price_asks_b_g_dfbtc 
		global qty_asks_b_g_dfbtc 

		symbol_b_g_dfbtc = symbol_b_l_dfbtc 
		price_bids_b_g_dfbtc = price_bids_b_l_dfbtc 
		qty_bids_b_g_dfbtc = qty_bids_b_l_dfbtc 
		price_asks_b_g_dfbtc = price_asks_b_l_dfbtc 
		qty_asks_b_g_dfbtc = qty_asks_b_l_dfbtc 


def on_close_dfbtc(ws): 
	print('### closed ###') 

def on_error_dfbtc(ws, message): 
	print(message) 

def on_open_dfbtc(ws): 
	ws.send(json.dumps({'sub': f'market.dfbtc.ticker'})) 

def loop_dfbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dfbtc, 
		on_close=on_close_dfbtc, 
		on_error=on_error_dfbtc) 
	ws.on_open = on_open_dfbtc 
	ws.run_forever() 

Thread(target=loop_dfbtc).start() 

def loop_dfusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_dfusdt != 0.0 and qty_bids_a_g_dfusdt != 0.0 and price_asks_a_g_dfusdt != 0.0 and qty_asks_a_g_dfusdt != 0.0 and price_bids_b_g_dfbtc != 0.0 and qty_bids_b_g_dfbtc != 0.0 and price_asks_b_g_dfbtc != 0.0 and qty_asks_b_g_dfbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_dfusdt) 
			price_b = float(price_bids_b_g_dfbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_dfbtc, pribil)

Thread(target=loop_dfusdt_Trade).start() 

symbol_a_g_luncusdt = 'luncusdt' 
price_bids_a_g_luncusdt = float(0.0) 
qty_bids_a_g_luncusdt = float(0.0) 
price_asks_a_g_luncusdt = float(0.0) 
qty_asks_a_g_luncusdt = float(0.0) 

def on_message_luncusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_luncusdt = 'luncusdt' 
		price_bids_a_l_luncusdt = data['tick']['bid'] 
		qty_bids_a_l_luncusdt = data['tick']['bidSize'] 
		price_asks_a_l_luncusdt = data['tick']['ask'] 
		qty_asks_a_l_luncusdt = data['tick']['askSize'] 

		global symbol_a_g_luncusdt 
		global price_bids_a_g_luncusdt 
		global qty_bids_a_g_luncusdt 
		global price_asks_a_g_luncusdt 
		global qty_asks_a_g_luncusdt 

		symbol_a_g_luncusdt = symbol_a_l_luncusdt 
		price_bids_a_g_luncusdt = price_bids_a_l_luncusdt 
		qty_bids_a_g_luncusdt = qty_bids_a_l_luncusdt 
		price_asks_a_g_luncusdt = price_asks_a_l_luncusdt 
		qty_asks_a_g_luncusdt = qty_asks_a_l_luncusdt 

def on_close_luncusdt(ws): 
	print('### closed ###') 

def on_error_luncusdt(ws, message): 
	print(message) 

def on_open_luncusdt(ws): 
	ws.send(json.dumps({'sub': f'market.luncusdt.ticker'})) 

def loop_luncusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_luncusdt, 
		on_close=on_close_luncusdt, 
		on_error=on_error_luncusdt) 
	ws.on_open = on_open_luncusdt 
	ws.run_forever() 

Thread(target=loop_luncusdt).start() 

symbol_b_g_luncusdd = 'luncusdd' 
price_bids_b_g_luncusdd = float(0.0) 
qty_bids_b_g_luncusdd = float(0.0) 
price_asks_b_g_luncusdd = float(0.0) 
qty_asks_b_g_luncusdd = float(0.0) 

def on_message_luncusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_luncusdd = 'luncusdd' 
		price_bids_b_l_luncusdd = data['tick']['bid'] 
		qty_bids_b_l_luncusdd = data['tick']['bidSize']
		price_asks_b_l_luncusdd = data['tick']['ask'] 
		qty_asks_b_l_luncusdd = data['tick']['askSize'] 

		global symbol_b_g_luncusdd 
		global price_bids_b_g_luncusdd 
		global qty_bids_b_g_luncusdd 
		global price_asks_b_g_luncusdd 
		global qty_asks_b_g_luncusdd 

		symbol_b_g_luncusdd = symbol_b_l_luncusdd 
		price_bids_b_g_luncusdd = price_bids_b_l_luncusdd 
		qty_bids_b_g_luncusdd = qty_bids_b_l_luncusdd 
		price_asks_b_g_luncusdd = price_asks_b_l_luncusdd 
		qty_asks_b_g_luncusdd = qty_asks_b_l_luncusdd 


def on_close_luncusdd(ws): 
	print('### closed ###') 

def on_error_luncusdd(ws, message): 
	print(message) 

def on_open_luncusdd(ws): 
	ws.send(json.dumps({'sub': f'market.luncusdd.ticker'})) 

def loop_luncusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_luncusdd, 
		on_close=on_close_luncusdd, 
		on_error=on_error_luncusdd) 
	ws.on_open = on_open_luncusdd 
	ws.run_forever() 

Thread(target=loop_luncusdd).start() 

def loop_luncusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_luncusdt != 0.0 and qty_bids_a_g_luncusdt != 0.0 and price_asks_a_g_luncusdt != 0.0 and qty_asks_a_g_luncusdt != 0.0 and price_bids_b_g_luncusdd != 0.0 and qty_bids_b_g_luncusdd != 0.0 and price_asks_b_g_luncusdd != 0.0 and qty_asks_b_g_luncusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_luncusdt) 
			price_b = float(price_bids_b_g_luncusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_luncusdd, pribil)

Thread(target=loop_luncusdt_Trade).start() 

symbol_a_g_uniusdt = 'uniusdt' 
price_bids_a_g_uniusdt = float(0.0) 
qty_bids_a_g_uniusdt = float(0.0) 
price_asks_a_g_uniusdt = float(0.0) 
qty_asks_a_g_uniusdt = float(0.0) 

def on_message_uniusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_uniusdt = 'uniusdt' 
		price_bids_a_l_uniusdt = data['tick']['bid'] 
		qty_bids_a_l_uniusdt = data['tick']['bidSize'] 
		price_asks_a_l_uniusdt = data['tick']['ask'] 
		qty_asks_a_l_uniusdt = data['tick']['askSize'] 

		global symbol_a_g_uniusdt 
		global price_bids_a_g_uniusdt 
		global qty_bids_a_g_uniusdt 
		global price_asks_a_g_uniusdt 
		global qty_asks_a_g_uniusdt 

		symbol_a_g_uniusdt = symbol_a_l_uniusdt 
		price_bids_a_g_uniusdt = price_bids_a_l_uniusdt 
		qty_bids_a_g_uniusdt = qty_bids_a_l_uniusdt 
		price_asks_a_g_uniusdt = price_asks_a_l_uniusdt 
		qty_asks_a_g_uniusdt = qty_asks_a_l_uniusdt 

def on_close_uniusdt(ws): 
	print('### closed ###') 

def on_error_uniusdt(ws, message): 
	print(message) 

def on_open_uniusdt(ws): 
	ws.send(json.dumps({'sub': f'market.uniusdt.ticker'})) 

def loop_uniusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_uniusdt, 
		on_close=on_close_uniusdt, 
		on_error=on_error_uniusdt) 
	ws.on_open = on_open_uniusdt 
	ws.run_forever() 

Thread(target=loop_uniusdt).start() 

symbol_b_g_unieth = 'unieth' 
price_bids_b_g_unieth = float(0.0) 
qty_bids_b_g_unieth = float(0.0) 
price_asks_b_g_unieth = float(0.0) 
qty_asks_b_g_unieth = float(0.0) 

def on_message_unieth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_unieth = 'unieth' 
		price_bids_b_l_unieth = data['tick']['bid'] 
		qty_bids_b_l_unieth = data['tick']['bidSize']
		price_asks_b_l_unieth = data['tick']['ask'] 
		qty_asks_b_l_unieth = data['tick']['askSize'] 

		global symbol_b_g_unieth 
		global price_bids_b_g_unieth 
		global qty_bids_b_g_unieth 
		global price_asks_b_g_unieth 
		global qty_asks_b_g_unieth 

		symbol_b_g_unieth = symbol_b_l_unieth 
		price_bids_b_g_unieth = price_bids_b_l_unieth 
		qty_bids_b_g_unieth = qty_bids_b_l_unieth 
		price_asks_b_g_unieth = price_asks_b_l_unieth 
		qty_asks_b_g_unieth = qty_asks_b_l_unieth 


def on_close_unieth(ws): 
	print('### closed ###') 

def on_error_unieth(ws, message): 
	print(message) 

def on_open_unieth(ws): 
	ws.send(json.dumps({'sub': f'market.unieth.ticker'})) 

def loop_unieth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_unieth, 
		on_close=on_close_unieth, 
		on_error=on_error_unieth) 
	ws.on_open = on_open_unieth 
	ws.run_forever() 

Thread(target=loop_unieth).start() 

def loop_uniusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_uniusdt != 0.0 and qty_bids_a_g_uniusdt != 0.0 and price_asks_a_g_uniusdt != 0.0 and qty_asks_a_g_uniusdt != 0.0 and price_bids_b_g_unieth != 0.0 and qty_bids_b_g_unieth != 0.0 and price_asks_b_g_unieth != 0.0 and qty_asks_b_g_unieth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_uniusdt) 
			price_b = float(price_bids_b_g_unieth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_unieth, pribil)

Thread(target=loop_uniusdt_Trade).start() 

symbol_a_g_aaveusdt = 'aaveusdt' 
price_bids_a_g_aaveusdt = float(0.0) 
qty_bids_a_g_aaveusdt = float(0.0) 
price_asks_a_g_aaveusdt = float(0.0) 
qty_asks_a_g_aaveusdt = float(0.0) 

def on_message_aaveusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_aaveusdt = 'aaveusdt' 
		price_bids_a_l_aaveusdt = data['tick']['bid'] 
		qty_bids_a_l_aaveusdt = data['tick']['bidSize'] 
		price_asks_a_l_aaveusdt = data['tick']['ask'] 
		qty_asks_a_l_aaveusdt = data['tick']['askSize'] 

		global symbol_a_g_aaveusdt 
		global price_bids_a_g_aaveusdt 
		global qty_bids_a_g_aaveusdt 
		global price_asks_a_g_aaveusdt 
		global qty_asks_a_g_aaveusdt 

		symbol_a_g_aaveusdt = symbol_a_l_aaveusdt 
		price_bids_a_g_aaveusdt = price_bids_a_l_aaveusdt 
		qty_bids_a_g_aaveusdt = qty_bids_a_l_aaveusdt 
		price_asks_a_g_aaveusdt = price_asks_a_l_aaveusdt 
		qty_asks_a_g_aaveusdt = qty_asks_a_l_aaveusdt 

def on_close_aaveusdt(ws): 
	print('### closed ###') 

def on_error_aaveusdt(ws, message): 
	print(message) 

def on_open_aaveusdt(ws): 
	ws.send(json.dumps({'sub': f'market.aaveusdt.ticker'})) 

def loop_aaveusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_aaveusdt, 
		on_close=on_close_aaveusdt, 
		on_error=on_error_aaveusdt) 
	ws.on_open = on_open_aaveusdt 
	ws.run_forever() 

Thread(target=loop_aaveusdt).start() 

symbol_b_g_aaveeth = 'aaveeth' 
price_bids_b_g_aaveeth = float(0.0) 
qty_bids_b_g_aaveeth = float(0.0) 
price_asks_b_g_aaveeth = float(0.0) 
qty_asks_b_g_aaveeth = float(0.0) 

def on_message_aaveeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_aaveeth = 'aaveeth' 
		price_bids_b_l_aaveeth = data['tick']['bid'] 
		qty_bids_b_l_aaveeth = data['tick']['bidSize']
		price_asks_b_l_aaveeth = data['tick']['ask'] 
		qty_asks_b_l_aaveeth = data['tick']['askSize'] 

		global symbol_b_g_aaveeth 
		global price_bids_b_g_aaveeth 
		global qty_bids_b_g_aaveeth 
		global price_asks_b_g_aaveeth 
		global qty_asks_b_g_aaveeth 

		symbol_b_g_aaveeth = symbol_b_l_aaveeth 
		price_bids_b_g_aaveeth = price_bids_b_l_aaveeth 
		qty_bids_b_g_aaveeth = qty_bids_b_l_aaveeth 
		price_asks_b_g_aaveeth = price_asks_b_l_aaveeth 
		qty_asks_b_g_aaveeth = qty_asks_b_l_aaveeth 


def on_close_aaveeth(ws): 
	print('### closed ###') 

def on_error_aaveeth(ws, message): 
	print(message) 

def on_open_aaveeth(ws): 
	ws.send(json.dumps({'sub': f'market.aaveeth.ticker'})) 

def loop_aaveeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_aaveeth, 
		on_close=on_close_aaveeth, 
		on_error=on_error_aaveeth) 
	ws.on_open = on_open_aaveeth 
	ws.run_forever() 

Thread(target=loop_aaveeth).start() 

def loop_aaveusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_aaveusdt != 0.0 and qty_bids_a_g_aaveusdt != 0.0 and price_asks_a_g_aaveusdt != 0.0 and qty_asks_a_g_aaveusdt != 0.0 and price_bids_b_g_aaveeth != 0.0 and qty_bids_b_g_aaveeth != 0.0 and price_asks_b_g_aaveeth != 0.0 and qty_asks_b_g_aaveeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_aaveusdt) 
			price_b = float(price_bids_b_g_aaveeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_aaveeth, pribil)

Thread(target=loop_aaveusdt_Trade).start() 

symbol_a_g_chzusdt = 'chzusdt' 
price_bids_a_g_chzusdt = float(0.0) 
qty_bids_a_g_chzusdt = float(0.0) 
price_asks_a_g_chzusdt = float(0.0) 
qty_asks_a_g_chzusdt = float(0.0) 

def on_message_chzusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_chzusdt = 'chzusdt' 
		price_bids_a_l_chzusdt = data['tick']['bid'] 
		qty_bids_a_l_chzusdt = data['tick']['bidSize'] 
		price_asks_a_l_chzusdt = data['tick']['ask'] 
		qty_asks_a_l_chzusdt = data['tick']['askSize'] 

		global symbol_a_g_chzusdt 
		global price_bids_a_g_chzusdt 
		global qty_bids_a_g_chzusdt 
		global price_asks_a_g_chzusdt 
		global qty_asks_a_g_chzusdt 

		symbol_a_g_chzusdt = symbol_a_l_chzusdt 
		price_bids_a_g_chzusdt = price_bids_a_l_chzusdt 
		qty_bids_a_g_chzusdt = qty_bids_a_l_chzusdt 
		price_asks_a_g_chzusdt = price_asks_a_l_chzusdt 
		qty_asks_a_g_chzusdt = qty_asks_a_l_chzusdt 

def on_close_chzusdt(ws): 
	print('### closed ###') 

def on_error_chzusdt(ws, message): 
	print(message) 

def on_open_chzusdt(ws): 
	ws.send(json.dumps({'sub': f'market.chzusdt.ticker'})) 

def loop_chzusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_chzusdt, 
		on_close=on_close_chzusdt, 
		on_error=on_error_chzusdt) 
	ws.on_open = on_open_chzusdt 
	ws.run_forever() 

Thread(target=loop_chzusdt).start() 

symbol_b_g_chzusdc = 'chzusdc' 
price_bids_b_g_chzusdc = float(0.0) 
qty_bids_b_g_chzusdc = float(0.0) 
price_asks_b_g_chzusdc = float(0.0) 
qty_asks_b_g_chzusdc = float(0.0) 

def on_message_chzusdc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_chzusdc = 'chzusdc' 
		price_bids_b_l_chzusdc = data['tick']['bid'] 
		qty_bids_b_l_chzusdc = data['tick']['bidSize']
		price_asks_b_l_chzusdc = data['tick']['ask'] 
		qty_asks_b_l_chzusdc = data['tick']['askSize'] 

		global symbol_b_g_chzusdc 
		global price_bids_b_g_chzusdc 
		global qty_bids_b_g_chzusdc 
		global price_asks_b_g_chzusdc 
		global qty_asks_b_g_chzusdc 

		symbol_b_g_chzusdc = symbol_b_l_chzusdc 
		price_bids_b_g_chzusdc = price_bids_b_l_chzusdc 
		qty_bids_b_g_chzusdc = qty_bids_b_l_chzusdc 
		price_asks_b_g_chzusdc = price_asks_b_l_chzusdc 
		qty_asks_b_g_chzusdc = qty_asks_b_l_chzusdc 


def on_close_chzusdc(ws): 
	print('### closed ###') 

def on_error_chzusdc(ws, message): 
	print(message) 

def on_open_chzusdc(ws): 
	ws.send(json.dumps({'sub': f'market.chzusdc.ticker'})) 

def loop_chzusdc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_chzusdc, 
		on_close=on_close_chzusdc, 
		on_error=on_error_chzusdc) 
	ws.on_open = on_open_chzusdc 
	ws.run_forever() 

Thread(target=loop_chzusdc).start() 

def loop_chzusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDCUSDT != 0.0 and qty_bids_c_g_USDCUSDT != 0.0 and price_asks_c_g_USDCUSDT != 0.0 and qty_asks_c_g_USDCUSDT != 0.0 and price_bids_a_g_chzusdt != 0.0 and qty_bids_a_g_chzusdt != 0.0 and price_asks_a_g_chzusdt != 0.0 and qty_asks_a_g_chzusdt != 0.0 and price_bids_b_g_chzusdc != 0.0 and qty_bids_b_g_chzusdc != 0.0 and price_asks_b_g_chzusdc != 0.0 and qty_asks_b_g_chzusdc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_chzusdt) 
			price_b = float(price_bids_b_g_chzusdc) * price_a 
			price_c = float(price_bids_c_g_USDCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_chzusdc, pribil)

Thread(target=loop_chzusdt_Trade).start() 

symbol_a_g_nknusdt = 'nknusdt' 
price_bids_a_g_nknusdt = float(0.0) 
qty_bids_a_g_nknusdt = float(0.0) 
price_asks_a_g_nknusdt = float(0.0) 
qty_asks_a_g_nknusdt = float(0.0) 

def on_message_nknusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_nknusdt = 'nknusdt' 
		price_bids_a_l_nknusdt = data['tick']['bid'] 
		qty_bids_a_l_nknusdt = data['tick']['bidSize'] 
		price_asks_a_l_nknusdt = data['tick']['ask'] 
		qty_asks_a_l_nknusdt = data['tick']['askSize'] 

		global symbol_a_g_nknusdt 
		global price_bids_a_g_nknusdt 
		global qty_bids_a_g_nknusdt 
		global price_asks_a_g_nknusdt 
		global qty_asks_a_g_nknusdt 

		symbol_a_g_nknusdt = symbol_a_l_nknusdt 
		price_bids_a_g_nknusdt = price_bids_a_l_nknusdt 
		qty_bids_a_g_nknusdt = qty_bids_a_l_nknusdt 
		price_asks_a_g_nknusdt = price_asks_a_l_nknusdt 
		qty_asks_a_g_nknusdt = qty_asks_a_l_nknusdt 

def on_close_nknusdt(ws): 
	print('### closed ###') 

def on_error_nknusdt(ws, message): 
	print(message) 

def on_open_nknusdt(ws): 
	ws.send(json.dumps({'sub': f'market.nknusdt.ticker'})) 

def loop_nknusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nknusdt, 
		on_close=on_close_nknusdt, 
		on_error=on_error_nknusdt) 
	ws.on_open = on_open_nknusdt 
	ws.run_forever() 

Thread(target=loop_nknusdt).start() 

symbol_b_g_nknbtc = 'nknbtc' 
price_bids_b_g_nknbtc = float(0.0) 
qty_bids_b_g_nknbtc = float(0.0) 
price_asks_b_g_nknbtc = float(0.0) 
qty_asks_b_g_nknbtc = float(0.0) 

def on_message_nknbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_nknbtc = 'nknbtc' 
		price_bids_b_l_nknbtc = data['tick']['bid'] 
		qty_bids_b_l_nknbtc = data['tick']['bidSize']
		price_asks_b_l_nknbtc = data['tick']['ask'] 
		qty_asks_b_l_nknbtc = data['tick']['askSize'] 

		global symbol_b_g_nknbtc 
		global price_bids_b_g_nknbtc 
		global qty_bids_b_g_nknbtc 
		global price_asks_b_g_nknbtc 
		global qty_asks_b_g_nknbtc 

		symbol_b_g_nknbtc = symbol_b_l_nknbtc 
		price_bids_b_g_nknbtc = price_bids_b_l_nknbtc 
		qty_bids_b_g_nknbtc = qty_bids_b_l_nknbtc 
		price_asks_b_g_nknbtc = price_asks_b_l_nknbtc 
		qty_asks_b_g_nknbtc = qty_asks_b_l_nknbtc 


def on_close_nknbtc(ws): 
	print('### closed ###') 

def on_error_nknbtc(ws, message): 
	print(message) 

def on_open_nknbtc(ws): 
	ws.send(json.dumps({'sub': f'market.nknbtc.ticker'})) 

def loop_nknbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_nknbtc, 
		on_close=on_close_nknbtc, 
		on_error=on_error_nknbtc) 
	ws.on_open = on_open_nknbtc 
	ws.run_forever() 

Thread(target=loop_nknbtc).start() 

def loop_nknusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_nknusdt != 0.0 and qty_bids_a_g_nknusdt != 0.0 and price_asks_a_g_nknusdt != 0.0 and qty_asks_a_g_nknusdt != 0.0 and price_bids_b_g_nknbtc != 0.0 and qty_bids_b_g_nknbtc != 0.0 and price_asks_b_g_nknbtc != 0.0 and qty_asks_b_g_nknbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_nknusdt) 
			price_b = float(price_bids_b_g_nknbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_nknbtc, pribil)

Thread(target=loop_nknusdt_Trade).start() 

symbol_a_g_dotusdt = 'dotusdt' 
price_bids_a_g_dotusdt = float(0.0) 
qty_bids_a_g_dotusdt = float(0.0) 
price_asks_a_g_dotusdt = float(0.0) 
qty_asks_a_g_dotusdt = float(0.0) 

def on_message_dotusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_dotusdt = 'dotusdt' 
		price_bids_a_l_dotusdt = data['tick']['bid'] 
		qty_bids_a_l_dotusdt = data['tick']['bidSize'] 
		price_asks_a_l_dotusdt = data['tick']['ask'] 
		qty_asks_a_l_dotusdt = data['tick']['askSize'] 

		global symbol_a_g_dotusdt 
		global price_bids_a_g_dotusdt 
		global qty_bids_a_g_dotusdt 
		global price_asks_a_g_dotusdt 
		global qty_asks_a_g_dotusdt 

		symbol_a_g_dotusdt = symbol_a_l_dotusdt 
		price_bids_a_g_dotusdt = price_bids_a_l_dotusdt 
		qty_bids_a_g_dotusdt = qty_bids_a_l_dotusdt 
		price_asks_a_g_dotusdt = price_asks_a_l_dotusdt 
		qty_asks_a_g_dotusdt = qty_asks_a_l_dotusdt 

def on_close_dotusdt(ws): 
	print('### closed ###') 

def on_error_dotusdt(ws, message): 
	print(message) 

def on_open_dotusdt(ws): 
	ws.send(json.dumps({'sub': f'market.dotusdt.ticker'})) 

def loop_dotusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dotusdt, 
		on_close=on_close_dotusdt, 
		on_error=on_error_dotusdt) 
	ws.on_open = on_open_dotusdt 
	ws.run_forever() 

Thread(target=loop_dotusdt).start() 

symbol_b_g_dotusdd = 'dotusdd' 
price_bids_b_g_dotusdd = float(0.0) 
qty_bids_b_g_dotusdd = float(0.0) 
price_asks_b_g_dotusdd = float(0.0) 
qty_asks_b_g_dotusdd = float(0.0) 

def on_message_dotusdd(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_dotusdd = 'dotusdd' 
		price_bids_b_l_dotusdd = data['tick']['bid'] 
		qty_bids_b_l_dotusdd = data['tick']['bidSize']
		price_asks_b_l_dotusdd = data['tick']['ask'] 
		qty_asks_b_l_dotusdd = data['tick']['askSize'] 

		global symbol_b_g_dotusdd 
		global price_bids_b_g_dotusdd 
		global qty_bids_b_g_dotusdd 
		global price_asks_b_g_dotusdd 
		global qty_asks_b_g_dotusdd 

		symbol_b_g_dotusdd = symbol_b_l_dotusdd 
		price_bids_b_g_dotusdd = price_bids_b_l_dotusdd 
		qty_bids_b_g_dotusdd = qty_bids_b_l_dotusdd 
		price_asks_b_g_dotusdd = price_asks_b_l_dotusdd 
		qty_asks_b_g_dotusdd = qty_asks_b_l_dotusdd 


def on_close_dotusdd(ws): 
	print('### closed ###') 

def on_error_dotusdd(ws, message): 
	print(message) 

def on_open_dotusdd(ws): 
	ws.send(json.dumps({'sub': f'market.dotusdd.ticker'})) 

def loop_dotusdd(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dotusdd, 
		on_close=on_close_dotusdd, 
		on_error=on_error_dotusdd) 
	ws.on_open = on_open_dotusdd 
	ws.run_forever() 

Thread(target=loop_dotusdd).start() 

def loop_dotusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_USDDUSDT != 0.0 and qty_bids_c_g_USDDUSDT != 0.0 and price_asks_c_g_USDDUSDT != 0.0 and qty_asks_c_g_USDDUSDT != 0.0 and price_bids_a_g_dotusdt != 0.0 and qty_bids_a_g_dotusdt != 0.0 and price_asks_a_g_dotusdt != 0.0 and qty_asks_a_g_dotusdt != 0.0 and price_bids_b_g_dotusdd != 0.0 and qty_bids_b_g_dotusdd != 0.0 and price_asks_b_g_dotusdd != 0.0 and qty_asks_b_g_dotusdd != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_dotusdt) 
			price_b = float(price_bids_b_g_dotusdd) * price_a 
			price_c = float(price_bids_c_g_USDDUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_dotusdd, pribil)

Thread(target=loop_dotusdt_Trade).start() 

symbol_a_g_oneusdt = 'oneusdt' 
price_bids_a_g_oneusdt = float(0.0) 
qty_bids_a_g_oneusdt = float(0.0) 
price_asks_a_g_oneusdt = float(0.0) 
qty_asks_a_g_oneusdt = float(0.0) 

def on_message_oneusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_oneusdt = 'oneusdt' 
		price_bids_a_l_oneusdt = data['tick']['bid'] 
		qty_bids_a_l_oneusdt = data['tick']['bidSize'] 
		price_asks_a_l_oneusdt = data['tick']['ask'] 
		qty_asks_a_l_oneusdt = data['tick']['askSize'] 

		global symbol_a_g_oneusdt 
		global price_bids_a_g_oneusdt 
		global qty_bids_a_g_oneusdt 
		global price_asks_a_g_oneusdt 
		global qty_asks_a_g_oneusdt 

		symbol_a_g_oneusdt = symbol_a_l_oneusdt 
		price_bids_a_g_oneusdt = price_bids_a_l_oneusdt 
		qty_bids_a_g_oneusdt = qty_bids_a_l_oneusdt 
		price_asks_a_g_oneusdt = price_asks_a_l_oneusdt 
		qty_asks_a_g_oneusdt = qty_asks_a_l_oneusdt 

def on_close_oneusdt(ws): 
	print('### closed ###') 

def on_error_oneusdt(ws, message): 
	print(message) 

def on_open_oneusdt(ws): 
	ws.send(json.dumps({'sub': f'market.oneusdt.ticker'})) 

def loop_oneusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_oneusdt, 
		on_close=on_close_oneusdt, 
		on_error=on_error_oneusdt) 
	ws.on_open = on_open_oneusdt 
	ws.run_forever() 

Thread(target=loop_oneusdt).start() 

symbol_b_g_oneht = 'oneht' 
price_bids_b_g_oneht = float(0.0) 
qty_bids_b_g_oneht = float(0.0) 
price_asks_b_g_oneht = float(0.0) 
qty_asks_b_g_oneht = float(0.0) 

def on_message_oneht(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_oneht = 'oneht' 
		price_bids_b_l_oneht = data['tick']['bid'] 
		qty_bids_b_l_oneht = data['tick']['bidSize']
		price_asks_b_l_oneht = data['tick']['ask'] 
		qty_asks_b_l_oneht = data['tick']['askSize'] 

		global symbol_b_g_oneht 
		global price_bids_b_g_oneht 
		global qty_bids_b_g_oneht 
		global price_asks_b_g_oneht 
		global qty_asks_b_g_oneht 

		symbol_b_g_oneht = symbol_b_l_oneht 
		price_bids_b_g_oneht = price_bids_b_l_oneht 
		qty_bids_b_g_oneht = qty_bids_b_l_oneht 
		price_asks_b_g_oneht = price_asks_b_l_oneht 
		qty_asks_b_g_oneht = qty_asks_b_l_oneht 


def on_close_oneht(ws): 
	print('### closed ###') 

def on_error_oneht(ws, message): 
	print(message) 

def on_open_oneht(ws): 
	ws.send(json.dumps({'sub': f'market.oneht.ticker'})) 

def loop_oneht(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_oneht, 
		on_close=on_close_oneht, 
		on_error=on_error_oneht) 
	ws.on_open = on_open_oneht 
	ws.run_forever() 

Thread(target=loop_oneht).start() 

def loop_oneusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_HTUSDT != 0.0 and qty_bids_c_g_HTUSDT != 0.0 and price_asks_c_g_HTUSDT != 0.0 and qty_asks_c_g_HTUSDT != 0.0 and price_bids_a_g_oneusdt != 0.0 and qty_bids_a_g_oneusdt != 0.0 and price_asks_a_g_oneusdt != 0.0 and qty_asks_a_g_oneusdt != 0.0 and price_bids_b_g_oneht != 0.0 and qty_bids_b_g_oneht != 0.0 and price_asks_b_g_oneht != 0.0 and qty_asks_b_g_oneht != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_oneusdt) 
			price_b = float(price_bids_b_g_oneht) * price_a 
			price_c = float(price_bids_c_g_HTUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_oneht, pribil)

Thread(target=loop_oneusdt_Trade).start() 

symbol_a_g_hbarusdt = 'hbarusdt' 
price_bids_a_g_hbarusdt = float(0.0) 
qty_bids_a_g_hbarusdt = float(0.0) 
price_asks_a_g_hbarusdt = float(0.0) 
qty_asks_a_g_hbarusdt = float(0.0) 

def on_message_hbarusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_hbarusdt = 'hbarusdt' 
		price_bids_a_l_hbarusdt = data['tick']['bid'] 
		qty_bids_a_l_hbarusdt = data['tick']['bidSize'] 
		price_asks_a_l_hbarusdt = data['tick']['ask'] 
		qty_asks_a_l_hbarusdt = data['tick']['askSize'] 

		global symbol_a_g_hbarusdt 
		global price_bids_a_g_hbarusdt 
		global qty_bids_a_g_hbarusdt 
		global price_asks_a_g_hbarusdt 
		global qty_asks_a_g_hbarusdt 

		symbol_a_g_hbarusdt = symbol_a_l_hbarusdt 
		price_bids_a_g_hbarusdt = price_bids_a_l_hbarusdt 
		qty_bids_a_g_hbarusdt = qty_bids_a_l_hbarusdt 
		price_asks_a_g_hbarusdt = price_asks_a_l_hbarusdt 
		qty_asks_a_g_hbarusdt = qty_asks_a_l_hbarusdt 

def on_close_hbarusdt(ws): 
	print('### closed ###') 

def on_error_hbarusdt(ws, message): 
	print(message) 

def on_open_hbarusdt(ws): 
	ws.send(json.dumps({'sub': f'market.hbarusdt.ticker'})) 

def loop_hbarusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_hbarusdt, 
		on_close=on_close_hbarusdt, 
		on_error=on_error_hbarusdt) 
	ws.on_open = on_open_hbarusdt 
	ws.run_forever() 

Thread(target=loop_hbarusdt).start() 

symbol_b_g_hbarbtc = 'hbarbtc' 
price_bids_b_g_hbarbtc = float(0.0) 
qty_bids_b_g_hbarbtc = float(0.0) 
price_asks_b_g_hbarbtc = float(0.0) 
qty_asks_b_g_hbarbtc = float(0.0) 

def on_message_hbarbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_hbarbtc = 'hbarbtc' 
		price_bids_b_l_hbarbtc = data['tick']['bid'] 
		qty_bids_b_l_hbarbtc = data['tick']['bidSize']
		price_asks_b_l_hbarbtc = data['tick']['ask'] 
		qty_asks_b_l_hbarbtc = data['tick']['askSize'] 

		global symbol_b_g_hbarbtc 
		global price_bids_b_g_hbarbtc 
		global qty_bids_b_g_hbarbtc 
		global price_asks_b_g_hbarbtc 
		global qty_asks_b_g_hbarbtc 

		symbol_b_g_hbarbtc = symbol_b_l_hbarbtc 
		price_bids_b_g_hbarbtc = price_bids_b_l_hbarbtc 
		qty_bids_b_g_hbarbtc = qty_bids_b_l_hbarbtc 
		price_asks_b_g_hbarbtc = price_asks_b_l_hbarbtc 
		qty_asks_b_g_hbarbtc = qty_asks_b_l_hbarbtc 


def on_close_hbarbtc(ws): 
	print('### closed ###') 

def on_error_hbarbtc(ws, message): 
	print(message) 

def on_open_hbarbtc(ws): 
	ws.send(json.dumps({'sub': f'market.hbarbtc.ticker'})) 

def loop_hbarbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_hbarbtc, 
		on_close=on_close_hbarbtc, 
		on_error=on_error_hbarbtc) 
	ws.on_open = on_open_hbarbtc 
	ws.run_forever() 

Thread(target=loop_hbarbtc).start() 

def loop_hbarusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_hbarusdt != 0.0 and qty_bids_a_g_hbarusdt != 0.0 and price_asks_a_g_hbarusdt != 0.0 and qty_asks_a_g_hbarusdt != 0.0 and price_bids_b_g_hbarbtc != 0.0 and qty_bids_b_g_hbarbtc != 0.0 and price_asks_b_g_hbarbtc != 0.0 and qty_asks_b_g_hbarbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_hbarusdt) 
			price_b = float(price_bids_b_g_hbarbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_hbarbtc, pribil)

Thread(target=loop_hbarusdt_Trade).start() 

symbol_a_g_trbusdt = 'trbusdt' 
price_bids_a_g_trbusdt = float(0.0) 
qty_bids_a_g_trbusdt = float(0.0) 
price_asks_a_g_trbusdt = float(0.0) 
qty_asks_a_g_trbusdt = float(0.0) 

def on_message_trbusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_trbusdt = 'trbusdt' 
		price_bids_a_l_trbusdt = data['tick']['bid'] 
		qty_bids_a_l_trbusdt = data['tick']['bidSize'] 
		price_asks_a_l_trbusdt = data['tick']['ask'] 
		qty_asks_a_l_trbusdt = data['tick']['askSize'] 

		global symbol_a_g_trbusdt 
		global price_bids_a_g_trbusdt 
		global qty_bids_a_g_trbusdt 
		global price_asks_a_g_trbusdt 
		global qty_asks_a_g_trbusdt 

		symbol_a_g_trbusdt = symbol_a_l_trbusdt 
		price_bids_a_g_trbusdt = price_bids_a_l_trbusdt 
		qty_bids_a_g_trbusdt = qty_bids_a_l_trbusdt 
		price_asks_a_g_trbusdt = price_asks_a_l_trbusdt 
		qty_asks_a_g_trbusdt = qty_asks_a_l_trbusdt 

def on_close_trbusdt(ws): 
	print('### closed ###') 

def on_error_trbusdt(ws, message): 
	print(message) 

def on_open_trbusdt(ws): 
	ws.send(json.dumps({'sub': f'market.trbusdt.ticker'})) 

def loop_trbusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_trbusdt, 
		on_close=on_close_trbusdt, 
		on_error=on_error_trbusdt) 
	ws.on_open = on_open_trbusdt 
	ws.run_forever() 

Thread(target=loop_trbusdt).start() 

symbol_b_g_trbbtc = 'trbbtc' 
price_bids_b_g_trbbtc = float(0.0) 
qty_bids_b_g_trbbtc = float(0.0) 
price_asks_b_g_trbbtc = float(0.0) 
qty_asks_b_g_trbbtc = float(0.0) 

def on_message_trbbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_trbbtc = 'trbbtc' 
		price_bids_b_l_trbbtc = data['tick']['bid'] 
		qty_bids_b_l_trbbtc = data['tick']['bidSize']
		price_asks_b_l_trbbtc = data['tick']['ask'] 
		qty_asks_b_l_trbbtc = data['tick']['askSize'] 

		global symbol_b_g_trbbtc 
		global price_bids_b_g_trbbtc 
		global qty_bids_b_g_trbbtc 
		global price_asks_b_g_trbbtc 
		global qty_asks_b_g_trbbtc 

		symbol_b_g_trbbtc = symbol_b_l_trbbtc 
		price_bids_b_g_trbbtc = price_bids_b_l_trbbtc 
		qty_bids_b_g_trbbtc = qty_bids_b_l_trbbtc 
		price_asks_b_g_trbbtc = price_asks_b_l_trbbtc 
		qty_asks_b_g_trbbtc = qty_asks_b_l_trbbtc 


def on_close_trbbtc(ws): 
	print('### closed ###') 

def on_error_trbbtc(ws, message): 
	print(message) 

def on_open_trbbtc(ws): 
	ws.send(json.dumps({'sub': f'market.trbbtc.ticker'})) 

def loop_trbbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_trbbtc, 
		on_close=on_close_trbbtc, 
		on_error=on_error_trbbtc) 
	ws.on_open = on_open_trbbtc 
	ws.run_forever() 

Thread(target=loop_trbbtc).start() 

def loop_trbusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_trbusdt != 0.0 and qty_bids_a_g_trbusdt != 0.0 and price_asks_a_g_trbusdt != 0.0 and qty_asks_a_g_trbusdt != 0.0 and price_bids_b_g_trbbtc != 0.0 and qty_bids_b_g_trbbtc != 0.0 and price_asks_b_g_trbbtc != 0.0 and qty_asks_b_g_trbbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_trbusdt) 
			price_b = float(price_bids_b_g_trbbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_trbbtc, pribil)

Thread(target=loop_trbusdt_Trade).start() 

symbol_a_g_dbcusdt = 'dbcusdt' 
price_bids_a_g_dbcusdt = float(0.0) 
qty_bids_a_g_dbcusdt = float(0.0) 
price_asks_a_g_dbcusdt = float(0.0) 
qty_asks_a_g_dbcusdt = float(0.0) 

def on_message_dbcusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_dbcusdt = 'dbcusdt' 
		price_bids_a_l_dbcusdt = data['tick']['bid'] 
		qty_bids_a_l_dbcusdt = data['tick']['bidSize'] 
		price_asks_a_l_dbcusdt = data['tick']['ask'] 
		qty_asks_a_l_dbcusdt = data['tick']['askSize'] 

		global symbol_a_g_dbcusdt 
		global price_bids_a_g_dbcusdt 
		global qty_bids_a_g_dbcusdt 
		global price_asks_a_g_dbcusdt 
		global qty_asks_a_g_dbcusdt 

		symbol_a_g_dbcusdt = symbol_a_l_dbcusdt 
		price_bids_a_g_dbcusdt = price_bids_a_l_dbcusdt 
		qty_bids_a_g_dbcusdt = qty_bids_a_l_dbcusdt 
		price_asks_a_g_dbcusdt = price_asks_a_l_dbcusdt 
		qty_asks_a_g_dbcusdt = qty_asks_a_l_dbcusdt 

def on_close_dbcusdt(ws): 
	print('### closed ###') 

def on_error_dbcusdt(ws, message): 
	print(message) 

def on_open_dbcusdt(ws): 
	ws.send(json.dumps({'sub': f'market.dbcusdt.ticker'})) 

def loop_dbcusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dbcusdt, 
		on_close=on_close_dbcusdt, 
		on_error=on_error_dbcusdt) 
	ws.on_open = on_open_dbcusdt 
	ws.run_forever() 

Thread(target=loop_dbcusdt).start() 

symbol_b_g_dbcbtc = 'dbcbtc' 
price_bids_b_g_dbcbtc = float(0.0) 
qty_bids_b_g_dbcbtc = float(0.0) 
price_asks_b_g_dbcbtc = float(0.0) 
qty_asks_b_g_dbcbtc = float(0.0) 

def on_message_dbcbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_dbcbtc = 'dbcbtc' 
		price_bids_b_l_dbcbtc = data['tick']['bid'] 
		qty_bids_b_l_dbcbtc = data['tick']['bidSize']
		price_asks_b_l_dbcbtc = data['tick']['ask'] 
		qty_asks_b_l_dbcbtc = data['tick']['askSize'] 

		global symbol_b_g_dbcbtc 
		global price_bids_b_g_dbcbtc 
		global qty_bids_b_g_dbcbtc 
		global price_asks_b_g_dbcbtc 
		global qty_asks_b_g_dbcbtc 

		symbol_b_g_dbcbtc = symbol_b_l_dbcbtc 
		price_bids_b_g_dbcbtc = price_bids_b_l_dbcbtc 
		qty_bids_b_g_dbcbtc = qty_bids_b_l_dbcbtc 
		price_asks_b_g_dbcbtc = price_asks_b_l_dbcbtc 
		qty_asks_b_g_dbcbtc = qty_asks_b_l_dbcbtc 


def on_close_dbcbtc(ws): 
	print('### closed ###') 

def on_error_dbcbtc(ws, message): 
	print(message) 

def on_open_dbcbtc(ws): 
	ws.send(json.dumps({'sub': f'market.dbcbtc.ticker'})) 

def loop_dbcbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_dbcbtc, 
		on_close=on_close_dbcbtc, 
		on_error=on_error_dbcbtc) 
	ws.on_open = on_open_dbcbtc 
	ws.run_forever() 

Thread(target=loop_dbcbtc).start() 

def loop_dbcusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_dbcusdt != 0.0 and qty_bids_a_g_dbcusdt != 0.0 and price_asks_a_g_dbcusdt != 0.0 and qty_asks_a_g_dbcusdt != 0.0 and price_bids_b_g_dbcbtc != 0.0 and qty_bids_b_g_dbcbtc != 0.0 and price_asks_b_g_dbcbtc != 0.0 and qty_asks_b_g_dbcbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_dbcusdt) 
			price_b = float(price_bids_b_g_dbcbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_dbcbtc, pribil)

Thread(target=loop_dbcusdt_Trade).start() 

symbol_a_g_requsdt = 'requsdt' 
price_bids_a_g_requsdt = float(0.0) 
qty_bids_a_g_requsdt = float(0.0) 
price_asks_a_g_requsdt = float(0.0) 
qty_asks_a_g_requsdt = float(0.0) 

def on_message_requsdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_requsdt = 'requsdt' 
		price_bids_a_l_requsdt = data['tick']['bid'] 
		qty_bids_a_l_requsdt = data['tick']['bidSize'] 
		price_asks_a_l_requsdt = data['tick']['ask'] 
		qty_asks_a_l_requsdt = data['tick']['askSize'] 

		global symbol_a_g_requsdt 
		global price_bids_a_g_requsdt 
		global qty_bids_a_g_requsdt 
		global price_asks_a_g_requsdt 
		global qty_asks_a_g_requsdt 

		symbol_a_g_requsdt = symbol_a_l_requsdt 
		price_bids_a_g_requsdt = price_bids_a_l_requsdt 
		qty_bids_a_g_requsdt = qty_bids_a_l_requsdt 
		price_asks_a_g_requsdt = price_asks_a_l_requsdt 
		qty_asks_a_g_requsdt = qty_asks_a_l_requsdt 

def on_close_requsdt(ws): 
	print('### closed ###') 

def on_error_requsdt(ws, message): 
	print(message) 

def on_open_requsdt(ws): 
	ws.send(json.dumps({'sub': f'market.requsdt.ticker'})) 

def loop_requsdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_requsdt, 
		on_close=on_close_requsdt, 
		on_error=on_error_requsdt) 
	ws.on_open = on_open_requsdt 
	ws.run_forever() 

Thread(target=loop_requsdt).start() 

symbol_b_g_reqeth = 'reqeth' 
price_bids_b_g_reqeth = float(0.0) 
qty_bids_b_g_reqeth = float(0.0) 
price_asks_b_g_reqeth = float(0.0) 
qty_asks_b_g_reqeth = float(0.0) 

def on_message_reqeth(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_reqeth = 'reqeth' 
		price_bids_b_l_reqeth = data['tick']['bid'] 
		qty_bids_b_l_reqeth = data['tick']['bidSize']
		price_asks_b_l_reqeth = data['tick']['ask'] 
		qty_asks_b_l_reqeth = data['tick']['askSize'] 

		global symbol_b_g_reqeth 
		global price_bids_b_g_reqeth 
		global qty_bids_b_g_reqeth 
		global price_asks_b_g_reqeth 
		global qty_asks_b_g_reqeth 

		symbol_b_g_reqeth = symbol_b_l_reqeth 
		price_bids_b_g_reqeth = price_bids_b_l_reqeth 
		qty_bids_b_g_reqeth = qty_bids_b_l_reqeth 
		price_asks_b_g_reqeth = price_asks_b_l_reqeth 
		qty_asks_b_g_reqeth = qty_asks_b_l_reqeth 


def on_close_reqeth(ws): 
	print('### closed ###') 

def on_error_reqeth(ws, message): 
	print(message) 

def on_open_reqeth(ws): 
	ws.send(json.dumps({'sub': f'market.reqeth.ticker'})) 

def loop_reqeth(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_reqeth, 
		on_close=on_close_reqeth, 
		on_error=on_error_reqeth) 
	ws.on_open = on_open_reqeth 
	ws.run_forever() 

Thread(target=loop_reqeth).start() 

def loop_requsdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_ETHUSDT != 0.0 and qty_bids_c_g_ETHUSDT != 0.0 and price_asks_c_g_ETHUSDT != 0.0 and qty_asks_c_g_ETHUSDT != 0.0 and price_bids_a_g_requsdt != 0.0 and qty_bids_a_g_requsdt != 0.0 and price_asks_a_g_requsdt != 0.0 and qty_asks_a_g_requsdt != 0.0 and price_bids_b_g_reqeth != 0.0 and qty_bids_b_g_reqeth != 0.0 and price_asks_b_g_reqeth != 0.0 and qty_asks_b_g_reqeth != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_requsdt) 
			price_b = float(price_bids_b_g_reqeth) * price_a 
			price_c = float(price_bids_c_g_ETHUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_reqeth, pribil)

Thread(target=loop_requsdt_Trade).start() 

symbol_a_g_elfusdt = 'elfusdt' 
price_bids_a_g_elfusdt = float(0.0) 
qty_bids_a_g_elfusdt = float(0.0) 
price_asks_a_g_elfusdt = float(0.0) 
qty_asks_a_g_elfusdt = float(0.0) 

def on_message_elfusdt(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_a_l_elfusdt = 'elfusdt' 
		price_bids_a_l_elfusdt = data['tick']['bid'] 
		qty_bids_a_l_elfusdt = data['tick']['bidSize'] 
		price_asks_a_l_elfusdt = data['tick']['ask'] 
		qty_asks_a_l_elfusdt = data['tick']['askSize'] 

		global symbol_a_g_elfusdt 
		global price_bids_a_g_elfusdt 
		global qty_bids_a_g_elfusdt 
		global price_asks_a_g_elfusdt 
		global qty_asks_a_g_elfusdt 

		symbol_a_g_elfusdt = symbol_a_l_elfusdt 
		price_bids_a_g_elfusdt = price_bids_a_l_elfusdt 
		qty_bids_a_g_elfusdt = qty_bids_a_l_elfusdt 
		price_asks_a_g_elfusdt = price_asks_a_l_elfusdt 
		qty_asks_a_g_elfusdt = qty_asks_a_l_elfusdt 

def on_close_elfusdt(ws): 
	print('### closed ###') 

def on_error_elfusdt(ws, message): 
	print(message) 

def on_open_elfusdt(ws): 
	ws.send(json.dumps({'sub': f'market.elfusdt.ticker'})) 

def loop_elfusdt(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_elfusdt, 
		on_close=on_close_elfusdt, 
		on_error=on_error_elfusdt) 
	ws.on_open = on_open_elfusdt 
	ws.run_forever() 

Thread(target=loop_elfusdt).start() 

symbol_b_g_elfbtc = 'elfbtc' 
price_bids_b_g_elfbtc = float(0.0) 
qty_bids_b_g_elfbtc = float(0.0) 
price_asks_b_g_elfbtc = float(0.0) 
qty_asks_b_g_elfbtc = float(0.0) 

def on_message_elfbtc(ws, message): 
	data = json.loads(gzip.decompress(message)) 

	if 'ping' in data: 
		ws.send(json.dumps({ 
			'pong': data['ping'] 
		})) 

	else: 

		symbol_b_l_elfbtc = 'elfbtc' 
		price_bids_b_l_elfbtc = data['tick']['bid'] 
		qty_bids_b_l_elfbtc = data['tick']['bidSize']
		price_asks_b_l_elfbtc = data['tick']['ask'] 
		qty_asks_b_l_elfbtc = data['tick']['askSize'] 

		global symbol_b_g_elfbtc 
		global price_bids_b_g_elfbtc 
		global qty_bids_b_g_elfbtc 
		global price_asks_b_g_elfbtc 
		global qty_asks_b_g_elfbtc 

		symbol_b_g_elfbtc = symbol_b_l_elfbtc 
		price_bids_b_g_elfbtc = price_bids_b_l_elfbtc 
		qty_bids_b_g_elfbtc = qty_bids_b_l_elfbtc 
		price_asks_b_g_elfbtc = price_asks_b_l_elfbtc 
		qty_asks_b_g_elfbtc = qty_asks_b_l_elfbtc 


def on_close_elfbtc(ws): 
	print('### closed ###') 

def on_error_elfbtc(ws, message): 
	print(message) 

def on_open_elfbtc(ws): 
	ws.send(json.dumps({'sub': f'market.elfbtc.ticker'})) 

def loop_elfbtc(): 
	ws = websocket.WebSocketApp('wss://api.huobi.pro/ws', 
		on_message=on_message_elfbtc, 
		on_close=on_close_elfbtc, 
		on_error=on_error_elfbtc) 
	ws.on_open = on_open_elfbtc 
	ws.run_forever() 

Thread(target=loop_elfbtc).start() 

def loop_elfusdt_Trade(): 
	while True: 
		time.sleep(0.1)


		if price_bids_c_g_BTCUSDT != 0.0 and qty_bids_c_g_BTCUSDT != 0.0 and price_asks_c_g_BTCUSDT != 0.0 and qty_asks_c_g_BTCUSDT != 0.0 and price_bids_a_g_elfusdt != 0.0 and qty_bids_a_g_elfusdt != 0.0 and price_asks_a_g_elfusdt != 0.0 and qty_asks_a_g_elfusdt != 0.0 and price_bids_b_g_elfbtc != 0.0 and qty_bids_b_g_elfbtc != 0.0 and price_asks_b_g_elfbtc != 0.0 and qty_asks_b_g_elfbtc != 0.0: 


			price_a = usdt_count / float(price_asks_a_g_elfusdt) 
			price_b = float(price_bids_b_g_elfbtc) * price_a 
			price_c = float(price_bids_c_g_BTCUSDT) * price_b 
			pribil =  price_c - usdt_count

			if pribil > 0:
				print(symbol_b_g_elfbtc, pribil)

Thread(target=loop_elfusdt_Trade).start() 

