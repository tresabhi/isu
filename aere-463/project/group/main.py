design_space_descriptions = [
    ("alpha", "angle of attack"),
    ("Lambda", "sweep angle"),
    ("theta_tip", "twist angle, linearly interpolated from root to tip"),
    ("c_root", "chord length at root"),
    ("c_tip", "length at tip"),
]
solution_descriptions = [
    ("C_L", "coefficient of lift"),
    ("C_D", "coefficient of drag"),
    ("V", "internal wing volume"),
]

Xs = [
    (0, 0, 0, 1, 1),
]
Ys = [
    #
]


def Augmented(X, Lambda):
    return (
        f(X)
        + constraint_1(X, Lambda)
        + constraint_2(X, Lambda)
        + constraint_3(X, Lambda)
        + constraint_4(X, Lambda)
        + constraint_5(X, Lambda)
    )


# 0 <= alpha <= 10
def constraint_1(X, Lambda):
    return Lambda[0] * -X[0] + Lambda[1] * (X[0] - 10)


# -10 <= Lambda <= 10
def constraint_2(X, Lambda):
    return Lambda[2] * (-X[1] - 10) + Lambda[3] * (X[1] - 10)


# -10 <= theta_tip <= 10
def constraint_3(X, Lambda):
    return Lambda[4] * (-X[2] - 10) + Lambda[5] * (X[2] - 10)


# 0.2 <= c_root <= 3
def constraint_4(X, Lambda):
    return Lambda[6] * (0.2 - X[3]) + Lambda[7] * (X[3] - 3)


# 0.2 <= c_tip <= 3
def constraint_5(X, Lambda):
    return Lambda[8] * (0.2 - X[4]) + Lambda[9] * (X[4] - 3)


def f(X):
    pass
