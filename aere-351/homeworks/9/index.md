# AERE 351 Homework 9

## 1.

From the Internet:

$$
R = 6378km
$$

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Given hyperbolic orbit parameters:

$$
h_p = 250km
$$

$$
v_\infty = 3.5km/s
$$

$$
i = 15\deg
$$

$$
\Omega = 178\deg
$$

$$
\omega = 25\deg
$$

Actual radius:

$$
r_p = R + h_p = 6378km + 250km = 6628 km
$$

Semi major axis:

$$
v_\infty = \sqrt{\frac{\mu}{-a}}
$$

$$
a = -\frac{\mu}{v_\infty^2} = - \frac{3.98600 * 10^5 km^3/s^2}{(3.5km/s)^2} = \boxed{-32500 km}
$$

Eccentricity:

$$
r_p = a (1 - e) \implies \frac{r_p}{a} = 1 - e
$$

$$
e = 1 - \frac{r_p}{a} = 1 - \frac{6628km}{-32500km} = \boxed{1.204}
$$

Required velocity at perigee:

$$
v_p = \sqrt{\mu \left( \frac{2}{r_p} - \frac{1}{a} \right)}
$$

$$
v_p = \sqrt{3.98600 * 10^5 km^3/s^2 * \left( \frac{2}{6628 km} - \frac{1}{-32500 km} \right)} = \boxed{11.513 km/s}
$$

Given burn gone wrong velocities:

$$
v_r = 1.6 km/s
$$

$$
v_\theta = 8.2 km/s
$$

$$
v' = \sqrt{v_r^2 + v_\theta^2} = \sqrt{(1.6km/s)^2 + (8.2km/s)^2} = 8.35 km/s
$$

Failed semi major axis:

$$
v' = \sqrt{\mu \left( \frac{2}{r_p} - \frac{1}{a'} \right)}
$$

$$
v'^2 = \mu \left( \frac{2}{r_p} - \frac{1}{a'} \right)
$$

$$
\frac{2}{r_p} - \frac{v'^2}{\mu} = \frac{1}{a'}
$$

$$
a' = \frac{1}{\frac{2}{r_p} - \frac{v'^2}{\mu}}
$$

$$
a' = \frac{1}{\frac{2}{6628 km} - \frac{(8.35km/s)^2}{3.98600 * 10^5 km^3/s^2}} = \boxed{7880 km}
$$

Eccentricity:

$$
h' = r_p v_\theta = 6628km * 8.2km/s = 54350 km^2/s
$$

$$
p' = \frac{h'^2}{\mu} = \frac{(54350 km^2/s)^2}{3.98600 * 10^5 km^3/s^2} = 7410.7 km
$$

$$
p' = a' (1 - e'^2)
$$

$$
e' = \sqrt{1 - \frac{p'}{a'}} = \sqrt{1 - \frac{7410.7 km}{7880 km}} = \boxed{0.244}
$$

The other parameters were attained even with the failure:

$$
i' = i = \boxed{15\deg}
$$

$$
\Omega' = \Omega = \boxed{178\deg}
$$

Except for the argument of periapsis since $v_r \neq 0$. And because we're in the right plane, this can be treated as a simple omega problem without any concern of inclination and RAAN:

$$
v_\theta = \sqrt{\frac{\mu}{p'}} (1 + e' \cos \theta') = \frac{\mu}{h'} (1 + e' \cos \theta')
$$

$$
\frac{h' v_\theta}{\mu} = 1 + e' \cos \theta'
$$

$$
\theta' = \arccos \left( \frac{h' v_\theta}{\mu e'} - \frac{1}{e'} \right)
$$

$$
\theta' = \arccos \left( \frac{54350 km^2/s * 8.2km/s}{3.98600 * 10^5 km^3/s^2 * 0.244} - \frac{1}{0.244} \right) = 61.06\deg
$$

But this is the faux $\theta$ since it's omega that's offset, not the current $\theta$:

![](https://i.imgur.com/fMu5JaA.png)

$$
\omega' = 360\deg + (\omega - \theta') = 360\deg + (25\deg - 61.06\deg) = \boxed{323.94\deg}
$$

The next question asks about the true anomaly again, which I already have:

$$
\theta' = \boxed{61.06\deg}
$$

Since we're already at the pericenter, we must waste no time and boost immediately. The intended velocities are:

$$
v_{\theta ~ \text{intended}} = v_p = 11.513 km/s
$$

$$
v_{r ~ \text{intended}} = 0
$$

$$
\Delta v = \sqrt{(v_{\theta ~ \text{intended}} - v_\theta)^2 + (v_{r ~ \text{intended}} - v_r)^2}
$$

$$
\Delta v = \sqrt{(11.513 km/s - 8.2 km/s)^2 + (0 - 1.6 km/s)^2} = \boxed{3.68 km/s}
$$

Earth's parameters:

$$
e_E = 1.67 * 10^{-3}
$$

$$
i_E = 0.88 * 10^{-3} \deg
$$

$$
\Omega_E = 175.4 \deg
$$

$$
\omega_E = 287.6 \deg
$$

$$
\mu_\odot = 1.3271244 * 10^{11} km^3/s^2
$$

$$
a_E = 1.4959787 * 10^8 km
$$

Earth is at its apocenter:

$$
p_E = a_E (1 - e_E^2) = 1.4959787 * 10^8 km * (1 - (1.67 * 10^{-3})^2) = 1.496×10^8 km
$$

$$
v_E = \sqrt{\frac{\mu_\odot}{p_E}} (1 - e_E) = \sqrt{\frac{1.3271244 * 10^{11} km^3/s^2}{1.496×10^8 km}} (1 - 1.67 * 10^{-3}) = 29.73474 km/s
$$

Satellite's aggregated velocity at the pericenter (I am now overriding older variables for convenience):

$$
v_p = v_E + v_\infty = 29.73474 km/s + 3.5 km/s = 33.23 km/s
$$

$$
r_p = r_{aE} = \frac{p_E}{1 - e_E} = \frac{1.496×10^8 km}{1 - 1.67 * 10^{-3}} = 1.4985×10^8 km
$$

From this the semi major axis can be harnesses:

$$
v_p = \sqrt{\mu_\odot \left( \frac{2}{r_p} - \frac{1}{a} \right)}
$$

$$
a = \frac{1}{\frac{2}{r_p} - \frac{v_p^2}{\mu_\odot}}
$$

$$
a = \frac{1}{\frac{2}{1.4985×10^8 km} - \frac{(33.23 km/s)^2}{1.3271244 * 10^{11} km^3/s^2}} = \boxed{1.99×10^8 km}
$$

And since this new orbit is coplanar with the Earth's orbit:

$$
i = i_E = \boxed{0.88 * 10^{-3} \deg}
$$

$$
\Omega = \Omega_E = \boxed{175.4 \deg}
$$

But since the apogee of Earth's orbit serves as the satellite's perigee:

$$
\omega = \omega_E - 180\deg = 287.6 \deg - 180\deg = \boxed{107.6\deg}
$$

Oh and, let's not forget:

$$
r_p = a (1 - e)
$$

$$
e = 1 - \frac{r_p}{a} = 1 - \frac{1.4985×10^8 km}{1.99×10^8 km} = \boxed{0.247}
$$

## 2.

Given:

$$
v_\infty = 6km/s
$$

$$
\phi_1 = 65\deg
$$

$$
\Delta = 20000km
$$

$$
r_E = 149.6*10^6km
$$

$$
R_E = 6378km
$$

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Recovering $a$:

$$
v_\infty = \sqrt{\frac{\mu}{-a}}
$$

$$
v_\infty^2 = \frac{\mu}{-a}
$$

$$
a = -\frac{\mu}{v_\infty^2} = -\frac{3.98600 * 10^5 km^3/s^2}{(6km/s)^2} = -11072.2 km
$$

Recovering $e$:

$$
\Delta = \frac{\mu}{v_\infty^2} \sqrt{e^2 - 1} = -a \sqrt{e^2 - 1}
$$

$$
-\frac{\Delta}{a} = \sqrt{e^2 - 1}
$$

$$
\frac{\Delta^2}{a^2} = e^2 - 1
$$

$$
e = \sqrt{\frac{\Delta^2}{a^2} + 1} = \sqrt{\frac{(20000km)^2}{(-11072.2 km)^2} + 1} = 2.0647
$$

For it to miss Earth:

$$
r_p > R_E
$$

But, will it?

$$
r_p = a (1 - e) = -11072.2 km * (1 - 2.0647) = \boxed{11789 km > 6378km \implies \text{Earth safe}}
$$

Now the leaving angle:

$$
\cos \beta = \frac{1}{e}
$$

$$
\beta = \arccos \frac{1}{e} = \arccos \frac{1}{2.0647} = 1.0652rad
$$

But the angle turned is actually:

$$
\delta = 2\beta = 2 * 1.0652rad = \boxed{2.13rad}
$$

This is what the above looks like:

![](https://i.imgur.com/eCRhgL8.png)

This is a triangle:

![](https://i.imgur.com/v0pojzr.png)

$$
\alpha = \pi - \delta = \pi - 2.13rad = 1.012rad
$$

Generalized Pythagorean theorem:

$$
\Delta v^2 = v_\infty^2 + v_\infty^2 - 2 v_\infty v_\infty \cos \alpha = 2 v_\infty^2 - 2 v_\infty^2 \cos \alpha = 2 v_\infty^2 (1 - \cos \alpha)
$$

$$
\Delta v = v_\infty \sqrt{2 (1 - \cos \alpha)} = 6km/s * \sqrt{2 (1 - \cos 1.012rad)} = \boxed{5.8162 km/s}
$$

The new angle:

$$
\phi_2 = \phi_1 + \delta = 65\deg + 2.13rad = \boxed{187\deg}
$$

## 3.

Given:

$$
m_\text{payload} = 100000kg
$$

$$
h = 300km
$$

$$
I_{sp, 2} = 450s
$$

$$
m_{\text{dry}, 2} = 80000kg
$$

$$
m_{\text{propellant}, 2} = 600000kg
$$

$$
m_{\text{propellant}, 1} = 0.85 m_1
$$

$$
I_{sp, 1} = 290s
$$

$$
\Delta v_\text{loss} = 1.59 km/s
$$

From the Internet:

$$
R = 6380km
$$

$$
g_0 = 9.81 m/s^2
$$

Actual orbit:

$$
r = R + h = 6380km + 300km = 6680 km
$$

Relation of all delta v's:

$$
\Delta v + \Delta v_\text{loss} = \Delta v_1 + \Delta v_2
$$
