import decimal
from decimal import Decimal
import sqlite3
import time
import datetime
import requests
import json
import json
import sqlite3
import datetime
from datetime import timedelta, datetime
from json import loads

from Scripts_arbitrzh_Django import API

from Scripts_arbitrzh_Django import Class_counting_trades

#########################################################


def f_minqty_size_up(kolichestvo, stepSize):
    def adjust_to_step(value, step, increase=False):
        return ((int(value * 100000000) - int(value * 100000000) % int(
            float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)

    sell_amount_a = adjust_to_step(kolichestvo, stepSize)

    return sell_amount_a


def f_minqty_size_down(kolichestvo, stepSize):
    def adjust_to_step(value, step, increase=False):
        return ((int(value * 100000000) - int(value * 100000000) % int(
            float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)

    sell_amount_a = adjust_to_step(kolichestvo, stepSize)

    return sell_amount_a


###########################################################
# Проходим по списку всех валют (data['symbols']) и если статус валюты равно 'TRADING' и i['permissions'] == 'SPOT',
# то добавляем в новый список 'ListAllPairsTradingInformation'
###########################################################\

aa = '2024-02-10 01:10:51'
bb = aa[0]+aa[1]+aa[2]+aa[3] + ', ' + aa[5]+aa[6] + ', ' + aa[8]+aa[9] + ', ' + aa[11]+aa[12] + ', ' + aa[14]+aa[15] + ', ' + aa[17]+aa[18]
print(bb)
# print(bb)
year = int(aa[0]+aa[1]+aa[2]+aa[3])
month = int(aa[5]+aa[6])
day = int(aa[8]+aa[9])
hour = int(aa[11]+aa[12])
minute = int(aa[14]+aa[15])
second = int(aa[17]+aa[18])
# b = '2024-02-09 21:36:08'
# mo_o = int(a[8] + a[9])
# h_o = int(a[11] + a[12])
# m_o = int(a[14] + a[15])
# s_o = int(a[17] + a[18])
#
# h_l = int(b[11] + b[12])
# m_l = int(b[14] + b[15])
# s_l = int(b[17] + b[18])
#
# date = datetime.now()
# #days=1
# #seconds=2
# #minutes=
# #hours=
# new_date = date - timedelta(hours=h_o, minutes=m_o, seconds=s_o)
#
# print(date)
# print(new_date)
# print(h_o,':', m_o, ":", s_o)
#
# datetime(year, month, day, hour, minute, second)
# b = datetime(2024, 2, 8, 18, 25, 30)


b = datetime(year, month, day, hour, minute, second)
a = datetime.now()

# returns a timedelta object
c = a - b
print('Difference: ', c)

# returns (minutes, seconds)
minutes = divmod(c.total_seconds(), 60)
print('Total difference in minutes: ', minutes[0], 'minutes', minutes[1], 'seconds')

# returns the difference of the time of the day (minutes, seconds)
minutes = divmod(c.seconds, 60)
print('Total difference in minutes: ', minutes[0], 'minutes', minutes[1], 'seconds')

minutess = divmod(c.seconds, 60)
print(minutess)