import sounddevice as sd
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

# Source from https://www.youtube.com/watch?v=n8ebYr25LO0
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.SetMasterVolumeLevel(-1, None)
# volume.SetMute(0, None)

current = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(current + 6.0, None)

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    # print (session.Process.name())
    if session.Process and session.Process.name() == "brave.exe":
        volume.SetMasterVolume(0.5 ,None)
    


# devices = sd.query_devices()
# # I_device = sd.query_devices(kind = "input")
# # O_device = sd.query_devices(kind = "output")
# # print(I_device)
# # print(O_device)