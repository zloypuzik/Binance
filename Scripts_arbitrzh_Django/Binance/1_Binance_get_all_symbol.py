import time
import sqlite3
import datetime
import requests

###########################################################
# Проходим по списку всех валют (getAllTickersFromBinance) и если статус валюты равно 'TRADING',
# то добавляем в новый список 'ListAllPairsTradingInformation'
###########################################################

url = "https://api.binance.com/api/v3/exchangeInfo"

# Выполняем GET запрос
response = requests.get(url)
data = response.json()

ListAllPairsTradingInformation = []  # Список всех торгуемых пар на бирже, со всей торговой информацией

couldPairs = int(0)  # Количество монет
startTimeProgram = time.time()  # Время начала работы скрипта

for i in data['symbols']:
    if i['status'] == 'TRADING' and 'SPOT' in i['permissions']:

        ListAllPairsTradingInformation.append(i)
        couldPairs += 1

##########################################################
# Проверка что валютные пары из списка 'ListAllPairsTradingInformation' есть в БД (таблица: arbitrazh_binance_all_pairs_trading_inf),
# если такой валютной пары нет, то удаляем запись из таблицы
##########################################################


with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:

    cursor = connect_db.cursor()
    cursor.execute(F"SELECT * FROM arbitrazh_binance_all_pairs_trading_inf")
    bd_binance_all_pairs_trading_inf = cursor.fetchall()
    delCouldPairs = 0

    for get_symbol_bd_binance_all_pairs_trading_inf in bd_binance_all_pairs_trading_inf:

        if get_symbol_bd_binance_all_pairs_trading_inf is not None:

            exists_in_the_table_bd = None
            bd_id = get_symbol_bd_binance_all_pairs_trading_inf[0]
            bd_symbol = get_symbol_bd_binance_all_pairs_trading_inf[1]

            for check_ListAllPairsTradingInformation in ListAllPairsTradingInformation:

                if check_ListAllPairsTradingInformation['symbol'] == bd_symbol:
                    exists_in_the_table_bd = bd_symbol
                    break
                else:
                    exists_in_the_table_bd = None

            if exists_in_the_table_bd is None:

                cursor.execute(F"DELETE from arbitrazh_binance_all_pairs_trading_inf where id = {bd_id}")
                delCouldPairs += 1

##########################################################
# Проходим по саписку (ListAllPairsTradingInformation) всех валютных пар со статусом 'TRADING' и добавляем в БД
##########################################################

new_ListAllPairsTradingInformation = []
newCouldPairs: int = 0

for i_ListAllPairsTradingInformation in ListAllPairsTradingInformation:
    """Создаем свой Json с торгуемыми парами"""

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:

        cursor = connect_db.cursor()
        cursor.execute(F"SELECT symbol FROM arbitrazh_binance_all_pairs_trading_inf WHERE symbol = '{i_ListAllPairsTradingInformation['symbol']}'")

        if cursor.fetchone() is None:

            symbol = i_ListAllPairsTradingInformation['symbol'],
            immutableNameBaseAsset = i_ListAllPairsTradingInformation['baseAsset'],
            immutableNameQuoteAsset = i_ListAllPairsTradingInformation['quoteAsset'],
            baseAsset = i_ListAllPairsTradingInformation['baseAsset'],
            quoteAsset = i_ListAllPairsTradingInformation['quoteAsset']
            stepSize = i_ListAllPairsTradingInformation['filters'][1]['stepSize']

            cursor.execute(F"INSERT INTO  arbitrazh_binance_all_pairs_trading_inf VALUES (NULL, ?, ?, ?, ?, ?, ?)", (symbol[0], immutableNameBaseAsset[0], immutableNameQuoteAsset[0], baseAsset[0], quoteAsset, stepSize))

            newCouldPairs += 1

##########################################################

print("\n")
print("#" * 79)
nowTime = datetime.datetime.now()
print(f'Дата и время:', nowTime.strftime("%d-%m-%Y %H:%M:%S"))
##########################################################
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Всего валютных пар: {couldPairs}")
print(f"Добавлено новых валютных пар в БД: {newCouldPairs}")
print(f"Удалено валютных пар из БД: {delCouldPairs}")

##########################################################

