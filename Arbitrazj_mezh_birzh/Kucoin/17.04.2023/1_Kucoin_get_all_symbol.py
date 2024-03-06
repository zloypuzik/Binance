import json
from kucoin.client import Client
import time

from Arbitrazj_mezh_birzh import Classes

##################################################################
# API Kucoin
##################################################################


api_key = '63cc9d027675230001bba629'
api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7'

client = Client(api_key, api_secret, passphrase='4796212')

getAllTickersFromKucoin = client.get_symbols()

###########################################################
# Меню выбора основной валюты
###########################################################

exchange = "Kucoin"


def def_checkMainCurrencyTrading(receivedMainCurrencyTrading):
    checkSymbol = None
    for i_def_allMainCurrencyKucoin in Classes.def_allMainCurrency(exchange):
        if i_def_allMainCurrencyKucoin != receivedMainCurrencyTrading:
            checkSymbol = None

        elif i_def_allMainCurrencyKucoin == receivedMainCurrencyTrading:
            checkSymbol = receivedMainCurrencyTrading
            break
    return checkSymbol


print("#" * 79)
print("Укажите основную валюту для торговли (например 'USDT') или используйте сразу все доступные.")
print("#" * 79)
print("\n1. Ввести основную валюту\n2. Посмотреть список доступных валют\n3. Использовать все доступные валюты\n")

mainCurrencyTradingBool = bool

while True:

    input_numberPressedKey = int(input("Выберите пункт меню:"))

    match input_numberPressedKey:
        case 1:
            inputMainCurrencyTrading = input(str("\nВведите основную валюта:")).upper()
            checkMainCurrencyTrading = def_checkMainCurrencyTrading(inputMainCurrencyTrading)

            if checkMainCurrencyTrading is not None:
                mainCurrencyTrading = checkMainCurrencyTrading
                mainCurrencyTradingBool = True
                break
            else:
                print(F"\nВы ввели не существующую валюту '{inputMainCurrencyTrading}', повторите попытку !\n")
        case 2:
            print(F"\nСписок доступных валют: {def_allMainCurrencyKucoin()}\n")
        case 3:
            mainCurrencyTradingBool = False
            break
        case _:
            print(F"\nВы ввели не существующий пункт мею: '{input_numberPressedKey}'\n")

if mainCurrencyTradingBool:
    print(F"\nВыбрана основная валюта '{mainCurrencyTrading}'")
    print("Начинается обработка ...")
elif not mainCurrencyTradingBool:
    print("\nВыбраны все доступные монеты")
    print("Начинается обработка ...\n")

###########################################################
#
###########################################################


ListAllTradedSymbolFromKucoin = []

couldPairs = int(0)
startTimeProgram = time.time()

for i_getAllTickersFromKucoin in getAllTickersFromKucoin:
    if i_getAllTickersFromKucoin["enableTrading"]:
        if mainCurrencyTradingBool:
            if i_getAllTickersFromKucoin['baseCurrency'] == mainCurrencyTrading or i_getAllTickersFromKucoin['quoteCurrency'] == mainCurrencyTrading:
                ListAllTradedSymbolFromKucoin.append(i_getAllTickersFromKucoin)
                couldPairs += 1
        elif not mainCurrencyTradingBool:
            ListAllTradedSymbolFromKucoin.append(i_getAllTickersFromKucoin)
            couldPairs += 1

#########################################################


with open('Kucoin_get_all_symbol.json', 'w') as file:
    json.dump(ListAllTradedSymbolFromKucoin, file, indent=2)

print("\n")
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Было добавлено: {couldPairs} пар.")
