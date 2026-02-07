# AERE 421 Homework 1

## 1.

![](https://i.imgur.com/9OPFIDF.png)

It only makes sense to solve this problem in Python, thus, I will be pursuing exactly that. All units are in pounds and inches, so I will keep the deformations in inches too. My code first starts by generating all local stiffness matrices, which `numpy` makes really easy:

```py
import numpy as np

k_1 = k_2 = k_3 = 1000
K_1 = K_2 = K_3 = k_1 * np.matrix(
    [
        [1, -1],
        [-1, 1],
    ]
)

print(K_1, end="\n\n")
print(K_2, end="\n\n")
print(K_3, end="\n\n")
```

This results in all the same matrices since the stiffness magnitudes are the same across all springs:

```
[[ 1000 -1000]
 [-1000  1000]]

[[ 1000 -1000]
 [-1000  1000]]

[[ 1000 -1000]
 [-1000  1000]]
```
