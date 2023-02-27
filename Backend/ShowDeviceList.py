#https://python-sounddevice.readthedocs.io/en/0.3.15/api/checking-hardware.html#sounddevice.check_input_settings
# print("sounddevice")

import sounddevice as sd
# print(sd.query_devices(device=None, kind=None))


device = sd.query_devices(device=None, kind=None)

# # print(device)

for i in device:
    # print(i['hostapi'])
    print(i['name'][0:30])


# from PyQt5.QtMultimedia import QAudioDeviceInfo,QAudio
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, IMMDevice

# all_devices = AudioUtilities.GetAllDevices()
# for device in all_devices:
#     if(device.DeviceType == 1):
#         print(device)

# input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)
# for i in input_audio_deviceInfos:
#     print(i.deviceName())

# print(sd.query_hostapis(index=None))
# print(sd.check_input_settings(device=None, channels=None, dtype=None, extra_settings=None, samplerate=None))
# print(sd.check_output_settings(device=None, channels=None, dtype=None, extra_settings=None, samplerate=None))


# from PyQt5.QtMultimedia import QAudioDeviceInfo,QAudio
# #https://stackoverflow.com/questions/20760589/list-all-audio-devices-with-pythons-pyaudio-portaudio-binding
# # print("pyaudio")
# output_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioOutput)

# devicesOutput_list = []
# for device in output_audio_deviceInfos:
#     if device.deviceName() not in devicesOutput_list and "Virtual Cable" not in device.deviceName():
#         devicesOutput_list.append(device.deviceName())

# print(devicesOutput_list)

# print('')

# import pyaudio
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     # print (f"'{p.get_device_info_by_index(i)['name']}'")
#     print (p.get_device_info_by_index(i)['name'])

# for i in range(p.get_device_count()):
#     if(p.get_device_info_by_index(i)['name']) in devicesOutput_list:
#         print(p.get_device_info_by_index(i))
    