# AERE 261 HW 8 Corrections

## 1.

$$
-1\leq n_{struct}\leq 2.6
$$

$$
V_\infty=46m/s
$$

$$
W=16481N
$$

$$
S=22.9m^2
$$

$$
C_{L,max}=1.37
$$

$$
\rho_\infty=1.156kg/m^3
$$

$$
g=9.81m/s^2
$$

## 1. (a) i.

> [!IMPORTANT]
> I did not quite understand the question and only ended up calculating the structurally limited radius. The equation to calculate the aerodynamically limited n is $n=\frac{\frac{1}{2}\rho V^2 C_{L,max}}{W}$.

$$
R_{pull\ up}=\frac{V_\infty^2}{g(n-1)}=\frac{(46m/s)^2}{9.81m/s^2 * (2.6 - 1)}=\boxed{134.8m}
$$

$$
\omega_{pull\ up}=\frac{g(n-1)}{V_\infty}=\frac{9.81m/s^2 * (2.6 - 1)}{46m/s}=0.3412rad/s=\boxed{19.549\deg/s}
$$

## 1. (a) ii.

> [!IMPORTANT]
> Once again, I did not realize there are two distinct limits.

$$
R_{turn}=\frac{V_\infty^2}{g\sqrt{n^2-1}}=\frac{(46m/s)^2}{9.81m/s^2 * \sqrt{2.6^2 - 1}}=\boxed{89.87m}
$$

$$
\omega_{turn}=\frac{g\sqrt{n^2-1}}{V_\infty}=\frac{9.81m/s^2 * \sqrt{2.6^2 - 1}}{46m/s}=0.5118rad/s=\boxed{29.324\deg/s}
$$

## 1. (b)

The maneuvering velocity of the pull-up maneuver does not exceed the velocity in which the aircraft is flying at.

$$
V_{maneuvering,\ pull\ up}=\omega R=0.3412/s * 134.8m=46.00m/s=V_\infty
$$

The maneuvering velocity of the turn maneuver does not exceed the velocity in which the aircraft is flying at.

$$
V_{maneuvering,\ turn}=\omega R=0.5118/s * 89.87m=46.00m/s=V_\infty
$$

## 1. (c)

The turn maneuver will be the right choice here as it offers a smaller turn radius of $89.87m$ which is superior to the pull-up maneuver even though the instantaneous turn rate is lower because the benefit of a smaller turn radius trumps the benefit of a faster instantaneous turn rate.

![](https://i.imgur.com/UE7wYrm.png)

_Yes, I took 7 years of art. How can you tell?_

## 2.

A (top): accelerated stall

A (bottom): inverted accelerated stall; the same thing as A where pulling up too much makes you stall but instead now pulling the nose too down

B (top): positive structural limit

B (bottom): negative structural limit; once again, the kinda of deal with stall; this one will deform you pulling down

C: airspeed limit after which structural damage may occur; calm down, you are not Chuck Yeager

![](https://i.imgur.com/RY2veK7.png)
