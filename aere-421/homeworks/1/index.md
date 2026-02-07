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

However, these can't be added together yet since all rows and columns represent different indices. To achieve the correct offsets, I pad the matrices:

```py
K_1 = np.pad(
    K_1,
    pad_width=(
        (0, 2),
        (0, 2),
    ),
)
K_2 = np.pad(
    K_2,
    pad_width=(
        (1, 1),
        (1, 1),
    ),
)
K_3 = np.pad(
    K_3,
    pad_width=(
        (2, 0),
        (2, 0),
    ),
)

print(K_1, end="\n\n")
print(K_2, end="\n\n")
print(K_3, end="\n\n")
```

This logs the padded matrices, ready for summing:

```
[[ 1000 -1000     0     0]
 [-1000  1000     0     0]
 [    0     0     0     0]
 [    0     0     0     0]]

[[    0     0     0     0]
 [    0  1000 -1000     0]
 [    0 -1000  1000     0]
 [    0     0     0     0]]

[[    0     0     0     0]
 [    0     0     0     0]
 [    0     0  1000 -1000]
 [    0     0 -1000  1000]]
```

The global stiffness matrix is now just a summation:

```py
S = K_1 + K_2 + K_3

print(S, end="\n\n")
```

And this of course results int he correct global matrix:

```
[[ 1000 -1000     0     0]
 [-1000  2000 -1000     0]
 [    0 -1000  2000 -1000]
 [    0     0 -1000  1000]]
```
