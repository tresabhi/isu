# %%

import numpy as np
import pint
from matplotlib import pyplot as plt

ur = pint.UnitRegistry()

EMPTY_MASS = 20000 * ur.kg
PAYLOAD_MASS = 750 * ur.kg
INITIAL_FUEL_MASS = 450000 * ur.kg

TSFC = 3.0 * 10 ** -4 * ur.s / ur.m
FULL_THRUST = 6750000 * ur.N

fuel_mass = INITIAL_FUEL_MASS
mass = PAYLOAD_MASS + fuel_mass + EMPTY_MASS

time = 0 * ur.s
time_array = np.array(time.magnitude) * ur.s
weight_array = np.array(mass.magnitude) * ur.kg

while fuel_mass > 0 * ur.kg:
  delta_time = 1 * ur.s

  # only accept fuel that can be burned to avoid negative mass.
  # the change in mass is going to be all the fuel mass available
  # when there's not enough fuel (which happens are the very last
  # iteration)
  delta_mass = -min(TSFC * FULL_THRUST * delta_time, fuel_mass)
  mass += delta_mass
  fuel_mass += delta_mass

  # recalculate delta time because last step of burn is
  # going to be less than 1 second as there is not enough fuel.
  # (simply rearranged the equation from line 1 inside the loop)
  delta_time = -delta_mass / (TSFC * FULL_THRUST)
  time += delta_time

  time_array = np.append(time_array, time)
  weight_array = np.append(weight_array, mass)

print("The rocket is out of fuel")
print(f"The final mass of the rocket: {mass}")
print(f"Time taken to run out of fuel: {time}")

plt.plot(time_array, weight_array)
plt.xlabel('Time (s)')
plt.ylabel('Weight of rocket (kg)')
plt.title('Rocket weight over time')
plt.grid()
