import numpy as np
import matplotlib.pyplot as plt
import openmdao.api as om
from smt.surrogate_models import KRG
from smt.sampling_methods import LHS

x_limits = np.array([[-10, 10], [-10, 10]])
sampling = LHS(xlimits=x_limits, criterion="maximin")


xt = sampling(10)
yt = (xt[:, 0] - 3) ** 2 + (xt[:, 1] - 2) ** 2

# print(xt)
# print(yt)
