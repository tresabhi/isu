import sympy as sp
from pint import Unit
from registry import ur

symbols: list["Symbol"] = []


class Symbol(sp.Symbol):
    unit: Unit

    def __new__(
        self,
        name: str,
        unit: str | None,
        positive=True,
    ):
        symbol = sp.Symbol.__new__(self, name, positive=positive)
        symbol.unit = ur("dimensionless" if unit is None else unit)

        symbols.append(symbol)

        return symbol


S = Symbol

d1 = S("d1", "m")
d2 = S("d2", "m")

A1 = S("A1", "m")
A2 = S("A2", "m")

V_dot1 = S("V_dot1", "m^3 / s")
V_dot2 = S("V_dot2", "m^3 / s")

m_dot = S("m_dot", "kg / s")
m_dot1 = S("m_dot1", "kg / s")
m_dot2 = S("m_dot2", "kg / s")

F = S("F", "N")

gamma = S("gamma", None)
R = S("R", "J / (kg * K)")
cp = S("cp", "J / (kg * K)")
cv = S("cv", "J / (kg * K)")

e1 = S("e1", "J / (kg * K)")
e2 = S("e2", "J / (kg * K)")
delta_e = S("delta_e", "J / (kg * K)")

h1 = S("h1", "J / kg")
h2 = S("h2", "J / kg")
delta_h = S("delta_h", "J / kg")
h2_h1 = S("h2/h1", None)

s1 = S("s1", "J / (kg * K)")
s2 = S("s2", "J / (kg * K)")
delta_s = S("delta_s", "J / (kg * K)")

u1 = S("u1", "m / s")
u2 = S("u2", "m / s")
u2_u1 = S("u2/u1", None)

a0 = S("a0", "m / s")
a1 = S("a1", "m / s")
a2 = S("a2", "m / s")
a_star = S("a*", "m / s")

M1 = S("M1", None)
M2 = S("M2", None)
M1_star = S("M1*", None)
M2_star = S("M2*", None)

p0 = S("p0", "Pa")
p1 = S("p1", "Pa")
p2 = S("p2", "Pa")
p01 = S("p01", "Pa")
p02 = S("p02", "Pa")
p0_p1 = S("p0/p1", None)
p0_p2 = S("p0/p2", None)
p2_p1 = S("p2/p1", None)
p01_p1 = S("p01/p1", None)
p01_p2 = S("p01/p2", None)
p02_p1 = S("p02/p1", None)
p02_p2 = S("p02/p2", None)
p02_p01 = S("p02/p01", None)
p_star = S("p*", "Pa")
p_star_p0 = S("p*/p0", None)
p_star_p1 = S("p*/p1", None)
p_star_p2 = S("p*/p2", None)

rho0 = S("rho0", "kg / m^3")
rho1 = S("rho1", "kg / m^3")
rho2 = S("rho2", "kg / m^3")
rho0_rho1 = S("rho0/rho1", None)
rho0_rho2 = S("rho0/rho2", None)
rho2_rho1 = S("rho2/rho1", None)
rho01 = S("rho01", "kg / m^3")
rho02 = S("rho02", "kg / m^3")
rho01_rho1 = S("rho01/rho1", None)
rho02_rho2 = S("rho02/rho2", None)
rho_star = S("rho*", "kg / m^3")
rho_star_rho0 = S("rho*/rho0", None)
rho_star_rho1 = S("rho*/rho1", None)
rho_star_rho2 = S("rho*/rho2", None)

T0 = S("T0", "K")
T1 = S("T1", "K")
T2 = S("T2", "K")
T0_T1 = S("T0/T1", None)
T0_T2 = S("T0/T2", None)
T2_T1 = S("T2/T1", None)
T01 = S("T01", "K")
T02 = S("T02", "K")
T_star = S("T*", "K")
T_star_T0 = S("T*/T0", None)
T_star_T1 = S("T*/T1", None)
T_star_T2 = S("T*/T2", None)

H1 = S("H1", "m")
H2 = S("H2", "m")
mu1 = S("mu1", "radian")
mu2 = S("mu2", "radian")
