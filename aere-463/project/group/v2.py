import pathlib
import aerosandbox as asb

# ALPHA = 4.063
ALPHA = 0

USE_GOOD_AIRFOIL = False

if USE_GOOD_AIRFOIL:
    script_dir = pathlib.Path(__file__).parent
    dat_path = script_dir / "n64212.dat"

    with open(dat_path, "r") as f:
        raw_text = f.readlines()

    coords = asb.geometry.airfoil.airfoil_families.get_coordinates_from_raw_dat(
        raw_text
    )

    airfoil = asb.Airfoil(name="naca641212", coordinates=coords).normalize()
else:
    print("???")
    airfoil = asb.Airfoil("naca0012")

root_xsec = asb.WingXSec(xyz_le=[0, 0, 0], chord=1.0, twist=0.0, airfoil=airfoil)
tip_xsec = asb.WingXSec(xyz_le=[0, 3.0, 0], chord=1.0, twist=0.0, airfoil=airfoil)

wing = asb.Wing(name="Main Wing", symmetric=True, xsecs=[root_xsec, tip_xsec])

wing_volume = wing.volume() / 2
print(f"Internal Wing Volume (V): {wing_volume:.4f} m^3")

airplane = asb.Airplane(
    name="Wing Analysis",
    wings=[wing],
    c_ref=1.0,
    s_ref=3.0,
    b_ref=6.0,
)

op_point = asb.OperatingPoint(
    velocity=102.0,
    alpha=ALPHA,
    atmosphere=asb.Atmosphere(altitude=0),
)

vlm = asb.VortexLatticeMethod(airplane=airplane, op_point=op_point)
aero_data = vlm.run()

C_L = aero_data["CL"]
C_D = aero_data["CD"]

print(f"Lift Coefficient (C_L): {C_L:.4f}")
print(f"Drag Coefficient (C_D): {C_D:.4f}")
