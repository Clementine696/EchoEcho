import sounddevice as sd
import numpy as np
import time
import keyboard
import os

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

def main():
    with sd.Stream(samplerate=44100, blocksize=1024, dtype=np.float32,
                    channels=2, callback=callback):
        while True:
            if keyboard.is_pressed('q'):
                quit()
                
            # ! ไม่เข้าใจว่า time.sleep 1000 กับ  0 มีผลต่างกันอย่างไร
            time.sleep(0)
            
if __name__ == '__main__':
    main()
    if keyboard.is_pressed('q'):
                quit()
    