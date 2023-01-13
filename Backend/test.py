import noisereduce as nr
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

# Open the input microphone stream
input_stream = p.open(format=pyaudio.paInt16,
                      channels=1,
                      rate=44100,
                      input=True,
                      frames_per_buffer=1024)

# Open the output microphone stream
output_stream = p.open(format=pyaudio.paInt16,
                       channels=1,
                       rate=44100,
                       output=True)

while True:
    # Read input microphone data
    input_data = input_stream.read(1024)
    # Perform noise reduction
    audio_frame = np.frombuffer(input_data, dtype=np.int16)
    reduced_noise = nr.reduce_noise(audio_frame, sr=44100)
    audio_data = reduced_noise.tobytes()
    # Write the audio data to the output microphone stream
    output_stream.write(audio_data)

input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()
p.terminate()