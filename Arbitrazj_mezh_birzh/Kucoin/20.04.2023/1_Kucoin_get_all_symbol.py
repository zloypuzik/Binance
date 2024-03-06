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


with open(f'{exchange}_AllPairsTradingInf.json', 'w') as file:
    json.dump(ListAllPairsTradingInformation, file, indent=2)

print("\n")
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Было добавлено: {couldPairs} пар.")