
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 15

def record_audio():
    audio = pyaudio.PyAudio()

    # Open input stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Start Recording...")

    frames = []

    # recording
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))

    print("Time is up!.")

    # Stop  
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return np.hstack(frames)

def plot_waveform(signal):
    plt.figure(figsize=(10, 4))
    plt.plot(signal)
    plt.title("Audio waveforms")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.show()

if __name__ == "__main__":
    audio_data = record_audio()
    plot_waveform(audio_data)