# tempo_detection.py
import librosa

def detect_tempo(audio_file):
    # Load audio data and sampling rate with downsampling
    y, sr = librosa.load(audio_file, sr=22050, mono=True, res_type='kaiser_fast')

    # Calculate tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    return tempo

if __name__ == "__main__":
    audio_file = "audio/CINDERVOMIT.wav"
    tempo = detect_tempo(audio_file)
    print(f"Estimated Tempo/BPM: {tempo}")

