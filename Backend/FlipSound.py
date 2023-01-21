# run RecAndSave.py first
import wave
import numpy as np

# เอาไฟล์ output.wav เก่ามากลับเสียง
with wave.open('output.wav', 'r') as wav_file:
    audio_data = wav_file.readframes(-1)
    audio_data = audio_data[::-1]
    with wave.open('flip.wav', 'w') as output_file:
        output_file.setsampwidth(wav_file.getsampwidth())
        output_file.setnchannels(wav_file.getnchannels())
        output_file.setframerate(wav_file.getframerate())
        output_file.writeframes(audio_data)

print("* flip complete")

# with wave.open('output.wav', 'r') as original_file:
#     original_data = original_file.readframes(-1)
#     original_data = np.frombuffer(original_data, np.int16)
#     original_channels = original_file.getnchannels()
#     original_rate = original_file.getframerate()
#     original_sample_width = original_file.getsampwidth()

# with wave.open('flip.wav', 'r') as flip_file:
#     flip_data = flip_file.readframes(-1)
#     flip_data = np.frombuffer(flip_data, np.int16)
#     flip_channels = flip_file.getnchannels()
#     flip_rate = flip_file.getframerate()
#     flip_sample_width = flip_file.getsampwidth()

# if original_channels == 2 and flip_channels == 2:
#     mixed_data = np.column_stack((original_data, flip_data))
# elif original_channels == 1 and flip_channels == 1:
#     mixed_data = original_data + flip_data
# else:
#     raise ValueError("Both files must have the same number of channels (1 or 2)")

# with wave.open('mixed.wav', 'w') as mixed_file:
#     mixed_file.setsampwidth(original_sample_width)
#     mixed_file.setnchannels(original_channels)
#     mixed_file.setframerate(original_rate)
#     mixed_file.writeframes(mixed_data.tobytes())
#     mixed_data = original_data * 0.8 + flip_data * 0.2

with wave.open('output.wav', 'r') as wav_file1, wave.open('flip.wav', 'r') as wav_file2:
    audio_data1 = wav_file1.readframes(-1)
    audio_data2 = wav_file2.readframes(-1)
    audio_data1 = np.frombuffer(audio_data1, np.int16)
    audio_data2 = np.frombuffer(audio_data2, np.int16)
    mixed_audio = audio_data1 + audio_data2
    mixed_audio = np.asarray(mixed_audio, np.int16)
    with wave.open('mixed.wav', 'w') as output_file:
        output_file.setsampwidth(wav_file1.getsampwidth())
        output_file.setnchannels(wav_file1.getnchannels())
        output_file.setframerate(wav_file1.getframerate())
        output_file.writeframes(mixed_audio.tobytes())

print("* mix complete")
# อย่าพึ่งลองนะ หูแตกไอเหี้ย