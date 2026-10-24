import airfoils
import solver

X = [
    0,  # alpha
]

solution = solver.Solver(airfoils.naca641212, X)

print(solution)
