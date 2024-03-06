import time

from Arbitrazj_mezh_birzh import Classes

##################################################################
# Открытие файла со всеми символами
##################################################################


exchange = "Kucoin"
getAllSymbols = Classes.def_FileOpenGetAllSymbols(exchange)

##################################################################
# API Binance
##################################################################


client = Classes.apiKucoin()

##################################################################
# Запрос цен и объемов по всем валютам
##################################################################


def def_getOrderbook():

    listPriceQty = []

    for i_kucoin_get_orderbooks in client.get_ticker()['ticker']:
        if i_kucoin_get_orderbooks['symbol'] in listAllSymbols:

            listPriceQty.append({
                'symbol': i_kucoin_get_orderbooks['symbol'],
                'bidPrice': i_kucoin_get_orderbooks['buy'],
                'bidQty': 0,
                'askPrice': i_kucoin_get_orderbooks['sell'],
                'askQty': 0
            })

    return listPriceQty

##################################################################
# Добавляем в переменную 'listAllSymbolsBinance' список всех валют, которые сейчас торгуются
##################################################################


listAllSymbols = []

for gei_fileGetAllSymbols in getAllSymbols:
    listAllSymbols.append(gei_fileGetAllSymbols['symbol'])


##################################################################
# Основная функция для добавления цен и объемов в БД
##################################################################


Classes.def_ClearTableMysql(f"{exchange}_get_orderbook_ticker")  # Очищение таблицы "binance_get_orderbook_ticker"


def runMainProgram():

    startTime = time.time()  # Время начала работы функции "run_sql"
    requestPrices = []  # Запрос списка цен и объёмов по всем парам с биржи
    ordersBook = []  # Книга всех цен биржи

    for i_requestPrices in def_getOrderbook():
        requestPrices.append(i_requestPrices)

    ##################################################################

    for i_listAllSymbols in listAllSymbols:  # Извлекаем символы
        for i_requestPrices in requestPrices:  # Извлекаем текущие цены и объёмы

            if i_listAllSymbols == i_requestPrices['symbol']:

                symbol = i_requestPrices['symbol']
                bidPrice = i_requestPrices['bidPrice']
                bidQty = i_requestPrices['bidQty']
                askPrice = i_requestPrices['askPrice']
                askQty = i_requestPrices['askQty']

                ordersBook.append([symbol, bidPrice, bidQty, askPrice, askQty])

                break

    Classes.UpdatingPricesTableMysql(exchange, ordersBook, startTime)


while True:
    runMainProgram()