import pyaudio

p = pyaudio.PyAudio()

print(p.get_default_input_device_info())
# create the virtual device
device_index = p.get_default_input_device_info()['index']
