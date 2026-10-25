import aerosandbox as asb
import numpy as np


def Solve(airfoil, X):
    print(*X)

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
    )

    operating_point = asb.OperatingPoint(
        velocity=102.0,
        alpha=alpha,
        atmosphere=asb.Atmosphere(altitude=0),
    )

    method = asb.AeroBuildup(airplane=airplane, op_point=operating_point)
    data = method.run()

    V = wing.volume() / 2

    rho_inf = 1.20
    U_inf = 102.0
    A_ref = 3.0

    q_inf = 0.5 * rho_inf * (U_inf**2)

    L = data["L"][0]
    D = data["D"][0]

    C_L = L / (q_inf * A_ref)
    C_D = D / (q_inf * A_ref)

    return float(C_L), float(C_D), float(V), method
