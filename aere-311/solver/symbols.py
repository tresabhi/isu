import sympy as sp
from pint import Unit
from registry import ur
import math

symbols: list["Symbol"] = []


class Symbol(sp.Symbol):
    unit: Unit

    def __new__(
        self,
        name: str,
        unit: str = None,
        initial: float = 0.1,
        positive=True,
    ):
        symbol = sp.Symbol.__new__(
            self, name, positive=True if positive else None, real=True
        )
        symbol.unit = ur("dimensionless" if unit is None else unit)
        symbol.initial = initial

        symbols.append(symbol)

        return symbol


S = Symbol

d1 = S("d_1", "m")
d2 = S("d_2", "m")

A1 = S("A_1", "m")
A2 = S("A_2", "m")

V_dot1 = S("\\dot{V}_1", "m^3 / s")
V_dot2 = S("\\dot{V}_2", "m^3 / s")

m_dot = S("\\dot{m}", "kg / s")
m_dot1 = S("\\dot{m}_1", "kg / s")
m_dot2 = S("\\dot{m}_2", "kg / s")

F = S("F", "N")

gamma = S("\\gamma")
R = S("R", "J / (kg * K)")
cp = S("c_p", "J / (kg * K)")
cv = S("c_v", "J / (kg * K)")

e1 = S("e_1", "J / kg")
e2 = S("e_2", "J / kg")
delta_e = S("\\Delta e", "J / (kg * K)")

h1 = S("h_1", "J / kg")
h2 = S("h_2", "J / kg")
delta_h = S("\\Delta h", "J / kg")
h2_h1 = S("{h_2}/{h_1}")

s1 = S("s_1", "J / (kg * K)")
s2 = S("s_2", "J / (kg * K)")
delta_s = S("\\Delta s", "J / (kg * K)")

u1 = S("u_1", "m / s")
u2 = S("u_2", "m / s")
u2_u1 = S("{u_2}/{u_1}")

a0 = S("a_0", "m / s")
a1 = S("a_1", "m / s")
a2 = S("a_2", "m / s")
a_star = S("a^*", "m / s")

M1 = S("M_1")
M2 = S("M_2")
Mn1 = S("M_{n1}")
Mn2 = S("M_{n2}")
M1_star = S("M_1^*")
M2_star = S("M_2^*")

p0 = S("p_0", "Pa")
p1 = S("p_1", "Pa")
p2 = S("p_2", "Pa")
p01 = S("p_{01}", "Pa")
p02 = S("p_{02}", "Pa")
p0_p1 = S("{p_0}/{p_1}")
p0_p2 = S("{p_0}/{p_2}")
p2_p1 = S("{p_2}/{p_1}")
p01_p1 = S("{p_{01}}/{p_1}")
p01_p2 = S("{p_{01}}/{p_2}")
p02_p1 = S("{p_{02}}/{p_1}")
p02_p2 = S("{p_{02}}/{p_2}")
p02_p01 = S("{p_{02}}/{p_{01}}")
p_star = S("p^*", "Pa")
p_star_p0 = S("{p^*}/{p_0}")
p_star_p1 = S("{p^*}/{p_1}")
p_star_p2 = S("{p^*}/{p_2}")

rho0 = S("\\rho_0", "kg / m^3")
rho1 = S("\\rho_1", "kg / m^3")
rho2 = S("\\rho_2", "kg / m^3")
rho0_rho1 = S("{\\rho_0}/{\\rho_1}")
rho0_rho2 = S("{\\rho_0}/{\\rho_2}")
rho2_rho1 = S("{\\rho_2}/{\\rho_1}")
rho01 = S("\\rho_{01}", "kg / m^3")
rho02 = S("\\rho_{02}", "kg / m^3")
rho01_rho1 = S("{\\rho_{01}}/{\\rho_1}")
rho02_rho2 = S("{\\rho_{02}}/{\\rho_2}")
rho_star = S("\\rho^*", "kg / m^3")
rho_star_rho0 = S("{\\rho^*}/{\\rho_0}")
rho_star_rho1 = S("{\\rho^*}/{\\rho_1}")
rho_star_rho2 = S("{\\rho^*}/{\\rho_2}")

T0 = S("T_0", "K")
T1 = S("T_1", "K")
T2 = S("T_2", "K")
T0_T1 = S("{T_0}/{T_1}")
T0_T2 = S("{T_0}/{T_2}")
T2_T1 = S("{T_2}/{T_1}")
T01 = S("T_{01}", "K")
T02 = S("T_{02}", "K")
T01_T1 = S("{T_{01}}/{T_1}")
T02_T2 = S("{T_{02}}/{T_2}")
T02_T01 = S("{T_{02}/T_{01}}")
T_star = S("T^*", "K")
T_star_T0 = S("{T^*}/{T_0}")
T_star_T1 = S("{T^*}/{T_1}")
T_star_T2 = S("{T^*}/{T_2}")

d = S("d", "m")
H = S("H", "m")

mu = S("\\mu", "radian")
theta = S("\\theta", "radian")
beta_weak = S("\\beta_\\text{weak}", "radian", 0.01)
beta_strong = S("\\beta_\\text{strong}", "radian", initial=math.pi / 2)

w1 = S("w_1", "m / s")
w2 = S("w_2", "m / s")
