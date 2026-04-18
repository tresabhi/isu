import pint

ur = pint.UnitRegistry()

Sy = 4 * ur.kN

r = 12 * ur.cm
w = 25 * ur.cm
L = 1 * ur.m

Ai = 1 * ur.cm**2

y1 = y2 = r
y3 = y4 = -r
y5 = 0 * ur.m

Ixx = Ai * y1**2 + Ai * y2**2 + Ai * y3**2 + Ai * y4**2 + Ai * y5**2
M = Sy * L

sigma1 = (M * y1) / Ixx
sigma2 = (M * y2) / Ixx
sigma3 = (M * y3) / Ixx
sigma4 = (M * y4) / Ixx
sigma5 = (M * y5) / Ixx

F1 = sigma1 * Ai
F2 = sigma2 * Ai
F3 = sigma3 * Ai
F4 = sigma4 * Ai
F5 = sigma5 * Ai

F1 = F1.to(ur.kN)
F2 = F2.to(ur.kN)
F3 = F3.to(ur.kN)
F4 = F4.to(ur.kN)
F5 = F5.to(ur.kN)

print(f"F1 = {F1}")
print(f"F2 = {F2}")
print(f"F3 = {F3}")
print(f"F4 = {F4}")
print(f"F5 = {F5}")
