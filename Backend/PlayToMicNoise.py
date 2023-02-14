import pyaudio
import wave
import sounddevice as sd
import keyboard

import numpy as np
import noisereduce as nr

# initialize PyAudio
p = pyaudio.PyAudio()
vb_index = p.get_default_output_device_info()['index']
#Search for virtual microphone index

device_list = sd.query_devices()
for i in (device_list):
    if "CABLE Input " in i['name']:
        vb_index = i['index']
        break

# if()...

#open a stream for microphone 
input_stream = p.open(format=pyaudio.paInt16,
                      channels=1,
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
# wf = wave.open("Backend/sound/Cheer.wav", "rb")
# start playing the audio
#read microphone "NEW"
# audio_data = input_stream.read(1024)

from threading import Thread
def threaded_function():
    print('Press X to stop')
    wf = wave.open("Backend/sound/Cheer.wav", "rb")
    data = wf.readframes(1024)
    while len(data) != 0:
        data = wf.readframes(1024)
        output_stream.write(data)
        if(keyboard.is_pressed('x')):
          break

def threaded_function2():
    audio_data = input_stream.read(1024)
    while len(audio_data) != 0:
        audio_data = input_stream.read(1024)

        #Noise suppression
        # if(nr):
        #     audio_frame = np.frombuffer(input_data, dtype=np.int16)
        #     reduced_noise = nr.reduce_noise(audio_frame, sr=44100)
        #     suppressed_audio_data = reduced_noise.tobytes()

        audio_frame = np.frombuffer(input_data, dtype=np.int16)
        reduced_noise = nr.reduce_noise(audio_frame, sr=44100)
        suppressed_audio_data = reduced_noise.tobytes()

        output_stream.write(suppressed_audio_data)
        if(keyboard.is_pressed('z')):
          break
    # while(keyboard.is_pressed('x')==0):
    #     break


while True:
    # Read input microphone data
    input_data = input_stream.read(1024)
    # Perform noise reduction
    audio_frame = np.frombuffer(input_data, dtype=np.int16)
    reduced_noise = nr.reduce_noise(audio_frame, sr=44100)
    audio_data = reduced_noise.tobytes()
    # Write the audio data to the output microphone stream
    output_stream.write(audio_data)




# threadA = Thread(target = threaded_function)
# threadA.start()
# threadA.join()

threadB = Thread(target = threaded_function2)
threadB.start()
threadB.join()


output_stream.start_stream()
# while output_stream.is_active():
#     # data = wf.readframes(1024)
#     # output_stream.write(data)
#     #MicVoice
#     print('running')
    # audio_data = input_stream.read(1024)
    # output_stream.write(audio_data)




# stream.start_stream()
# while stream.is_active():
#     data = wf.readframes(1024)
#     stream.write(data)
#     if len(data) == 0:
#         break

# stop the stream
output_stream.stop_stream()
output_stream.close()

# close PyAudio
p.terminate()