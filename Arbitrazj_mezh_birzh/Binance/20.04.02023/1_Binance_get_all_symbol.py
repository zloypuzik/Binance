import json
import time

from Arbitrazj_mezh_birzh import Classes

###########################################################
# Binance API settings
###########################################################


client = Classes.apiBinance()
getAllTickersFromBinance = client.get_all_tickers()

###########################################################
# Меню выбора основной валюты
###########################################################

exchange = 'Binance'
mainCurrencyTrading = Classes.MainCurrencySelectionMenu(exchange).mainCurrencyTrading

###########################################################
#
###########################################################


ListAllPairsTradingInformation = []  # Список всех торгуемых пар на бирже, со всей торговой информацией

couldPairs = int(0)
startTimeProgram = time.time()

for i_getAllTickersFromBinance in getAllTickersFromBinance:

    getSymbolFromAllTickersBinance = i_getAllTickersFromBinance['symbol']    # Нужно только для получения списка пар, существующих на бирже (нужно оптимизировать !!!), для использования в запросе 'getAllInfoSymbolFromBinance'
    getAllInfoSymbolFromBinance = client.get_symbol_info(getSymbolFromAllTickersBinance)

    if getAllInfoSymbolFromBinance is not None:
        time.sleep(0.2)

        SymbolTradingStatus = getAllInfoSymbolFromBinance['status']

        if SymbolTradingStatus == 'TRADING':
            if len(mainCurrencyTrading) == 1:
                if getAllInfoSymbolFromBinance['baseAsset'] == mainCurrencyTrading[0] or getAllInfoSymbolFromBinance['quoteAsset'] == mainCurrencyTrading[0]:
                    ListAllPairsTradingInformation.append(getAllInfoSymbolFromBinance)
                    couldPairs += 1
            elif len(mainCurrencyTrading) > 1:
                ListAllPairsTradingInformation.append(getAllInfoSymbolFromBinance)
                couldPairs += 1
    else:
        print("Нет пары:", getSymbolFromAllTickersBinance)

##########################################################


with open(f'{exchange}_AllPairsTradingInf.json', 'w') as file:
    json.dump(ListAllPairsTradingInformation, file, indent=2)

print("\n")
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Было добавлено: {couldPairs} пар.")
