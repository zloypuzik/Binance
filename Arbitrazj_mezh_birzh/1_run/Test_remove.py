from Arbitrazj_mezh_birzh import Classes
#
# # for i in  Classes.def_FileOpenNetworkInfo('Kucoin'):
# #     if i['networkList'][0]['withdrawFee'] == 0:
# #         print(i)
# #     # print(i['networkList'][0]['withdrawFee'])
#
# exchange = 'Binance'
# symbol = "BTCUSDT"
# # askPrice = 'askPrice'
# askPrice = 'bidPrice'
# #
# a = Classes.def_requestPriceTableMysql(symbol, exchange, askPrice)
# #
# print(a)

# bid_or_ask = 'bidPrice'
# a = 'AVAUSDT'
# b = 'Kucoin'
# exchange_first_price_ask = Classes.def_requestPriceTableMysql(a, b, bid_or_ask)
# print(exchange_first_price_ask)

a = "BTC"
b = "USDT"

c = a + '-' + b
print(c)

# a = Classes.def_connectingToMysql()

# def test(symbol, exchange):

 # Подключение к БД

# try:
#     connectingToMysql = Classes.def_connectingToMysql()
#     with connectingToMysql.cursor() as cursor:
#         requestMysqlSelectSymbols = F"SELECT askPrice FROM {exchange}_get_orderbook_ticker WHERE symbol = '{symbol}'"
#         # SELECT askPrice FROM Binance_get_orderbook_ticker WHERE symbol = 'BTCUSDT'
#         cursor.execute(requestMysqlSelectSymbols)
#         a = cursor.fetchone()
#         print(a)
#
# except Exception as ex:
#
#     cursor.close()
#
#     print("error")
#     print(ex)



