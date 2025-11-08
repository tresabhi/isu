import math
import pint

ur = pint.UnitRegistry()

specimens = [
    ("c_channel", 2.43 * ur.inch, 1.456 * ur.inch, 0.08 * ur.inch, None, None),
    ("c_channel", 0.84 * ur.inch, 0.56 * ur.inch, 0.055 * ur.inch, None, None),
    ("circular_open", None, None, 0.071 * ur.inch, 1.66 * ur.inch, 3.1 * ur.deg),
    ("circular_open", None, None, 0.071 * ur.inch, 1.66 * ur.inch, 36.3 * ur.deg),
    ("circular_open", None, None, 0.071 * ur.inch, 1.66 * ur.inch, 103.7 * ur.deg),
]

id = 1
for specimen in specimens:
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
