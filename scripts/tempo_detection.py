# tempo_detection.py
import librosa
from pydub import AudioSegment
import tempfile
import os

def convert_audio(audio_file):
    # Load audio file using pydub
    audio = AudioSegment.from_file(audio_file)
    
    # Export as WAV to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        audio.export(tmp_file.name, format="wav")
        return tmp_file.name

def detect_tempo(audio_file):
    converted_file = convert_audio(audio_file)
    
    # Load audio data and sampling rate with downsampling
    y, sr = librosa.load(converted_file, sr=22050, mono=True, res_type='kaiser_fast')
    
    # Calculate tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    # Clean up the temporary file
    os.remove(converted_file)

    return tempo

if __name__ == "__main__":
    audio_file = "audio/CINDERVOMIT.wav"
    tempo = detect_tempo(audio_file)
    print(f"Estimated Tempo/BPM: {tempo}")


