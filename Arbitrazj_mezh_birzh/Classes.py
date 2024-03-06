import json
import pymysql
import time
from datetime import datetime
from decimal import Decimal

from binance.client import Client as binance_client
from kucoin.client import Client as kucoin_client
from MexcClient.client import MexcClient as maxc_client

########################################################################################################################
# Лучше покупать Mexc, Gate.io, BitGet второстепенные OKX, Huobi
########################################################################################################################


def main():
    pass


def def_test():
    print("None" * 10)
    print("None" * 10)
    print("None" * 10)
    print("None" * 10)
    print("None" * 10)

########################################################################################################################


def apiBinance():

    apiKey = str("TZSHjpkEt8fEuquAaKU7rZaYIjYa2oO7xuJyAnzMZjPjVXsi74jCo76hFEtrOFFD")
    secretApiKey = str("HyDXw0T6WFq55ryrdZabmWDKnyUjAJPBxzFr310o50lNTYOHC2pdnUIO64pMBGBk")

    client = binance_client(
        apiKey,
        secretApiKey
    )

    return client


def apiKucoin():
    api_key = '63cc9d027675230001bba629'
    api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7'

    client = kucoin_client(api_key, api_secret, passphrase='4796212')

    return client


def apiMexc():

    API_KEY = 'mx0vglBiQfiK5Hkutx'
    API_SECRET = '0e6b2c7ab0d741ac8f435bf56a0ab892'

    client = maxc_client(API_KEY, API_SECRET)

    return  client


########################################################################################################################


def def_allMainCurrency(exchange):
    """Основные валюты торговых бирж"""

    allMainCurrency = None

    match exchange:

        case "Binance":
            allMainCurrency = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR',
                               'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']
        case "Kucoin":
            allMainCurrency = ['BTC', 'KCS', 'ETH', 'TRX', 'DOGE', 'USDT', 'TUSD', 'DAI', 'USDC']

        case "Mexc":
            allMainCurrency = ['USDT', 'USDC', 'ETH', 'BTC', 'BUSD', 'TUSD']

    return allMainCurrency

########################################################################################################################


def def_FileOpenGetAllSymbols(exchange):

    GetAllSymbols = f'../{exchange}/{exchange}_AllPairsTradingInf.json'

    with open(GetAllSymbols) as fileData:
        data = json.load(fileData)

    return data


def def_FileOpenNetworkInfo(exchange):

    GetAllSymbols = f'../{exchange}/{exchange}_coin_network_info.json'

    with open(GetAllSymbols) as fileData:
        data = json.load(fileData)

    return data

###########################################################
# Подключение к MySQL
###########################################################


def def_connectingToMysql():
    """Создание подключения к БД"""
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


def def_ClearTableMysql(table):
    """Очистка таблицы в БД"""
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

########################################################################################################################


class MainCurrencySelectionMenu:
    """Меню выбора основной валюты"""

    def def_checkMainCurrencyTrading(self, inputM):
        """Проверка валюты, что она есть в списке основных на бирже."""
        match inputM:

            case 1:
                for i_def_allMainCurrencyBinance in def_allMainCurrency(self.exchange):

                    if i_def_allMainCurrencyBinance != self.inputMainCurrencyTrading:
                        checkSymbol = None

                    elif i_def_allMainCurrencyBinance == self.inputMainCurrencyTrading:
                        checkSymbol = [self.inputMainCurrencyTrading]
                        break

                return checkSymbol

            case 3:
                checkSymbol = def_allMainCurrency(self.exchange)
                return checkSymbol

    def __init__(self, exchange):
        """Вывод и обработка пунктов меню"""
        self.exchange = exchange
        self.mainCurrencyTradingBool = None

        if def_allMainCurrency(exchange) is None:
            print(f"Указана недопустимая торговая биржа {exchange} (class MenuTest)!")

        else:
            print("#" * 79)
            print(f"Укажите основную валюту биржи {self.exchange}, для торговли (например 'USDT') или используйте сразу все доступные.")
            print("#" * 79)
            print("\n1. Ввести основную валюту\n2. Посмотреть список доступных валют\n3. Использовать все доступные валюты\n")

            while True:

                input_numberPressedKey = input("Выберите пункт меню:")

                match input_numberPressedKey:
                    case "1":
                        self.inputMainCurrencyTrading = input(str("\nВведите основную валюта:")).upper()
                        checkMainCurrencyTrading = self.def_checkMainCurrencyTrading(1)

                        if checkMainCurrencyTrading is not None:
                            self.mainCurrencyTrading = checkMainCurrencyTrading
                            mainCurrencyTradingBool = True
                            break
                        else:
                            print(F"\nВы ввели не существующую валюту '{self.inputMainCurrencyTrading}', повторите попытку !\n")

                    case "2":
                        print(F"\nСписок доступных валют биржи {exchange}: {def_allMainCurrency(exchange)}\n")

                    case "3":
                        self.mainCurrencyTrading = self.def_checkMainCurrencyTrading(3)
                        mainCurrencyTradingBool = False
                        break

                    case _:
                        print(F"\nВы ввели не существующий пункт мею: '{input_numberPressedKey}'\n")

            if mainCurrencyTradingBool:
                print(F"\nВыбрана основная валюта {self.mainCurrencyTrading}")
                print("Начинается обработка ...")
            elif not mainCurrencyTradingBool:
                print(F"\nВыбраны все доступные монеты {self.mainCurrencyTrading}")
                print("Начинается обработка ...\n")

########################################################################################################################


class ExchangeInfoBlockchainNetwork():
    """Формирование Json с информацией о сетях Blockchain монет"""

    def __init__(self, exchange, symbol, name, listNetwork):

        self.exchange = exchange
        self.listNetwork = listNetwork
        self.symbol = symbol
        self.CoinInfoModify = []
        self.listNetworkModifi = []

        for i in listNetwork:

            self.listNetworkModifi.append(
                {
                    'network': i[0],  # Имя сети
                    'secondaryNameNetwork': i[1],  # Альтернативное название сети
                    'depositEnable': i[2],  # Возможность внесения депозита
                    'withdrawEnable': i[3],  # Возможность вывода депозита
                    'withdrawFee': i[4],  # Комиссия за вывод средств (количество монет)
                    'withdrawMin': i[5],  # Минимальный вывод (количество монет)
                    'minConfirm': i[6]  # Минимальное подтверждение сети
                })

        self.CoinInfoModify = {
                'symbol': symbol,
                'name': name,
                'networkList': self.listNetworkModifi
            }

        with open(f'{exchange}_coin_network_info.json', encoding='utf8') as file:  # Добавление в Json информации о Blockchain networks
            data = json.load(file)
            data.append(self.CoinInfoModify)
            with open(f'{exchange}_coin_network_info.json', 'w') as file1:
                json.dump(data, file1, indent=2)

########################################################################################################################


class UpdatingPricesTableMysql():
    """Добавление и обновление в БД информации о предложениях (цен и объёмов) на бирже (медленно, только для межбиржевой !!!)"""

    def __init__(self, exchange, ordersBook, startTime):

        connectingToMysql = def_connectingToMysql()  # Подключение к БД
        countUpdateSQL = int(0)  # Счётчик обновлений записей в БД

        for i_ordersBook in ordersBook:

            symbol = i_ordersBook[0]  # Имя пары
            bidPrice = i_ordersBook[1]  # Лучшее предложение цены покупки на бирже
            bidQty = i_ordersBook[2]  # Объём лучшего предложения покупки
            askPrice = i_ordersBook[3]  # Лучшее предложение цены продажи на бирже
            askQty = i_ordersBook[4]  # Объём лучшего предложения продажи

            try:
                with connectingToMysql.cursor() as cursor:

                    requestMysqlSelectSymbols = F"SELECT symbol FROM {exchange}_get_orderbook_ticker WHERE symbol = '{symbol}'"
                    cursor.execute(requestMysqlSelectSymbols)

                    if cursor.fetchone() is None:
                        requestMysqlInsertTable = F"INSERT INTO {exchange}_get_orderbook_ticker (symbol, bidPrice, bidQty, askPrice, askQty) VALUES  ('{symbol}', '{bidPrice}', '{bidQty}', '{askPrice}', '{askQty}');"
                        cursor.execute(requestMysqlInsertTable)

                    else:
                        requestMysqlUpdateTable = F"UPDATE {exchange}_get_orderbook_ticker SET bidPrice = '{bidPrice}', bidQty = '{bidQty}', askPrice = '{askPrice}', askQty = '{askQty}' WHERE symbol = '{symbol}';"
                        countUpdateSQL += 1
                        cursor.execute(requestMysqlUpdateTable)

            except Exception as ex:

                cursor.close()

                print("error")
                print(ex)

        connectingToMysql.commit()  # Записываем результаты в БД
        connectingToMysql.close()  # Закрываем соединение sql

        datetimeNow = datetime.now()  # Текущая дата/время
        datetimeNow = datetimeNow.strftime("%H:%M:%S")  # Создаём строку, представляющую дату/время

        endTime = (time.time() - startTime)  # Время окончания работы основной функции "run_sql"

        print('______________________________________________________________')
        print(datetimeNow, 'Обновлено:', countUpdateSQL, 'записей в БД.')
        print(datetimeNow, 'Затрачено на обработку', endTime, 'секунд.')

########################################################################################################################


def def_requestPriceTableMysql(symbol, exchange, bid_or_ask):
    """Запрос цен из БД"""

    if bid_or_ask == 'bidPrice':

        connectingToMysql = def_connectingToMysql()  # Подключение к БД

        try:
            with connectingToMysql.cursor() as cursor:
                requestMysqlSelectSymbols = F"SELECT bidPrice FROM {exchange}_get_orderbook_ticker WHERE symbol = '{symbol}'"
                cursor.execute(requestMysqlSelectSymbols)
                result = cursor.fetchone()
                connectingToMysql.close()  # Закрываем соединение sql

        except Exception as ex:

            cursor.close()

            print("error")
            print(ex)

        return float(result[0])

    elif bid_or_ask == 'askPrice':

        connectingToMysql = def_connectingToMysql()  # Подключение к БД

        try:
            with connectingToMysql.cursor() as cursor:
                requestMysqlSelectSymbols = F"SELECT askPrice FROM {exchange}_get_orderbook_ticker WHERE symbol = '{symbol}'"
                cursor.execute(requestMysqlSelectSymbols)
                result = cursor.fetchone()
                connectingToMysql.close()  # Закрываем соединение sql

        except Exception as ex:

            cursor.close()

            print("error")
            print(ex)

        return float(result[0])

########################################################################################################################


def def_calculationArbitrationProfit(exchange_first_price_ask, exchange_second_price_bid, network_first_withdrawFee):

    countCoins = int(1000)
    """Количество монет для торговли"""

    CountsCoinsFirstExchange = Decimal(countCoins) / Decimal(exchange_first_price_ask)
    CountsCoinsFirstExchange_commission = CountsCoinsFirstExchange - Decimal(network_first_withdrawFee)

    CountsCoinsSecondExchange = CountsCoinsFirstExchange_commission * Decimal(exchange_second_price_bid)

    profit = CountsCoinsSecondExchange - countCoins

    return profit

    # kucoin_kolichestcvo_coin_posle_vivoda = kucoin_kolichestvo_coin - float(kucoin_withdrawFee)
    #
    # binance_usdt_posle_prodazhi = kucoin_kolichestcvo_coin_posle_vivoda * binance_price_bid
########################################################################################################################


if __name__ == '__main__':
    main()
