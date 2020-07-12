import csv
import numpy as np
import scipy as sp


class DataProcessor():
    '''Wrapper for estimating attention span.'''
    def __init__(self):
        self.time = []
        self.data = []
        self.avg_att_v = 0
        self.avg_att_t = 0
    
    def read_csv(self, filename):
        '''Read voltage or temperature file.'''
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time, data = row.strip().split(',')
                self.time.append(float(time))
                self.data.append(float(data))

    def detect_peaks(self, threshhold):
        '''Detects peaks for data analysis.'''
        if len(self.time) == 0:
            raise ValueError('No data has been loaded.')
        indices = sp.signal.find_peaks(-1*self.data, threshhold)
        timestamps = [self.time[i] for i in indices]
        self.avg_att_v = np.mean(np.diff(timestamps))

    def detect_lowering(self, tolerance):
        '''Detects lowering of signal for data analysis.'''
        if len(self.time) == 0:
            raise ValueError('No data has been loaded.')
        lengths = []
        current_length = 0
        for index in range(len(self.data)):
            if index == 0:
                pass
            else:
                if abs(self.data[index-1] - self.data[index]) < tolerance:
                    current_length += 1
                else:
                    lengths.append(current_length)
                    current_length = 0
        index_attention_mean = round(np.mean(lengths))
        try:
            self.avg_att_t = self.time[index_attention_mean]
        except:
            raise ValueError('Corrupted temperature data.')

    def show_avg(self):
        print(
            f'The avergate attention span in the session loaded is'\
            + f'approximately {round(self.avg_att_v)} (voltage) seconds, or'\
            + f'{round(self.avg_att_v / 60)} minutes.'
            )
        print(
            f'The avergate attention span in the session loaded is'\
            + f'approximately {round(self.avg_att_t)} (temperature) seconds,'\
            + f'or {round(self.avg_att_t / 60)} minutes.'
            )