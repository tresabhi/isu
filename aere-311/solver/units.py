from symbols import *
from registry import *

durbin_output_units = {
    p0: ur.atm,
    p1: ur.atm,
    p2: ur.atm,
    p01: ur.atm,
    p02: ur.atm,
    p_star: ur.atm,
    #
    mu: ur.deg,
    beta: ur.deg,
    theta: ur.deg,
}

imperial_output_units = {
    **durbin_output_units,
    #
    d: ur.ft,
    d1: ur.ft,
    d2: ur.ft,
    H: ur.ft,
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

ephemeral_units = {
    **durbin_output_units,
    #
    p2: ur.N / ur.m**2,
}
