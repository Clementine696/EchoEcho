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
    outdata[:] = indata
    
    fft_indata = np.abs(fft(indata[:, 0]))
    # Process the data
    # for example, you can apply a low-pass filter
        # cutoff_freq = 1000
        # fft_indata[cutoff_freq:] = 0
    # Inverse FFT to get back to time domain
    # filtered_indata = np.real(np.fft.ifft(fft_indata))
    # filtered_indata = filtered_indata.reshape(np.shape(indata)[0],1)
    # print(np.shape(filtered_indata))
    # outdata[:] = filtered_indata
    
    # plt.plot(filtered_indata)
    # plt.show()

def main():
    run = 0
    stream = sd.Stream(samplerate=44100, blocksize=1024, dtype=np.float32,
                    channels=2, callback=callback)
    print('')
    print('Press X to exit program')
    print('Press M to toggle microphone test')
    print("Program is running")
    while keyboard.is_pressed('x')==0:
        if keyboard.is_pressed('m'):
            # quit()
            if(run==0):
                run = 1
                stream.start()
                time.sleep(0.1)
                print('start mic test')
            else:
                run = 0
                stream.stop()
                time.sleep(0.1)
                print('stop mic test')
    print("stop running")
        # if keyboard.is_pressed('n'):
        #     # quit()
        #     if(Denoise==1):
        #         Denoise = Denoise + 1
        #         time.sleep(0.1)
        #     else:
        #         Denoise = Denoise - 1
        #         time.sleep(0.1)
                

if __name__ == '__main__':
    main()