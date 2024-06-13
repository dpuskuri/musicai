import librosa
from pydub import AudioSegment
import tempfile
import os
import logging

logging.basicConfig(level=logging.DEBUG)

def convert_audio(audio_file):
    try:
        # Load audio file using pydub
        audio = AudioSegment.from_file(audio_file)
        logging.info(f"Loaded audio file {audio_file} successfully with pydub.")
        
        # Export as WAV to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            audio.export(tmp_file.name, format="wav")
            logging.info(f"Converted audio file {audio_file} to {tmp_file.name}.")
            return tmp_file.name
    except Exception as e:
        logging.error(f"Error converting audio file {audio_file}: {e}")
        raise

def detect_tempo(audio_file):
    converted_file = convert_audio(audio_file)
    
    try:
        # Load audio data and sampling rate with downsampling
        y, sr = librosa.load(converted_file, sr=22050, mono=True, res_type='kaiser_fast')
        logging.info(f"Loaded audio data from {converted_file} with librosa.")
        
        # Calculate tempo
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        logging.info(f"Detected tempo: {tempo} BPM.")
        
        # Clean up the temporary file
        os.remove(converted_file)
        logging.info(f"Removed temporary file {converted_file}.")

        return tempo
    except Exception as e:
        logging.error(f"Error processing audio file {converted_file}: {e}")
        raise

if __name__ == "__main__":
    audio_file = "audio/CINDERVOMIT.wav"  # Ensure this path is correct
    try:
        tempo = detect_tempo(audio_file)
        print(f"Estimated Tempo/BPM: {tempo}")
    except Exception as e:
        logging.error(f"Failed to detect tempo: {e}")
