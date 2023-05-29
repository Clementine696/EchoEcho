import sounddevice as sd

# Define the callback function
def audio_callback(indata, frames, time, status):
    pass

# Create a virtual audio device
sd.callback(callback=audio_callback,channels=2,blocksize=1024)

# Get the index of the virtual audio device
virtual_device_index = next((index for (index, d) in enumerate(sd.query_devices())
                             if d["name"] == "Callback Sound Device (2 channels)"), None)