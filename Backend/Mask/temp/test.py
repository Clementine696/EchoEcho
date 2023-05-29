import sounddevice as sd
import numpy as np
from scipy import signal

# Define the cutoff frequency of the low-pass filter
cutoff_freq = 3000 # in Hz

# Define the sampling rate of the audio data
sampling_rate = 44100 # in samples per second

# Define the order of the filter (higher order = more filtering)
filter_order = 4

# Create the low-pass filter coefficients
b, a = signal.butter(filter_order, cutoff_freq, btype='low', 
                    analog=False, output='ba', fs=sampling_rate)

# Define the index of the microphone and target application audio device
microphone_device_index = 0
target_application_device_index = 1

# Connect microphone input to the target application audio device using sounddevice
sd.default.device = microphone_device_index
sd.default.channels = 1
sd.default.callback = lambda indata, frames, time, status: filtered_audio = signal.lfilter(b, a, indata)
sd.default.dtype = 'float32'

# Start the audio stream
stream = sd.OutputStream(callback=lambda indata, frames, time, status: indata[:] = filtered_audio,
                        device = target_application_device_index)
stream.start()