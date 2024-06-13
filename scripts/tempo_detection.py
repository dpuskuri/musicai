import sys
import numpy as np
import audioflux

def detect_tempo(audio_file):
    """
    Detect the tempo of the audio file.
    """
    try:
        # Load the audio file
        signal, sr = audioflux.load(audio_file)
        
        # Tempo detection
        tempo, _ = audioflux.tempo.beat_track(signal, sr)
        
        # Ensure the tempo is a single float value
        if isinstance(tempo, np.ndarray):
            tempo = tempo[0]
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
    print(f"Tempo type: {type(tempo)}")  # Debug information
    print(f"Detected tempo: {tempo:.2f} BPM")



