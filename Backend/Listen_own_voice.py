import sounddevice as sd
import numpy as np
import time
import keyboard
import os
from scipy.fft import fft
import matplotlib.pyplot as plt

# def callback(indata, outdata, frames, channels, time, status):
def callback(indata, outdata, frames, time, status):
# def callback(indata, outdata, frames, channels, time):
    if status:
        print(status)
        
    # fft_indata = np.abs(fft(indata[:, 0]))
    # print(np.shape(outdata[:]))
    # outdata[:] = indata
    
    fft_indata = np.abs(fft(indata[:, 0]))
    # Process the data
    # for example, you can apply a low-pass filter
    cutoff_freq = 1000
    fft_indata[cutoff_freq:] = 0
    # Inverse FFT to get back to time domain
    filtered_indata = np.real(np.fft.ifft(fft_indata))
    filtered_indata = filtered_indata.reshape(np.shape(indata)[0],1)
    # print(np.shape(filtered_indata))
    outdata[:] = filtered_indata
    
    plt.plot(filtered_indata)
    plt.show()

def main():
    with sd.Stream(samplerate=44100, blocksize=1024, dtype=np.float32,
                    channels=2, callback=callback):
        while True:
            if keyboard.is_pressed('q'):
                # quit()
                sd.Stream.stop()
                
            # ! ไม่เข้าใจว่า time.sleep (1000) กับ  (0) มีผลต่างกันอย่างไร
            # time.sleep(1000)
            
if __name__ == '__main__':
    main()