# AERE 261 HW 7

Abhigyaan Deep

Refer the adjacent Python file for the code. Refer to the provided CLI per section to run the script.

## 1. (a)

`py index.py --plot=temperature`

![](https://i.imgur.com/JjfCAv8.png)

## 1. (b)

`py index.py --plot=pressure`

![](https://i.imgur.com/47g5CXB.png)

## 1. (c)

`py index.py --plot=density`

![](https://i.imgur.com/r91RnYE.png)

## 2. (a)

`py index.py --plot=v_stall`

![](https://i.imgur.com/tXf3J3g.png)

## 2. (b)

`py index.py --plot=v_r_c_max`

![](https://i.imgur.com/7IhKa87.png)

## 2. (c)

Yes, it is.

## 3. (a)

`py index.py --plot=p_r`

![](https://i.imgur.com/1fkANzm.png)

## 3. (b)

`py index.py --plot=p_a`

![](https://i.imgur.com/CF5b2O7.png)

## 3. (c)

`py index.py --plot=p_e`

![](https://i.imgur.com/TWeR79O.png)

## 4. (a)

`py index.py --plot=r_c_max`

![](https://i.imgur.com/FdF0Z8Q.png)

## 4. (b)

`py index.py --plot=ceilings`

Service ceiling is about $16.8km$ and the absolute ceiling is about $17.5km$.

![](https://i.imgur.com/iOO1UBp.png)

## 5. (a)

$$
C_{D,0}=0.017
$$

$$
K=0.056
$$

$$
(C_L)_{max}=1.37
$$

$$
S_{wing}=22.9m^2
$$

$$
\eta_{pr}=90\%=0.9
$$

$$
W_0=16481N
$$

$$
P=180000W
$$

$$
h=7000ft=2134m
$$

$$
\rho_\infty=0.993kg/m^3
$$

$$
\tan\theta_{min}=\frac{1}{(L/D)_{max}}=\frac{1}{(C_L/C_D)_{max}}
$$

$$
\theta_{min}=\arctan\frac{1}{(C_L/C_D)_{max}}
$$

$$
(C_L/C_D)_{max}=\sqrt{\frac{1}{4KC_{D,0}}}=\sqrt{\frac{1}{4 * 0.056 * 0.017}}=16.21
$$

$$
\theta_{min}=\arctan\frac{1}{16.21}=\boxed{3.53\degree}
$$

## 5. (b)

$$
d_{max}=\frac{h}{\tan\theta_{min}}=\frac{2134m}{\tan3.53\degree}=\boxed{34590m}
$$

## 5. (c)

$$
V_\infty=\sqrt{\frac{2W}{\rho_\infty S}\sqrt{\frac{K}{C_{D,0}}}}=\sqrt{\frac{2 * 16481N}{0.993kg/m^3 * 22.9m^2}\sqrt{\frac{0.056}{0.017}}}=\boxed{51.29m/s}
$$

## 5. (d)

$$
V_s=V_\infty\sin\theta_{min}=51.29m/s * \sin 3.53\degree=\boxed{3.158m/s}
$$
