import socket
from collections import defaultdict, namedtuple
from data_recv_wired import DataReceiver


UDPReceived = namedtuple('data', ['host', 'port', 'data'])

class Server():
    def __init__(self):
        self.data_recv = defaultdict(list)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 15000))
        self.counter = 0
        self.end = False

    def run(self):
        while not self.end:
            data, (client_host, client_port) = self.socket.recvfrom(4096)
            self.data_recv[client_host] = UDPReceived(
                client_host, client_port, data
                )
            if not data:
                self.counter += 1
            if self.counter > 20:
                self.end = True
        self.end = False
        self.counter = 0

class WiFiDataReceiver(DataReceiver):
    pass
