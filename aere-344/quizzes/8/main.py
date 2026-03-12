import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

dt = 0.00002
Fs = 1 / dt
window = 2048


def process(file_name):
    with open(file_name) as file:
        data = []

        for line in file.readlines():
            t, v = [float(column) for column in line.split()]
            data.append((t, v))

        data = np.array(data)
        t = data[:, 0]
        u = data[:, 1]
        u_bar = np.mean(u)
        u_prime = u - u_bar

        f, Pxx = sp.signal.welch(u_prime, Fs, nperseg=window)

        print(file_name)
        print(f"u_prime = {u_prime}")
        print(f"f = {f}")
        print()

        plt.figure()
        plt.title(f"{file_name} v vs t")
        plt.xlabel("Time")
        plt.ylabel("Velocity")
        plt.plot(t, u)
        plt.savefig(f"{file_name}_v.png")

        plt.figure()
        plt.title(f"{file_name} Power Spectral Density")
        plt.xlabel("Frequency")
        plt.ylabel("Power Spectral Density")
        plt.plot(f, Pxx)
        plt.yscale("log")
        plt.savefig(f"{file_name}_psd.png")


process("data/cylinder_wake.dat")
process("data/free_stream.dat")
