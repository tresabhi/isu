from registry import *

anderson_units = {
    ur("Pa"): ur("atm"),
}

imperial_units = {
    **anderson_units,
    ur("m"): ur("ft"),
}
