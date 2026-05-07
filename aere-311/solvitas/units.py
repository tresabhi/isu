from registry import *

anderson_units = {
    ur("Pa"): ur("atm"),
    ur("rad"): ur("deg"),
}

imperial_units = {
    **anderson_units,
    #
    ur("K"): ur("rankine"),
    ur("m"): ur("ft"),
    ur("m / s"): ur("ft / s"),
    ur("kg / m^3"): ur("slug / ft^3"),
    ur("kg / s"): ur("slug / s"),
    ur("m^2"): ur("ft^2"),
    ur("J / kg"): ur("(ft * lbf) / slug"),
    ur("J / (K * kg)"): ur("(ft * lbf) / (slug * rankine)"),
}

ephemeral_units = {
    **anderson_units,
    #
    ur("Pa"): ur("N/m^2"),
}
