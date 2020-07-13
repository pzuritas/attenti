from data_recv_wired import DataReceiver
from data_recv_wireless import WiFiDataReceiver


# Example script
reciever = DataReceiver()
session_length = 1000
reciever.capture_start(session_length)
reciever.add_capture()
reciever.save_capture()

time_0 = float(input('Enter first stimulus time:'))
while time_0 not > 0:
    time_0 = float(input('Enter first stimulus time:'))
time_1 = float(input('Enter second stimulus time:'))
while time_1 not > 0:
    time_1 = float(input('Enter second stimulus time:'))
time_2 = float(input('Enter third stimulus time:'))
while time_2 not > 0:
    time_2 = float(input('Enter third stimulus time:'))

times = [time_0, time_1, time_2]

reciever.plot_session('test_plot', show=True, times=times)

# Example script for WiFi
'''
receiver = WiFiDataReceiver()
session_length = 1000
reciever.capture_start(session_length)
reciever.add_capture()
reciever.save_capture()
reciever.plot_session('test_plot', show=True)
'''