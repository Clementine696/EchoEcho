import pyaudio
import numpy as np
from scipy import signal

# Define the cutoff frequency of the low-pass filter
cutoff_freq = 10000 # in Hz

# Define the sampling rate of the audio data
sampling_rate = 44100 # in samples per second

# Define the order of the filter (higher order = more filtering)
filter_order = 4

# Create the low-pass filter coefficients
b, a = signal.butter(filter_order, cutoff_freq, btype='low', 
                    analog=False, output='ba', fs=sampling_rate)

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open a microphone input stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sampling_rate, input=True, frames_per_buffer=1024)

while True:
    # Read audio data from the microphone
    microphone_input = stream.read(1024)
    # Convert the microphone input to a NumPy array
    microphone_input = np.fromstring(microphone_input, dtype=np.int16)
    # Apply the low-pass filter to the microphone input
    filtered_audio = signal.lfilter(b, a, microphone_input)
    # Do something with the filtered audio
    # ...

# Close the microphone input stream
stream.stop_stream()
stream.close()
p.terminate()