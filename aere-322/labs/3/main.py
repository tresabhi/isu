import os
import csv
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), 'formatted.csv')
time = []
elongation = []
load = []

with open(path, 'r') as file:
  reader = csv.DictReader(file)

  for row in reader:
    time.append(float(row['Time (s)']))
    elongation.append(float(row['Elongation (in)']))
    load.append(float(row['Load (lbf)']))

max_load = max(load)
max_load_time = time[load.index(max_load)]

fig, ax1 = plt.subplots()

color = "tab:blue"
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Load (lbf)", color=color)
ax1.plot(time, load, color=color)
ax1.tick_params(axis="y", labelcolor=color)

ax1.hlines(y=max_load, xmin=40, xmax=max_load_time, color="tab:blue", linestyle="--", alpha=0.7)
ax1.scatter(max_load_time, max_load, color="tab:blue")
ax1.text(35, max_load, f"Max Load = {max_load:.1f} lbf", va="center", ha="right", color="tab:blue")

ax2 = ax1.twinx()
color = "tab:red"
ax2.set_ylabel("Elongation (in)", color=color)
ax2.plot(time, elongation, color=color)
ax2.tick_params(axis="y", labelcolor=color)

fig.tight_layout()
plt.grid()
plt.show()