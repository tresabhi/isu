from symbols import gamma


def ratio_curry(_x):
    a, b, a_b, b_a = _x

    return [
        (a_b, a / b),
        (b_a, b / a),
        (a_b, 1 / b_a),
    ]


def state_curry(M, _p):
    p, p0, p_p0, p0_p = _p

    return [
        (p0_p, (1 + ((gamma - 1) / 2) * M**2) ** (gamma / (gamma - 1))),
        *ratio_curry(_p),
    ]
