import json
import time

from Arbitrazj_mezh_birzh import Classes


allTest = []
count = 0
# Kucoin Binance Mexc
i_exchange_first = 'Mexc'
i_exchange_second = 'Binance'
mainCurrency = ['USDT']
globalProfitList10mins = []

while True:

    temporaryProfitList10mins = []  # Временный список с прибыльными связками

    for i_def_FileOpenGetAllSymbols_first in Classes.def_FileOpenGetAllSymbols(i_exchange_first):
        symbol_i_exchange_first = i_def_FileOpenGetAllSymbols_first['immutableNameBaseAsset'] + i_def_FileOpenGetAllSymbols_first['immutableNameQuoteAsset']
        symbol_i_exchange_first_original = i_def_FileOpenGetAllSymbols_first['symbol']
        """Формирования символа на первой бирже"""

        for i_def_FileOpenGetAllSymbols_second in Classes.def_FileOpenGetAllSymbols(i_exchange_second):
            symbol_i_exchange_second = i_def_FileOpenGetAllSymbols_second['immutableNameBaseAsset'] + i_def_FileOpenGetAllSymbols_second['immutableNameQuoteAsset']
            symbol_i_exchange_second_original = i_def_FileOpenGetAllSymbols_second['symbol']
            """Формирование символа на второй бирже"""

            if symbol_i_exchange_first == symbol_i_exchange_second:
                """Проверка, что символ первой и второй биржи совпадают"""

                # if symbol_i_exchange_first not in allTest:  # Проверить зачем !!!!!!!!
                #     allTest.append(symbol_i_exchange_first)
                #     count += 1
                #     """Проверка, что символа нет в списке, если нет, то добавляем символ в список"""

                symbolNetworkSearch = None

                if i_def_FileOpenGetAllSymbols_first['immutableNameBaseAsset'] not in mainCurrency:
                    symbolNetworkSearch = i_def_FileOpenGetAllSymbols_first['immutableNameBaseAsset']
                    """Если символ не основная валюта то добавляем символ в переменную для поиска сетей"""

                elif i_def_FileOpenGetAllSymbols_first['immutableNameQuoteAsset'] not in mainCurrency:
                    symbolNetworkSearch = i_def_FileOpenGetAllSymbols_first['immutableNameQuoteAsset']
                    """Если символ не основная валюта то добавляем символ в переменную для поиска сетей"""

                for i_def_FileOpenNetworkInfo_first in Classes.def_FileOpenNetworkInfo(i_exchange_first):
                    """Цикл сетей blockchain первой биржи """

                    if i_def_FileOpenNetworkInfo_first['symbol'] == symbolNetworkSearch:
                        """Добавление символа из первой биржи в переменную"""

                        for i_def_FileOpenNetworkInfo_second in Classes.def_FileOpenNetworkInfo(i_exchange_second):
                            """Цикл сетей blockchain второй биржи """

                            if i_def_FileOpenNetworkInfo_second['symbol'] == symbolNetworkSearch:
                                """Добавление символа из второй биржи в переменную"""

                                index_network_exchange_first = len(i_def_FileOpenNetworkInfo_first['networkList'])
                                """Подсчет количества сетей для перевода у валюты на первой бирже"""
                                network_count_exchange_first = 0
                                """Счетчик количества валют первой биржи"""

                                while network_count_exchange_first < index_network_exchange_first:

                                    # print(i_def_FileOpenNetworkInfo_first['networkList'][network_count_exchange_first]['network'])
                                    network_first = i_def_FileOpenNetworkInfo_first['networkList'][network_count_exchange_first]['network']
                                    network_first_withdrawEnable = i_def_FileOpenNetworkInfo_first['networkList'][network_count_exchange_first]['withdrawEnable']
                                    network_first_withdrawFee = i_def_FileOpenNetworkInfo_first['networkList'][network_count_exchange_first]['withdrawFee']

                                    network_count_exchange_first += 1

                                    index_network_exchange_second = len(i_def_FileOpenNetworkInfo_second['networkList'])
                                    """Подсчет количества сетей для перевода у валюты на второй бирже"""
                                    network_count_exchange_second = 0
                                    """Счетчик количества валют второй биржи"""

                                    while network_count_exchange_second < index_network_exchange_second:

                                        network_second = i_def_FileOpenNetworkInfo_second['networkList'][network_count_exchange_second]['network']
                                        network_second_depositEnable = i_def_FileOpenNetworkInfo_second['networkList'][network_count_exchange_second]['depositEnable']

                                        network_count_exchange_second += 1

                                        if network_first == network_second:
                                            """Если сети ровны"""

                                            if network_first_withdrawEnable and network_second_depositEnable:

                                                bid = 'bidPrice'
                                                ask = 'askPrice'
                                                # print(symbol_i_exchange_first)
                                                exchange_first_price_ask = Classes.def_requestPriceTableMysql(symbol_i_exchange_first_original, i_exchange_first, ask)
                                                exchange_second_price_bid = Classes.def_requestPriceTableMysql(symbol_i_exchange_second_original, i_exchange_second, bid)

                                                profit = Classes.def_calculationArbitrationProfit(exchange_first_price_ask, exchange_second_price_bid, network_first_withdrawFee)

                                                if symbol_i_exchange_first != 'MCUSDT':


                                                    if profit > 1:

                                                        # print('#' * 79)
                                                        # print(f'Биржа покупки: "{i_exchange_first}" | биржа продажи: "{i_exchange_second}"')
                                                        # print('_' * 79)
                                                        # print(symbol_i_exchange_first, '|', 'сеть:', network_first, '|', 'комиссия:', network_first_withdrawFee, '|', 'прибыль:', profit)
                                                        # print('-' * 79)
                                                        # print("")



                                                        temporaryProfitList10mins.append(
                                                            {
                                                                'symbol': symbol_i_exchange_first,
                                                                'data':
                                                                    {
                                                                        'i_exchange_first': i_exchange_first,
                                                                        'i_exchange_second': i_exchange_second,
                                                                        'network_first': network_first,
                                                                        'network_first_withdrawFee': network_first_withdrawFee,
                                                                        'profit': profit,
                                                                        'startTime': time.monotonic()
                                                                    }
                                                            }
                                                        )


                        break

    if globalProfitList10mins == []:

        # globalProfitList10mins = []
        globalProfitList10mins.append(temporaryProfitList10mins)

    for i in temporaryProfitList10mins:

        test2 = False
        test4 = []

        for ii in globalProfitList10mins[0]:

            if i['symbol'] == ii['symbol']:
                test2 = True
                break

        a = temporaryProfitList10mins.index(i)



        test4.append({
            'a': a,
            'test2': test2
        })
        #print(test4[0]['test2'])
        # print(test4)
        # print(test4)
        #


        if test4[0]['test2'] == False:
            # print('_' * 66)
            # print('Добавлена монета:', i['symbol'])
            # print('_' * 66)


            globalProfitList10mins[0].append(i)

        elif test4[0]['test2'] == True:

            # print(globalProfitList10mins[0][a]['data']['profit'])
            # print(i['data']['profit'])
            startTime = i['data']['startTime']

            globalProfitList10mins[0][a] = 'asd'
            globalProfitList10mins[0][a] =  {
                                                                'symbol': i['symbol'],
                                                                'data':
                                                                    {
                                                                        'i_exchange_first': i['data']['i_exchange_first'],
                                                                        'i_exchange_second': i['data']['i_exchange_second'],
                                                                        'network_first': i['data']['network_first'],
                                                                        'network_first_withdrawFee': i['data']['network_first_withdrawFee'],
                                                                        'profit': i['data']['profit'],
                                                                        'startTime': startTime
                                                                    }
                                                            }

    for i in globalProfitList10mins[0]:

        test2 = False
        test4 = []

        for ii in temporaryProfitList10mins:

            if i['symbol'] == ii['symbol']:
                test2 = True
                break

        a = globalProfitList10mins[0].index(i)

        test4.append({
            'a': a,
            'test2': test2
        })
        # print(test4)
        # print(test4)
        #
        if test4[0]['test2'] == False:
            globalProfitList10mins[0].pop(test4[0]['a'])

    # print('#' * 79)
    # print('Количество монет:', len(globalProfitList10mins[0]))
    # print('#' * 79)

    # {'symbol': 'NAKAUSDT', 'data': {'i_exchange_first': 'Mexc', 'i_exchange_second': 'Kucoin', 'network_first': 'MATIC', 'network_first_withdrawFee': 1.6, 'profit': Decimal('27.269569442790208075176567'), 'time': 37858.484}}

    for i in globalProfitList10mins[0]:
        workingTime = time.monotonic() - i['data']['startTime']
        # print('#' * 79)
        # print(f'Биржа покупки:', i["data"]["i_exchange_first"], '|', 'биржа продажи:', i["data"]["i_exchange_second"])
        # print('_' * 79)
        # if workingTime > 600:
        print(i['symbol'], '|', 'сеть:', i["data"]['network_first'], '|', 'комиссия:', i["data"]['network_first_withdrawFee'], '|', 'прибыль:', i['data']['profit'], 'Время работы связки:', workingTime)
    print('-' * 79)
# print("")
    #global globalProfitList10mins
    # for i in globalProfitList10mins:
    #     if i['symbol'] != test:
    #         testList.pop(testList.index(i))
    # globalProfitList10mins = temporaryProfitList10mins
    # print(globalProfitList10mins)
                # """Buy symbol first exchange and sell symbol second exchange """


                        # print(i_def_FileOpenNetworkInfo_first['symbol'])


                        #
                        #     index_network_exchange_first = len(i_def_FileOpenNetworkInfo_first['networkList'])
                        #     network_count_exchange_first = 0
                        #     print(i_def_FileOpenNetworkInfo_first)
                            # while network_count_exchange_first < index_network_exchange_first:
                            #
                            #     index_network_exchange_second = len(i_def_FileOpenNetworkInfo_second['networkList'])
                            #     network_count_exchange_second = 0


                                #
                                # while network_count_exchange_second < index_network_exchange_second:
                                #
                                #     print(i_def_FileOpenNetworkInfo_first)

                        # index_network_exchange_first = len(i_def_FileOpenNetworkInfo_first['networkList'])
                        # index_network_exchange_second = len(i_def_FileOpenNetworkInfo_second['networkList'])
                        #
                        # list_network_exchange_first = []
                        # list_network_exchange_second = []
                        #
                        # network_count_exchange_first = 0
                        # network_count_exchange_second = 0
                        #
                        #
                        #
                        # while network_count_exchange_first < network_count_exchange_first:
                        #
                        #     network_exchange_first = i_def_FileOpenNetworkInfo_first
                        #     # kucoin_network = kucoin['networkList'][network_count_kucoin]['network']
                        #     # kucoin_withdrawEnable = kucoin['networkList'][network_count_kucoin]['withdrawEnable']
                        #     # kucoin_depositEnable = kucoin['networkList'][network_count_kucoin]['depositEnable']
                        #     # kucoin_withdrawFee = kucoin['networkList'][network_count_kucoin]['withdrawFee']
                        #     network_count_exchange_first += 1

                    # break


