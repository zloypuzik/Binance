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
binance_get_all_symboll = '../Binance/Binance_get_all_symboll.json'


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
    symbol = symbol_l + '@depth5@1000ms'
    a = streams.append(symbol)
    count += 1
    if count == 200:
        break

# for i in streams:
# print(streams)
streams2 = [
    'btcusdt@depth5@1000ms'
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
            symbol_stream = data['stream']

            symbol_coin = str(symbol_stream.split('@')[0])
            bidPrice = data['data']['bids'][0][0]
            bidQty = data['data']['bids'][0][1]
            askPrice = data['data']['asks'][0][0]
            askQty = data['data']['asks'][0][1]
            print(symbol, bidPrice, bidQty, askPrice, askQty)

            # try:
            #     with connect_mysql.cursor() as cursor:
            #         select_symbol_query = F"SELECT symbol FROM binance_get_orderbook_ticker WHERE symbol = '{symbol_coin}'"
            #         cursor.execute(select_symbol_query)
            #         # print(cursor.fetchone())
            #         # a = cursorr.fetchone()
            #         if cursor.fetchone() is None:
            #             # with connect_mysql.cursor() as cursor:
            #                 # insert_orderbook_ticker = F"INSERT INTO binance_get_orderbook_ticker VALUES (NULL, ?, ?, ?, ?, ?)", (symbol, bidPrice, bidQty, askPrice, askQty)
            #             insert_orderbook_ticker = F"INSERT INTO binance_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol_coin}', '{bidPrice}', '{bidQty}', '{askPrice}', '{askQty}');"
            #             cursor.execute(insert_orderbook_ticker)
            #             connect_mysql.commit()
            #
            #         else:
            #             # print("2222222222222222222222")
            #             update_orderbook_ticker = F"UPDATE binance_get_orderbook_ticker SET bidPrice = '{bidPrice}', bidQty = '{bidQty}', askPrice = '{askPrice}', askQty = '{askQty}' WHERE symbol = '{symbol_coin}';"
            #             cursor.execute(update_orderbook_ticker)
            #             connect_mysql.commit()
            #
            # except Exception as ex:
            #     print("error")
            #     print(ex)


    # connect_mysql.close()
    # Timer(10, to_streams).start()
            # with connect_mysql.cursor() as cursor:
            #     select_symbol_query = F"SELECT * FROM binance_get_orderbook_ticker WHERE symbol = 'btcusdt'"
            #     cursor.execute(select_symbol_query)
            #     print(cursor.fetchone())
            # sql.execute(F"SELECT symbol FROM binance_get_orderbook_ticker WHERE symbol = '{symbol}'")
            #
            # if sql.fetchone() is None:
            #
            #     sql.execute(F"INSERT INTO binance_get_orderbook_ticker VALUES (NULL, ?, ?, ?, ?, ?)", (symbol, bidPrice, bidQty, askPrice, askQty))
            #
            #     db.commit()
            #
            # else:
            #
            #     sql.execute(F"UPDATE binance_get_orderbook_ticker SET bidPrice = {bidPrice}, bidQty = {bidQty}, askPrice = {askPrice}, askQty = {askQty} WHERE symbol = '{symbol}'")
            #     db.commit()
#
asyncio.run(to_streams())
