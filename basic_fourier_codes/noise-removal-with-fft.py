# import numpy as np 
# import matplotlib.pyplot as plt

# t = np.linspace(0,1,500)
# f = 5
# signal = np.sin(2 * np.pi * 6 * t) + np.cos( 2 * np.pi * 4 * t)


# N = len(t)


# noise = 0.5 * np.random.randn(N)    # Gaussian noise, scaled 0.5
# noisy_signal = signal + noise
# FFT = np.fft.fft(noise)

# freq = np.fft.fftfreq(N, d=(t[1] - t[0]))

# # Plot

# plt.plot(freq , np.abs(FFT) ,label="FFT")

# plt.plot(t, noisy_signal, label="Signal + Noise")
# plt.plot(t, signal, label="Original Signal", alpha=0.7)

# plt.title("Frequency-domain (FFT)")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.legend()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Parameters ---
T = 2         # total time in seconds
N = 500        # number of samples
t = np.linspace(0, T, N, endpoint=False)
d = t[1] - t[0]  # time step

# --- 2. Original signal ---
freq1 = 5      # 5 Hz
freq2 = 12     # 12 Hz
signal = np.sin(2*np.pi*freq1*t) + 0.5*np.sin(2*np.pi*freq2*t)

# --- 3. Add random noise ---
noise = 0.8 * np.random.randn(N)  # Gaussian noise
noisy_signal = signal + noise

# --- 4. Compute FFT ---
fft_vals = np.fft.fft(noisy_signal)
freqs = np.fft.fftfreq(N, d)

# --- 5. Noise removal (simple thresholding) ---
threshold = 50   # you can adjust this
fft_filtered = fft_vals.copy()
fft_filtered[np.abs(fft_filtered) < threshold] = 0  # zero out small components

# --- 6. Inverse FFT to get cleaned signal ---
cleaned_signal = np.fft.ifft(fft_filtered)



# --- 7. Plot time domain ---
plt.figure(figsize=(12,6))
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.6)
plt.plot(t, cleaned_signal.real, label="Cleaned Signal", linewidth=2)
plt.plot(t, signal, '--', label="Original Signal", alpha=0.7)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.title("FFT Noise Removal Example")
plt.show(block=False)

# --- 8. Plot frequency domain ---

final_fft = np.fft.fft(cleaned_signal)
final_frequencies = np.fft.fftfreq(N , d)

plt.figure(figsize=(12,5))
plt.stem(final_frequencies[:N//2], 2.0/N*np.abs(final_fft[:N//2]), linefmt='C0-', markerfmt='C0o', basefmt=" ")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.title("Original FFT Spectrum")
plt.show()
