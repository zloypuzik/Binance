import time

from Arbitrazj_mezh_birzh import Classes

##################################################################
# API Binance
##################################################################


client = Classes.apiBinance()

##################################################################
# Открытие файла со всеми символами
##################################################################


exchange = "Binance"
getAllSymbolsBinance = Classes.def_FileOpenGetAllSymbols(exchange)

##################################################################
# Запрос цен и объемов по всем валютам
##################################################################


def def_getOrderbookBinance():
    return client.get_orderbook_ticker()

##################################################################
# Добавляем в переменную 'listAllSymbolsBinance' список всех валют, которые сейчас торгуются
##################################################################


listAllSymbolsBinance = []

for gei_fileGetAllSymbolsBinance in getAllSymbolsBinance:
    listAllSymbolsBinance.append(gei_fileGetAllSymbolsBinance['symbol'])

##################################################################
# Основная функция для добавления цен и объемов в БД
##################################################################


Classes.def_ClearTableMysql(f"{exchange}_get_orderbook_ticker")  # Очищение таблицы "binance_get_orderbook_ticker"


def runMainProgram():

    startTime = time.time()  # Время начала работы функции "run_sql"
    requestPricesBinance = []  # Запрос списка цен и объёмов по всем парам с биржи
    ordersBook = []  # Книга всех цен биржи

    for i_requestPricesBinance in def_getOrderbookBinance():
        requestPricesBinance.append(i_requestPricesBinance)

    ##################################################################

    for i_listAllSymbolsBinance in listAllSymbolsBinance:  # Извлекаем символы
        for i_requestPricesBinance in requestPricesBinance:  # Извлекаем текущие цены и объёмы

            if i_listAllSymbolsBinance == i_requestPricesBinance['symbol']:

                symbol = i_requestPricesBinance['symbol']
                bidPrice = i_requestPricesBinance['bidPrice']
                bidQty = i_requestPricesBinance['bidQty']
                askPrice = i_requestPricesBinance['askPrice']
                askQty = i_requestPricesBinance['askQty']

                ordersBook.append([symbol, bidPrice, bidQty, askPrice, askQty])

                break

    Classes.UpdatingPricesTableMysql(exchange, ordersBook, startTime)


while True:
    runMainProgram()
