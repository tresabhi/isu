import solver
import airfoils
import debug

X_initial = [
    0,  # alpha [deg]
    0,  # Gamma [deg]
    0,  # theta_tip [deg]
    1,  # c_root [m]
    1,  # c_tip [m]
]

solution = solver.Solve(airfoils.naca0012, X_initial)

print(solution)

debug.render_airfoil(airfoils.naca0012)
