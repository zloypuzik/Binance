# import requests
# import websocket
# import json
#
# def on_message(_wsa, data):
#     print(data)
#
# def run():
#
#     print('asdasdasdasd')
#     #symbol = 'btcusdt'
#     #limit = 1
#     #stream_name = f'SPOT'
#     #stream_name = f'{symbol}@depth5@100ms'
#     #wss = 'wss://stream.binance.com:9443/ws/%s' % stream_name
#     wss = 'wss://ws.okx.com:8443/ws/api/v5/public/opt-summary?uly=BTC-USD'
#     wsa = websocket.WebSocketApp(wss, on_message=on_message)
#     #wsd = websocket.W
#     wsa.run_forever()
#
# if __name__ == '__main__':
#     run()
#
# gjQDijheC4HPn3PA1n
# MfGbarybWCPhQ4VRrka1bIAsHoUK8svQIFZH
import bybit
#from pybit import spot

# client = bybit.bybit(
#     test=False,
#     api_key='gjQDijheC4HPn3PA1n',
#     api_secret='MfGbarybWCPhQ4VRrka1bIAsHoUK8svQIFZH'
# )
import json
from pybit import spot
session_unauth = spot.HTTP(
    endpoint="https://api.bybit.com"
)
info = (session_unauth.query_symbol())
#key_info = info[]
#print(info)
all_symbol_info = []
for i in (info['result']):
    all_symbol_info.append(i)
    print(i)
# print(all_symbol_info)
#
# for ii in all_symbol_info:
#     get_symbol = ii['symbol']
#     get_all_info_symbol = client.get_symbol_info(get_symbol)
#     time.sleep(0.2)
#     status = get_all_info_symbol['status']
#     if status == 'TRADING':
#         aa.append(get_all_info_symbol)

with open('step_1_pairs_trade.json', 'w') as file1:
    json.dump(all_symbol_info, file1, indent=2)

# for i in info:
#      print(i['result'][0])
# aa = []
#
# for i in tickers:
#     get_symbol = i['symbol']
#     get_all_info_symbol = client.get_symbol_info(get_symbol)
#     time.sleep(0.2)
#     status = get_all_info_symbol['status']
#     if status == 'TRADING':
#         aa.append(get_all_info_symbol)
#
# with open('step_1_pairs_trade.json', 'w') as file1:
#     json.dump(aa, file1, indent=2)
# info = client.Market.Market_symbolInfo().result()
# key_info = info[0]['result']
# print(key_info)
#
# info2 = client.



