# tempo_detection.py
import librosa

# Load the audio file
audio_file = "audio/CINDERVOMIT.wav"

# Load audio data and sampling rate
y, sr = librosa.load(audio_file)

# Calculate tempo
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

print(f"Tempo/BPM: {tempo}")

