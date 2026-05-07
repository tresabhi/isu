from shaker import *
from hoppers import *


class NormalShockNozzleShaker(Shaker):
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
