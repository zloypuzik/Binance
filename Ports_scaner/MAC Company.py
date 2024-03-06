# import requests
#
# res = requests.get('https://api.maclookup.app/v2/macs/{c0:9f:e1:a8:88:5c}')
#
# print(res)

import requests


def main():
    r = requests.get('https://api.maclookup.app/v2/macs/c0:9f:e1:a8:88:5c')
    data = r.json()
    test = data['success']
    print(data,  type(data))

s = main()