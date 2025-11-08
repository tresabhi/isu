from math import sin, cos
import pint

ur = pint.UnitRegistry()
km = ur.kilometer
s = ur.second
deg = ur.degree

mu = 398600.4418 * (km**3) / (s**2)

r_p = 8000 * km
r_a = 12000 * km
i_1 = 10 * deg
i_2 = 30 * deg
delta_i = i_2 - i_1

v_inf = 3 * km / s

a_elliptical = (r_p + r_a) / 2
e_elliptical = (r_a - r_p) / (r_a + r_p)

a_hyperbolic = -mu / (v_inf**2)


def vis_viva_speed(r, a):
    return (mu * (2.0 / r - 1.0 / a)) ** 0.5


# speeds at pericenter and apocenter for ellipse and hyperbola
v_p_ell = vis_viva_speed(r_p, a_elliptical)
v_a_ell = vis_viva_speed(r_a, a_elliptical)

v_p_h = vis_viva_speed(r_p, a_hyperbolic)
v_a_h = vis_viva_speed(r_a, a_hyperbolic)


# plane change delta-v for a rotation of angle delta_i at speed v: 2*v*sin(delta_i/2)
def plane_change_dv(v, delta_i):
    return 2.0 * v * sin(delta_i.to("rad").magnitude / 2.0)


# combined single-burn vector difference (assume position along x, initial vel along +y at burn)
# rotate target velocity by delta_i about x-axis (node line). initial v vector (0, v0, 0)
# target v vector (0, v1*cos(di), v1*sin(di))
def combined_dv(v0, v1, delta_i):
    vy = v1 * cos(delta_i.to("rad").magnitude)
    vz = v1 * sin(delta_i.to("rad").magnitude)
    dvx = 0.0 * (km / s)  # always zero
    dvy = vy - v0
    dvz = vz - 0.0 * (km / s)
    return (dvy**2 + dvz**2) ** 0.5


# CASE 1: burns at pericenter
# 1) change shape then inclination
dv_shape_then_plane_p = abs(
    v_p_h - v_p_ell
)  # change speed magnitude along same direction
dv_plane_after_shape_p = plane_change_dv(v_p_h, delta_i)
total_shape_then_plane_p = dv_shape_then_plane_p + dv_plane_after_shape_p

# 2) change inclination then shape
dv_plane_then_shape_p = plane_change_dv(v_p_ell, delta_i)
dv_shape_after_plane_p = abs(
    v_p_h - v_p_ell
)  # magnitude change (direction already changed but speed same)
total_plane_then_shape_p = dv_plane_then_shape_p + dv_shape_after_plane_p

# 3) combined
dv_combined_p = combined_dv(v_p_ell, v_p_h, delta_i)

# CASE 2: burns at apocenter (repeat same computations at r = ra)
dv_shape_then_plane_a = abs(v_a_h - v_a_ell)
dv_plane_after_shape_a = plane_change_dv(v_a_h, delta_i)
total_shape_then_plane_a = dv_shape_then_plane_a + dv_plane_after_shape_a

dv_plane_then_shape_a = plane_change_dv(v_a_ell, delta_i)
dv_shape_after_plane_a = abs(v_a_h - v_a_ell)
total_plane_then_shape_a = dv_plane_then_shape_a + dv_shape_after_plane_a

dv_combined_a = combined_dv(v_a_ell, v_a_h, delta_i)


# Present results
def show(val):
    return f"{val.to(km/s):.6f}"


print("Inputs:")
print(f"  rp = {r_p}, ra = {r_a}, a_ell = {a_elliptical:.3f}")
print(f"  v_inf = {v_inf}, a_h = {a_hyperbolic:.3f}")
print()
print("Speeds at pericenter:")
print(f"  v_p (ellipse) = {show(v_p_ell)} km/s")
print(f"  v_p (hyperbola) = {show(v_p_h)} km/s")
print()
print("Speeds at apocenter:")
print(f"  v_a (ellipse) = {show(v_a_ell)} km/s")
print(f"  v_a (hyperbola) = {show(v_a_h)} km/s")
print()
print("Delta-i = {:.3f} deg".format(delta_i.to(deg).magnitude))
print()
print("CASE 1 — ALL BURNS AT PERICENTER (rp = 8000 km):")
print(
    f"  1) shape then plane:    Δv_shape = {show(dv_shape_then_plane_p)} km/s, Δv_plane = {show(dv_plane_after_shape_p)} km/s, total = {show(total_shape_then_plane_p)} km/s"
)
print(
    f"  2) plane then shape:    Δv_plane = {show(dv_plane_then_shape_p)} km/s, Δv_shape = {show(dv_shape_after_plane_p)} km/s, total = {show(total_plane_then_shape_p)} km/s"
)
print(f"  3) combined single burn: total Δv = {show(dv_combined_p)} km/s")
print()
print("CASE 2 — ALL BURNS AT APOCENTER (ra = 12000 km):")
print(
    f"  1) shape then plane:    Δv_shape = {show(dv_shape_then_plane_a)} km/s, Δv_plane = {show(dv_plane_after_shape_a)} km/s, total = {show(total_shape_then_plane_a)} km/s"
)
print(
    f"  2) plane then shape:    Δv_plane = {show(dv_plane_then_shape_a)} km/s, Δv_shape = {show(dv_shape_after_plane_a)} km/s, total = {show(total_plane_then_shape_a)} km/s"
)
print(f"  3) combined single burn: total Δv = {show(dv_combined_a)} km/s")
print()

# Summary upright: which option is cheapest at each location?
totals_p = {
    "shape_then_plane": total_shape_then_plane_p,
    "plane_then_shape": total_plane_then_shape_p,
    "combined": dv_combined_p,
}
totals_a = {
    "shape_then_plane": total_shape_then_plane_a,
    "plane_then_shape": total_plane_then_shape_a,
    "combined": dv_combined_a,
}

best_p = min(totals_p, key=lambda k: totals_p[k])
best_a = min(totals_a, key=lambda k: totals_a[k])

print("Cheapest options:")
print(f"  At pericenter  -> {best_p}  (Δv = {show(totals_p[best_p])} km/s)")
print(f"  At apocenter   -> {best_a}  (Δv = {show(totals_a[best_a])} km/s)")

# Also report totals in m/s for easier intuition
print()
print("Totals in m/s (pericenter):")
for k, v in totals_p.items():
    print(f"  {k}: {v.to('m/s'):.2f}")
print("Totals in m/s (apocenter):")
for k, v in totals_a.items():
    print(f"  {k}: {v.to('m/s'):.2f}")
