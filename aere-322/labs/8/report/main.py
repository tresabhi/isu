import math
import pint
import numpy as np

ur = pint.UnitRegistry()

I = ur.inch
flipped_ruler = 6 * I
ruler_padding = (1 / 16) * I
crossbar_length = 44 * ur.cm

specimens = [
    ("c_channel", 2.43 * I, 1.456 * I, 0.08 * I, None, None),
    ("c_channel", 0.84 * I, 0.56 * I, 0.055 * I, None, None),
    ("circular_open", None, None, 0.071 * I, 1.66 * I, 3.1 * ur.deg),
    ("circular_open", None, None, 0.071 * I, 1.66 * I, 36.3 * ur.deg),
    ("circular_open", None, None, 0.071 * I, 1.66 * I, 103.7 * ur.deg),
]

setups = [
    (0.1 * ur.kg, 7 * ur.mm, 6.8 * ur.mm, "open_right"),
    (0.2 * ur.kg, (1 + 9 / 16) * I, (1 + 3 / 8) * I, "open_left"),
    (0.1 * ur.kg, (1 + 1 / 4) * I, 1 * I, "open_left"),
    (0.1 * ur.kg, (1 + 7 / 16) * I, (1 + 3 / 8) * I, "open_right"),
    (0.1 * ur.kg, (1 + 2 / 5) * I, (1 + 2 / 5) * I, "open_left"),
]

experiments = [
    [
        ("to_right", 2 * I, (3 + 9 / 16) * I, (6 + 1 / 8) * I),
        ("to_left", (4 + 1 / 4) * I, (1 + 6 / 8) * I, (1 + 1 / 8) * I),
        ("to_left", (7 + 7 / 16) * I + ruler_padding, (2 + 9 / 16) * I, 0),
    ],
    [
        ("to_left", 3 * I, (2 + 6 / 8) * I, (11 / 16) * I),
        ("to_right", 3 * I, (15 / 16) * I, (2 + 1 / 4) * I),
        ("to_right", 4.5 * I, (7 / 16) * I, (2 + 3 / 4) * I),
    ],
    [
        ("to_left", 1.5 * I, (2 + 1 / 8) * I, (3 / 8) * I),
        ("to_right", 4 * I, (1 / 4) * I, (2 + 5 / 8) * I),
        ("to_left", 3 * I, (2 + 3 / 8) * I, (1 / 4) * I),
    ],
    [
        ("to_right", 4 * I, 1 * I, (3 + 3 / 8) * I),
        ("to_left", (3 + 1 / 4) * I, (2 + 9 / 16) * I, (1 + 3 / 8) * I),
        ("to_left", 2.5 * I, (2 + 7 / 16) * I, (1 + 9 / 16) * I),
    ],
    [
        ("to_right", (2 + 3 / 10) * I, (3 / 10) * I, (2 + 3 / 10) * I),
        ("to_left", 2 * I, (2 + 7 / 10) * I, (3 / 10) * I),
        ("to_right", (3 + 3 / 10) * I, 0, (2 + 7 / 10) * I),
    ],
]

# convert all to open_right to match diagram
i = 0
for setup in setups:
    (m, l, r, open_side) = setup

    if open_side == "open_left":
        setups[i] = (m, r, l, "open_right")

        j = 0
        for experiment in experiments[i]:
            (read_direction, x_raw, l, r) = experiment
            read_direction = "to_left" if read_direction == "to_right" else "to_right"
            experiments[i][j] = (read_direction, x_raw, r, l)
            j += 1

    i += 1


def angle(l_inverted, r_inverted):
    l = flipped_ruler - l_inverted
    r = flipped_ruler - r_inverted

    return math.asin((r - l) / crossbar_length) * ur.rad


i = 0
for specimen in specimens:
    id = i + 1

    (type, h, b, t, d, two_theta) = specimen
    (m, l_0, r_0, open_side) = setups[i]

    e = None

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
        raise ValueError(f"Unknown cross-section type: {type}")

    theta_0 = angle(l_0, r_0)
    xs = []
    thetas = []

    for experiment in experiments[i]:
        (read_direction, x_raw, l, r) = experiment

        x = x_raw + t / 2 if read_direction == "to_right" else -x_raw - t / 2
        theta = angle(l, r) - theta_0

        xs.append(x.to(ur.inch).magnitude)
        thetas.append(theta.to(ur.rad).magnitude)

    a, b = np.polyfit(xs, thetas, 1)
    root = -(b / a) * I
    e_experimental = -root

    print(f"e_{id} = {e}")
    print(f"e_experimental_{id} = {e_experimental}\n")

    i += 1
