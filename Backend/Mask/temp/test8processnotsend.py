import pyaudio
import numpy as np

p = pyaudio.PyAudio()

# Get the default input device
info = p.get_default_input_device_info()

# Open a new audio input stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=info['index'])

# Start Recording
stream.start_stream()

while True:
    # Read the audio data
    data = stream.read(1024)

    # Convert the audio data from bytes to a numpy array
    audio_data = np.fromstring(data, dtype=np.int16)

    # Pass the audio data to another application or process here

    # Break the loop if the stream is stopped
    if not stream.is_active():
        break

# Stop Recording
stream.stop_stream()

# Close the stream
stream.close()
p.terminate()
