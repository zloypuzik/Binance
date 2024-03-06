import json
from kucoin.client import Client
import pymysql
import time
from datetime import datetime

kucoin_coin_info = '../Kucoin/symbol_list.json'

##################################################################
# API Kucoin
##################################################################


api_key = '63cc9d027675230001bba629'
api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7'

client = Client(api_key, api_secret, passphrase='4796212')

##################################################################
# Открытие файла со всеми символами Kucoin
##################################################################


def f_file_kucoin_coin_info():
    with open(kucoin_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a

##################################################################
# Запрос цен и объемов по всем валютам Binance
##################################################################


def f_get_orderbook_kucoin():
    kucoin_get_orderbook = client.get_ticker()
    orderbook_kucoin = []
    for i in kucoin_get_orderbook['ticker']:
        orderbook_kucoin.append(i)
        # print(i)
    return orderbook_kucoin

##################################################################
# Добавляем в переменную 'symbol_binance' список всех валют, которые сейчас торгуются
##################################################################


symbol_trading_usdt = []

for get_all_symbol_kucoin in f_file_kucoin_coin_info():
    if get_all_symbol_kucoin['baseCurrency'] == 'USDT' or get_all_symbol_kucoin['quoteCurrency'] == 'USDT':
        symbol_trading_usdt.append(get_all_symbol_kucoin['symbol'])

##################################################################
# Основная функция для добавления цен и объемов в БД
##################################################################


def run_sql():

    start_time = time.time()  # Время начала работы функции
    count_update = 0  # Счётчик обновлений записей в БД

    # orderbook_kucoin = []
    # for i in f_get_orderbook_kucoin():
    #     orderbook_kucoin.append(i)

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
        # print('Подключение к SQL: прошло успешно.')

    except Exception as ex:
        print('Подключение к SQL: произошла ошибка !!!')
        print(ex)

    ##################################################################

    # orderbook_kucoin = f_get_orderbook_kucoin()
    a = f_get_orderbook_kucoin()
    for t in symbol_trading_usdt:  # Извлекаем символы
        for tt in a:  # Извлекаем текущие цены и объёмы
            # print(tt)
            if t == tt['symbol']:
                #
                symbol_l = tt['symbol']
                chars = '.-!'  # Вырезает '-' из symbol
                symbol = symbol_l.translate(str.maketrans('', '', chars))
                # symbol = tt['symbol']
                bidPrice = tt['buy']
                bidQty = 0
                askPrice = tt['sell']
                askQty = 0
                #
                try:
                    with connect_mysql.cursor() as cursor:

                        select_symbol_query = F"SELECT symbol FROM kucoin_get_orderbook_ticker WHERE symbol = '{symbol}'"
                        cursor.execute(select_symbol_query)

                        if cursor.fetchone() is None:
                            insert_orderbook_ticker = F"INSERT INTO kucoin_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol}', '{bidPrice}', NULL, '{askPrice}', NULL);"
                            cursor.execute(insert_orderbook_ticker)
                            # connect_mysql.commit()

                        else:
                            update_orderbook_ticker = F"UPDATE kucoin_get_orderbook_ticker SET bidPrice = '{bidPrice}', bidQty = '{bidQty}', askPrice = '{askPrice}', askQty = '{askQty}' WHERE symbol = '{symbol}';"
                            count_update += 1
                            cursor.execute(update_orderbook_ticker)

                            # connect_mysql.commit()

                except Exception as ex:

                    print("error")
                    print(ex)

                break

    connect_mysql.commit()  # Записываем результаты в БД

    connect_mysql.close()  # Закрываем соединение sql

    now = datetime.now()  # Текущая дата/время
    current_time = now.strftime("%H:%M:%S")  # Создаём строку, представляющую дату/время

    print('______________________________________________________________')
    print(current_time, 'Обновлено:', count_update, 'записей в БД.')
    print(current_time, 'Затрачено на обработку', (time.time() - start_time), 'секунд.')


while True:
    run_sql()

