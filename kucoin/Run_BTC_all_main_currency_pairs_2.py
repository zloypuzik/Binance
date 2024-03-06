import time 
import datetime 
import threading 
import requests 
from decimal import Decimal 
import json 
import websocket 
from kucoin.client import Client 
from threading import * 


def f_minqty_size_up(kolichestvo, stepSize): 

	sell_amount_a = Decimal(kolichestvo) + Decimal(stepSize) 
	return sell_amount_a 


def f_minqty_size_down(kolichestvo, stepSize): 

	sell_amount_a = ((int(kolichestvo * 100000000000000) - int(kolichestvo * 100000000000000) % (stepSize * 100000000000000)) / 100000000000000) 
	return sell_amount_a 


api_key = '63cc9d027675230001bba629' 
api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7' 

client = Client(api_key, api_secret, passphrase='4796212') 

usdt_count = Decimal(input('Укажите количество монет:')) 

all_pribil = Decimal('0.0') 

locker = threading.RLock() 
symbol_g_BTCUSDT = 'BTCUSDT' 
price_bids_g_BTCUSDT = Decimal('0.0') 
qty_bids_g_BTCUSDT = Decimal('0.0') 
price_asks_g_BTCUSDT = Decimal('0.0') 
qty_asks_g_BTCUSDT = Decimal('0.0') 
stepSize_base_g_BTCUSDT = Decimal('0.00000001') 
stepSize_quote_g_BTCUSDT = Decimal('0.000001') 

symbol_g_AGIXBTC = 'AGIXBTC' 
price_bids_g_AGIXBTC = Decimal('0.0') 
qty_bids_g_AGIXBTC = Decimal('0.0') 
price_asks_g_AGIXBTC = Decimal('0.0') 
qty_asks_g_AGIXBTC = Decimal('0.0') 
stepSize_base_g_AGIXBTC = Decimal('0.0001') 
stepSize_quote_g_AGIXBTC = Decimal('0.000000001') 

symbol_g_AGIXUSDT = 'AGIXUSDT' 
price_bids_g_AGIXUSDT = Decimal('0.0') 
qty_bids_g_AGIXUSDT = Decimal('0.0') 
price_asks_g_AGIXUSDT = Decimal('0.0') 
qty_asks_g_AGIXUSDT = Decimal('0.0') 
stepSize_base_g_AGIXUSDT = Decimal('0.0001') 
stepSize_quote_g_AGIXUSDT = Decimal('0.00001') 



def loop_BTCUSDT_AGIXBTC_AGIXUSDT_Trade(): 

	while True: 
		time.sleep(0.1)

		if price_bids_g_BTCUSDT != 0.0 and qty_bids_g_BTCUSDT != 0.0 and price_asks_g_BTCUSDT != 0.0 and qty_asks_g_BTCUSDT != 0.0 and price_bids_g_AGIXBTC != 0.0 and qty_bids_g_AGIXBTC != 0.0 and price_asks_g_AGIXBTC != 0.0 and qty_asks_g_AGIXBTC != 0.0 and price_bids_g_AGIXUSDT != 0.0 and qty_bids_g_AGIXUSDT != 0.0 and price_asks_g_AGIXUSDT != 0.0 and qty_asks_g_AGIXUSDT != 0.0: 

			quantity_pair_c_raschet = Decimal(usdt_count) / Decimal(price_bids_g_AGIXUSDT) 
			quantity_pair_c_raschet = Decimal(f_minqty_size_down(quantity_pair_c_raschet, stepSize_base_g_AGIXUSDT)) 
			test3 = quantity_pair_c_raschet 
			float_qty_bids_g_AGIXUSDT = float(qty_bids_g_AGIXUSDT) 
			if float_qty_bids_g_AGIXUSDT > test3: 
				dd = Decimal(f_minqty_size_down(test3, stepSize_base_g_AGIXBTC)) 
				while dd < test3: 
					dd = (f_minqty_size_up(dd, stepSize_base_g_AGIXBTC)) 
				test3 = dd 
				quantity_pair_b_raschet = Decimal(test3) * Decimal(price_asks_g_AGIXBTC) 
				test2 = quantity_pair_b_raschet 
				float_qty_asks_g_AGIXBTC = float(qty_asks_g_AGIXBTC) 
				if float_qty_asks_g_AGIXBTC > test3: 

					ddd = Decimal(f_minqty_size_down(test2, stepSize_base_g_BTCUSDT)) 
					while ddd < test2: 
						ddd = Decimal(f_minqty_size_up(ddd, stepSize_base_g_BTCUSDT)) 
					test2 = ddd 

					test1 = ddd 
					float_qty_asks_g_BTCUSDT = float(qty_asks_g_BTCUSDT) 
					if float_qty_asks_g_BTCUSDT > test1:
						quantity_pair_a = test1 
						quantity_pair_b = test3 
						quantity_pair_c = test3 
						price_a = Decimal(quantity_pair_a) * Decimal(price_asks_g_BTCUSDT) 
						price_b = Decimal(quantity_pair_b) * Decimal(price_asks_g_AGIXBTC) 
						price_c = Decimal(quantity_pair_c) * Decimal(price_bids_g_AGIXUSDT) 
						pribil = Decimal(price_c) - Decimal(price_a) 

						time_test = datetime.datetime.now() 
						a = Decimal(price_c) 
						b = Decimal(price_a) 
						c = Decimal((a / b - 1) * 100) 
						commission_a = Decimal('0.08') 
						commission_b = Decimal('0.08') 
						commission_c = Decimal('0.08') 
						commission_all = Decimal(commission_a) + Decimal(commission_b) + Decimal(commission_c) 
						if c > commission_all: 
							locker.acquire()
							print('################################################################################################################') 
							print(time_test) 
							print('Общая коммисия:', commission_all) 
							print('Пара_А:', symbol_g_BTCUSDT, '#', 'Покупаем', quantity_pair_a, 'BTC', 'за', price_a, 'USDT', 'по цене', price_asks_g_BTCUSDT) 
							print('Пара_B:', symbol_g_AGIXBTC, '#', 'Покупаем', quantity_pair_b, 'AGIX', 'за', price_b, 'BTC', 'по цене', price_asks_g_AGIXBTC) 
							print('Пара_C:', symbol_g_AGIXUSDT, '#', 'Продаем', quantity_pair_c, 'AGIX', 'за', price_c, 'USDT', 'по цене', price_bids_g_AGIXUSDT) 
							print('Прибыль:', pribil, 'Прибыль в %:', c, '%') 
							time.sleep(1.0) 
							locker.release() 


Thread(target=loop_BTCUSDT_AGIXBTC_AGIXUSDT_Trade).start() 

count_message = 0 
start_time = time.time() 


def get_ticker_all(ws, message): 

	global pingInterval, pingTime, id_channel, count_message, start_time 
	data = json.loads(message) 

	if 'type' in data: 
		if data['type'] == 'welcome': 
			id_channel = data['id'] 
			ws.send(json.dumps({'id': data['id'], 'type': 'subscribe', 'topic': '/market/ticker:all', 'response': 'true'})) 
		elif data['type'] == 'message': 
			count_message += 1 

			symbol = data['subject'] 
			price_bids_g = data['data']['bestBid'] 
			qty_bids_g = data['data']['bestBidSize'] 
			price_asks_g = data['data']['bestAsk'] 
			qty_asks_g = data['data']['bestAskSize'] 

			chars = '.-!' 
			symbol = symbol.translate(str.maketrans('', '', chars)) 
			price_bids_g_ = 'price_bids_g_' + symbol 
			globals()[price_bids_g_] = price_bids_g 
			qty_bids_g_ = 'qty_bids_g_' + symbol 
			globals()[qty_bids_g_] = qty_bids_g 

			price_asks_g_ = 'price_asks_g_' + symbol 
			globals()[price_asks_g_] = price_asks_g 

			qty_asks_g_ = 'qty_asks_g_' + symbol 
			globals()[qty_asks_g_] = qty_asks_g 
		else: 
			pass 
	else: 
		print(data) 

	if (pingTime + pingInterval) <= round(time.time()): 
		ws.send(json.dumps({'id': id_channel, 'type': 'ping'})) 
		pingTime = round(time.time())  # Запомним новое время для сообщения 
		count_message = 0  # Обнуляем счетчик сообщений 
		start_time = time.time()  # Сбросим счетчик времени 


def on_close(ws): 
	print('### closed ###') 


def on_error(ws, message): 
	print(message) 


def loadSetting(): 
	return requests.post('https://api.kucoin.com/api/v1/bullet-public').json() 


settings = loadSetting() 
pingInterval = round((settings['data']['instanceServers'][0]['pingInterval'] / 1000) / 2) - 1 
pingTime = round(time.time()) 
id_channel = '' 

ws = websocket.WebSocketApp(f"{settings['data']['instanceServers'][0]['endpoint']}?token={settings['data']['token']}", on_message=get_ticker_all, on_close=on_close, on_error=on_error) 
ws.run_forever() 
