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

solver = Solver(
    equations=[
        *linearized_flat_plate_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    diamond_wedge(
        {
            **air,
            epsilon: 10 * ur.deg,
            alpha: 15 * ur.deg,
            M1: 3,
        }
    )
