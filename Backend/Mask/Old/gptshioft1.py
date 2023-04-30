import pyaudio
import librosa, time
import soundfile as sf
import numpy as np

# Parameters for pitch shifting
sr = 44100  # sampling rate
n_steps = 3  # pitch shift in semitones
bins_per_octave = 12  # number of frequency bins per octave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = sr
RECORD_SECONDS = 10
swidth = 2

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=chunk)

print("* recording")

start = time.time()
while (time.time() - start < RECORD_SECONDS):
    data = stream.read(chunk)
    data = np.array(
        np.frombuffer(data, dtype=np.int16)
    )  # convert data to numpy array of integers

    # Apply pitch shift in real time
    # data = librosa.effects.pitch_shift(data, sr, n_steps=n_steps, bins_per_octave=bins_per_octave, preserve=True)
    data = librosa.effects.pitch_shift(data, sr, n_steps=4)

    # Convert data back to 16-bit integer format and write to output stream
    dataout = np.array(data, dtype=np.int16)
    chunkout = dataout.tobytes()
    stream.write(chunkout)

print("* done")

stream.stop_stream()
stream.close()
p.terminate()