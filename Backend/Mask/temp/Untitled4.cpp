#include <Windows.h>
IMMDeviceEnumerator* deviceEnumerator = NULL;
HRESULT hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), NULL, CLSCTX_ALL, __uuidof(IMMDeviceEnumerator), (void**)&deviceEnumerator);
if (FAILED(hr)) {
    // handle error
}
IAudioClient* audioClient = NULL;
IMMDevice* defaultDevice = NULL;
hr = deviceEnumerator->GetDefaultAudioEndpoint(eCapture, eMultimedia, &defaultDevice);
if (FAILED(hr)) {
    // handle error
}
hr = defaultDevice->Activate(__uuidof(IAudioClient), CLSCTX_ALL, NULL, (void**)&audioClient);
if (FAILED(hr)) {
    // handle error
}
WAVEFORMATEX* waveFormat;
hr = audioClient->GetMixFormat(&waveFormat);
if (FAILED(hr)) {
    // handle error
}
hr = audioClient->Initialize(AUDCLNT_SHAREMODE_SHARED, 0, 5000000, 0, waveFormat, NULL);
if (FAILED(hr)) {
    // handle error
}
IAudioCaptureClient* audioCaptureClient = NULL;
hr = audioClient->GetService(__uuidof(IAudioCaptureClient), (void**)&audioCaptureClient);
if (FAILED(hr)) {
    // handle error
}
hr = audioClient->Start();
if (FAILED(hr)) {
    // handle error
}
UINT32 packetLength = 0;
BYTE* data = NULL;
while (true) {
    hr = audioCaptureClient->GetNextPacketSize(&packetLength);
    if (FAILED(hr)) {
        // handle error
    }
    if (packetLength == 0) {
        break;
    }
    hr = audioCaptureClient->GetBuffer(&data, &packetLength, NULL, NULL, NULL);
    if (FAILED(hr)) {
       
