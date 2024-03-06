from MexcClient.client import MexcClient
import json

API_KEY = 'mx0vglBiQfiK5Hkutx'
API_SECRET= '0e6b2c7ab0d741ac8f435bf56a0ab892'

client = MexcClient(API_KEY, API_SECRET)
a = client.test()

b = []

for i in a:
    b.append(i)

with open(f'test_AllPairsTradingInf.json', 'w') as file:
    json.dump(b, file, indent=2)
#     aa = i.encode("utf-8")
#     b.append(aa)
# print(b)
# print(b.encode("utf-8"))
# client = MexcClient("mx0vglBiQfiK5Hkutx", "0e6b2c7ab0d741ac8f435bf56a0ab892")
#
# a = client.network_info()
#
# print(a)

# https://api.mexc.com/api/v3/exchangeInfo

# requestsAllCoinsInfo = requests.get(f'https://api.mexc.com/api/v3/exchangeInfo').json()
#
# count = 0
#
# for a in requestsAllCoinsInfo['symbols']:
#     count += 1
#     print(a)
# # print(requestsAllCoinsInfo['symbol'])
# print(count)

# curl cOMAN
#
# api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
# api += key
#
# getAllInfoSymbolFromExchange = requests.get(f'https://api.mexc.com/api/v3/capital/config/getall', params={
#     a
# }).json()
#
#
# print(getAllInfoSymbolFromExchange)
# for i_getAllInfoSymbolFromExchange in getAllInfoSymbolFromExchange['symbols']:
#
#     SymbolTradingStatus = i_getAllInfoSymbolFromExchange['status']
#     print(SymbolTradingStatus)
