import sqlite3
import time
import datetime
import requests
from binance.client import Client
import websocket
import asyncio
import json
from threading import *


#########################################################
#  Удалить все из таблицы с ценами и добавить новую, актуальную, информацию
#########################################################

while True:

    try:

        with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:

            cursor = connect_db.cursor()

            r = requests.get("https://api.binance.com/api/v3/ticker/bookTicker")
            results = r.json()

            cursor.execute(F"DELETE FROM arbitrazh_binance_bookticker")
            cursor.execute(F"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'arbitrazh_binance_bookticker';")

            for i_results in results:

                cursor.execute( F"INSERT INTO  arbitrazh_binance_bookticker VALUES (NULL, ?, ?, ?, ?, ?)", (i_results['symbol'], i_results['bidPrice'], i_results['bidQty'], i_results['askPrice'], i_results['askQty']))

    except:

        print('Что-то не так с запистю в БД !!!')

    print('Обновление завершенно')
    nowTime = datetime.datetime.now()
    print(f'Дата и время:', nowTime.strftime("%d-%m-%Y %H:%M:%S"))
    print("#" * 79)
    time.sleep(1)
