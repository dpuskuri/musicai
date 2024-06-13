import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sys

def dofft(wavfile, bass=True, tenor=True, inverse=False, *args):
    print("Reading WAV file:", wavfile)  # Debugging
    rate, data = wav.read(wavfile)
    n = len(data)
    f = np.fft.fftfreq(n, d=1/rate)
    fdata = np.fft.fft(data)
    
    if inverse:
        for freq in args:
            if freq > 0 and freq < rate / 2:
                fdata[np.abs(f - freq) < 2.69] = 0
        data_inv = np.fft.ifft(fdata).real.astype(np.int16)
        wav.write(wavfile.split('.')[0] + '_inverse.wav', rate, data_inv)

    plt.figure(figsize=(10, 6))
    plt.plot(f[:n//2], np.abs(fdata[:n//2]))
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
    # Save frequency spectrum plot
    plt.savefig(wavfile.split('.')[0] + '_frequency_spectrum.png')
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tempo_detection.py <path/to/filename.wav> [bass] [tenor] [inverse] [freq1 freq2 ...]")
        sys.exit(1)

    filename = sys.argv[1]
    dofft(filename, *sys.argv[2:])





