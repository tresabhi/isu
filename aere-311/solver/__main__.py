from solver import Solver
from registry import ur
from symbols import *
from equations import *
from units import *
from utils import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

# solver = Solver(
#     equations=[
#         *composite_equations,
#         *shock_static_equations,
#         *state_equations,
#         *specific_heat_equations,
#         *diamond_wedge_equations,
#     ],
#     output_units=durbin_output_units,
# )

if __name__ == "__main__":
    flat_plate(
        {
            **air,
            M1: 5,
            alpha: 5 * ur.deg,
        }
    )
