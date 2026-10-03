from scipy.optimize import minimize
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
    (3.819660112501051, 0.0, 0.0, 1.0, 1.0),
    (6.180339887498947, 0.0, 0.0, 1.0, 1.0),
    (2.360679774997897, 0.0, 0.0, 1.0, 1.0),
]
Ys = [
    (0.1211, 0.01100, 0.2339),
    (0.1410, 0.01900, 0.2339),
    (0.1977, 0.03900, 0.2339),
    (0.1377, 0.01500, 0.2339),
]

V0 = 0


def Dispatch(U):
    i = 0

    print("Design variables this iteration:")
    for name, description in design_space_descriptions:
        print(f"  {name} = {U[i]} {description}")
        i += 1

    print("\nInvariants of the wing:")
    for name, description, value in wing_invariant_descriptions:
        print(f"  {name} = {value} {description}")

    print("\nInvariants of the environment:")
    for name, description, value in environment_invariant_descriptions:
        print(f"  {name} = {value} {description}")

    print("\nPlease find the following:")
    for name, description in solution_descriptions:
        print(f"  {name} = ? {description}")


r_max = 1e-20


def Solver(U):
    for existing_U, existing_Y in zip(Us, Ys):
        r = math.sqrt(sum((u - eu) ** 2 for u, eu in zip(U, existing_U)))

        if r < r_max:
            print(f"{U} -> {existing_U}")
            return existing_Y

    print(
        f"{tuple(U.tolist())} didn't match a documented solution. Dispatching humans...\n"
    )
    # Dispatch(U)

    return (0.15, 0.02, 0.2339)

    # exit(0)


def objective_function(U):
    Y = Solver(U)
    return f(Y)


# C_D is what's being minimized
def f(Y):
    _, C_D, _ = Y
    return C_D


result = minimize(
    objective_function,
    Us[0],
    method="Powell",
    bounds=[
        (0, 10),  # alpha
        (-10, 10),  # Lambda
        (-10, 10),  # theta_tip
        (0.2, 3),  # c_root
        (0.2, 3),  # c_tip
    ],
)
