import math

alpha = -2 * (math.pi / 180)

with open("data.csv") as file:
    lines = file.readlines()[1:]

    c_N = 0
    c_A = 0

    c_m_LE = 0

    for i in range(len(lines)):
        line = lines[i]
        next_line = lines[(i + 1) % len(lines)]

        x_i, y_i, c_p_i = [float(x) for x in line.split(",")]
        x_i_next, y_i_next, c_p_i_next = [float(x) for x in next_line.split(",")]

        x_half = (x_i + x_i_next) / 2
        y_half = (y_i + y_i_next) / 2
        c_half = (c_p_i + c_p_i_next) / 2

        delta_x_i = x_i_next - x_i
        delta_y_i = y_i_next - y_i

        c_N += c_half * delta_x_i
        c_A += -c_half * delta_y_i

        c_m_LE -= c_half * delta_x_i * x_half + c_half * delta_y_i * y_half

    c_l = c_N * math.cos(alpha) - c_A * math.sin(alpha)
    c_d = c_N * math.sin(alpha) + c_A * math.cos(alpha)

    print(f"c_N =", c_N)
    print(f"c_A =", c_A)

    print()

    print(f"c_l =", c_l)
    print(f"c_d =", c_d)
    print(f"c_m_LE =", c_m_LE)
