# scripts/test_extract_features.py
import numpy as np
from extract_features import extract_features

def test_extract_features():
    file_path = 'audio/CINDERVOMIT.wav'
    features = extract_features(file_path)
    assert features is not None
    assert len(features) > 0
    print("Test passed!")

if __name__ == "__main__":
    test_extract_features()
