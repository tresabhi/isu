import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend

raw = pd.read_csv("aere-322/labs/10/data.csv", header=None)
run_labels = raw.iloc[0]
column_labels = raw.iloc[1]
data = raw.iloc[2:].reset_index(drop=True)
data.columns = pd.MultiIndex.from_arrays([run_labels, column_labels])
runs = {
    run: data[run].apply(pd.to_numeric, errors="coerce") for run in run_labels.unique()
}

for i in range(6):
    run = runs[f"Run #{i+1}"]

    t = run["Time (s)"]
    x = run["Position (m)"]

    x = detrend(x)

    dt = np.mean(np.diff(t))
    fs = 1 / dt
    N = len(x)

    Y = np.fft.fft(x)
    frequencies = np.fft.fftfreq(N, d=dt)

    mask = frequencies >= 0
    frequencies = frequencies[mask]
    Y = Y[mask]

    magnitudes = np.abs(Y) * 2 / N

    plt.figure()
    plt.plot(frequencies, magnitudes)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (m)")
    plt.title(f"Run {i + 1} FFT")

plt.show()
