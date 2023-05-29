import sounddevice as sd
import time
# Define the callback function that will be called when the virtual device is used
def audio_callback(outdata, frames, time, status):
    # Get the audio data from another process or application here
    pass

# Create a virtual audio output device
virtual_output = sd.OutputStream(callback=audio_callback,
                                channels=2,
                                samplerate=44100)

virtual_output.start()

# Do some processing here
i = 0
while(1):
    print("running")
    time.sleep(1)
    print(i)
    i = i + 1
# Stop the virtual audio output device
virtual_output.stop()
