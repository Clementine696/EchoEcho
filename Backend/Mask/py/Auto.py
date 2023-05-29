import pyaudio
import numpy as np
import aubio
import time

# initialize PyAudio
p = pyaudio.PyAudio()

# open a stream for microphone
input_stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# open a stream for playing audio
output_stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

# initialize pitch detection
win_s = 4096
hop_s = 512
t = aubio.pitch("yin", win_s, hop_s, 44100)
t.set_tolerance(0.8)

# initialize Auto-Tune parameters
target_pitch = 440.0  # A440Hz
scale = 1.0  # no transposition
win_size = 4096
hop_size = 512
buffersize = hop_size * 4
overlap = buffersize - hop_size
auto_tune = aubio.autotuner(win_size, hop_size, 44100)
auto_tune.set_target(target_pitch)
auto_tune.set_scale(scale)

print("Auto-Tune is ready! Press 'q' to quit.")

while True:
    # read input audio
    input_data = input_stream.read(buffersize, exception_on_overflow=False)
    x = np.frombuffer(input_data, dtype=np.float32)

    # pitch detection
    pitch = t(x)[0]

    # Auto-Tune processing
    if pitch != 0:
        transposition = 12 * np.log2(pitch / target_pitch)
        auto_tune.set_trans(transposition)
        y = auto_tune(x)
    else:
        y = x

    # write output audio
    output_data = y.tobytes()
    output_stream.write(output_data)

    # check if user pressed 'q'
    if input("Press 'q' to quit") == 'q':
        break

# stop the streams
input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()

# close PyAudio
p.terminate()
