import time

import scapy.all as scapy
import requests

def scan(ip):

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []

    for i in answered_list:

        time.sleep(0.5)
        mac_address = (i[1].hwsrc)
        try:
            r = requests.get(f'https://api.maclookup.app/v2/macs/{mac_address}')
            data = r.json()

            found = data['found']

            if found == True:
                test = data['company']
                # print(test)
            else:
                test = data['None']
        except:
            test = 'None'

        clients_dict = {"ip": i[1].psrc, "mac": i[1].hwsrc, "Company": test}
        clients_list.append(clients_dict)

    return clients_list


def print_result(results_list):
    # print("IP\t\t\tMAC Address\n-----------------------------------------")

    for i in results_list:
        print(i["ip"] + "\t\t" + i["mac"] + "\t\t" + i["Company"])


scan_result = scan("192.168.1.1/24")
print_result(scan_result)
