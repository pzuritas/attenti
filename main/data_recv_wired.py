import serial
import time as tm
from collections import namedtuple
from pc_parameters import PORT, BAUDRATE, TIMEOUT


# Define a simple data structure for datapoints.
Datapoint = namedtuple('data', ['time', 'voltage', 'temperature'])

class DataReceiver():
    '''Wrapper class for data receiving.'''
    def __init__(self):
        self.port = PORT
        self.baudrate = BAUDRATE
        self.timeout = TIMEOUT
        self.period = PERIOD
        self.t0 = tm.time()
        self.session_data = dict() # Data for last session
        self.all_data = [] # To save more than one session

    def set_time(self):
        '''Reset time'''
        self.t0 = tm.time()

    def capture_start(self, session_length):
        '''Çapture data for a determined session_length.'''
        with serial.Serial(
            port=self.port, baudrate=self.baudrate, timeout=self.timeout
            ) as port:

            self.set_time()

            for _ in range(session_length):
                data_0 = port.readline().strip()
                data_1 = port.readline().strip()
                if data_0[0] == 'V':
                    voltage = float(data_1[2:])
                    temperature = float(data_0[2:])
                else:
                    voltage = float(data_0[2:])
                    temperature = float(data_1[2:])

                time = tm.time() - self.t0

                # Data is saved as dictionary to ensure no repeat information
                self.session_data[time] = Datapoint(time, voltage, temperature)
                tm.sleep(self.period)

voltage = list(map(lambda dp: dp.voltage, session_data.values()))
temp = list(map(lambda dp: dp.temperature, session_data.values()))
