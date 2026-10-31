import numpy as np


def calc_obj(x):
    f = x[0] ** 2 + 2 * x[1] ** 2 - 2 * x[0] * x[1] - 4 * x[0]
    return f


def decode(design_var_bin, bounds, n_dvs, n_bits):
    design_var_real = []

    for i in range(n_dvs):
        start = i * n_bits
        end = start + n_bits

        design_var_i = design_var_bin[start:end]
        binary_str = ""

        for b in design_var_i:
            binary_str += str(b)

        real_idx = int(binary_str, 2)

        min_b = bounds[i][0]
        max_b = bounds[i][1]

        real_val = min_b + real_idx * (max_b - min_b) / (2**n_bits - 1)
        design_var_real.append(real_val)
