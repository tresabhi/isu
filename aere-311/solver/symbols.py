import sympy as sp
from pint import Unit
from registry import ur
import math

symbols: list["Symbol"] = []
EPSILON = 2**-2


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


d1 = Symbol("d1", "m", "Diameter (1)")
d2 = Symbol("d2", "m", "Diameter (2)")

A1 = Symbol("A1", "m", "Area (1)")
A2 = Symbol("A2", "m", "Area (2)")
A_star = Symbol("A*", "m^2", "Area (critical)")
A1_A_star = Symbol("A1/A*", None, "Area (1 / critical)")
A2_A_star = Symbol("A2/A*", None, "Area (2 / critical)")
A = Symbol("A", "m^2", "Area")
A_A_star = Symbol("A/A*", None, "Area (generic / critical)")
A_sub = Symbol("A_sub", "m^2", "Area (subsonic)")
A_sup = Symbol("A_sup", "m^2", "Area (supersonic)")
Ae_At = Symbol("Ae/At", None, "Area ratio (exit / throat)")

V_dot1 = Symbol("V_dot1", "m^3 / s", "Volumetric flow rate (1)")
V_dot2 = Symbol("V_dot2", "m^3 / s", "Volumetric flow rate (2)")
V_dot_sub = Symbol("V_dot_sub", "m^3 / s", "Volumetric flow rate (subsonic)")
V_dot_sup = Symbol("V_dot_sup", "m^3 / s", "Volumetric flow rate (supersonic)")

m_dot = Symbol("m_dot", "kg / s", "Mass flow rate (generic)")
m_dot1 = Symbol("m_dot1", "kg / s", "Mass flow rate (1)")
m_dot2 = Symbol("m_dot2", "kg / s", "Mass flow rate (2)")
m_dot_sub = Symbol("m_dot_sub", "kg / s", "Mass flow rate (subsonic)")
m_dot_sup = Symbol("m_dot_sup", "kg / s", "Mass flow rate (supersonic)")

F = Symbol("F", "N", "Force")

gamma = Symbol("gamma", None, "Heat capacity ratio")
R = Symbol("R", "J / (kg * K)", "Gas constant (specific)")
cp = Symbol("cp", "J / (kg * K)", "Specific heat (constant pressure)")
cv = Symbol("cv", "J / (kg * K)", "Specific heat (constant volume)")

e1 = Symbol("e1", "J / kg", "Total energy (1)")
e2 = Symbol("e2", "J / kg", "Total energy (2)")
delta_e = Symbol("e2-e1", "J / kg", "Total energy (2 - 1)")

h1 = Symbol("h1", "J / kg", "Enthalpy (1)")
h2 = Symbol("h2", "J / kg", "Enthalpy (2)")
delta_h = Symbol("h2-h1", "J / kg", "Enthalpy (2 - 1)")
h2_h1 = Symbol("h2/h1", None, "Enthalpy ratio (2/1)")
h_sub = Symbol("h_sub", "J / kg", "Enthalpy (subsonic)")
h_sup = Symbol("h_sup", "J / kg", "Enthalpy (supersonic)")

s1 = Symbol("s1", "J / (kg * K)", "Entropy (1)")
s2 = Symbol("s2", "J / (kg * K)", "Entropy (2)")
delta_s = Symbol("s2-s1", "J / (kg * K)", "Entropy (2 - 1)")

u1 = Symbol("u1", "m / s", "Velocity (1)")
u2 = Symbol("u2", "m / s", "Velocity (2)")
u2_u1 = Symbol("u2/u1", None, "Velocity (2/1)")
u_star = Symbol("u*", "m / s", "Velocity (critical)")
a_star_u1 = Symbol("a*/u1", None, "Speed of sound / velocity (critical / 1)")
a_star_u2 = Symbol("a*/u2", None, "Speed of sound / velocity (critical / 2)")
u1_a_star = Symbol("u1/a*", None, "Velocity (1) / speed of sound (critical)")
u2_a_star = Symbol("u2/a*", None, "Velocity (2) / speed of sound (critical)")
u_sub = Symbol("u_sub", "m / s", "Velocity (subsonic)")
u_sup = Symbol("u_sup", "m / s", "Velocity (supersonic)")
u_sub_a_star = Symbol(
    "u_sub/a*", None, "Velocity (subsonic) / speed of sound (critical)"
)
u_sup_a_star = Symbol(
    "u_sup/a*", None, "Velocity (supersonic) / speed of sound (critical)"
)

a0 = Symbol("a0", "m / s", "Speed of sound (stagnant)")
a1 = Symbol("a1", "m / s", "Speed of sound (1)")
a2 = Symbol("a2", "m / s", "Speed of sound (2)")
a_star = Symbol("a*", "m / s", "Speed of sound (critical)")
a_sub = Symbol("a_sub", "m / s", "Speed of sound (subsonic)")
a_sup = Symbol("a_sup", "m / s", "Speed of sound (supersonic)")
a_star_u_sub = Symbol(
    "a*/u_sub", None, "Speed of sound / velocity (critical / subsonic)"
)
a_star_u_sup = Symbol(
    "a*/u_sup", None, "Speed of sound / velocity (critical / supersonic)"
)

M1 = Symbol("M1", None, "Mach number (1)", initial=2)
M2 = Symbol("M2", None, "Mach number (2)", initial=2)
Mn1 = Symbol("Mn1", None, "Mach number (normal 1)", initial=2)
Mn2 = Symbol("Mn2", None, "Mach number (normal 2)", initial=2)
M1_star = Symbol("M1*", None, "Mach number (critical 1)", initial=2)
M2_star = Symbol("M2*", None, "Mach number (critical 2)", initial=2)
M_star = Symbol("M*", None, "Mach number (critical)", initial=2)
M_sub = Symbol("M_sub", None, "Mach number (generic)", initial=EPSILON)
M_sup = Symbol("M_sup", None, "Mach number (generic)", initial=2)
Me = Symbol("Me", None, "Mach number (exit)")

p0 = Symbol("p0", "Pa", "Pressure (stagnant)")
p1 = Symbol("p1", "Pa", "Pressure (1)")
p2 = Symbol("p2", "Pa", "Pressure (2)")
p3 = Symbol("p3", "Pa", "Pressure (3)")
p01 = Symbol("p01", "Pa", "Pressure (stagnant 1)")
p02 = Symbol("p02", "Pa", "Pressure (stagnant 2)")
p0_p1 = Symbol("p0/p1", None, "Pressure ratio (stagnant / 1)")
p0_p2 = Symbol("p0/p2", None, "Pressure ratio (stagnant / 2)")
p1_p01 = Symbol("p1/p01", None, "Pressure ratio (1 / stagnant 1)")
p2_p1 = Symbol("p2/p1", None, "Pressure ratio (2 / 1)")
p3_p1 = Symbol("p3/p1", None, "Pressure ratio (3 / 1)")
p3_p2 = Symbol("p3/p2", None, "Pressure ratio (3 / 2)")
p4_p1 = Symbol("p4/p1", None, "Pressure ratio (4 / 1)")
p5_p1 = Symbol("p5/p1", None, "Pressure ratio (5 / 1)")
p5_p4 = Symbol("p5/p4", None, "Pressure ratio (5 / 4)")
p2_p02 = Symbol("p2/p02", None, "Pressure ratio (2 / stagnant 2)")
p01_p1 = Symbol("p01/p1", None, "Pressure ratio (stagnant 1 / 1)")
p01_p2 = Symbol("p01/p2", None, "Pressure ratio (stagnant 1 / 2)")
p02_p1 = Symbol("p02/p1", None, "Pressure ratio (stagnant 2 / 1)")
p02_p2 = Symbol("p02/p2", None, "Pressure ratio (stagnant 2 / 2)")
p02_p01 = Symbol("p02/p01", None, "Pressure ratio (stagnant 2 / stagnant 1)")
p_star = Symbol("p*", "Pa", "Pressure (critical)")
p_star_p0 = Symbol("p*/p0", None, "Pressure ratio (critical / stagnant)")
p_star_p1 = Symbol("p*/p1", None, "Pressure ratio (critical / 1)")
p_star_p2 = Symbol("p*/p2", None, "Pressure ratio (critical / 2)")
p_sub = Symbol("p_sub", "Pa", "Pressure (subsonic)")
p_sup = Symbol("p_sup", "Pa", "Pressure (supersonic)")
p0_p_sub = Symbol("p0/p_sub", None, "Pressure ratio (stagnant / subsonic)")
p0_p_sup = Symbol("p0/p_sup", None, "Pressure ratio (stagnant / supersonic)")
p_sub_p0 = Symbol("p_sub/p0", None, "Pressure ratio (subsonic / stagnant)")
p_sup_p0 = Symbol("p_sup/p0", None, "Pressure ratio (supersonic / stagnant)")
pe = Symbol("pe", "Pa", "Pressure (exit)")

rho0 = Symbol("rho0", "kg / m^3", "Density (stagnant)")
rho1 = Symbol("rho1", "kg / m^3", "Density (1)")
rho2 = Symbol("rho2", "kg / m^3", "Density (2)")
rho0_rho1 = Symbol("rho0/rho_1", None, "Density ratio (stagnant / 1)")
rho0_rho2 = Symbol("rho0/rho_2", None, "Density ratio (stagnant / 2)")
rho2_rho1 = Symbol("rho2/rho_1", None, "Density ratio (2 / 1)")
rho01 = Symbol("rho01", "kg / m^3", "Density (stagnant 1)")
rho02 = Symbol("rho02", "kg / m^3", "Density (stagnant 2)")
rho01_rho1 = Symbol("rho01/rho1", None, "Density ratio (stagnant 1 / 1)")
rho02_rho2 = Symbol("rho02/rho2", None, "Density ratio (stagnant 2 / 2)")
rho_star = Symbol("rho*", "kg / m^3", "Density (critical)")
rho_star_rho0 = Symbol("rho*/rho_0", None, "Density (critical / stagnant)")
rho_star_rho1 = Symbol("rho*/rho_1", None, "Density (critical / 1)")
rho_star_rho2 = Symbol("rho*/rho_2", None, "Density (critical / 2)")
rho_star_rho01 = Symbol("rho*/rho_01", None, "Density (critical / stagnant 1)")
rho_star_rho02 = Symbol("rho*/rho_02", None, "Density (critical / stagnant 2)")
rho_sub = Symbol("rho_sub", "kg / m^3", "Density (subsonic)")
rho_sup = Symbol("rho_sup", "kg / m^3", "Density (supersonic)")
rho_star_rho_sub = Symbol("rho*/rho_sub", None, "Density ratio (critical / subsonic)")
rho_star_rho_sup = Symbol("rho*/rho_sup", None, "Density ratio (critical / supersonic)")
rho0_rho_sub = Symbol("rho0/rho_sub", None, "Density ratio (stagnant / subsonic)")
rho0_rho_sup = Symbol("rho0/rho_sup", None, "Density ratio (stagnant / supersonic)")

T0 = Symbol("T0", "K", "Temperature (stagnant)")
T1 = Symbol("T1", "K", "Temperature (1)")
T2 = Symbol("T2", "K", "Temperature (2)")
T0_T1 = Symbol("T0/T1", None, "Temperature ratio (stagnant / 1)")
T0_T2 = Symbol("T0/T2", None, "Temperature ratio (stagnant / 2)")
T1_T01 = Symbol("T1/T01", None, "Temperature ratio (1 / stagnant 1)")
T2_T1 = Symbol("T2/T1", None, "Temperature ratio (2 / 1)")
T2_T02 = Symbol("T2/T02", None, "Temperature ratio (2 / stagnant 2)")
T01 = Symbol("T01", "K", "Temperature (stagnant 1)")
T02 = Symbol("T02", "K", "Temperature (stagnant 2)")
T01_T1 = Symbol("T01/T1", None, "Temperature ratio (stagnant 1 / 1)")
T02_T2 = Symbol("T02/T2", None, "Temperature ratio (stagnant 2 / 2)")
T02_T01 = Symbol("T02/T01", None, "Temperature ratio (stagnant 2 / stagnant 1)")
T_star = Symbol("T*", "K", "Temperature (critical)")
T_star_T0 = Symbol("T*/T0", None, "Temperature ratio (critical / stagnant)")
T_star_T1 = Symbol("T*/T1", None, "Temperature ratio (critical / 1)")
T_star_T2 = Symbol("T*/T2", None, "Temperature ratio (critical / 2)")
T_sub = Symbol("T_sub", "K", "Temperature (subsonic)")
T_sup = Symbol("T_sup", "K", "Temperature (supersonic)")
T0_T_sub = Symbol("T0/T_sub", None, "Temperature ratio (stagnant / subsonic)")
T0_T_sup = Symbol("T0/T_sup", None, "Temperature ratio (stagnant / supersonic)")

d = Symbol("d", "m", "Distance")
H = Symbol("H", "m", "Elevation")

mu1 = Symbol("mu1", "radian", "Mach line (1)")
mu2 = Symbol("mu2", "radian", "Mach line (2)")
theta = Symbol("theta", "radian", "Angle (generic)")
beta_weak = Symbol("beta_weak", "radian", "Shock angle (weak)", initial=EPSILON)
beta_strong = Symbol(
    "beta_strong", "radian", "Shock angle (strong)", initial=math.pi / 2
)

w1 = Symbol("w1", "m / s", "Wave tangential velocity (1)")
w2 = Symbol("w2", "m / s", "Wave tangential velocity (2)")

nu1 = Symbol("nu1", "radian", "Flow turning angle (1)")
nu2 = Symbol("nu2", "radian", "Flow turning angle (2)")

alpha = Symbol("alpha", "radian", "Angle of attack")
epsilon = Symbol("epsilon", "radian", "Diamond wedge inner half angle")

cl = Symbol("cl", None, "Lift coefficient", positive=None)
cd = Symbol("cd", None, "Drag coefficient", positive=None)

c = Symbol("c", "m", "Chord length")
t = Symbol("t", "m", "Airfoil max thickness")

R_prime = Symbol("R'", "N / m", "Reaction per unit span")
L_prime = Symbol("L'", "N / m", "Lift per unit span")
D_prime = Symbol("D'", "N / m", "Drag per unit span")

S = Symbol("S", "m^2", "Planform area")

q1 = Symbol("q1", "Pa", "Dynamic pressure (1)")
q2 = Symbol("q2", "Pa", "Dynamic pressure (2)")
