import json
import time

from Arbitrazj_mezh_birzh import Classes

client = Classes.apiKucoin()  # Binance API settings

###########################################################
# Меню выбора основной валюты
###########################################################

exchange = 'Kucoin'
mainCurrencyTrading = Classes.MainCurrencySelectionMenu(exchange).mainCurrencyTrading  # Список основных валют биржи

###########################################################


getAllTickersFromKucoin = client.get_symbols()  # # Список всех торгуемых пар на бирже, со всей торговой информацией.

ListAllPairsTradingInformation = []

couldPairs = int(0)
startTimeProgram = time.time()

for i_getAllTickersFromKucoin in getAllTickersFromKucoin:
    if i_getAllTickersFromKucoin["enableTrading"]:

        if len(mainCurrencyTrading) == 1:

            if i_getAllTickersFromKucoin['baseCurrency'] == mainCurrencyTrading[0] or i_getAllTickersFromKucoin['quoteCurrency'] == mainCurrencyTrading[0]:
                ListAllPairsTradingInformation.append(i_getAllTickersFromKucoin)

                couldPairs += 1
        elif len(mainCurrencyTrading) > 1:
            ListAllPairsTradingInformation.append(i_getAllTickersFromKucoin)
            couldPairs += 1

###########################################################


new_ListAllPairsTradingInformation = []

for i_ListAllPairsTradingInformation in ListAllPairsTradingInformation:
    """Создаем свой Json с торгуемыми парами"""

    ###########################################################

    """
        Особенности Kucoin биржи:
        "symbol": "BCHSV-USDT",  # Уникальный код символа, он не изменится после переименования
        "name": "BSV-USDT",
        "baseCurrency": "BSV",  # Название торговых пар, оно изменится после переименования
        "quoteCurrency": "USDT",

        т.к. "baseCurrency" или "quoteCurrency" изменяемые (согласно документации к API), то нужно использовать название из "symbol" (т.к оно не изменяемо)
    """

    immutableNameBaseAsset = i_ListAllPairsTradingInformation['symbol'].upper()
    immutableNameBaseAsset = immutableNameBaseAsset.split("-")[0]  # Вырезает все, что перед '-'

    immutableNameQuoteAsset = i_ListAllPairsTradingInformation['symbol'].upper()
    immutableNameQuoteAsset = immutableNameQuoteAsset.split("-")[1]  # Вырезает все, что после '-'

    ###########################################################

    new_ListAllPairsTradingInformation.append({

        'symbol': i_ListAllPairsTradingInformation['symbol'],
        'immutableNameBaseAsset': immutableNameBaseAsset,
        'immutableNameQuoteAsset': immutableNameQuoteAsset,
        "baseAsset": i_ListAllPairsTradingInformation['baseCurrency'],
        "quoteAsset": i_ListAllPairsTradingInformation['quoteCurrency']

    })

###########################################################


with open(f'{exchange}_AllPairsTradingInf.json', 'w') as file:
    json.dump(new_ListAllPairsTradingInformation, file, indent=2)

print("\n")
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Было добавлено: {couldPairs} пар.")