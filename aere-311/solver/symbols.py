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
        unit: str,
        memo: str,
        initial: float = 0.1,
        positive=True,
    ):
        symbol = sp.Symbol.__new__(
            self, name, positive=True if positive else None, real=True, imaginary=False
        )
        symbol.unit = ur("dimensionless" if unit is None else unit)
        symbol.initial = initial
        symbol.memo = memo

        symbols.append(symbol)

        return symbol


S = Symbol

d1 = S("d1", "m", "Diameter (1)")
d2 = S("d2", "m", "Diameter (2)")

A1 = S("A1", "m", "Area (1)")
A2 = S("A2", "m", "Area (2)")

V_dot1 = S("V_dot1", "m^3 / s", "Volumetric flow rate (1)")
V_dot2 = S("V_dot2", "m^3 / s", "Volumetric flow rate (2)")

m_dot = S("m_dot", "kg / s", "Mass flow rate (generic)")
m_dot1 = S("m_dot1", "kg / s", "Mass flow rate (1)")
m_dot2 = S("m_dot2", "kg / s", "Mass flow rate (2)")

F = S("F", "N", "Force")

gamma = S("gamma", None, "Heat capacity ratio")
R = S("R", "J / (kg * K)", "Gas constant (specific)")
cp = S("cp", "J / (kg * K)", "Specific heat (constant pressure)")
cv = S("cv", "J / (kg * K)", "Specific heat (constant volume)")

e1 = S("e1", "J / kg", "Total energy (1)")
e2 = S("e2", "J / kg", "Total energy (2)")
delta_e = S("e2-e1", "J / kg", "Total energy (2 - 1)")

h1 = S("h1", "J / kg", "Enthalpy (1)")
h2 = S("h2", "J / kg", "Enthalpy (2)")
delta_h = S("h2-h1", "J / kg", "Enthalpy (2 - 1)")
h2_h1 = S("h2/h1", None, "Enthalpy ratio (2/1)")

s1 = S("s1", "J / (kg * K)", "Entropy (1)")
s2 = S("s2", "J / (kg * K)", "Entropy (2)")
delta_s = S("s2-s1", "J / (kg * K)", "Entropy (2 - 1)")

u1 = S("u1", "m / s", "Velocity (1)")
u2 = S("u2", "m / s", "Velocity (2)")
u2_u1 = S("u2/u1", None, "Velocity (2/1)")

a0 = S("a0", "m / s", "Speed of sound (stagnant)")
a1 = S("a1", "m / s", "Speed of sound (1)")
a2 = S("a2", "m / s", "Speed of sound (2)")
a_star = S("a*", "m / s", "Speed of sound (critical)")

M1 = S("M1", None, "Mach number (1)", initial=2)
M2 = S("M2", None, "Mach number (2)", initial=2)
Mn1 = S("Mn1", None, "Mach number (normal 1)", initial=2)
Mn2 = S("Mn2", None, "Mach number (normal 2)", initial=2)
M1_star = S("M1*", None, "Mach number (critical 1)", initial=2)
M2_star = S("M2*", None, "Mach number (critical 2)", initial=2)

p0 = S("p0", "Pa", "Pressure (stagnant)")
p1 = S("p1", "Pa", "Pressure (1)")
p2 = S("p2", "Pa", "Pressure (2)")
p01 = S("p01", "Pa", "Pressure (stagnant 1)")
p02 = S("p02", "Pa", "Pressure (stagnant 2)")
p0_p1 = S("p0/p1", None, "Pressure ratio (stagnant / 1)")
p0_p2 = S("p0/p2", None, "Pressure ratio (stagnant / 2)")
p1_p01 = S("p1/p01", None, "Pressure ratio (1 / stagnant 1)")
p2_p1 = S("p2/p1", None, "Pressure ratio (2 / 1)")
p3_p1 = S("p3/p1", None, "Pressure ratio (3 / 1)")
p2_p02 = S("p2/p02", None, "Pressure ratio (2 / stagnant 2)")
p01_p1 = S("p01/p1", None, "Pressure ratio (stagnant 1 / 1)")
p01_p2 = S("p01/p2", None, "Pressure ratio (stagnant 1 / 2)")
p02_p1 = S("p02/p1", None, "Pressure ratio (stagnant 2 / 1)")
p02_p2 = S("p02/p2", None, "Pressure ratio (stagnant 2 / 2)")
p02_p01 = S("p02/p01", None, "Pressure ratio (stagnant 2 / stagnant 1)")
p_star = S("p*", "Pa", "Pressure (critical)")
p_star_p0 = S("p*/p0", None, "Pressure ratio (critical / stagnant)")
p_star_p1 = S("p*/p1", None, "Pressure ratio (critical / 1)")
p_star_p2 = S("p*/p2", None, "Pressure ratio (critical / 2)")

rho0 = S("rho0", "kg / m^3", "Density (stagnant)")
rho1 = S("rho1", "kg / m^3", "Density (1)")
rho2 = S("rho2", "kg / m^3", "Density (2)")
rho0_rho1 = S("rho0/rho_1", None, "Density ratio (stagnant / 1)")
rho0_rho2 = S("rho0/rho_2", None, "Density ratio (stagnant / 2)")
rho2_rho1 = S("rho2/rho_1", None, "Density ratio (2 / 1)")
rho01 = S("rho01", "kg / m^3", "Density (stagnant 1)")
rho02 = S("rho02", "kg / m^3", "Density (stagnant 2)")
rho01_rho1 = S("rho01/rho1", None, "Density ratio (stagnant 1 / 1)")
rho02_rho2 = S("rho02/rho2", None, "Density ratio (stagnant 2 / 2)")
rho_star = S("rho*", "kg / m^3", "Density (critical)")
rho_star_rho0 = S("rho*/rho_0", None, "Density (critical / stagnant)")
rho_star_rho1 = S("rho*/rho_1", None, "Density (critical / 1)")
rho_star_rho2 = S("rho*/rho_2", None, "Density (critical / 2)")

T0 = S("T0", "K", "Temperature (stagnant)")
T1 = S("T1", "K", "Temperature (1)")
T2 = S("T2", "K", "Temperature (2)")
T0_T1 = S("T0/T1", None, "Temperature ratio (stagnant / 1)")
T0_T2 = S("T0/T2", None, "Temperature ratio (stagnant / 2)")
T1_T01 = S("T1/T01", None, "Temperature ratio (1 / stagnant 1)")
T2_T1 = S("T2/T1", None, "Temperature ratio (2 / 1)")
T2_T02 = S("T2/T02", None, "Temperature ratio (2 / stagnant 2)")
T01 = S("T01", "K", "Temperature (stagnant 1)")
T02 = S("T02", "K", "Temperature (stagnant 2)")
T01_T1 = S("T01/T1", None, "Temperature ratio (stagnant 1 / 1)")
T02_T2 = S("T02/T2", None, "Temperature ratio (stagnant 2 / 2)")
T02_T01 = S("T02/T01", None, "Temperature ratio (stagnant 2 / stagnant 1)")
T_star = S("T*", "K", "Temperature (critical)")
T_star_T0 = S("T*/T0", None, "Temperature ratio (critical / stagnant)")
T_star_T1 = S("T*/T1", None, "Temperature ratio (critical / 1)")
T_star_T2 = S("T*/T2", None, "Temperature ratio (critical / 2)")

d = S("d", "m", "Distance")
H = S("H", "m", "Elevation")

mu1 = S("mu1", "radian", "Mach line (1)")
mu2 = S("mu2", "radian", "Mach line (2)")
theta = S("theta", "radian", "Angle (generic)")
beta_weak = S("beta_weak", "radian", "Shock angle (weak)", initial=0.001)
beta_strong = S("beta_strong", "radian", "Shock angle (strong)", initial=math.pi / 2)

w1 = S("w1", "m / s", "Wave tangential velocity (1)")
w2 = S("w2", "m / s", "Wave tangential velocity (2)")

nu1 = S("nu1", "radian", "Flow turning angle (1)")
nu2 = S("nu2", "radian", "Flow turning angle (2)")

alpha = S("alpha", "radian", "Angle of attack")
epsilon = S("epsilon", "radian", "Diamond wedge inner half angle")
cl = S("cl", None, "Lift coefficient")
cd = S("cd", None, "Drag coefficient")

c = S("c", "m", "Chord length")
t = S("t", "m", "Airfoil max thickness")

R_prime = S("R'", "N / m", "Reaction per unit span")
L_prime = S("R'", "N / m", "Lift per unit span")
D_prime = S("R'", "N / m", "Drag per unit span")
