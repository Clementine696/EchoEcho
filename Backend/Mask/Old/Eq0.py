import numpy as np
import pyaudio
import wave
import soundfile as sf
from scipy.signal import freqs, iirfilter

def equalizer(signal, bands, gain):
    """Applies a graphic equalizer to an audio signal"""
    # Divide the audio signal into frequency bands
    bands = np.array(bands)
    low_frequencies = signal[(signal.freq >= bands[:-1][::-1]).sum(axis=1)]
    high_frequencies = signal[(signal.freq < bands[1:][::-1]).sum(axis=1)]
    # Apply the gain to each band
    low_frequencies *= 10**(gain[0] / 20)
    high_frequencies *= 10**(gain[1] / 20)
    # Combine the bands back into a single audio signal
    equalized_signal = np.concatenate((low_frequencies, high_frequencies))
    return equalized_signal

# Load an audio file
# wf = wave.open("Backend/sound/Cheer.wav", "rb")
# data = wf.readframes(1024)

data = sf.read('Backend/sound/Cheer.wav') 
# signal = load_audio_file("audio_file.wav")
# Define the frequency bands
bands = [0, 100, 1000, 10000, 20000]
# Define the gain for each band
gain = [0, 0, 0, 0, 0]
# Apply the equalizer to the audio signal
equalized_signal = equalizer(data, bands, gain)

# Play the equalized audio
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(data.sample_width),
                channels=data.channels,
                rate=data.sample_rate,
                output=True)

stream.start_stream()
stream.write(equalized_signal.tobytes())
stream.stop_stream()
stream.close()
p.terminate()