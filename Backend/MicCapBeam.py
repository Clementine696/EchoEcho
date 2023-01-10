# Source from https://www.youtube.com/watch?v=n8ebYr25LO0

import sounddevice as sd
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# หาก SetMasterVolumeLevel  = 0.0 volume จะเป็น 100 และ SetMasterVolumeLevel  = -61 (65.25) volume จะเป็น 0
# volume.SetMasterVolumeLevel(-61, None)
# volume.SetMasterVolumeLevel(0, None)

#SetMute ลำโพง หากเป็น 0 เปิดลำโพง และเป็น 1 จะปิดลำโพง 
volume.SetMute(0, None)
# volume.SetMute(1, None)

current = volume.GetMasterVolumeLevel()
print("Current Value MasterVolumeLevel: ", current )
# หากจะปรับ volume ที่ละ 1 ให้ปรับตวามต่างไปที่ 0.151 หรือ -0.15066957473754883

# ปรับ volume ลง
volume.SetMasterVolumeLevel(current - 0.15066957473754883, None)

# ปรับ volume ขึ้น
# volume.SetMasterVolumeLevel(current + 0.151, None)

# หากจะปรับ volume ที่ละ 5 ให้ปรับตวามต่างไปที่ 0.755 หรือ -0.7533478736877442

# ปรับ volume ลง
# volume.SetMasterVolumeLevel(current - 0.7533478736877442, None)

# ปรับ volume ขึ้น
# volume.SetMasterVolumeLevel(current + 0.755, None)


sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    print (session.Process.name())
    # if session.Process and session.Process.name() == "brave.exe":
    #     volume.SetMasterVolume(0.5 ,None)
    


# devices = sd.query_devices()
# # I_device = sd.query_devices(kind = "input")
# # O_device = sd.query_devices(kind = "output")
# # print(I_device)
# # print(O_device)