import socket
from tqdm import tqdm
from multiprocessing.pool import ThreadPool

HOST = '192.168.1.6'
PORTS = 2 ** 16


def test(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
        return None if scan.connect_ex((HOST, port)) else port

# 65536
if __name__ == '__main__':
    pool = ThreadPool(50)
    scaned = list(tqdm(pool.imap(test, range(1, 100 )), total=PORTS-1, desc=f'Scaning {HOST}'))

    print([port for port in scaned if port])


# def test(port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
#         return not scan.connect_ex((HOST, port))
#
# if __name__ == '__main__':
#     pool = ThreadPool(100)
#     pool.imap(test, )
#
# for port in tqdm(range(1, 65536 ), total=PORTS-1, desc=f'Scaning {HOST}' ):
#     if test(port):
#         print(f'Port  {port} open')
