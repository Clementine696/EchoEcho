#https://python-sounddevice.readthedocs.io/en/0.3.15/api/checking-hardware.html#sounddevice.check_input_settings
print("sounddevice")
import sounddevice as sd
print(sd.query_devices(device=None, kind=None))
# print(sd.query_hostapis(index=None))
# print(sd.check_input_settings(device=None, channels=None, dtype=None, extra_settings=None, samplerate=None))
# print(sd.check_output_settings(device=None, channels=None, dtype=None, extra_settings=None, samplerate=None))


#https://stackoverflow.com/questions/20760589/list-all-audio-devices-with-pythons-pyaudio-portaudio-binding
# print("pyaudio")
# import pyaudio
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print (p.get_device_info_by_index(i))