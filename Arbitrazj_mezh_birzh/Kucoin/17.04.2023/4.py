import json
import requests
import time
import websocket

from threading import *
from decimal import Decimal
import pymysql

##################################################################
# Открытие файла со всеми символами
##################################################################


binance_get_all_symboll = '../Kucoin/symbol_list.json'


def f_file_binance_get_all_symboll():
    with open(binance_get_all_symboll) as file_data:
        data_a = json.load(file_data)

    return data_a

symbol_usdt = []

case_list = {}
count_test = 0


for i in f_file_binance_get_all_symboll():
    if count_test < 100:

        # if i['quoteCurrency'] == 'USDT':

        symbol_usdt.append(i['symbol'])
        count_test += 1
print(count_test)

a = {'testtest': f'{symbol_usdt}'}
b = a['testtest']
chars = '.\' []!' # Вырезает '-' из symbol
symbol2 = b.translate(str.maketrans('', '', chars))

print(symbol_usdt)
# print(symbol2)

symbol3 = 'AVA-USDT,ETH-USDT'
count_message = 0
start_time = time.time()

# def test():
#     try:
#         connect_mysql = pymysql.connect(
#             host='192.168.1.50',
#             port=3306,
#             user='test',
#             password='Zz_479621212',
#             database='arbitrazh_mezbirzh'
#         )
#         # print('Подключение к SQL: прошло успешно.')
#
#     except Exception as ex:
#         print('Подключение к SQL: произошла ошибка !!!')
#         print(ex)
#     # pass
##################################################################
# Подключение к серверу SQL
##################################################################



connect_mysql = pymysql.connect(
    host='192.168.1.50',
    port=3306,
    user='test',
    password='Zz_479621212',
    database='arbitrazh_mezbirzh'
)

cursor = connect_mysql.cursor()

# for ii in symbol_usdt:

# print(symbol_usdt)
#
# j = {'test': symbol_usdt}
# print(j['test'])
# chars = '. !' # Вырезает '-' из symbol
# chars2 = '."!' # Вырезает '-' из symbol
# symbol2 = j['test'].translate(str.maketrans('', '', chars))
# print(symbol2)

# def test():
#     # time.sleep(5)
#     a = 'sadasd'
#     return a
#     time.sleep(3)
#     cursor.execute(F"INSERT INTO kucoin_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('sadasd', 'sadasd', 'sadasd', 'sadasd', 'sadasd');")

def get_ticker_all(ws, message):

    global pingInterval, pingTime, id_channel, count_message, start_time
    data = json.loads(message)
    #################################################################
    #Подключение к серверу SQL
    #################################################################
    a = []




    if 'type' in data:
        if data['type'] == 'welcome':
            id_channel = data['id']
            ws.send(json.dumps(
                {
                    "id": data['id'],
                    "type": "subscribe",
                    # "topic": "/market/ticker:all",
                    "topic": f"/market/level2:{symbol2}",
                    "response": 'true'
                }
            ))

        elif data['type'] == 'message':
            # pass
            ##################################################################
            # Подключение к серверу SQL
            ##################################################################
            # try:
            #     connect_mysql = pymysql.connect(
            #         host='192.168.1.50',
            #         port=3306,
            #         user='test',
            #         password='Zz_479621212',
            #         database='arbitrazh_mezbirzh'
            #     )
            #     # print('Подключение к SQL: прошло успешно.')
            #
            # except Exception as ex:
            #     print('Подключение к SQL: произошла ошибка !!!')
            #     print(ex)
            #
            # connect_mysql.close()
            # # time.sleep(1)
            # for ii in symbol_usdt:
            #     if ii == data['subject']:

            count_message += 1
            # print(data)
                    # print(data['subject'])
                    #
            gg = data['subject']
                    # ggprint()
            symbol = (data['data']['symbol'])
            #print(data['data']['symbol'])
                    # bidPrice = data['data']['bestBid']
                    # bidQty = data['data']['bestBidSize']
                    # askPrice = data['data']['bestAsk']
                    # askQty = data['data']['bestAskSize']
                    # a = test()
                    # print("################")
                    # print(symbol)
                    # cursor.execute(F"INSERT INTO kucoin_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol}', '{bidPrice}', '{bidQty}', '{askPrice}', '{askQty}');")
                    #a.append(symbol)
            try:
                cursor.execute(F"SELECT symbol FROM kucoin_get_orderbook_ticker WHERE symbol = '{symbol}'")
            except:
                pass

            cursor.execute(F"SELECT symbol FROM kucoin_get_orderbook_ticker WHERE symbol = '{symbol}'")
            if cursor.fetchone() is None:
                # print('2222222')
                cursor.execute(F"INSERT INTO kucoin_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol}', '{symbol}', '{symbol}', '{symbol}', '{symbol}');")
                    # try:
                    #     with connect_mysql.cursor() as cursor:
                    #
                    #         select_symbol_query = F"SELECT symbol FROM kucoin_get_orderbook_ticker WHERE symbol = '{symbol}'"
                    #         cursor.execute(select_symbol_query)
                    #
                    #         if cursor.fetchone() is None:
                    #             insert_orderbook_ticker = F"INSERT INTO kucoin_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol}', '{bidPrice}', '{bidQty}', '{askPrice}', '{askQty}');"
                    #             cursor.execute(insert_orderbook_ticker)
                    #             # connect_mysql.commit()
                    #
                    #         else:
                    #             update_orderbook_ticker = F"UPDATE kucoin_get_orderbook_ticker SET bidPrice = '{bidPrice}', bidQty = '{bidQty}', askPrice = '{askPrice}', askQty = '{askQty}' WHERE symbol = '{symbol}';"
                    #             cursor.execute(update_orderbook_ticker)
                    #             # connect_mysql.commit()
                    #
                    # except Exception as ex:
                    #
                    #     print("error")
                    #     print(ex)

                    # chars = '.-!' # Вырезает '-' из symbol
                    # symbol2 = symbol.translate(str.maketrans('', '', chars))
                    # break

        else:
            print(data)
    else:
        print(data)

    # connect_mysql.commit()  # Записываем результаты в БД
    #
    # connect_mysql.close()  # Закрываем соединение sql

    if (pingTime+pingInterval) <= round(time.time()):
        ws.send(json.dumps(
            {
                "id": id_channel,
                "type": "ping"
            }
        ))
        print(f'За {round(time.time()-start_time,2)} секунд записали {count_message} сообщений')

        pingTime = round(time.time())  # Запомним новое время для сообщения
        count_message = 0  # Обнуляем счетчик сообщений
        start_time = time.time()  # Сбросим счетчик времени

    connect_mysql.commit()
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
