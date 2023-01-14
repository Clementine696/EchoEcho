import pyaudio
import wave

# initialize PyAudio
p = pyaudio.PyAudio()

# open a stream for playing audio
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=True,
                frames_per_buffer=1024)

# open the audio file to be played
wf = wave.open("Backend/sound/StarWars60.wav", "rb")

# start playing the audio

stream.start_stream()
while stream.is_active():
    data = wf.readframes(1024)
    stream.write(data)
    if len(data) == 0:
        break

# stop the stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()