import aerosandbox as asb
import numpy as np


def Solve(airfoil, X):
    airfoil.normalize()

    alpha, Gamma, theta_tip, c_root, c_tip = X

    b_2 = 3
    x_tip = b_2 * np.tan(np.radians(Gamma))

    root_cross_section = asb.WingXSec(
        xyz_le=[0, 0, 0], chord=c_root, twist=0.0, airfoil=airfoil
    )
    tip_cross_section = asb.WingXSec(
        xyz_le=[x_tip, b_2, 0], chord=c_tip, twist=theta_tip, airfoil=airfoil
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

    operating_point = asb.OperatingPoint(
        velocity=102.0,
        alpha=alpha,
        atmosphere=asb.Atmosphere(altitude=0),
    )

    method = asb.VortexLatticeMethod(airplane=airplane, op_point=operating_point)
    data = method.run()

    V = wing.volume() / 2

    return float(data["CL"]), float(data["CD"]), float(V)
