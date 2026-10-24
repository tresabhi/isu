import math
from pathlib import Path
import numpy as np
import aerosandbox as asb
import openmdao.api as om

A_INF = 340.0
U_INF = 102.0
RHO_INF = 1.20
MU_INF = 2.448e-5
P_INF = 101325.0

C_REF = 1.0
A_REF = 3.0
B_SEMI = 3.0

THETA_ROOT = 0.0

V0 = 0.2488
CL_MIN = 0.4

INITIAL_ALPHA = 2.0
INITIAL_SWEEP = 0.0
INITIAL_THETA_TIP = 0.0
INITIAL_C_ROOT = 1.0
INITIAL_C_TIP = 1.0

# https://m-selig.ae.illinois.edu/ads/coord/n64212.dat
SCRIPT_DIR = Path(__file__).resolve().parent
AIRFOIL_FILE = SCRIPT_DIR / "n64212.dat"


def read_coordinate_file(filename):
    points = []
    found_first_coordinate = False

    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            fields = line.replace(",", " ").split()

            if len(fields) < 2:
                continue

            try:
                x = float(fields[0])
                y = float(fields[1])
            except ValueError:
                continue

            if not (math.isfinite(x) and math.isfinite(y)):
                continue

            if not found_first_coordinate:
                if abs(x) > 2.0 or abs(y) > 0.5:
                    continue

                if abs(x) > 0.05:
                    continue

                found_first_coordinate = True

            points.append([x, y])

    return np.asarray(points, dtype=float)


def load_airfoil():
    coords = read_coordinate_file(AIRFOIL_FILE)

    x_min = float(np.min(coords[:, 0]))
    x_max = float(np.max(coords[:, 0]))
    chord_range = x_max - x_min

    coords[:, 0] = (coords[:, 0] - x_min) / chord_range
    coords[:, 1] = coords[:, 1] / chord_range

    leading_edge_indices = np.flatnonzero(
        np.isclose(coords[:, 0], 0.0, rtol=0.0, atol=1e-8)
    )

    if len(leading_edge_indices) == 2 and leading_edge_indices[0] == 0:
        split = int(leading_edge_indices[1])
        first_surface = coords[:split]
        second_surface = coords[split:]

        surfaces_are_le_to_te = (
            len(first_surface) >= 2
            and len(second_surface) >= 2
            and np.all(np.diff(first_surface[:, 0]) >= -1e-8)
            and np.all(np.diff(second_surface[:, 0]) >= -1e-8)
            and np.isclose(first_surface[-1, 0], 1.0, atol=1e-8)
            and np.isclose(second_surface[-1, 0], 1.0, atol=1e-8)
        )

        if surfaces_are_le_to_te:
            if np.mean(first_surface[:, 1]) >= np.mean(second_surface[:, 1]):
                upper_surface, lower_surface = first_surface, second_surface
            else:
                upper_surface, lower_surface = second_surface, first_surface
            coords = np.concatenate((upper_surface[::-1], lower_surface[1:]))

    airfoil = asb.Airfoil(
        name="NACA 64(1)-212",
        coordinates=coords,
    )

    return airfoil


AIRFOIL = load_airfoil()

print(AIRFOIL.coordinates[:3], AIRFOIL.coordinates[24:28])
print(AIRFOIL.local_camber(0.4))


def get_airfoil_area(airfoil):
    coords = np.asarray(airfoil.coordinates, dtype=float)

    x = coords[:, 0]
    y = coords[:, 1]

    area = 0.5 * abs(np.sum(x * np.roll(y, -1) - y * np.roll(x, -1)))

    return float(area)


A_AIRFOIL = get_airfoil_area(AIRFOIL)


def wing_volume(c_root, c_tip):
    return 2.0 * B_SEMI * A_AIRFOIL / 3.0 * (c_root**2 + c_root * c_tip + c_tip**2)


def Solver(alpha, sweep, theta_tip, c_root, c_tip):
    wing = asb.Wing(
        name="OptimizedWing",
        symmetric=True,
        xsecs=[
            asb.WingXSec(
                xyz_le=[0.0, 0.0, 0.0],
                chord=c_root,
                twist=THETA_ROOT,
                airfoil=AIRFOIL,
            ),
            asb.WingXSec(
                xyz_le=[
                    B_SEMI * math.tan(math.radians(sweep)),
                    B_SEMI,
                    0.0,
                ],
                chord=c_tip,
                twist=theta_tip,
                airfoil=AIRFOIL,
            ),
        ],
    )

    airplane = asb.Airplane(
        name="OptimizedWing",
        wings=[wing],
        s_ref=A_REF,
        c_ref=C_REF,
        b_ref=2.0 * B_SEMI,
    )

    op_point = asb.OperatingPoint(
        velocity=U_INF,
        alpha=alpha,
    )

    analysis = asb.VortexLatticeMethod(
        airplane=airplane,
        op_point=op_point,
        spanwise_resolution=40,
        chordwise_resolution=16,
    )

    aero = analysis.run()

    C_L = float(aero["CL"])
    C_D = float(aero["CD"])
    V = wing_volume(c_root, c_tip)

    return C_L, C_D, V


class WingOptimization(om.ExplicitComponent):

    def setup(self):
        self.add_input("alpha", val=INITIAL_ALPHA)
        self.add_input("sweep", val=INITIAL_SWEEP)
        self.add_input("theta_tip", val=INITIAL_THETA_TIP)
        self.add_input("c_root", val=INITIAL_C_ROOT)
        self.add_input("c_tip", val=INITIAL_C_TIP)

        self.add_output("C_L", val=0.0)
        self.add_output("C_D", val=0.0)
        self.add_output("V", val=0.0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd", form="central", step=1e-3)

    def compute(self, inputs, outputs):
        C_L, C_D, V = Solver(
            alpha=float(inputs["alpha"][0]),
            sweep=float(inputs["sweep"][0]),
            theta_tip=float(inputs["theta_tip"][0]),
            c_root=float(inputs["c_root"][0]),
            c_tip=float(inputs["c_tip"][0]),
        )

        outputs["C_L"] = C_L
        outputs["C_D"] = C_D
        outputs["V"] = V


prob = om.Problem()

prob.model.add_subsystem(
    "wing",
    WingOptimization(),
    promotes=["*"],
)

prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"
prob.driver.options["maxiter"] = 200
prob.driver.options["tol"] = 1e-8
prob.driver.options["disp"] = True


prob.model.add_design_var("alpha", lower=0.0, upper=10.0)
prob.model.add_design_var("sweep", lower=-10.0, upper=10.0)
prob.model.add_design_var("theta_tip", lower=-10.0, upper=10.0)
prob.model.add_design_var("c_root", lower=0.2, upper=3.0)
prob.model.add_design_var("c_tip", lower=0.2, upper=3.0)


prob.model.add_objective("C_D")
prob.model.add_constraint("C_L", lower=CL_MIN)
prob.model.add_constraint("V", equals=V0)

equal_chord = math.sqrt(V0 / (2.0 * B_SEMI * A_AIRFOIL))

prob.setup()

prob.set_val("alpha", INITIAL_ALPHA)
prob.set_val("sweep", INITIAL_SWEEP)
prob.set_val("theta_tip", INITIAL_THETA_TIP)
prob.set_val("c_root", equal_chord)
prob.set_val("c_tip", equal_chord)

prob.run_model()
print("initial C_L, C_D:", prob.get_val("C_L"), prob.get_val("C_D"))
print(prob.compute_totals(["C_D", "C_L"], ["alpha", "sweep"]))

prob.run_driver()
prob.check_totals(compact_print=True)

prob.model.list_inputs()
prob.model.list_outputs()
