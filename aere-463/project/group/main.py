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


def Augmented(U, Lambda):
    Y = Solver(U)

    return (
        f(Y)
        + constraint_1(U, Lambda)
        + constraint_2(U, Lambda)
        + constraint_3(U, Lambda)
        + constraint_4(U, Lambda)
        + constraint_5(U, Lambda)
        + constraint_6(Y, Lambda)
        + constraint_7(Y, Lambda)
    )


# 0 <= alpha <= 10
def constraint_1(U, Lambda):
    return Lambda[0] * -U[0] + Lambda[1] * (U[0] - 10)


# -10 <= Lambda <= 10
def constraint_2(U, Lambda):
    return Lambda[2] * (-U[1] - 10) + Lambda[3] * (U[1] - 10)


# -10 <= theta_tip <= 10
def constraint_3(U, Lambda):
    return Lambda[4] * (-U[2] - 10) + Lambda[5] * (U[2] - 10)


# 0.2 <= c_root <= 3
def constraint_4(U, Lambda):
    return Lambda[6] * (0.2 - U[3]) + Lambda[7] * (U[3] - 3)


# 0.2 <= c_tip <= 3
def constraint_5(U, Lambda):
    return Lambda[8] * (0.2 - U[4]) + Lambda[9] * (U[4] - 3)


# C_L >= 0.4
def constraint_6(Y, Lambda):
    C_L, _, _ = Y
    return Lambda[10] * (0.4 - C_L)


# V >= V0
def constraint_7(Y, Lambda):
    _, _, V = Y
    return Lambda[11] * (V0 - V)


# C_D is what's being minimized so that gets passed through
def f(Y):
    _, C_D, _ = Y
    return C_D
