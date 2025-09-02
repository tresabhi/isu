# AERE 261 HW 9 Corrections

Abhigyaan Deep

## 1.

General givens:

$$
m=1680kg
$$

$$
S_{ref}=22.9m^2
$$

$$
\rho=1.225kg/m^3
$$

$$
C_{L,max}=1.37
$$

$$
C_{L,rolling}=0.6
$$

$$
K=0.056
$$

$$
C_{D,0}=0.017
$$

Takeoff givens:

$$
\mu_{rolling}=0.05
$$

$$
h_\text{obstacle,takeoff}=50ft
$$

$$
\eta_{pr}=0.9
$$

$$
P_{shaft}=180000W
$$

$$
\text{climb angle}=3\degree
$$

$$
n_\text{liftoff}=1.05
$$

$$
V_{LO}=1.2V_{stall}
$$

Landing givens:

$$
n_{flare}=1.08
$$

$$
V_{flare}=V_{TD}=1.3V_{stall}
$$

$$
\theta_{a}=3\degree
$$

$$
h_\text{obstacle,landing}=50ft
$$

$$
\mu_{braking}=0.5
$$

### Takeoff ground roll

$$
g=9.81m/s^2
$$

$$
W=mg=1680kg*9.81m/s^2=16480N
$$

$$
V_{stall}=\sqrt{\frac{2 W}{\rho S C_{L,max}}}=\sqrt{\frac{2 * 16480N}{1.225kg/m^3 * 22.9m^2 * 1.37}}=29.29m/s
$$

$$
V_{LO}=1.2V_{stall}=1.2 * 29.29m/s=35.15m/s
$$

$$
P_a=\eta_{pr} P_{shaft}=0.9 * 180000W=162000W
$$

$$
P_a=TV_{LO}
$$

> [!IMPORTANT]
> To calculate $T$, we were supposed to use $V_\infty=0.7V_{LO}$, not $V_{LO}$. This caused my $T$ to be lower than expected.

$$
T=\frac{P_a}{V_{LO}}=\frac{162000W}{35.15m/s}=4609N
$$

$$
D=\frac{1}{2} \rho (0.7 V_{LO})^2 S (C_{D,0} + K C_{L,rolling}^2)
$$

$$
D=\frac{1}{2} * 1.225kg/m^3 * (0.7 * 35.15m/s)^2 * 22.9m^2 * (0.017 + 0.056 * (0.6)^2)=315.5N
$$

$$
L=\frac{1}{2} \rho (0.7 V_{LO})^2 S C_{L,rolling}=\frac{1}{2} 1.225kg/m^3 (0.7 * 35.15m/s)^2 * 22.9m^2 * 0.6=5095N
$$

> [!IMPORTANT]
> The error of a lower $T$ carried through the rest of this document and resulted in a higher $s_g$ value.

$$
s_g=\frac{1.44 W^2}{g \rho S C_{L,max} (T - D - \mu_r (W - L))}
$$

$$
s_g=\frac{1.44 * (16480N)^2}{9.81m/s^2 * 1.225kg/m^3 * 22.9m^2 * 1.37 * (4609N - 315.5N - 0.05 * (16480N - 5095N))}
$$

$$
s_g=\boxed{278.5m}
$$

### Takeoff transition

$$
R=\frac{1.44V_{stall}^2}{g(n-1)}=\frac{1.44 * (29.29m/s)^2}{9.81m/s^2 * (1.05 - 1)}=2519m
$$

$$
s_{tr}=R \sin \theta=2519m \sin 3\degree=\boxed{131.8m}
$$

### Takeoff air

$$
h=50ft=15.24m
$$

$$
h_a=h - R + R \cos \theta
$$

$$
h_a=15.24m - 2519m + 2519m \cos 3\degree=11.788m
$$

$$
s_a=\frac{h_a}{\tan \theta}=\frac{11.788m}{\tan 3\degree}=\boxed{224.9m}
$$

> [!IMPORTANT]
> All values but $s_g$ are okay.

### Takeoff total

$$
s_\text{takeoff}=s_g+s_{tr}+s_a=278.5m+131.8m+224.9m=\boxed{635.2m}
$$

### Landing approach

$$
h_f=R-R \cos \theta_a=2519m - 2519m \cos 3\degree=3.452m
$$

$$
h=50ft=15.24m
$$

$$
h_f+h_a=h
$$

$$
h_a=h-h_f=15.24m-3.452m=11.788m
$$

$$
s_a=\frac{h_a}{\tan \theta_a}=\frac{11.788m}{\tan 3\degree}=\boxed{224.9m}
$$

### Landing flare

> [!IMPORTANT]
>
> $R$ must've been recalculated with $n=1.08$ which was not performed.

$$
\theta_f=\theta_a=3\degree
$$

$$
s_f=R \sin \theta_f=2519m \sin 3\degree=\boxed{131.8m}
$$

### Landing ground roll

$$
V_{TD}=1.3V_{stall}=1.3 * 29.29m/s=38.077m/s
$$

$$
D=\frac{1}{2} \rho (0.7 V_{TD})^2 S (C_{D,0} + K C_L^2)
$$

$$
D=\frac{1}{2} * 1.225kg/m^3 * (0.7 * 38.077m/s)^2 * 22.9m^2 * (0.017 + 0.056 * (0.6)^2)=370.3N
$$

$$
L=\frac{1}{2} \rho (0.7 V_{TD})^2 S C_{L}=\frac{1}{2} * 1.225kg/m^3 * (0.7 * 38.077m/s)^2 * 22.9m^2 * 0.6=5979N
$$

$$
s_g=\frac{1.69 W^2}{g \rho S C_{L,max} (D + \mu_r (W - L))}
$$

> [!IMPORTANT]
> Calculation error but everything is okay.

$$
s_g=\frac{1.69 * (16480N)^2}{9.81m/s^2 * 1.225kg/m^3 * 22.9m^2 * 1.37 (370.3N + 0.05 * (16480N - 5979N))}=\boxed{1360m}
$$

### Landing total

$$
s_\text{landing}=s_a+s_f+s_g=224.9m + 131.8m + 1360m=\boxed{1716.7m}
$$
