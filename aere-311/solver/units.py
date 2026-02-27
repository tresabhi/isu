from symbols import *
from registry import *

durbin_output_units = {
    p0: ur.atm,
    p1: ur.atm,
    p2: ur.atm,
    p01: ur.atm,
    p02: ur.atm,
    p_star: ur.atm,
}

imperial_output_units = {
    **durbin_output_units,
    #
    d1: ur.ft,
    d2: ur.ft,
    H1: ur.ft,
    H2: ur.ft,
    #
    T0: ur.rankine,
    T1: ur.rankine,
    T2: ur.rankine,
    T01: ur.rankine,
    T02: ur.rankine,
    #
    p0: ur.lbf / ur.ft**2,
    p1: ur.lbf / ur.ft**2,
    p2: ur.lbf / ur.ft**2,
    p01: ur.lbf / ur.ft**2,
    p02: ur.lbf / ur.ft**2,
    p_star: ur.lbf / ur.ft**2,
}
