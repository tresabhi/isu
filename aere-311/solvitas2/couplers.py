from coupler import *
from hoppers import *
from utils import *


class NormalShockNozzle(Coupler):
    hoppers = [
        SupersonicNozzle,
        NormalShock,
        SubsonicNozzle,
        PostShockNozzle,
    ]

    transformers = [
        ("generic", 1),
        (2, "generic"),
        ("nozzle_post_shock", "nozzle_post_shock_exit"),
    ]
