design_space_descriptions = [
    ("alpha", "angle of attack"),
    ("Lambda", "sweep angle"),
    ("theta_tip", "twist angle, linearly interpolated from root to tip"),
    ("c_root", "chord length at root"),
    ("c_tip", "length at tip"),
]
invariants = [""]
solution_descriptions = [
    ("C_L", "coefficient of lift"),
    ("C_D", "coefficient of drag"),
    ("V", "internal wing volume"),
]

Us = [
    (0, 0, 0, 1, 1),
]
Ys = [
    #
]

V0 = 0


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
