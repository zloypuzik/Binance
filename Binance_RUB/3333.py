symbol_c_g_BTCUSDT = 'BTCUSDT'
price_bids_c_g_BTCUSDT = float(0.0)
qty_bids_c_g_BTCUSDT = float(0.0)
price_asks_c_g_BTCUSDT = float(0.0)
qty_asks_c_g_BTCUSDT = float(0.0)
stepSize_BTCUSDT = '0.00001000'

def on_message_BTCUSDT(ws, message):
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
    price_bids_c_g_BTCUSDT = price_bids_c_l_BTCUSDT
    qty_bids_c_g_BTCUSDT = qty_bids_c_l_BTCUSDT
    price_asks_c_g_BTCUSDT = price_asks_c_l_BTCUSDT
    qty_asks_c_g_BTCUSDT = qty_asks_c_l_BTCUSDT


def loop_BTCUSDT():
    socket1 = f'wss://stream.binance.com:9443/ws/btcusdt@depth5@100ms'
    ws = websocket.WebSocketApp(socket1, on_message=on_message_BTCUSDT)
    ws.run_forever()


Thread(target=loop_BTCUSDT).start()