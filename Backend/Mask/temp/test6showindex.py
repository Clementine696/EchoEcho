import sounddevice as sd

print(sd.query_devices(device=None, kind=None))

#0 > input
#1 > output
print(sd.default.device[1])