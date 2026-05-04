import pint

ur = pint.UnitRegistry()

ur.define("angle = [angle]")
ur.define("rad = angle")
ur.define("deg = pi / 180 * rad")
