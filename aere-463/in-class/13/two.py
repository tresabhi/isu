import matplotlib.pyplot as plt
import numpy as np

from smt.applications import EGO
from smt.design_space import DesignSpace
from smt.surrogate_models import KRG

from smt.sampling_methods import LHS

np.random.seed(0)

xlimits = np.array([[-10, 10], [-10, 10]])
sampling = LHS(xlimits=xlimits, criterion="maximin")

nt = 14
xt = sampling(nt)

nv = 6
xv = sampling(nv)

plt.plot(xt[:, 0], xt[:, 1], "o")
plt.plot(xv[:, 0], xv[:, 1], "rs")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

yt = (xt[:, 0] - 3) ** 2 + (xt[:, 1] - 2) ** 2

sm = KRG(theta0=[13 - 2], print_prediction=False)
sm.set_training_values(xt, yt)
sm.train()

yv = sm.predict_values(xv)[:, 0]
yv_ref = (xv[:, 0] - 3) ** 2 + (xv[:, 1] - 2) ** 2

print(yv_ref)
print(yv)

s = (yv - yv_ref) ** 2
print(s)

rmse = np.sqrt(np.mean(s))
print(rmse)
