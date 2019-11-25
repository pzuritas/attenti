import serial
import time as tm
from collections import namedtuple

time = tm.time()
session_data = dict()
Datapoint = namedtuple('Data', ['Voltage', 'Time'])

with serial.Ser('/dev/ttyUSB0') as port0:
    with serial.Ser('/dev/ttyS1') as port1:
        while True:
            voltage = float(port0.read())
            temperature = float(port1.read())
            time = tm.time() - time
            session_data[time] = Datapoint(voltage, time)
            tm.sleep(0.5)