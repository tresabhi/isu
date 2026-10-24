import aerosandbox as asb
import airfoils

# ALPHA = 4.063
ALPHA = 0

USE_GOOD_AIRFOIL = False


def Solver(airfoil, operating_point):
    root_cross_section = asb.WingXSec(
        xyz_le=[0, 0, 0], chord=1.0, twist=0.0, airfoil=airfoil
    )
    tip_cross_section = asb.WingXSec(
        xyz_le=[0, 3.0, 0], chord=1.0, twist=0.0, airfoil=airfoil
    )
    wing = asb.Wing(
        name="Wing", symmetric=True, xsecs=[root_cross_section, tip_cross_section]
    )

    airplane = asb.Airplane(
        name="Airplane",
        wings=[wing],
        c_ref=1.0,
        s_ref=3.0,
        b_ref=6.0,
    )

    method = asb.VortexLatticeMethod(airplane=airplane, op_point=operating_point)
    data = method.run()

    V = wing_volume = wing.volume() / 2

    return data["CL"], data["CD"], V


operating_point = asb.OperatingPoint(
    velocity=102.0,
    alpha=ALPHA,
    atmosphere=asb.Atmosphere(altitude=0),
)


print(Solver(airfoils.naca0012, operating_point))
