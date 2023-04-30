import pyaudio
import sys, time
import numpy as np
import wave
import librosa
n = 3 # this is how the pitch should change, positive integers increase the frequency, negative integers decrease it.
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 41000
RECORD_SECONDS = 10
swidth = 2
 
p = pyaudio.PyAudio()
 
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)
 
 
print("* recording")
 
start = time.time()
while(time.time()-start < RECORD_SECONDS):
 
    data = stream.read(chunk)
    data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))
 
    # do real fast Fourier transform 
    data = np.fft.rfft(data)
    
    # This does the shifting
    data = librosa.effects.pitch_shift(data, 44100, n_steps=4)
    
    data = np.array(data)
    # Done shifting
    
    # inverse transform to get back to temporal data
    data = np.fft.irfft(data)
    
    dataout = np.array(data, dtype='int16') 
    chunkout = wave.struct.pack("%dh"%(len(dataout)), *list(dataout)) #convert back to 16-bit data
    stream.write(chunkout)
 
    
 
 
print("* done")
 
stream.stop_stream()
stream.close()
p.terminate()