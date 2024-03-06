import json
import requests
import time
import websocket
import threading
from threading import *
from decimal import Decimal

symbol_original_g_ALGOUSDT = 'ALGO-USDT'
symbol_g_ALGOUSDT = 'ALGOUSDT'
price_bids_g_ALGOUSDT = Decimal('0.0')
qty_bids_g_ALGOUSDT = Decimal('0.0')
price_asks_g_ALGOUSDT = Decimal('0.0')
qty_asks_g_ALGOUSDT = Decimal('0.0')
stepSize_g_ALGOUSDT = Decimal('0.0001')

# def on_message_ALGOUSDT():
#
#     while True:
#         time.sleep(0.1)
#         print(stepSize_g_ALGOUSDT)
# Thread(target=on_message_ALGOUSDT).start()
#price_bids_c_l_BTCUSDT = ''

def on_message_BNBUSDT():

    while True:
        time.sleep(1)
        if qty_bids_g_ALGOUSDT != Decimal('0.0'):
            print(price_bids_g_ALGOUSDT, qty_bids_g_ALGOUSDT, price_asks_g_ALGOUSDT, qty_asks_g_ALGOUSDT)

Thread(target=on_message_BNBUSDT).start()

count_message = 0
start_time = time.time()


def get_ticker_all(ws, message):

    global pingInterval, pingTime, id_channel, count_message, start_time
    data = json.loads(message)

    if 'type' in data:
        if data['type'] == 'welcome':
            id_channel = data['id']
            ws.send(json.dumps(
                {
                    "id": data['id'],
                    "type": "subscribe",
                    "topic": "/market/ticker:all",
                    "response": 'true'
                }
            ))

        elif data['type'] == 'message':
            time.sleep(1)
            count_message += 1

            symbol = data['subject']
            price_bids_g = data['data']['bestBid']
            qty_bids_g = data['data']['bestBidSize']
            price_asks_g = data['data']['bestAsk']
            qty_asks_g = data['data']['bestAskSize']

            chars = '.-!'
            symbol = symbol.translate(str.maketrans('', '', chars))
            try:
                price_bids_g_ = 'price_bids_g_' + symbol
                globals()[price_bids_g_] = price_bids_g

                qty_bids_g_ = 'qty_bids_g_' + symbol
                globals()[qty_bids_g_] = qty_bids_g

                price_asks_g_ = 'price_asks_g_' + symbol
                globals()[price_asks_g_] = price_asks_g

                qty_asks_g_ = 'qty_asks_g_' + symbol
                globals()[qty_asks_g_] = qty_asks_g

                # global price_bids_g_BNBUSDT
                # global qty_bids_g_BNBUSDT
                # global price_asks_g_BNBUSDT
                # global qty_asks_g_BNBUSDT

                #str_ = ''
                # a = ['price_bids_c_l_' + symbol]
                # f"price_bids_c_l_{symbol} = 123
                #print(price_bids_c_l_BTCUSDT)
            except:
                pass
            #test = 'sada'
            # name = "str_"
            # for n in range(5):
            #     exec(name + "%s = %d" % (n, n))
            # print(name)


            # 'price_bids_c_l_'[symbol] = 0
            # print()


            # global price_bids_g_BNBUSDT
            #
            # price_bids_g_BNBUSDT = Decimal(price_bids_c_l_BNBUSDT)
            #print(symbol)
            # print(count_message )
        else:
            print(data)
    else:
        print(data)

    if (pingTime+pingInterval) <= round(time.time()):
        ws.send(json.dumps(
            {
                "id":id_channel,
                "type":"ping"
            }
        ))
        #print(f'За {round(time.time()-start_time,2)} секунд записали {count_message} сообщений')

        pingTime = round(time.time())  # Запомним новое время для сообщения
        count_message = 0  # Обнуляем счетчик сообщений
        start_time = time.time()  # Сбросим счетчик времени


# При закрытии соединения к бирже
def on_close(ws):
    print('### closed ###')

# При ошибки в соединение
def on_error(ws, message):
    print(message)

# Получаем настройки от сервера.

def loadSetting():
    return requests.post('https://api.kucoin.com/api/v1/bullet-public').json()


settings = loadSetting()

pingInterval = round((settings['data']['instanceServers'][0]['pingInterval'] / 1000) / 2) - 1

pingTime = round(time.time())

id_channel = ''

ws = websocket.WebSocketApp(f"{settings['data']['instanceServers'][0]['endpoint']}?token={settings['data']['token']}",
                            on_message=get_ticker_all,
                            on_close=on_close,
                            on_error=on_error
                            )
ws.run_forever()
