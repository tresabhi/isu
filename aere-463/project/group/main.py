from skopt import gp_minimize
from skopt.space import Real
import math

design_space_descriptions = [
    ("alpha", "[deg] angle of attack"),
    ("Lambda", "[deg] sweep angle"),
    ("theta_tip", "[deg] twist angle, linearly interpolated from root to tip"),
    ("c_root", "[m] chord length at root"),
    ("c_tip", "[m] length at tip"),
]
wing_invariant_descriptions = [
    ("p_root", "[1] cross-sectional airfoil at the root", "NACA 64-212"),
    ("p_tip", "[1] cross-sectional airfoil at the tip", "NACA 64-212"),
    ("theta_root", "[deg] twist angle at the root", 0),
    ("b/2", "[m] wing semi-span", 3),
]
environment_invariant_descriptions = [
    ("a_inf", "[m/s] speed of sound", 340),
    ("U_inf", "[m/s] free stream velocity", 102),
    ("rho_inf", "[kg/m^3] air density", 1.20),
    ("mu_inf", "[Pa s] dynamic viscosity", 2.448e-5),
    ("p_inf", "[Pa] free stream pressure", 101325),
    ("c_ref", "[m] reference chord (used for Re; ignore)", 1.00),
    ("A_ref", "[m^2] reference area (used for C_L and C_D)", 3.00),
]
solution_descriptions = [
    ("C_L", "[1] coefficient of lift"),
    ("C_D", "[1] coefficient of drag"),
    ("V", "[m^3] internal wing volume"),
]

Us = [
    (0, 0, 0, 1, 1),
]
Ys = [
    (0.1211, 0.01100, 0.2339),
]

V0 = 0.2488


def Dispatch(U):
    return "god help us"


r_max = 1e-20


def Solver(U):
    return Dispatch(U)


def objective_function(U):
    Y = Solver(U)
    return f(Y)


# C_D is what's being minimized
def f(Y):
    _, C_D, _ = Y
    return C_D


space = [
    Real(0, 10, name="alpha"),
    Real(-10, 10, name="Lambda"),
    Real(-10, 10, name="theta_tip"),
    Real(0.2, 3, name="c_root"),
    Real(0.2, 3, name="c_tip"),
]


result = gp_minimize(
    objective_function,
    space,
    x0=Us,
    y0=[f(Y) for Y in Ys],
    n_calls=20,
    n_initial_points=0,
    random_state=42,
)

print(result)
