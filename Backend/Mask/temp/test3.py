import sounddevice as sd

# Define the input and output devices
input_device = sd.default.device[1]
output_device = sd.default.device[4]

# Define the callback function that will handle audio data
def callback(indata, frames, time, status):
    sd.default.callback(indata, frames, time, status)

# Start the virtual microphone
with sd.InputStream(callback=callback, device=input_device):
    sd.OutputStream(callback=callback, device=output_device).start()
    sd.sleep(duration * 1000)