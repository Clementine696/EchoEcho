import wave
import sounddevice as sd
import keyboard

import numpy as np

import pyaudio

# initialize PyAudio
p = pyaudio.PyAudio()

# open a stream for microphone
input_stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    #   input_device_index=input_device_index,
    frames_per_buffer=1024,
)

# open a stream for playing audio
output_stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer=1024
)


audio_data = input_stream.read(1024)
print('running press z to stop')
while len(audio_data) != 0:
    audio_data = input_stream.read(1024)
    output_stream.write(audio_data)
    if keyboard.is_pressed("z"):
        break
# stop the stream
output_stream.stop_stream()
output_stream.close()

# close PyAudio
p.terminate()