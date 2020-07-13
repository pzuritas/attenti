import serial
import csv
import os
import time as tm
import copy
import scipy.signal as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import platform
mpl.style.use('ggplot')
from collections import namedtuple
from pc_parameters import PORT, BAUDRATE, TIMEOUT, PERIOD, MACPORT, FREQ


# Define a simple data structure for datapoints.
Datapoint = namedtuple('data', ['time', 'voltage', 'temperature'])
SessionData = namedtuple('session', ['voltage', 'temperature'])

class DataReceiver():
    '''Wrapper class for data receiving through serial port.'''
    def __init__(self):
        if platform.system() == 'Windows':
            self.port = PORT
        elif platform.system() == 'Darwin':
            self.port = MACPORT
        else:
            raise NotImplementedError('No suitable OS (Win/Mac) found.')
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

    def add_capture(self, filter=False):
        '''Stores data from last session on active history.'''
        if not filter:
            voltage = list(
                map(lambda dp: dp.voltage, self.session_data.values())
                )
            temp = list(
                map(lambda dp: dp.temperature, self.session_data.values())
                )
            time = self.session_data.keys()
            volt_series = zip(time, voltage)
            temp_series = zip(time, temp)
            self.all_data.append(SessionData(volt_series, temp_series))
        else:
            voltage = list(
                map(lambda dp: dp.voltage, self.session_data.values())
                )
            filt = sp.butter(1, FREQ)
            voltage = sp.lfilter(*filt, voltage)
            temp = list(
                map(lambda dp: dp.temperature, self.session_data.values())
                )
            time = self.session_data.keys()
            volt_series = zip(time, voltage)
            temp_series = zip(time, temp)
            self.all_data.append(SessionData(volt_series, temp_series))

    def save_capture(self, i=-1):
        '''Saves data session. Defaults to last.'''
        if i == -1:
            j = len(self.all_data)-1
        else:
            j = i
        volt = list(copy.deepcopy(self.all_data[j].voltage))
        temp = list(copy.deepcopy(self.all_data[j].temperature))
        if not os.path.exists(f'./sessions/session_{j}'):
            os.makedirs(f'./sessions/session_{j}')
        with open(f'./sessions/session_{j}/voltage.csv', 'w') as output:
                writer = csv.writer(output, lineterminator='\n')
                for line in volt:
                    writer.writerow(line)
        with open(f'./sessions/session_{j}/temperature.csv', 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            for line in temp:
                writer.writerow(line)

    def plot_session(self, filename, i=-1, show=False, times=None):
        '''Plots the i-th session. Defaults to last.'''
        if i == -1:
            j = len(self.all_data)-1
        else:
            j = i
        volt = list(self.all_data[j].voltage)
        temp = list(self.all_data[j].temperature)
        vtime = [dp[0] for dp in volt]
        ttime = [dp[0] for dp in temp]
        v = [dp[1] for dp in volt]
        t = [dp[1] for dp in temp]
        plt.figure()
        plt.title(f'session {i}')
        plt.subplot(1, 2, 1)
        plt.xlabel('time [s]')
        plt.ylabel('voltage [mV]')
        plt.plot(vtime, v, label='voltage')
        if times:
            for time in times:
                plt.axvline(time, ymin=np.min(v), ymax=np.max(v))
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.xlabel('time [s]')
        plt.ylabel('temperature [K]')
        plt.plot(ttime, t, label='temperature')
        if times:
            for time in times:
                plt.axvline(time, ymin=np.min(t), ymax=np.max(t))
        plt.legend()
        plt.tight_layout()
        if show:
            plt.show()
        if not os.path.exists(f'./figures/'):
            os.makedirs(f'./figures/')
        plt.savefig(f'figures/{filename}.png')

    def plot_volt(self, filename, i=-1, show=False):
        '''Plots the i-th voltage series. Defaults to last.'''
        if i == -1:
            j = len(self.all_data)-1
        else:
            j = i
        volt = list(self.all_data[j].voltage)
        vtime = [dp[0] for dp in volt]
        v = [dp[1] for dp in volt]
        plt.figure()
        plt.title(f'voltage series for session {i}')
        plt.xlabel('time [s]')
        plt.ylabel('voltage [mV]')
        plt.plot(vtime, v)
        if show:
            plt.show()
        if not os.path.exists(f'./figures/'):
            os.makedirs(f'./figures/')
        plt.savefig(f'figures/{filename}.png')

    def plot_temp(self, filename, i=-1, show=False):
        '''Plots the i-th temperature series. Defaults to last.'''
        if i == -1:
            j = len(self.all_data)-1
        else:
            j = i
        temp = list(self.all_data[j].temperature)
        ttime = [dp[0] for dp in temp]
        t = [dp[1] for dp in temp]
        plt.figure()
        plt.title(f'voltage series for session {i}')
        plt.xlabel('time [s]')
        plt.ylabel('temperature [K]')
        plt.plot(ttime, t)
        if show:
            plt.show()
        if not os.path.exists(f'./figures/'):
            os.makedirs(f'./figures/')
        plt.savefig(f'figures/{filename}.png')

if __name__ == '__main__':
    time = [i for i in range(10)]
    print(f'time = {time}')
    volt = [i**2 for i in range(10)]
    print(f'volt = {volt}')
    recv = DataReceiver()
    for i in range(len(time)):
        recv.session_data[time[i]] = Datapoint(time[i], volt[i], volt[i])
    recv.add_capture(filter=True)
    recv.save_capture()
    recv.plot_session('test', show=True)