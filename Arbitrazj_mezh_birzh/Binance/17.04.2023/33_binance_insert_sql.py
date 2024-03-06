import json
from binance.client import Client
import pymysql
import time
from datetime import datetime

from typing import Literal
from typing import NamedTuple  # Именованный кортеж


# def test() -> dict[Literal["chest"] |Literal["chest2"], int]:
#
#     return {"chest": 3, "chest2": 3, "chest3": 3, "chest4": 3, "b": 5}
#
#
# dfgdf = test()
# print(dfgdf["chest"])

##################################################################
# API Binance
##################################################################


apiKey = "A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG"
secretApiKey = "zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA"

client = Client(
    apiKey,
    secretApiKey
)

##################################################################
# Открытие файла со всеми символами
##################################################################


getAllSymbolsBinance = '../Binance/Binance_AllPairsTradingInf.json'


def def_filegetAllSymbolsBinance():
    with open(getAllSymbolsBinance) as dataFromFile:
        data = json.load(dataFromFile)

    return data

##################################################################
# Запрос цен и объемов по всем валютам Binance
##################################################################


def def_getOrderbookBinance():
    return client.get_orderbook_ticker()

##################################################################
# Добавляем в переменную 'listAllSymbolsBinance' список всех валют, которые сейчас торгуются
##################################################################


listAllSymbolsBinance = []

for gei_fileGetAllSymbolsBinance in def_filegetAllSymbolsBinance():
    listAllSymbolsBinance.append(gei_fileGetAllSymbolsBinance['symbol'])

###########################################################
# Подключение к MySQL
###########################################################


def def_connectingToMysql():
    try:
        connectingToMySQL = pymysql.connect(
            host='192.168.1.50',
            port=3306,
            user='test',
            password='Zz_479621212',
            database='arbitrazh_mezbirzh'
        )

        return connectingToMySQL
        # print('Подключение к SQL: прошло успешно.')

    except Exception as exception:
        print('Подключение к SQL: произошла ошибка !!!')
        print(exception)

##################################################################
# Очищение таблицы "binance_get_orderbook_ticker"
##################################################################


def defClearTableToMysql(table):

    defConnectingToMysql = def_connectingToMysql()

    try:
        with defConnectingToMysql.cursor() as cursorClearingTable:

            requestMysqlSelectSymbols = F"TRUNCATE TABLE {table};"
            cursorClearingTable.execute(requestMysqlSelectSymbols)

            defConnectingToMysql.commit()  # Записываем результаты в БД
            defConnectingToMysql.close()  # Закрываем соединение sql

    except Exception as ex:

        defConnectingToMysql.close()

        print("error")
        print(ex)


defClearTableToMysql("binance_get_orderbook_ticker")

##################################################################
# Основная функция для добавления цен и объемов в БД
##################################################################


def runMainProgram():

    startTime = time.time()  # Время начала работы функции "run_sql"
    countUpdateSQL = int(0)  # Счётчик обновлений записей в БД

    # Запрос списка цен и объёмов по всем парам с биржы
    requestPricesBinance = []

    for i_requestPricesBinance in def_getOrderbookBinance():
        requestPricesBinance.append(i_requestPricesBinance)

    ##################################################################
    # Подключение к серверу БД
    ##################################################################

    defConnectingToMysql = def_connectingToMysql()

    ##################################################################

    for i_listAllSymbolsBinance in listAllSymbolsBinance:  # Извлекаем символы
        for i_requestPricesBinance in requestPricesBinance:  # Извлекаем текущие цены и объёмы

            if i_listAllSymbolsBinance == i_requestPricesBinance['symbol']:

                symbol = i_requestPricesBinance['symbol']
                bidPrice = i_requestPricesBinance['bidPrice']
                bidQty = i_requestPricesBinance['bidQty']
                askPrice = i_requestPricesBinance['askPrice']
                askQty = i_requestPricesBinance['askQty']

                try:
                    with defConnectingToMysql.cursor() as cursor:

                        requestMysqlSelectSymbols = F"SELECT symbol FROM binance_get_orderbook_ticker WHERE symbol = '{symbol}'"
                        cursor.execute(requestMysqlSelectSymbols)

                        if cursor.fetchone() is None:
                            requestMysqlInsertTable = F"INSERT INTO binance_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol}', '{bidPrice}', '{bidQty}', '{askPrice}', '{askQty}');"
                            cursor.execute(requestMysqlInsertTable)
                            # connectingToMySQL.commit()

                        else:
                            requestMysqlUpdateTable = F"UPDATE binance_get_orderbook_ticker SET bidPrice = '{bidPrice}', bidQty = '{bidQty}', askPrice = '{askPrice}', askQty = '{askQty}' WHERE symbol = '{symbol}';"
                            countUpdateSQL += 1
                            cursor.execute(requestMysqlUpdateTable)
                            # connectingToMySQL.commit()

                except Exception as ex:

                    defConnectingToMysql.close()

                    print("error")
                    print(ex)

                break

    defConnectingToMysql.commit()  # Записываем результаты в БД

    defConnectingToMysql.close()  # Закрываем соединение sql

    datetimeNow = datetime.now()  # Текущая дата/время
    datetimeNow = datetimeNow.strftime("%H:%M:%S")  # Создаём строку, представляющую дату/время

    endTime = (time.time() - startTime)  # Время окончания работы основной функции "run_sql"

    print('______________________________________________________________')
    print(datetimeNow, 'Обновлено:', countUpdateSQL, 'записей в БД.')
    print(datetimeNow, 'Затрачено на обработку', endTime, 'секунд.')


while True:
    runMainProgram()
