from sympy import symbols

u, u0, u_inf, u_star = symbols("u u0 u_inf u*")
a, a0, a_inf, a_star = symbols("a a0 a_inf a*")
M, M0, M_inf, M_star = symbols("M M0 M_inf M*")

p, p0, p_inf, p_star = symbols("p p0 p_inf p*")
rho, rho0, rho_inf, rho_star = symbols("rho rho0 rho_inf rho*")
T, T0, T_inf, T_star = symbols("T T0 T_inf T*")

p0_p, p0_p_inf, p0_p_star = symbols("p0/p p0/p_inf p0/p*")
rho0_rho, rho0_rho_inf, rho0_rho_star = symbols("rho0/rho rho0/rho_inf rho0/rho*")
T0_T, T0_T_inf, T0_T_star = symbols("T0/T T0/T_inf T0/T*")

q, q0, q_inf, q_star = symbols("q q0 q_inf q*")

gamma = symbols("gamma")
c_p, c_v, R = symbols("c_p c_v R")
