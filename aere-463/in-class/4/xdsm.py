from pyxdsm.XDSM import airfoils
import solver

X = [
    0,  # alpha
]

solution = solver.Solver(airfoils.naca641212, X)

print(solution)
import XDSM, FUNC

x = XDSM()

x.add_system("Aero", FUNC, "AeroComp")
x.add_system("Struct", FUNC, "StructComp")
x.add_system("Thermal", FUNC, "ThermalComp")

x.add_input("Aero", "\\theta")
x.add_output("Aero", "\\Gamma")

x.connect("Aero", "Struct", "\\Gamma")
x.connect("Struct", "Thermal", "T_{1, 2, 3}")
x.connect("Aero", "Thermal", "S")
x.connect("Struct", "Aero", "d")

x.add_input("Struct", "\\sigma")
x.add_output("Struct", "t")

x.write("test/singleComp")
