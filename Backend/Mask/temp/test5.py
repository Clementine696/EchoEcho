from pydub import AudioSegment
from pydub.generators import Sine

# Generate a sine wave with a frequency of 440 Hz and a duration of 10 seconds
sine_wave = Sine(440).to_audio_segment(duration=10000)

# Use Pyaudio to play the sine wave through a virtual microphone device
import pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(sine_wave.sample_width),
                channels=sine_wave.channels,
                rate=sine_wave.frame_rate,
                output=True,
                output_device_index=2)
stream.start_stream()
# stream.write(sine_wave.raw_data)
stream.stop_stream()
stream.close()
p.terminate()