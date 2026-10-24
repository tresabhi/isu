import matplotlib.pyplot as plt
import pathlib
import aerosandbox as asb

script_dir = pathlib.Path(__file__).parent
dat_path = script_dir / "../n64212.dat"

with open(dat_path, "r") as f:
    raw_text = f.readlines()

coords = asb.geometry.airfoil.airfoil_families.get_coordinates_from_raw_dat(raw_text)
naca641212 = asb.Airfoil(name="naca641212", coordinates=coords)

naca0012 = asb.Airfoil("naca0012")
