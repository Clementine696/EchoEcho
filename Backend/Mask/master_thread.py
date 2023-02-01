import sounddevice as sd
import numpy as np
import time
import keyboard
import os
from scipy.fft import fft
import matplotlib.pyplot as plt
from threading import Thread


def threaded_function(value):
    while True:
        print("thread running", value)
        time.sleep(1)

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
        # cutoff_freq = 1000
        # fft_indata[cutoff_freq:] = 0
    # Inverse FFT to get back to time domain
    filtered_indata = np.real(np.fft.ifft(fft_indata))
    filtered_indata = filtered_indata.reshape(np.shape(indata)[0],1)
    # print(np.shape(filtered_indata))
    outdata[:] = filtered_indata
    
    # plt.plot(filtered_indata)
    # plt.show()

def main():
    run = 1
    AppThread = Thread(target = threaded_function, args = (1, ))
    AppThread.start()
    AppThread.join()
    with sd.Stream(samplerate=44100, blocksize=1024, dtype=np.float32,
                    channels=2, callback=callback):
        while True:
            if keyboard.is_pressed('m'):
                # quit()
                if(run==1):
                    run = run + 1
                    AppThread.args = (0, )
                    time.sleep(0.5)
                else:
                    run = run - 1
                    AppThread = Thread(target = threaded_function, args = (1, ))
                    time.sleep(0.5)
            print("running", run)
            
                # sd.Stream.stop()
        
            # ! ไม่เข้าใจว่า time.sleep (1000) กับ  (0) มีผลต่างกันอย่างไร
            # time.sleep(1000)
            
            
if __name__ == '__main__':
    main()