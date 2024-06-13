import sys
import librosa

def detect_tempo(audio_file):
    """
    Detect the tempo of the audio file.
    """
    try:
        y, sr = librosa.load(audio_file)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return tempo
    except Exception as e:
        print(f"Failed to detect tempo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tempo_detection.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    tempo = detect_tempo(audio_file)
    print(f"Detected tempo: {tempo:.2f} BPM")
