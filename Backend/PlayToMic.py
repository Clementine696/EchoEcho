import pyaudio
import wave
import sounddevice as sd

#Search for virtual microphone index
device_list = sd.query_devices()
for i in (device_list):
    if "CABLE Input " in i['name']:
        vb_index = i['index']
        break

# initialize PyAudio
p = pyaudio.PyAudio()

#open a stream for microphone 
input_stream = p.open(format=pyaudio.paInt16,
                      channels=2,
                      rate=44100,
                      input=True,
                    #   input_device_index=input_device_index,
                      frames_per_buffer=1024)

# open a stream for playing audio
output_stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=True,
                frames_per_buffer=1024,
                output_device_index=vb_index)

# open the audio file to be played
# wf = wave.open("Backend/sound/StarWars60.wav", "rb")
wf = wave.open("Backend/sound/Cheer.wav", "rb")
# start playing the audio

#read microphone "NEW"
audio_data = input_stream.read(1024)

output_stream.start_stream()
while output_stream.is_active():
    data = wf.readframes(1024)
    output_stream.writoutput_streame(data)
    if len(data) == 0:
        break

# stop the stream
output_stream.stop_stream()
output_stream.close()

# close PyAudio
p.terminate()