import csv
import numpy as np
import scipy as sp


class DataProcessor():
    '''Wrapper for estimating attention span.'''
    def __init__(self):
        self.time = []
        self.data = []
        self.avg_att = 0
    
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
        indices = sp.signal.find_peaks(self.data, threshold)
        timestamps = [self.time[i] for i in indices]
        self.avg_att = np.mean(np.diff(timestamps))

    def show_avg(self):
        print(
            f'The avergate attention span in the session loaded is'\
            + f'approximately {round(self.avg_att)} seconds, or'\
            + f'{round(self.avg_att / 60)} minutes.'
            )