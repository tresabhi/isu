import pint

ur = pint.UnitRegistry()

shell_area = 1377.836029 * ur.inch**2
hatch_area = 337.758770 * ur.inch**2
area = 2 * (shell_area + hatch_area)  # Total radiating area
normal_area = 718.181822 * ur.inch**2  # Sun-facing area

sun_heat = 1361 * ur.W / ur.m**2

# Example: White thermal coating (low solar absorption, high IR emission)
alpha = 0.20  # Solar absorptivity

internal_power = (5.35 + 2 + 5 + 80) * ur.W
solar_power = alpha * sun_heat * normal_area

# At steady state, heat expelled = heat absorbed + heat generated internally
heat_expelled = internal_power + solar_power

print(f"Internal Heat: {internal_power.to(ur.W):.1f}")
print(f"Solar Heat Absorbed: {solar_power.to(ur.W):.1f}")
print(f"Heat Expelled: {heat_expelled.to(ur.W):.1f}")
print(f"Heat Expelled per Total Area: {(heat_expelled / area).to(ur.W / ur.m**2):.1f}")
