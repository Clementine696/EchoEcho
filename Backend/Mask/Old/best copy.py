import pyaudio
import keyboard
import wave

# Create a PyAudio object
p = pyaudio.PyAudio()

# Create a virtual output device
output_device_index = p.get_default_output_device_info()['index']
output_stream = p.open(format=pyaudio.paInt16,
                      channels=1,
                      rate=44100,
                      output=True,
                      output_device_index=output_device_index,
                      frames_per_buffer=1024)

# Start a loop to read audio from the input stream and write it to the output stream
print('running')
wf = wave.open("Backend/sound/StarWars60.wav", "rb")
data = wf.readframes(1024)

while len(data) != 0:
    output_stream.write(data)
    data = wf.readframes(1024)
    if(keyboard.is_pressed('x')):
        break

# Close the streams and terminate the PyAudio object when done
print('stop and terminate program')
output_stream.stop_stream()
output_stream.close()
p.terminate()
