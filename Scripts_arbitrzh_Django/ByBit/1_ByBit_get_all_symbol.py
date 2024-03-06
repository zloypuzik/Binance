import json
import time
import sqlite3
from pybit import spot
session_unauth = spot.HTTP(
    endpoint="https://api.bybit.com"
)
info = (session_unauth.query_symbol())

couldPairs = int(0)
startTimeProgram = time.time()

for i_ListAllPairsTradingInformation in (info['result']):

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:
    # with sqlite3.connect('../../test_site/db.sqlite3') as connect_db:

        cursor = connect_db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS arbitrazh_bybit_all_pairs_trading_inf(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        immutableNameBaseAsset TEXT,
        immutableNameQuoteAsset TEXT,
        baseAsset TEXT,
        quoteAsset TEXT
        )""")

        cursor.execute(F"SELECT symbol FROM arbitrazh_bybit_all_pairs_trading_inf WHERE symbol = '{i_ListAllPairsTradingInformation['name']}'")
        #cursor.execute(F"SELECT symbol FROM test WHERE symbol = '{i_ListAllPairsTradingInformation['symbol']}'")
        #
        print(1)
        if cursor.fetchone() is None:
            print(i_ListAllPairsTradingInformation['name'])

            symbol = i_ListAllPairsTradingInformation['name'],
            immutableNameBaseAsset = i_ListAllPairsTradingInformation['baseCurrency'],
            immutableNameQuoteAsset = i_ListAllPairsTradingInformation['quoteCurrency'],
            baseAsset = i_ListAllPairsTradingInformation['baseCurrency'],
            quoteAsset = i_ListAllPairsTradingInformation['quoteCurrency']


            cursor.execute(F"INSERT INTO  arbitrazh_bybit_all_pairs_trading_inf VALUES (NULL, ?, ?, ?, ?, ?)", (symbol[0], immutableNameBaseAsset[0], immutableNameQuoteAsset[0], baseAsset[0], quoteAsset))

            print(3)
            connect_db.commit()

##########################################################

print("\n")
print("#" * 79)
print("dsaf.")
print(F"sdfsd: {(time.time() - startTimeProgram) / 60}")
print(f"sdfsdf: {couldPairs} sf.")
