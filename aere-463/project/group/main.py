design_space_descriptions = [
    ("alpha", "[deg] angle of attack"),
    ("Lambda", "[deg] sweep angle"),
    ("theta_tip", "[deg] twist angle, linearly interpolated from root to tip"),
    ("c_root", "[m] chord length at root"),
    ("c_tip", "[m] length at tip"),
]
wing_invariant_descriptions = [
    ("p_root", "[1] cross-sectional airfoil at the root", "NACA 0012"),
    ("p_tip", "[1] cross-sectional airfoil at the tip", "NACA 0012"),
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
    #
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


def Solver(U):
    print("Couldn't find a documented solution. Dispatching humans...\n")
    Dispatch(U)
    exit(0)


def F(X):
    U = X[:5]
    Lambda = X[5:17]
    S = X[17:29]

    return Augmented(U, Lambda, S)


def Augmented(U, Lambda, S):
    Y = Solver(U)

    return (
        f(Y)
        + constraint_1(U, Lambda, S)
        + constraint_2(U, Lambda, S)
        + constraint_3(U, Lambda, S)
        + constraint_4(U, Lambda, S)
        + constraint_5(U, Lambda, S)
        + constraint_6(Y, Lambda, S)
        + constraint_7(Y, Lambda, S)
    )


# 0 <= alpha <= 10
def constraint_1(U, Lambda, S):
    return Lambda[0] * (-U[0] + S[0] ** 2) + Lambda[1] * (U[0] - 10 + S[1] ** 2)


# -10 <= Lambda (sweep angle) <= 10
def constraint_2(U, Lambda, S):
    return Lambda[2] * (-U[1] - 10 + S[2] ** 2) + Lambda[3] * (U[1] - 10 + S[3] ** 2)


# -10 <= theta_tip <= 10
def constraint_3(U, Lambda, S):
    return Lambda[4] * (-U[2] - 10 + S[4] ** 2) + Lambda[5] * (U[2] - 10 + S[5] ** 2)


# 0.2 <= c_root <= 3
def constraint_4(U, Lambda, S):
    return Lambda[6] * (0.2 - U[3] + S[6] ** 2) + Lambda[7] * (U[3] - 3 + S[7] ** 2)


# 0.2 <= c_tip <= 3
def constraint_5(U, Lambda, S):
    return Lambda[8] * (0.2 - U[4] + S[8] ** 2) + Lambda[9] * (U[4] - 3 + S[9] ** 2)


# C_L >= 0.4
def constraint_6(Y, Lambda, S):
    C_L, _, _ = Y
    return Lambda[10] * (0.4 - C_L + S[10] ** 2)


# V >= V0
def constraint_7(Y, Lambda, S):
    _, _, V = Y
    return Lambda[11] * (V0 - V + S[11] ** 2)


# C_D is what's being minimized
def f(Y):
    _, C_D, _ = Y
    return C_D


Solver(Us[0])
