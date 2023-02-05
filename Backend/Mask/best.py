import pyaudio
import keyboard
import wave

# Create a PyAudio object
p = pyaudio.PyAudio()

# Get the index of the default input device
input_device_index = p.get_default_input_device_info()['index']

# Open a stream to the default input device
input_stream = p.open(format=pyaudio.paInt16,
                      channels=2,
                      rate=44100,
                      input=True,
                      input_device_index=input_device_index,
                      frames_per_buffer=1024)


# Create a virtual output device
output_device_index = p.get_default_output_device_info()['index']
output_stream = p.open(format=pyaudio.paInt16,
                      channels=2,
                      rate=44100,
                      output=True,
                      output_device_index=output_device_index,
                      frames_per_buffer=1024)

# Start a loop to read audio from the input stream and write it to the output stream
print('running')
while output_stream.is_active():
    audio_data = input_stream.read(1024)
    output_stream.write(audio_data)
    if(keyboard.is_pressed('s')):
        print('Starwar')
        wf = wave.open("Backend/sound/StarWars60.wav", "rb")
        data = wf.readframes(1024)
        output_stream.write(data)
        if len(data) == 0:
            break
    if(keyboard.is_pressed('x')):
        break
# Close the streams and terminate the PyAudio object when done
print('stop and terminate program')
input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()
p.terminate()
