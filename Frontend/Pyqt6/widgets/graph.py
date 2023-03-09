import pyaudio
import queue
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Audio parameters
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = 1024

# Plot parameters
WINDOW_SIZE = 1000  # ms
DOWN_SAMPLE = 1
CHANNELS_TO_PLOT = [0]

# Initialize queue for incoming audio data
q = queue.Queue()

# Calculate number of samples to display in window
window_samples = int(WINDOW_SIZE * RATE / 1000 / DOWN_SAMPLE)

# Initialize plot data
plot_data = np.zeros((window_samples, len(CHANNELS_TO_PLOT)))

# Initialize plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("PyShine")
lines = ax.plot(plot_data, color=(0, 1, 0.29))

def audio_callback(in_data, frame_count, time_info, status):
    """Called by pyaudio whenever new audio data is available"""
    # Convert byte stream to numpy array
    audio_data = np.frombuffer(in_data, dtype=np.float32)

    # Add new audio data to queue
    q.put(audio_data)

    return (None, pyaudio.paContinue)

def update_plot(frame):
    """Called by FuncAnimation to update the plot"""
    global plot_data

    # Get all the available audio data from the queue
    while not q.empty():
        data = q.get()

        # Downsample the data if needed
        if DOWN_SAMPLE > 1:
            data = data[::DOWN_SAMPLE]

        # Update the plot data
        shift = len(data)
        plot_data = np.roll(plot_data, -shift, axis=0)
        plot_data[-shift:, :] = data[:, np.newaxis]

    # Update the plot lines with the new data
    for column, line in enumerate(lines):
        line.set_ydata(plot_data[:, column])

    return lines

# Initialize pyaudio and stream object
pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                 frames_per_buffer=CHUNK_SIZE, stream_callback=audio_callback)

# Initialize the plot
ax.set_facecolor((0, 0, 0))
ax.set_yticks([0])
ax.yaxis.grid(True)

# Start the animation
ani = FuncAnimation(fig, update_plot, interval=30, blit=True)

# Show the plot
plt.show()

# Cleanup
stream.stop_stream()
stream.close()
pa.terminate()
