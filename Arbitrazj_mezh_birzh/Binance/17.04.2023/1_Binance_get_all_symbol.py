import json
import time

from binance.client import Client

from Arbitrazj_mezh_birzh import Classes

###########################################################
# Binance API settings
###########################################################


apiKey = "A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG"
secretApiKey = "zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA"

client = Client(
    apiKey,
    secretApiKey
)

getAllTickersFromBinance = client.get_all_tickers()

###########################################################
# Меню выбора основной валюты
###########################################################


mainCurrencyTrading = Classes.MainCurrencySelectionMenu("Binance").mainCurrencyTrading

###########################################################
#
###########################################################


ListAllTradedSymbolFromBinance = []

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
                    ListAllTradedSymbolFromBinance.append(getAllInfoSymbolFromBinance)
                    couldPairs += 1
            elif len(mainCurrencyTrading) > 1:
                ListAllTradedSymbolFromBinance.append(getAllInfoSymbolFromBinance)
                couldPairs += 1
    else:
        print("Нет пары:", getSymbolFromAllTickersBinance)

##########################################################


with open('Binance_get_all_symbol.json', 'w') as file:
    json.dump(ListAllTradedSymbolFromBinance, file, indent=2)

print("\n")
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Было добавлено: {couldPairs} пар.")
