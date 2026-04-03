from symbols import *
from registry import *

durbin_output_units = {
    p0: ur.atm,
    p1: ur.atm,
    p2: ur.atm,
    p3: ur.atm,
    p01: ur.atm,
    p02: ur.atm,
    p_star: ur.atm,
    #
    q1: ur.atm,
    q2: ur.atm,
    #
    mu1: ur.deg,
    mu2: ur.deg,
    beta_weak: ur.deg,
    beta_strong: ur.deg,
    theta: ur.deg,
    #
    nu1: ur.deg,
    nu2: ur.deg,
    #
    alpha: ur.deg,
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
    p0: ur.atm,
    p1: ur.atm,
    p2: ur.atm,
    p01: ur.atm,
    p02: ur.atm,
    p_star: ur.atm,
    #
    rho0: ur.slug / ur.ft**3,
    rho1: ur.slug / ur.ft**3,
    rho2: ur.slug / ur.ft**3,
    rho01: ur.slug / ur.ft**3,
    rho02: ur.slug / ur.ft**3,
    rho_star: ur.slug / ur.ft**3,
}

ephemeral_units = {
    **durbin_output_units,
    #
    p2: ur.N / ur.m**2,
    p02: ur.N / ur.m**2,
}
