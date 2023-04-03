import wave
import sounddevice as sd
import keyboard
from math import sqrt
import numpy as np
from scipy import signal

import pyaudio

# initialize PyAudio
p = pyaudio.PyAudio()

# open a stream for microphone
input_stream = p.open(format=pyaudio.paInt16,channels=1,rate=48000,input=True,frames_per_buffer=256,)

# open a stream for playing audio
output_stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, output=True, frames_per_buffer=256)


import librosa
# define the pitch shift factor
pitch_shift_factor = 2 # double the pitch
bins = 12
# calculate the pitch shift amount in semitones
pitch_shift_amount = librosa.hz_to_midi(pitch_shift_factor * librosa.midi_to_hz(0))


import scipy.signal as signal
# define filter parameters
cutoff_freq = 4000  # Hz
filter_order = 10
# create the filter
nyquist_freq = 0.5 * 48000
b, a = signal.butter(filter_order, cutoff_freq/nyquist_freq, btype='lowpass')


audio_data = input_stream.read(2048)
print('running, press z to stop')
print('press a to increase pitch_shift_factor')
print('press b to decrease pitch_shift_factor')
print('press c to increase bins')
print('press b to decrease bins')
while len(audio_data) != 0:

    numpy_data = np.fromstring(audio_data, dtype=np.int16)
    numpy_data_float = numpy_data.astype('float32') / 32767.0 # scale to range [-1, 1]
    # pitch shift the audio data
    pitch_shifted_data = librosa.effects.pitch_shift(numpy_data_float, 48000, n_steps=pitch_shift_amount, bins_per_octave=bins)

    # apply the filter to the pitch shifted data
    filtered_data = signal.filtfilt(b, a, pitch_shifted_data)

    # convert the pitch shifted data to a string for playback
    output_sound = (pitch_shifted_data * 32767).astype(np.int16).tostring()
    # output_sound = pitch_shifted_data.astype(np.int16).tostring()

    output_sound = (pitch_shifted_data * 32767).astype(np.int16).tostring()

    output_stream.write(output_sound)

    audio_data = input_stream.read(2048)

    if keyboard.is_pressed("z"):
        break
    
    if keyboard.is_pressed("a"):
        pitch_shift_factor = pitch_shift_factor + 1
        pitch_shift_amount = librosa.hz_to_midi(pitch_shift_factor * librosa.midi_to_hz(0))
        print('pitch_shift_factor = ', pitch_shift_factor)
    
    if keyboard.is_pressed("b"):
        pitch_shift_factor = pitch_shift_factor - 1
        if pitch_shift_factor < 2:
            pitch_shift_factor = 2
        pitch_shift_amount = librosa.hz_to_midi(pitch_shift_factor * librosa.midi_to_hz(0))
        print('pitch_shift_factor = ', pitch_shift_factor)

    if keyboard.is_pressed("c"):
        bins = bins + 1
        print('bins = ', bins)

    if keyboard.is_pressed("d"):
        bins = bins - 1
        if bins < 2:
            bins = 2
        print('bins = ', bins)
        
# stop the stream
output_stream.stop_stream()
output_stream.close()

# close PyAudio
p.terminate()