import sounddevice as sd

I_device = sd.query_devices(kind = "input")
O_device = sd.query_devices(kind = "output")
print(I_device)
print(O_device)