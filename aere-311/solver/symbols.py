from sympy import symbols

u, u0, u1, u2, u_inf, u_star = symbols("u u0:3 u_inf u*")
a, a0, a1, a2, a_inf, a_star = symbols("a a0:3 a_inf a*")
M, M0, M1, M2, M_inf, M_star = symbols("M M0:3 M_inf M*")

p, p0, p1, p2, p01, p02, p_inf, p_star = symbols("p p0:3 p01 p02 p_inf p*")
rho, rho0, rho1, rho2, rho_inf, rho_star = symbols("rho rho0:3 rho_inf rho*")
T, T0, T1, T2, T01, T02, T_inf, T_star = symbols("T T0:3 T01 T02 T_inf T*")

p0_p, p0_p_inf, p0_p_star, p2_p1, p01_p1, p02_p1 = symbols(
    "p0/p p0/p_inf p0/p* p2/p1 p01/p1 p02/p1"
)
rho0_rho, rho0_rho_inf, rho0_rho_star, rho2_rho1 = symbols(
    "rho0/rho rho0/rho_inf rho0/rho* rho2/rho1"
)
T0_T, T0_T_inf, T0_T_star, T2_T1 = symbols("T0/T T0/T_inf T0/T* T2/T1")
u2_u1 = symbols("u2/u1")

q, q0, q1, q2, q_inf, q_star = symbols("q q0:3 q_inf q*")

gamma = symbols("gamma")
c_p, c_v, R = symbols("c_p c_v R")
h1, h2, h2_h1 = symbols("h1:3 h2/h1")
s1, s2, s2_s1 = symbols("s1:3 s2-s1")
