import json
import os
import threading
import time

from kucoin.client import Client
from threading import *
import websocket
import comm as a

x = a.check_commissions('a_1', 'a_2')
print(x)
api_key = '63cc9d027675230001bba629'
api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7'

client = Client(api_key, api_secret, passphrase='4796212')


#
# def test():
#     while True:
#         a = client.get_ticker(
#             symbol='ALGO-USDT'
#         )
#         return a
#         #print('111111111111', a)
# Thread(target=test).start()
#     # ws = websocket.WebSocketApp(a, on_message=on_message_USDTUSDC)
#     # ws.run_forever()
# a = []
# def test_test():
#     #while True:
#     data = client.get_(
#         # symbol='KCS-USDT'
#     )
    # a.append(data)
    #symbol_c_l_ATOMUSDT = 'ATOMUSDT'
    # price_bids_c_l_ATOMUSDT = data['bestBid']
    # qty_bids_c_l_ATOMUSDT = data['bestBidSize']
    # price_asks_c_l_ATOMUSDT = data['bestAsk']
    # qty_asks_c_l_ATOMUSDT = data['bestAskSize']
    #return a
# {'orderId': '63d36bcbbaa4cf00014c2c61'}
# <class 'dict'> 63d372a928a9ee000154c41d
# {'currentPage': 1, 'pageSize': 50, 'totalNum': 0, 'totalPage': 0, 'items': []}

# x = time.time()
# order = client.create_market_order(
#     symbol='ADA-USDT',
#     side='sell',
#     size='1'
# )
# # test = {'orderId': '63d36bcbbaa4cf00014c2c61'}
#
#
# #print(test['orderId'])
# # print(test['orderId'])
#
# ooo = order['orderId']
# time.sleep()
# ddd = 0
# c = time.time()
# while ddd == 0:
#
#     fills = client.get_fills(
#         order_id=ooo
#     )
#     ddd = fills['totalNum']
# cc = time.time()
# itog = fills['items'][0]['funds']
# xx = time.time()
# ccc = cc - c
# xxx = xx - x
# print(fills)
# print(xxx)
# print(ccc)

#itog = fills['items'][0]['funds']

# fills = client.get_fills(
#         order_id='63d36bcbbaa4cf00014c2c61'
#     )
#
# print(fills['totalNum'])


#
# xx = time.time()
# xxx = xx - x
# print(xxx)
# print(itog)
# print(order)
# order = client.create_market_order(
#     symbol='ADA-USDT',
#     side='sell',
#     size='1'
# )
# print(order)
# print(type(order))

# for i in a:
#     print(i)
#print(test(), test_test())
# for i in a:
#     count += 1
#     print(i)
# def loop_USDTUSDC():
#
# 	socket1 = f'wss://stream.binance.com:9443/ws/usdtusdc@bookTicker'
# 	ws = websocket.WebSocketApp(socket1, on_message=on_message_USDTUSDC)
# 	ws.run_forever()
# b = {'currentPage': 1, 'pageSize': 50, 'totalNum': 3, 'totalPage': 1, 'items': [{'symbol': 'NIM-ETH', 'tradeId': '2328942849562631', 'orderId': '63d3b44817f8760001a4e677', 'counterOrderId': '63d3b4440f2fb200018049f6', 'side': 'buy', 'liquidity': 'taker', 'forceTaker': False, 'price': '0.00000094', 'size': '84.824', 'funds': '0.00007973456', 'fee': '0.00000007973456', 'feeRate': '0.001', 'feeCurrency': 'ETH', 'stop': '', 'tradeType': 'TRADE', 'type': 'market', 'createdAt': 1674818632000},{'symbol': 'NIM-ETH', 'tradeId': '2328942849562628', 'orderId': '63d3b44817f8760001a4e677', 'counterOrderId': '63d3b4449ce239000136132b', 'side': 'buy', 'liquidity': 'taker', 'forceTaker': False, 'price': '0.00000094', 'size': '168.701', 'funds': '0.00015857894', 'fee': '0.00000015857894', 'feeRate': '0.001', 'feeCurrency': 'ETH', 'stop': '', 'tradeType': 'TRADE', 'type': 'market', 'createdAt': 1674818632000},{'symbol': 'NIM-ETH', 'tradeId': '2328942849562625', 'orderId': '63d3b44817f8760001a4e677', 'counterOrderId': '63d3b44440bae200010aad17', 'side': 'buy', 'liquidity': 'taker', 'forceTaker': False, 'price': '0.000000938', 'size': '285.149', 'funds': '0.000267469762', 'fee': '0.000000267469762', 'feeRate': '0.001', 'feeCurrency': 'ETH', 'stop': '', 'tradeType': 'TRADE', 'type': 'market', 'createdAt': 1674818632000}]}
# print(b['items'][0])
# print(b['items'][1])
# print(b['items'][2])

#Thread(target=loop_USDTUSDC).start()

# a = {'currentPage': 1, 'pageSize': 50, 'totalNum': 2, 'totalPage': 1, 'items': [{'symbol': 'ACQ-USDC', 'tradeId': '237993103460356', 'orderId': '63d3b444fbc32c0001ac02ed', 'counterOrderId': '63d3b43f9d799e00018523ce', 'side': 'sell', 'liquidity': 'taker', 'forceTaker': False, 'price': '0.0267', 'size': '29.6296', 'funds': '0.79111032', 'fee': '0.00158222064', 'feeRate': '0.002', 'feeCurrency': 'USDC', 'stop': '', 'tradeType': 'TRADE', 'type': 'market', 'createdAt': 1674818629000}, {'symbol': 'ACQ-USDC', 'tradeId': '237993103460353', 'orderId': '63d3b444fbc32c0001ac02ed', 'counterOrderId': '63d3b441f109f00001a54cd5', 'side': 'sell', 'liquidity': 'taker', 'forceTaker': False, 'price': '0.0269', 'size': '0.0001', 'funds': '0.00000269', 'fee': '0.00000000538', 'feeRate': '0.002', 'feeCurrency': 'USDC', 'stop': '', 'tradeType': 'TRADE', 'type': 'market', 'createdAt': 1674818629000}]}

# for i in a:
# print(a['items'][0])
# print(a['items'][1])
# x = time.time()
# deposits = client.get_accounts(
#     currency='USDT'
# )
# xx = time.time()
# xxx = xx - x
# print(xxx)
# print(deposits[0])
# print(deposits[0]['balance'])
# x = 0
# y = 1
#
# while x < y:
#     time.sleep(1)
#     print('test')
