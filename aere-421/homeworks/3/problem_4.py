import sympy

omega = sympy.Symbol("omega")

a = 14.8 * 10**7 - omega**2 * 0.38475
b = -6 * 10**7 - omega**2 * 0.049875
c = -6 * 10**7 - omega**2 * 0.049875
d = 6 * 10**7 - omega**2 * 0.049875

det = a * d - b * c

omega_solutions = sympy.solve(det, omega)

print(omega_solutions)
