import solver
import airfoils

X_initial = [
    0,  # alpha [deg]
    0,  # Gamma [deg]
    0,  # theta_tip [deg]
    1,  # c_root [m]
    1,  # c_tip [m]
]

_, _, V0, _ = solver.Solve(airfoils.naca0012, X_initial)
