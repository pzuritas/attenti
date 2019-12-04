import serial
import time as tm
from collections import namedtuple
import matplotlib.pyplot as plt

zero_time = tm.time()
session_data = dict()
Datapoint = namedtuple('data', ['time', 'voltage', 'temperature'])

with serial.Serial(port='COM4', baudrate=9600, timeout=5) as port0:
        for _ in range(200):
            print('In while')
            data_0 = port0.readline().strip()
            print('data_0 read: ', data_0)
            data_1 = port0.readline().strip()
            print('data_1 read: ', data_1)
            if data_0[0] == 'V':
                print('V')
                voltage = float(data_1[2:])
                temperature = float(data_0[2:])
            else:
                print('Not V')
                voltage = float(data_0[2:])
                temperature = float(data_1[2:])
            print('data recognized')
            time = tm.time() - zero_time
            session_data[time] = Datapoint(time, voltage, temperature)
            print(session_data[time])
            tm.sleep(0.15)
            print('-'*15)
            print(len(session_data))

voltage = list(map(lambda dp: dp.voltage, session_data.values()))
temp = list(map(lambda dp: dp.temperature, session_data.values()))

plt.figure(figsize=(8,4))
plt.subplot(121)
plt.plot(list(session_data.keys()), voltage)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.subplot(122)
plt.plot(list(session_data.keys()), temp)
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (K)')
plt.suptitle('Variables en una sesión')
plt.show()