import socket
import time as tm
from collections import defaultdict, namedtuple
from data_recv_wired import DataReceiver, Datapoint


UDPReceived = namedtuple('data', ['host', 'port', 'data'])

class Server():
    '''Class to start a server for wireless connection.'''
    def __init__(self):
        self.data_recv = defaultdict(list)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 15000))
        self.counter = 0
        self.end = False

    def run(self):
        '''
        Starts the server for data collection. Must be runn after starting datastream.
        '''
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
    '''Overloads the DataReceiver methods to work with wifi.'''
    def __init__(self):
        super().__init__()
        self.server = Server()
    
    def capture_start(self, session_length):
        self.set_time()
        self.server.run()
        data_list = self.server.data_recv.values()
        for data_tuple in data_list:
            volt, temp = data_tuple['data'].strip().split(';')
            volt = float(volt)
            temp = float(temp)
            time = tm.time() - self.t0
            # Data is saved as dictionary to ensure no repeat information
            self.session_data[time] = Datapoint(time, volt, temp)

