from sympy import symbols

u, u_0, u_inf, u_star = symbols("u u_0 u_inf u*")
a, a_0, a_inf, a_star = symbols("a a_0 a_inf a*")
M, M_0, M_inf, M_star = symbols("M M_0 M_inf M*")

p, p_0, p_inf, p_star = symbols("p p_0 p_inf p*")
rho, rho_0, rho_inf, rho_star = symbols("rho rho_0 rho_inf rho*")
T, T_0, T_inf, T_star = symbols("T T_0 T_inf T*")

p_0_p, p_0_p_inf, p_0_p_star = symbols("p_0/p p_0/p_inf p_0/p*")
rho_0_rho, rho_0_rho_inf, rho_0_rho_star = symbols("rho_0/rho rho_0/rho_inf rho_0/rho*")
T_0_T, T_0_T_inf, T_0_T_star = symbols("T_0/T T_0/T_inf T_0/T*")

q, q_0, q_inf, q_star = symbols("q q_0 q_inf q*")

gamma = symbols("gamma")
c_p, c_v, R = symbols("c_p c_v R")
