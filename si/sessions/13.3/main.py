import math

transforms = 0
principals = 0


def transform(epsilon_x, epsilon_y, gamma_xy, theta_deg):
    global transforms

    theta = theta_deg * math.pi / 180

    epsilon_x_prime = (
        (epsilon_x + epsilon_y) / 2
        + ((epsilon_x - epsilon_y) / 2) * math.cos(2 * theta)
        + (gamma_xy / 2) * math.sin(2 * theta)
    )
    epsilon_y_prime = (
        (epsilon_x + epsilon_y) / 2
        - ((epsilon_x - epsilon_y) / 2) * math.cos(2 * theta)
        - (gamma_xy / 2) * math.sin(2 * theta)
    )
    gamma_x_prime_y_prime = -(epsilon_x - epsilon_y) * math.sin(
        2 * theta
    ) + gamma_xy * math.cos(2 * theta)

    transforms += 1

    print(f"Transform {transforms}")
    print(f"  {epsilon_x_prime=:.4g}")
    print(f"  {epsilon_y_prime=:.4g}")
    print(f"  {gamma_x_prime_y_prime=:.4g}")
    print()


def principal(epsilon_x, epsilon_y, gamma_xy):
    global principals

    theta_p = (1 / 2) * math.atan(gamma_xy / (epsilon_x - epsilon_y))
    theta_p_deg = theta_p * 180 / math.pi

    gamma_max = math.sqrt(((epsilon_x - epsilon_y) / 2) ** 2 + (gamma_xy / 2) ** 2)

    epsilon_avg = (epsilon_x + epsilon_y) / 2
    epsilon_p1 = epsilon_avg + gamma_max
    epsilon_p2 = epsilon_avg - gamma_max

    principals += 1

    print(f"Principal {principals}")
    print(f"  {epsilon_p1=:.4g}")
    print(f"  {epsilon_p2=:.4g}")
    print(f"  {gamma_max=:.4g}")
    print(f"  {theta_p_deg=:.4g}")
    print()


transform(-500, 250, 0, 15)
transform(240, 160, 150, -60)
transform(-800, 450, 200, -25)
transform(0, 320, -100, 30)

principal(-260, -60, 480)
principal(-600, -400, 350)
principal(160, -480, -600)
principal(30, 570, 720)
