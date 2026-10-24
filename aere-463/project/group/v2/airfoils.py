import matplotlib.pyplot as plt
import pathlib
import aerosandbox as asb

script_dir = pathlib.Path(__file__).parent
dat_path = script_dir / "../n64212.dat"

with open(dat_path, "r") as f:
    raw_text = f.readlines()

coords = asb.geometry.airfoil.airfoil_families.get_coordinates_from_raw_dat(raw_text)
naca641212 = asb.Airfoil(name="naca641212", coordinates=coords).normalize()

naca0012 = asb.Airfoil("naca0012")


coords = naca641212.coordinates

plt.figure(figsize=(9, 4))
plt.plot(coords[:, 0], coords[:, 1], "b.-", label="Airfoil Surface")
plt.axis("equal")
plt.title("Airfoil Shape Verification (NACA 64-1212)")
plt.xlabel("x / c")
plt.ylabel("y / c")
plt.grid(True)
plt.legend()
plt.show()
