import numpy as np
import pint

ur = pint.UnitRegistry()

mass = 40 * ur.slug
print(f"The mass is {mass}")

g = 32.2 * ur.ft / ur.s ** 2
print(f"The acceleration is {g}")

F = mass * g
print(f"The force is {F}")
print(f"The force in Newtons is {F.to(ur.N)}")

array_example = np.array([mass.magnitude]) * ur.kg
print(array_example)
