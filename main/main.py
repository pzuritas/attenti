from data_recv_wired import DataReceiver
from data_recv_wireless import WiFiDataReceiver


# Example script
reciever = DataReceiver()
session_length = 1000
reciever.capture_start(session_length)
reciever.add_capture()
reciever.save_capture()
reciever.plot_session('test_plot', show=True)

# Example script for WiFi
'''
receiver = WiFiDataReceiver()
session_length = 1000
reciever.capture_start(session_length)
reciever.add_capture()
reciever.save_capture()
reciever.plot_session('test_plot', show=True)
'''