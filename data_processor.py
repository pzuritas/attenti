import serial
import time as tm
from collections import namedtuple

time = tm.time()
session_data = dict()
Datapoint = namedtuple('data', ['time', 'voltage', 'temperature'])

with serial.Serial(port=3, baudrate=9600, timeout=5) as port0:
        while True:
            print('In while')
            data_0 = port0.readline()
            print('data_0 read: ', data_0)
            data_1 = port0.readline()
            print('data_1 read: ', data_1)
            if data_0[0] == 'V':
                print('V')
                voltage = float(data_0[2:])
                temperature = float(data_1[2:])
            else:
                print('Not V')
                voltage = float(data_1[2:])
                temperature = float(data_0[2:])
            print('data recognized')
            time = tm.time() - time
            session_data[time] = Datapoint(time, voltage, temperature)
            tm.sleep(0.25)
            print('.')
            print(len(session_data))