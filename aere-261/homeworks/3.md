# AERE 261 HW 3

Abhigyaan Deep

Hello, grader of my homework! In order to preserve my sanity, I am moving away from clunky Google Docs. I am now trying out Markdown and $\LaTeX$ with the GitHub flavor so my homeworks should be prettier for you and easier for me to write.

## Knowns

$M_{\infty}=0.27$

$V_{\infty}=89.6m/s$

$\rho=0.993kg/m^3$

$\mu=1.7*10^{-5}\frac{kg}{m*s}$

$b=12.4m$

$S=22.9m^2$

## 1. (a)

$$
AR=\frac{b^2}{S}=\frac{(12.4m)^2}{22.9m^2}=\boxed{6.71}
$$

## 1. (b)

More info that we got:

$\alpha_{\text{stall}}=17.5\deg$

$\alpha_{L=0}=-1.19\deg$

$a_0=0.119\deg^{-1}$

$e=0.92$

I'm going to use the degree version of the formula to extend the 2D airfoil to a 3D wing.

$$
a=\frac{a_0}{1+\frac{57.3\deg a_0}{\pi e AR}}=\frac{0.119\deg^{-1}}{1+\frac{57.3\deg*0.119\deg^{-1}}{\pi*0.92*6.71}}=0.0880\deg^{-1}
$$

Now for $C_L$

$$
C_L=a(\alpha-\alpha_{L=0})=\boxed{0.0880\deg^{-1}(\alpha+1.19\deg)}
$$

## 1. (c)

$$
\alpha=\alpha_{\text{stall}}=17.5\deg
$$

$$
C_L=0.0880\deg^{-1}(17.5\deg+1.19\deg)=\boxed{1.643}
$$

## 1. (d)

Given

$m_\text{full}=1680kg$

$g=9.81m/s^2$

Converting mass to force (or weight):

$$
L=W=m_\text{full}g=1680kg*9.81m/s^2=16480N=16.48kN
$$

Rewriting $C_L$ in terms of $L$

$$
L=\frac{1}{2}\rho_\infty V_\infty^2 S C_L
$$

$$
C_L=\frac{2L}{\rho_\infty V_\infty^2 S}=\frac{2*16.48kN}{0.993kg/m^3 * (89.6m/s)^2 * 22.9m^2}=\boxed{0.1805}
$$

## 1. (e)

Pulling this from up above:

$C_{L,\text{stall}}=1.643$

$L=16.48kN$

Solving for $V_\infty$ with $C_L$ equal to the stall value:

$$
W=\frac{1}{2}\rho_\infty V_\infty^2 S C_{L,\text{stall}}
$$

$$
V_\infty=\sqrt{\frac{2W}{\rho_\infty S C_{L,\text{stall}}}}=\sqrt{\frac{2*16.48kN}{0.993kg/m^3 * 22.9m^2 * 1.643}}=\boxed{29.7m/s}
$$

## 1. (f)

There is no wing sweep so $\Lambda=0$

And AR from above: $AR=6.71$

$$
e_0=1.78(1-0.045AR^{0.68})-0.64=1.78(1-0.045*6.71^{0.68})-0.64=\boxed{0.8477}
$$

## 1. (g)

$$
K=\frac{1}{piARe}=\frac{1}{pi*6.71*0.8477}=0.0560
$$

And now the drag coefficient:

$$
C_D=C_{D,0}+KC_L^2
$$

From last homework: $C_{d,0}=0.006$

$$
C_D=0.006+0.0560*(0.1805)^2=\boxed{0.00782}
$$

## 2. (a)

$$
A_{top}=\frac{1}{2}(103.5in)(53.9in)+(207.5in)(53.9in)=13970in^2=9.013m^2
$$

$$
A_{side}=(39.4in)(69.3in)+(138.2in)(66in)+\frac{1}{2}(103.5in)(66in)=15267in^2=9.8497m^2
$$

$$
S_{\text{wet,fuselage}}=3.4\left(\frac{A_{top}+A_{side}}{2}\right)=3.4\left(\frac{9.013m^2+9.8497m^2}{2}\right)=\boxed{32.1 m^2}
$$

## 2. (b)

Given

$A_{\text{{max}}}=2.22m^2$

$l=7.9m$

$S_\text{wet}=32.26 m^2$ (value given in the question differs a negligible amount from my calculations so I am going with the one provided in the question)

$t/c=0.15$

$M=0.27$

$S_\text{wing}=22.9m^2$

$S_{\text{wet}}=32.1 m^2$

This is from the estimation document

$Q_c=1.0$

$$
R=\frac{\rho V l}{\mu}=\frac{0.993kg/m^3 * 89.6m/s * 7.9m}{1.7*10^{-5}\frac{kg}{m*s}}=4.135×10^7
$$

$$
C_f=\frac{0.455}{(\log_{10}R)^{2.58}(1+0.144M^2)^{0.65}}=\frac{0.455}{(\log_{10}(4.135×10^7))^{2.58}(1+0.144(0.27)^2)^{0.65}}=0.0023996
$$

$$
f=\frac{l}{d}=\frac{l}{\sqrt{(4/\pi)A_{\text{{max}}}}}=\frac{7.9m}{\sqrt{(4/\pi)*2.22m^2}}=4.699
$$

$$
FF_{\text{fuselage}}=0.9+\frac{5}{f^{1.5}}+\frac{f}{400}=0.9+\frac{5}{4.699^{1.5}}+\frac{4.699}{400}=1.403
$$

$$
C_{\text{D,fuselage}}=C_f FF Q_c \frac{S_\text{wet}}{S_\text{wing}}=0.0023996 * 1.403 * 1.0* \frac{32.1 m^2}{22.9m^2}=\boxed{0.004719}
$$

## 2. (c)

$t/c=0.15$

$(x/c)_m=0.3$

$M=0.27$

$\Lambda_m=0$

$Q_\text{wing}=1.0$

$S_\text{wing}=22.9m^2$

$R=9.67*10^6$

Assuming turbulent flow

$$
C_f=\frac{0.455}{(\log_{10}R)^{2.58}(1+0.144M^2)^{0.65}}=\frac{0.455}{(\log_{10}(9.67*10^6))^{2.58}(1+0.144(0.27)^2)^{0.65}}=0.002999
$$

$$
FF=\left[1+\frac{0.6}{(x/c)_m}\left(\frac{t}{c}\right)+100\left(\frac{t}{c}\right)^4\right]\left[1.34M^{0.18}(\cos\Lambda_m)^{0.28}\right]
$$

$$
=\left[1+\frac{0.6}{0.3}\left(0.15\right)+100\left(0.15\right)^4\right]\left[1.34(0.27)^{0.18}(\cos0)^{0.28}\right]=1.430
$$

$$
S_\text{wet}=[1.977+0.52(t/c)]S_\text{exposed}=[1.977+0.52(0.15)](22.9m^2)=47.06 m^2
$$

$$
C_{\text{D,wing}}=C_f FF Q_\text{wing} \frac{S_\text{wet}}{S_\text{wing}}=0.002999 * 1.430 * 1.0 * \frac{47.06 m^2}{22.9m^2}=\boxed{0.008813}
$$

$C_D$ from xflr5 was $0.00475$ but our approximation is $0.008813$ which almost double. Most of these equations are "hand-wavy" and extremely imprecise so this is somewhat expected. I have triple checked my numbers so I am unsure why they're so different.

## 2. (d)

$$
C_D=C_{D,0}+KC_L^2=C_{D,fuselage}+C_{D,wing}+KC_{L,wing}^2
$$

$$
=0.004719+0.008813+0.0560C_L^2=\boxed{0.0135 + 0.0560C_L^2}
$$
