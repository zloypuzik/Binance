import time
import socket
from tqdm import tqdm
from multiprocessing.pool import ThreadPool
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




        HOST = i[1].psrc

        def scan_ports(port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                return None if scan.connect_ex((HOST, port)) else port

        # 65536
        if __name__ == '__main__':
            pool = ThreadPool(3000)
            scaned = list(tqdm(pool.imap(scan_ports, range(1, 65536)), desc=f'Scaning {HOST}'))

        # ports = [port for port in scaned if port]
            ports = str([port for port in scaned if port])



        clients_dict = {"ip": i[1].psrc, "mac": i[1].hwsrc, "Company": test, "Open_Ports": ports}
        clients_list.append(clients_dict)

    return clients_list


def print_result(results_list):
    # print("IP\t\t\tMAC Address\n-----------------------------------------")

    for i in results_list:
        print(i["ip"] + "\t\t" + i["mac"] + "\t\t" + i["Company"] + "\t\t" + i["Open_Ports"])


scan_result = scan("192.168.1.1/24")
print_result(scan_result)