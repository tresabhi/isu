import pint

ur = pint.UnitRegistry()

T = 982 * ur.rankine
p = 7.8 * ur.atm
R = 287 * ur.J / (ur.kg * ur.K)

rho = p / (R * T)
rho = rho.to(ur.slug / ur.ft**3)

print(rho)
