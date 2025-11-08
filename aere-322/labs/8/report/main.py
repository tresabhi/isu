import math
import pint

ur = pint.UnitRegistry()

i = ur.inch
g = 9.81 * ur.m / ur.s**2

specimens = [
    ("c_channel", 2.43 * i, 1.456 * i, 0.08 * i, None, None),
    ("c_channel", 0.84 * i, 0.56 * i, 0.055 * i, None, None),
    ("circular_open", None, None, 0.071 * i, 1.66 * i, 3.1 * ur.deg),
    ("circular_open", None, None, 0.071 * i, 1.66 * i, 36.3 * ur.deg),
    ("circular_open", None, None, 0.071 * i, 1.66 * i, 103.7 * ur.deg),
]

experiment_masses = [
    0.1 * ur.kg,
    0.2 * ur.kg,
    0.1 * ur.kg,
    0.1 * ur.kg,
    0.1 * ur.kg,
]

experiment_weights = [g * m for m in experiment_masses]

torsion_experiments = [
    [
        ("R", 2 * i, (3 + 9 / 16) * i, (6 + 1 / 8) * i),
        ("L", (4 + 1 / 4) * i, (1 + 6 / 8) * i, (1 + 1 / 8) * i),
        ("L", (7 + 7 / 16) * i, (2 + 9 / 16) * i, 0),
    ],
    [
        ("L", 3 * i, (2 + 6 / 8) * i, (11 / 16) * i),
        ("R", 3 * i, (15 / 16) * i, (2 + 1 / 4) * i),
        ("R", 4.5 * i, (7 / 16) * i, (2 + 3 / 4) * i),
    ],
    [
        ("L", 1.5 * i, (2 + 1 / 8) * i, (3 / 8) * i),
        ("R", 4 * i, (1 / 4) * i, (2 + 5 / 8) * i),
        ("L", 3 * i, (2 + 3 / 8) * i, (1 / 4) * i),
    ],
    [
        ("R", 4 * i, 1 * i, (3 + 3 / 8) * i),
        ("L", (3 + 1 / 4) * i, (2 + 9 / 16) * i, (1 + 3 / 8) * i),
        ("L", 2.5 * i, (2 + 7 / 16) * i, (1 + 9 / 16) * i),
    ],
    [
        ("R", (2 + 3 / 10) * i, (3 / 10) * i, (2 + 3 / 10) * i),
        ("L", 2 * i, (2 + 7 / 10) * i, (3 / 10) * i),
        ("R", (3 + 3 / 10) * i, 0, (2 + 7 / 10) * i),
    ],
]


index = 0
for specimen in specimens:
    id = index + 1

    (type, h, b, t, d, two_theta) = specimen
    e: float

    if type == "c_channel":
        I = (1 / 2) * b * h**2 * t + (1 / 6) * b * t**3 + (1 / 12) * t * (h - t) ** 3
        e = (h**2 * b**2 * t) / (4 * I)
    elif type == "circular_open":
        theta = two_theta / 2

        r = d / 2 - t / 2
        e = (
            2 * r * (math.cos(theta) * (2 * math.pi - 2 * theta) + 2 * math.sin(theta))
        ) / (2 * math.pi - 2 * theta + math.sin(2 * theta))
    else:
        raise ValueError(f"Unknown type: {type}")

    print(f"e_{id} = {e}")
    id += 1
