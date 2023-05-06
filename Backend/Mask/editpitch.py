import wave
import sounddevice as sd
import keyboard
from math import sqrt
import numpy as np
from scipy import signal

import pyaudio
import librosa

# initialize PyAudio
p = pyaudio.PyAudio()

# open a stream for microphone
input_stream = p.open(format=pyaudio.paInt16,channels=1,rate=48000,input=True,frames_per_buffer=2048)

# open a stream for playing audio
output_stream = p.open(format=pyaudio.paInt16, channels=1, rate=48000, output=True, frames_per_buffer=2048)

# define the pitch shift amount in semitones
pitch_shift_factor = 2 # double the pitch
bins = 12
hz = 0
# calculate the pitch shift amount in semitones
pitch_shift_amount = librosa.hz_to_midi(pitch_shift_factor * librosa.midi_to_hz(hz))

###1
import scipy.signal as signal
# define filter parameters
cutoff_freq = 4000  # Hz
filter_order = 10
# create the filter
nyquist_freq = 0.5 * 48000
b, a = signal.butter(filter_order, cutoff_freq/nyquist_freq, btype='lowpass')

####2
# import numpy as np
from scipy import signal

# define notch filter parameters
notch_freq = 60.0  # Hz
quality_factor = 30.0

# create notch filter coefficients
d, c = signal.iirnotch(notch_freq, quality_factor, fs=48000)

audio_data = input_stream.read(2048)
print('running press z to stop')
while len(audio_data) != 0:

    numpy_data = np.fromstring(audio_data, dtype=np.int16)
    numpy_data_float = numpy_data.astype('float32') / 32767.0 # scale to range [-1, 1]
    
    # get the pitch of the input audio
    # pitches, magnitudes = librosa.core.piptrack(y=numpy_data_float, sr=48000)
    # pitch = pitches[np.argmax(magnitudes)]
    
    # # calculate the pitch shift amount in semitones
    # chroma = librosa.hz_to_chroma(pitch)
    # pitch_shift_amount = librosa.midi_to_hz(librosa.util.midi_to_note(chroma)) - pitch
    
    # pitch shift the audio data
    pitch_shifted_data = librosa.effects.pitch_shift(numpy_data_float, sr = 48000, n_steps=pitch_shift_amount, bins_per_octave=12)

    # filtered_data = signal.filtfilt(b, a, pitch_shifted_data)
    # filtered_data = signal.filtfilt(d, c, filtered_data)

    # convert the pitch shifted data to a string for playback
    output_sound = (pitch_shifted_data * 32767).astype(np.int16).tostring()

    output_stream.write(output_sound)

    audio_data = input_stream.read(2048)
    
    if keyboard.is_pressed("z"):
        break

# stop the stream
output_stream.stop_stream()
output_stream.close()

# close PyAudio
p.terminate()
