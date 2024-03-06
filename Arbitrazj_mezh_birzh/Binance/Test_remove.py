import time
testList = [
    {
        "symbol": "USDT",
        'values':
        {
            "time": 12
        }
    },
    {
        "symbol": "BTC",
        'values':
        {
            "time": 15
        }
    },
    {
        "symbol": "ETH",
        'values':
        {
            "time": 15
        }
    },
    {
        "symbol": "ETH2",
        'values':
            {
                "time": 15
            }
    }

]
testList33 = [
    {
        "symbol": "USDT",
        'values':
        {
            "time": 12
        }
    },
    # {
    #     "symbol": "BTC",
    #     'values':
    #     {
    #         "time": 15
    #     }
    # },
    {
        "symbol": "ETH",
        'values':
        {
            "time": 15
        }
    },
    {
        "symbol": "ETH2",
        'values':
            {
                "time": 15
            }
    }

]
profitList10mins = []

test = "ETH"

# print(testList)
#
# if test in testList:
#     print('yes')
# elif test not in testList:
#     print('no')
# if testList[0]['symbol'] in testList:
# for i in testList:
# if test in testList:
#     # a = testList.index(i)
#     # testList.remove(testList.index(i))
#     print(testList.index(test))


for i in testList:

    test2 = False
    test4 = []

    for ii in testList33:

        if i['symbol'] == ii['symbol']:

            test2 = True
            break

    a = testList.index(i)

    test4.append({
        'a': a,
        'test2': test2
    })
    #print(test4)
    # print(test4)
    #
    if test4[0]['test2'] == False:
        testList.pop(test4[0]['a'])

# testList.pop(test4)
a = time.monotonic()

time.sleep(5)



c = time.monotonic() - a

print(c)
###############################################################################
# Биржа покупки: "Mexc" | биржа продажи: "Kucoin"
# _______________________________________________________________________________
# KARATEUSDT | сеть: HBAR | комиссия: 0.1 | прибыль: 3.0851773177739297960379361
# -------------------------------------------------------------------------------

