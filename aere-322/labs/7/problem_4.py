import pint
import math

ur = pint.UnitRegistry()

# Stainless 304 annealed cold finish steel
E_st = 29000 * ur.ksi
sigma_Y_st = 35 * ur.ksi

# 6061-T6 aluminum
E_al = 10000 * ur.ksi
sigma_Y_al = 40 * ur.ksi

cases = [
    (E_al, "circle", (3 / 8) * ur.inch, 30 * ur.inch, "pinned_pinned"),
    (
        E_al,
        "rectangle",
        (1 * ur.inch, (1 / 4) * ur.inch),  # this is backwards to make h = 1/4"
        30 * ur.inch,
        "pinned_pinned",
    ),
    (E_st, "circle", (1 / 4) * ur.inch, 30 * ur.inch, "pinned_pinned"),
    (E_st, "circle", (1 / 4) * ur.inch, 24 * ur.inch, "pinned_pinned"),
    (E_st, "circle", (1 / 4) * ur.inch, 27.5 * ur.inch, "pinned_fixed"),
]

index = 1
for case in cases:
    E, shape, size, L, ends = case
    I, L_effective = 0, 0

    if shape == "circle":
        r = size / 2
        I = (math.pi / 4) * r**4
    elif shape == "rectangle":
        b, h = size
        I = (b * h**3) / 12
    else:
        raise ValueError(f"Unknown shape: {shape}")

    if ends == "fixed_fixed":
        L_effective = L / 2
    elif ends == "fixed_pinned" or ends == "pinned_fixed":
        L_effective = L / math.sqrt(2)
    elif ends == "pinned_pinned":
        L_effective = L
    elif ends == "fixed_free" or ends == "free_fixed":
        L_effective = 2 * L
    else:
        raise ValueError(f"Unknown ends: {ends}")

    P = (math.pi**2 * E * I) / (L_effective**2)
    P = P.to(ur.kip)

    L_rho = 0

    if shape == "circle":
        r = size / 2
        L_rho = (2 * L_effective) / r
    elif shape == "rectangle":
        b, h = size
        L_rho = (L_effective * math.sqrt(12)) / h

    L_rho = L_rho.magnitude

    print(f"Case {index}:")
    print(f"  L_eff =", L_effective)
    print(f"  P =", P)
    print(f"  L/rho =", L_rho, end="\n\n")

    index += 1
