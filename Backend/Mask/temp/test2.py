import sounddevice as sd

# Define the index of the virtual audio device
virtual_device_index = 30

# Stream the filtered audio data to the virtual audio device
sd.default.device = virtual_device_index
sd.default.channels = 1
sd.default.samplerate = sampling_rate

stream = sd.OutputStream(callback=lambda indata, frames, time, status: indata[:] = filtered_audio)
stream.start()