from registry import *

anderson_units = {
    ur("Pa"): ur("atm"),
    ur("rad"): ur("deg"),
}

imperial_units = {
    **anderson_units,
    #
    ur("m"): ur("ft"),
    ur("kg / m^3"): ur("slug / ft^3"),
}
