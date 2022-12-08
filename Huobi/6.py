import time
import json
import websocket
import gzip
from threading import *

symbol_c_g_BTCUSDT = 'BTCUSDT'
price_bids_c_g_BTCUSDT = float(0.0)
qty_bids_c_g_BTCUSDT = float(0.0)
price_asks_c_g_BTCUSDT = float(0.0)
qty_asks_c_g_BTCUSDT = float(0.0)

# При получении сообщения
def on_message_BTCUSDT(ws, message):

    # Распакуем сообщение из архива и выгрузим его в массив.
    data = json.loads(gzip.decompress(message))
    #print(data)


    if 'ping' in data:
        # Отправить pong
        ws.send(json.dumps({
            "pong": data['ping']
        }))
    else:
        price_bids_c_l_BTCUSDT = data['tick']['bid']
        qty_bids_c_l_BTCUSDT = data['tick']['bidSize']
        price_asks_c_l_BTCUSDT = data['tick']['ask']
        qty_asks_c_l_BTCUSDT = data['tick']['askSize']
        print(price_bids_c_l_BTCUSDT, qty_bids_c_l_BTCUSDT, price_asks_c_l_BTCUSDT, qty_asks_c_l_BTCUSDT)

        global symbol_c_g_BTCUSDT
        global price_bids_c_g_BTCUSDT
        global qty_bids_c_g_BTCUSDT
        global price_asks_c_g_BTCUSDT
        global qty_asks_c_g_BTCUSDT

        #symbol_c_g_BTCUSDT = symbol_c_l_BTCUSDT
        price_bids_c_g_BTCUSDT = price_bids_c_l_BTCUSDT
        qty_bids_c_g_BTCUSDT = qty_bids_c_l_BTCUSDT
        price_asks_c_g_BTCUSDT = price_asks_c_l_BTCUSDT
        qty_asks_c_g_BTCUSDT = qty_asks_c_l_BTCUSDT

    # При закрытии подключения к бирже
def on_close_BTCUSDT(ws):
    print("### closed ###")

def on_error_BTCUSDT(ws, message):
    print(message)

# При открытии подключения
def on_open_BTCUSDT(ws):
    ws.send(json.dumps({"sub": f"market.avaxusdt.ticker"}))

def loop_BTCUSDT():
    ws = websocket.WebSocketApp("wss://api.huobi.pro/ws",
                                on_message=on_message_BTCUSDT,
                                on_close=on_close_BTCUSDT,
                                on_error=on_error_BTCUSDT)
    ws.on_open = on_open_BTCUSDT
    ws.run_forever()  # Set dispatcher to automatic reconnection
Thread(target=loop_BTCUSDT).start()