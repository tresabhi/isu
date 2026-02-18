from sympy import symbols

R = symbols("R")
gamma = symbols("gamma")
cp, cv = symbols("cp cv")
e1, e2, delta_e = symbols("e1:3 delta_e")
h1, h2, delta_h, h2_h1 = symbols("h1:3 delta_h h2_h1")
s1, s2, delta_s = symbols("s1:3 delta_s")

u1, u2, u2_u1 = symbols("u1:3 u2/u1")
M1, M2 = symbols("M1:3")
a0, a1, a2, a_star = symbols("a0:3 a*")

p0, p1, p2, p2_p1, p0_p1, p0_p2, p01, p02, p02_p01 = symbols(
    "p0:3 p2/p1 p0/p1 p0/p2 p01 p02 p02/p01"
)
rho0, rho1, rho2, rho2_rho1, rho0_rho1, rho0_rho2 = symbols(
    "rho0:3 rho2/rho1 rho0/rho1 rho0/rho2"
)
T0, T1, T2, T2_T1, T0_T1, T0_T2, T01, T02 = symbols("T0:3 T2/T1 T0/T1 T0/T2 T01 T02")
