# scripts/extract_features.py
import librosa
import numpy as np
import os

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=44100)
    zcr = librosa.feature.zero_crossing_rate(y)
    rmse = librosa.feature.rms(y=y)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    spectral_flux = np.mean(np.diff(librosa.stft(y, n_fft=2048)).mean(axis=1))
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr)
    tonnetz = librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr)
    
    feature_vector = np.hstack([
        np.mean(zcr), np.mean(rmse), np.mean(mfccs, axis=1), np.mean(spectral_centroid),
        np.mean(spectral_rolloff), spectral_flux, tempo, np.mean(chromagram, axis=1), np.mean(tonnetz, axis=1)
    ])
    
    return feature_vector

if __name__ == "__main__":
    file_path = 'audio/your_darkpsy_track.wav'
    features = extract_features(file_path)
    print("Extracted features:", features)
