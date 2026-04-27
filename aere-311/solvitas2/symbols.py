from symbol import *

h1 = Symbol("h1", "J / kg")
h2 = Symbol("h2", "J / kg")
h1_h2 = Symbol("h1/h2")
h2_h1 = Symbol("h2/h1")

delta_s = Symbol("delta_s", "J / (kg * K)")

gamma = Symbol("gamma")
R = Symbol("R", "J / (kg * K)")
cp = Symbol("cp", "J / (kg * K)")
cv = Symbol("cv", "J / (kg * K)")
Q = Symbol("Q", "J / kg")

M = Symbol("M")
M1 = Symbol("M1")
M2 = Symbol("M2")
M_inf = Symbol("M_inf")
M_cr = Symbol("M_cr")

p = Symbol("p", "Pa")
p1 = Symbol("p1", "Pa")
p2 = Symbol("p2", "Pa")
p0 = Symbol("p0", "Pa")
p01 = Symbol("p01", "Pa")
p02 = Symbol("p02", "Pa")
p_star = Symbol("p*", "Pa")
p_cr = Symbol("p_cr", "Pa")
p_inf = Symbol("p_inf", "Pa")

p1_p2 = Symbol("p1/p2")
p2_p1 = Symbol("p2/p1")

p_p0 = Symbol("p/p0")
p1_p01 = Symbol("p1/p01")
p2_p02 = Symbol("p2/p02")
p0_p = Symbol("p0/p")
p01_p1 = Symbol("p01/p1")
p02_p2 = Symbol("p02/p2")
p01_p02 = Symbol("p01/p02")
p02_p01 = Symbol("p02/p01")

p1_p_star = Symbol("p1/p*")
p2_p_star = Symbol("p2/p*")
p_star_p1 = Symbol("p*/p1")
p_star_p2 = Symbol("p*/p2")

p_cr_p_inf = Symbol("p_cr/p_inf")
p_inf_p_cr = Symbol("p_inf/p_cr")

rho = Symbol("rho", "kg / m^3")
rho1 = Symbol("rho1", "kg / m^3")
rho2 = Symbol("rho2", "kg / m^3")
rho0 = Symbol("rho0", "kg / m^3")
rho01 = Symbol("rho01", "kg / m^3")
rho02 = Symbol("rho02", "kg / m^3")
rho_star = Symbol("rho*", "kg / m^3")

rho1_rho2 = Symbol("rho1/rho2")
rho2_rho1 = Symbol("rho2/rho1")

rho_rho0 = Symbol("rho/rho0")
rho1_rho01 = Symbol("rho1/rho01")
rho2_rho02 = Symbol("rho2/rho02")
rho0_rho = Symbol("rho0/rho")
rho01_rho1 = Symbol("rho01/rho1")
rho02_rho2 = Symbol("rho02/rho2")

rho1_rho_star = Symbol("rho1/rho*")
rho2_rho_star = Symbol("rho2/rho*")
rho_star_rho1 = Symbol("rho*/rho1")
rho_star_rho2 = Symbol("rho*/rho2")

T = Symbol("T", "K")
T0 = Symbol("T0", "K")
T1 = Symbol("T1", "K")
T2 = Symbol("T2", "K")
T01 = Symbol("T01", "K")
T02 = Symbol("T02", "K")
T_star = Symbol("T*", "K")
T0_star = Symbol("T0*", "K")

delta_T0 = Symbol("delta_T0", "K")

T1_T2 = Symbol("T1/T2")
T2_T1 = Symbol("T2/T1")

T_T0 = Symbol("T/T0")
T1_T01 = Symbol("T1/T01")
T2_T02 = Symbol("T2/T02")
T0_T = Symbol("T0/T")
T01_T1 = Symbol("T01/T1")
T02_T2 = Symbol("T02/T2")
T01_T0_star = Symbol("T01/T0*")
T02_T0_star = Symbol("T02/T0*")
T0_star_T01 = Symbol("T0*/T01")
T0_star_T02 = Symbol("T0*/T02")

T1_T_star = Symbol("T1/T*")
T2_T_star = Symbol("T2/T*")
T_star_T1 = Symbol("T*/T1")
T_star_T2 = Symbol("T*/T2")

A_At = Symbol("A/At")

u1 = Symbol("u1", "m/s")
u2 = Symbol("u2", "m/s")
u_star = Symbol("u*", "m/s")

u1_u2 = Symbol("u1/u2")
u2_u1 = Symbol("u2/u1")

u1_u_star = Symbol("u1/u*")
u2_u_star = Symbol("u2/u*")
u_star_u1 = Symbol("u*/u1")
u_star_u2 = Symbol("u*/u2")

a1 = Symbol("a1", "m/s")
a2 = Symbol("a2", "m/s")

Cp = Symbol("Cp")
Cp0 = Symbol("Cp0")
Cp_cr = Symbol("Cp_cr")

# to do: finalize these ephemeral symbols

Ae_At1 = Symbol("Ae/At1")
Ae_At2 = Symbol("Ae/At2")
As_At1 = Symbol("As/At1")
As_At2 = Symbol("As/At2")
pe = Symbol("pe")
