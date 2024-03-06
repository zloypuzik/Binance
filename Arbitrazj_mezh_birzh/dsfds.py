from threading import Timer
import asyncio
import websockets
import json
import pymysql
import time

##################################################################
# Подключение к серверу SQL
##################################################################

try:
    connect_mysql = pymysql.connect(
        host='192.168.1.50',
        port=3306,
        user='test',
        password='Zz_479621212',
        database='arbitrazh_mezbirzh'
    )
    print('Подключение к SQL: прошло успешно.')

except Exception as ex:
    print('Подключение к SQL: произошла ошибка.')
    print(ex)

##################################################################
# Открытие файла со всеми символами
##################################################################
binance_get_all_symboll = '../Arbitrazj_mezh_birzh/Binance/Binance_get_all_symboll.json'


def f_file_binance_get_all_symboll():
    with open(binance_get_all_symboll) as file_data:
        data_a = json.load(file_data)

    return data_a

##################################################################

streams = []

count = 0
for i in f_file_binance_get_all_symboll():
    symbol = i['symbol']
    symbol_l = symbol.lower()
    symbol = symbol_l + '@bookTicker'
    a = streams.append(symbol)
    count += 1
    if count == 100:
        break

# for i in streams:
# print(streams)
streams2 = [
    'btcusdt@bookTicker'
]


async def to_streams():
    url = 'wss://stream.binance.com:443/stream?streams='
    async with websockets.connect(url) as websocket:
        subscribe_request = {
            "method": "SUBSCRIBE",
            "params": streams,
            "id": 1
        }
        await websocket.send(json.dumps(subscribe_request))

        response = json.loads(await websocket.recv())
        print(response)

        async for message in websocket:
            data = json.loads(message)
            print(data)
            symbol_stream = data['stream']



#
asyncio.run(to_streams())
