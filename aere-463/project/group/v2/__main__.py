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

C_L, C_D, V, method = solver.Solve(airfoils.naca641212, X_initial)

print(C_L, C_D, V)

# debug.render_airplane(method)
# debug.render_airfoil(airfoils.naca0012)
