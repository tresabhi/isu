import math
import pint

ur = pint.UnitRegistry()

i = ur.inch
flipped_ruler = 6 * i
ruler_padding = (1 / 16) * i
crossbar_length = 44 * ur.cm

specimens = [
    ("c_channel", 2.43 * i, 1.456 * i, 0.08 * i, None, None),
    ("c_channel", 0.84 * i, 0.56 * i, 0.055 * i, None, None),
    ("circular_open", None, None, 0.071 * i, 1.66 * i, 3.1 * ur.deg),
    ("circular_open", None, None, 0.071 * i, 1.66 * i, 36.3 * ur.deg),
    ("circular_open", None, None, 0.071 * i, 1.66 * i, 103.7 * ur.deg),
]

setups = [
    (0.1 * ur.kg, 7 * ur.mm, 6.8 * ur.mm, "open_right"),
    (0.2 * ur.kg, (1 + 9 / 16) * i, (1 + 3 / 8) * i, "open_left"),
    (0.1 * ur.kg, (1 + 1 / 4) * i, 1 * i, "open_left"),
    (0.1 * ur.kg, (1 + 7 / 16) * i, 2 * i, "open_right"),
    (0.1 * ur.kg, (1 + 2 / 5) * i, (1 + 2 / 5) * i, "open_left"),
]

experiments = [
    [
        ("to_right", 2 * i, (3 + 9 / 16) * i, flipped_ruler - (6 + 1 / 8) * i),
        ("to_left", (4 + 1 / 4) * i, (1 + 6 / 8) * i, (1 + 1 / 8) * i),
        ("to_left", (7 + 7 / 16) * i + ruler_padding, (2 + 9 / 16) * i, 0),
    ],
    [
        ("to_left", 3 * i, (2 + 6 / 8) * i, (11 / 16) * i),
        ("to_right", 3 * i, (15 / 16) * i, (2 + 1 / 4) * i),
        ("to_right", 4.5 * i, (7 / 16) * i, (2 + 3 / 4) * i),
    ],
    [
        ("to_left", 1.5 * i, (2 + 1 / 8) * i, (3 / 8) * i),
        ("to_right", 4 * i, (1 / 4) * i, (2 + 5 / 8) * i),
        ("to_left", 3 * i, (2 + 3 / 8) * i, (1 / 4) * i),
    ],
    [
        ("to_right", 4 * i, 1 * i, (3 + 3 / 8) * i),
        ("to_left", (3 + 1 / 4) * i, (2 + 9 / 16) * i, (1 + 3 / 8) * i),
        ("to_left", 2.5 * i, (2 + 7 / 16) * i, (1 + 9 / 16) * i),
    ],
    [
        ("to_right", (2 + 3 / 10) * i, (3 / 10) * i, (2 + 3 / 10) * i),
        ("to_left", 2 * i, (2 + 7 / 10) * i, (3 / 10) * i),
        ("to_right", (3 + 3 / 10) * i, 0, (2 + 7 / 10) * i),
    ],
]

# convert all to open_right to match diagram

i = 0
for setup in setups:
    (m, l, r, open_side) = setup

    if open_side == "open_left":
        setups[i] = (m, l, r, "open_right")

        j = 0
        for experiment in experiments[i]:
            (read_direction, x_raw, l, r) = experiment
            read_direction = "to_left" if read_direction == "to_right" else "to_right"
            l, r = r, l
            experiments[i][j] = (read_direction, x_raw, l, r)
            j += 1

    i += 1


def theta(l_inverted, r_inverted):
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

    theta_0 = theta(l_0, r_0)

    for experiment in experiments[i]:
        (read_direction, x_raw, l, r) = experiment

        x_shifted = x_raw + t / 2 if read_direction == "to_right" else -x_raw - t / 2
        x = x_shifted + e

        print(x.to(ur.inch))

        theta_i = theta(l, r)

    print()

    i += 1
