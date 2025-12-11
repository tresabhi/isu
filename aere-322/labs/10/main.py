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

weight_removal_runs = [3, 6]
weight_removal_time = 6

for i in range(6):
    run_index = i + 1
    run = runs[f"Run #{run_index}"]

    t = run["Time (s)"].values
    x = run["Position (m)"].values

    segments = [(t, x, "")]
    if run_index in weight_removal_runs:
        segments = [
            (
                t[t <= weight_removal_time],
                x[t <= weight_removal_time],
                " (Before Removal)",
            ),
            (
                t[t >= weight_removal_time],
                x[t >= weight_removal_time],
                " (After Removal)",
            ),
        ]

    for t_segment, x_segment, label in segments:
        x_segment = detrend(x_segment)
        dt = np.mean(np.diff(t_segment))

        N = len(x_segment)
        Y = np.fft.fft(x_segment)

        frequencies = np.fft.fftfreq(N, d=dt)
        mask = frequencies >= 0

        plt.figure()
        plt.plot(frequencies[mask], np.abs(Y[mask]) * 2 / N)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude (m)")
        plt.title(f"Run {run_index} FFT{label}")

plt.show()
