import serial
import time as tm
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('ggplot')
from collections import namedtuple
from pc_parameters import PORT, BAUDRATE, TIMEOUT, PERIOD


# Define a simple data structure for datapoints.
Datapoint = namedtuple('data', ['time', 'voltage', 'temperature'])
SessionData = namedtuple('session', ['voltage', 'temperature'])

class DataReceiver():
    '''Wrapper class for data receiving through serial port.'''
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

    def save_capture(self):
        '''Saves data on last session.'''
        voltage = list(map(lambda dp: dp.voltage, self.session_data.values()))
        temp = list(map(lambda dp: dp.temperature, self.session_data.values()))
        time = self.session_data.keys()
        volt_series = zip(time, voltage)
        temp_series = zip(time, temp)
        self.all_data.append(SessionData(volt_series, temp_series))

    def plot_session(self, filename, i=0, show=False):
        '''Plots the i-th session'''
        plt.figure()
        plt.title(f'session {i}')
        plt.subplot(1, 2, 1)
        plt.xlabel('time [s]')
        plt.ylabel('voltage [mV]')
        plt.plot(self.all_data[i]['voltage'])
        plt.subplot(1, 2, 2)
        plt.xlabel('time [s]')
        plt.ylabel('temperature [K]')
        plt.plot(self.all_data[i]['temperature'])
        if show:
            plt.show()
        plt.savefig(f'figures/{filename}.png')

    def plot_volt(self, filename, i=0, show=False):
        '''Plots the i-th voltage series'''
        plt.figure()
        plt.title(f'voltage series for session {i}')
        plt.xlabel('time [s]')
        plt.ylabel('voltage [mV]')
        plt.plot(self.all_data[i]['voltage'])
        if show:
            plt.show()
        plt.savefig(f'figures/{filename}.png')

    def plot_temp(self, filename, i=0, show=False):
        '''Plots the i-th temperature series'''
        plt.figure()
        plt.title(f'voltage series for session {i}')
        plt.xlabel('time [s]')
        plt.ylabel('temperature [K]')
        plt.plot(self.all_data[i]['temperature'])
        if show:
            plt.show()
        plt.savefig(f'figures/{filename}.png')

