import time
import numpy as np
from matplotlib import pyplot as plt
import pint

# I added quality of life features like on-the-fly tweaking time warp
# and rocket-centered camera but Ms. Riedel said that modded.
# So, here's the code without thos features... the simplified version

ur = pint.UnitRegistry()

# made the arrow length smaller than the requirement because it's way better this way
arrow_length = 50 * ur.km
arrow_width= 30 * ur.km
simulation_time = 3600 * 4 * ur.s
# time warping ability to go "time_warp" times faster than real time
time_warp = 16

rocket_empty_mass = 29500 * ur.kg
rocket_payload_mass = 1000 * ur.kg
rocket_fuel_mass = 480000 * ur.kg
rocket_fuel_mass_initial = rocket_fuel_mass
rocket_mass = rocket_empty_mass + rocket_payload_mass + rocket_fuel_mass
rocket_tsfc = 3.5e-4 * ur.s / ur.m
rocket_full_thrust = 7600000 * ur.N

gravitational_constant = 6.674e-11 * ur.m ** 3 / (ur.kg * ur.s ** 2)

earth_mass = 5.98e24 * ur.kg
earth_diameter = 12700000 * ur.m
earth_equator_vel = 460 * ur.m / ur.s

position = np.array((0.0, earth_diameter.magnitude / 2.0)) * ur.m
velocity = np.array((0.0, 0.0)) * ur.m / ur.s
thrust_angle = 60.0 * ur.degree
thrust_direction = np.array((0.0, 0.0))

figure = plt.figure()
earth = plt.Circle((0, 0), float(earth_diameter.magnitude / 2.0), color = 'g')
figure.gca().add_artist(earth)

# draw a random arrow; it's gonna be removed instantly so doesn't matter
arrow_plt = plt.arrow(0, 0, 0, 0)

def event_handler(event):
    global thrust_angle, time_warp
    
    if event.key == ',':
        # turn left
        thrust_angle += 10.0 * ur.degree
    elif event.key == '.':
        # turn right
        thrust_angle -= 10.0 * ur.degree
    elif hasattr(event, 'button') and event.button == 1:
        if event.xdata < 0.0:
            # turn left
            thrust_angle += 10.0 * ur.degree
        else:
            # turn right
            thrust_angle -= 10.0 * ur.degree

figure.canvas.mpl_connect('key_press_event', event_handler)
figure.canvas.mpl_connect('button_press_event', event_handler)

min_screenspace = earth_diameter / 8
max_screenspace = earth_diameter / 2

# declare variables
last_time = time.time() * ur.s
t = 0.0 * ur.s
d_t = 0.0 * ur.s

while t < simulation_time:
    arrow_plt.remove()
    
    # crash into Earth detection
    rocket_distance = np.sqrt(np.sum(position ** 2))
    if t > 0 and rocket_distance <= earth_diameter / 2:
        velocity = np.array((0.0, 0.0)) * ur.m / ur.s
        break
    
    # calculate the change in time using the change in time since the last iteration times time warp
    new_time = time.time() * ur.s
    d_t = new_time - last_time
    d_t *= time_warp
    last_time = new_time
    t += d_t
    
    force_of_gravity = (
        (gravitational_constant * earth_mass * rocket_mass)
        / (rocket_distance ** 2)
    ).to(ur.N)
    gravity_direction = -position / rocket_distance
    gravity_force = gravity_direction * force_of_gravity
    
    thrust_magnitude = rocket_full_thrust if rocket_fuel_mass > 0 * ur.kg else 0 * ur.N
    thrust_direction = np.array((np.cos(thrust_angle), np.sin(thrust_angle)))
    thrust = thrust_direction * thrust_magnitude
    # change in mass is the fuel consumed or whatever is left in the tank (in the last step of burn)
    d_mass = max(-rocket_tsfc * thrust_magnitude * d_t, -rocket_fuel_mass).to(ur.kg)
    
    # record change in mass seperatly for both fuel left and the mass of the rocket
    rocket_fuel_mass += d_mass
    rocket_mass += d_mass
    
    sigma_forces = gravity_force + thrust
    acceleration = sigma_forces / rocket_mass
    velocity += acceleration * d_t
    position += velocity * d_t
    
    arrow_direction = (thrust_direction * arrow_length).to(ur.m).magnitude
    
    plt.ion()
    plt.grid(True)
    arrow_plt = plt.arrow(
        position[0].to(ur.m).magnitude,
        position[1].to(ur.m).magnitude,
        arrow_direction[0],
        arrow_direction[1],
        width = arrow_width.to(ur.m).magnitude
    )
    
    # perfected values for smooth zooming in and out
    fuel_progress = (1 - (rocket_fuel_mass / rocket_fuel_mass_initial))
    screenspace_x = min_screenspace + (fuel_progress ** 8)* (max_screenspace - min_screenspace)
    # use 3:4 aspect ratio
    screenspace_y = screenspace_x * 3 / 4
    
    plt.title(f"Fuel remaining: {round(rocket_fuel_mass.magnitude)}kg")
    plt.xlabel(f"Time elapsed: {round(t.magnitude * 100) / 100}s (x{time_warp} time warp)")
    plt.axis((
        -screenspace_x.magnitude,
        screenspace_x.magnitude,
        earth_diameter.magnitude / 2.0 - screenspace_y.magnitude,
        earth_diameter.magnitude / 2.0 + screenspace_y.magnitude
    ))
    
    figure.canvas.draw()
    figure.canvas.flush_events()