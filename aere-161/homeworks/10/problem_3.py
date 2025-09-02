"""
Abhigyaan Deep
AER E 161

Purpose:
Write a script to create a dictionary to store material properties such as
density, yield strength, and thermal conductivity for different materials like steel,
aluminum, and copper. Access the density of steel in your dictionary and print it to
the screen. Add a new material, titanium, to the dictionary to demonstrate how to
update it.
"""

# create a dictionary
materials = {
    # append a child dictionary
    "steel": {
        # standard way of adding properties
        "density": 7.8,
        "yield_strength": 250,
        "thermal_conductivity": 50,
    },
    # and so on...
    "aluminum": {
        "density": 2.7,
        "yield_strength": 90,
        "thermal_conductivity": 205,
    },
    "copper": {
        "density": 8.96,
        "yield_strength": 210,
        "thermal_conductivity": 398,
    },
}

# pretty print some info
print("Properties of steel")
# first access the steel dictionary and then the properties
print(f"  Density: {materials['steel']['density']}")
print(f"  Yield strength: {materials['steel']['yield_strength']}")
print(f"  Thermal conductivity: {materials['steel']['thermal_conductivity']}")

# append a new material
materials["titanium"] = {
    "density": 4.5,
    # why is this so low lol, must be a mistake in the assignment
    "yield_strength": 140,
    "thermal_conductivity": 21,
}
