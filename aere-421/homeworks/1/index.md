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

Looking at the image again, however, reveals that only indices $2$, $3$, and $4$ are free. Thus, I trim the global matrix to just have the movable nodes, but I use the indices $1$, $2$, and $3$ since Python is a 0-indexed language, unlike English. The indices show up twice to ask `numpy` to slice both vertically and horizontally:

```py
free = [1, 2, 3]
S = S[np.ix_(free, free)]

print(S, end="\n\n")
```

And we get the expected slice:

```
[[ 2000 -1000     0]
 [-1000  2000 -1000]
 [    0 -1000  1000]]
```

Now would be an appropriate time to declare the external forces:

```py
F = np.matrix(
    [
        [0],
        [-1000],
        [0],
        [4000],
    ]
)[np.ix_(free)]
```

Now I know it's a little silly to declare the full external force matrix, just to trim off the first value instantly, but it's the consistency that matters. Nevertheless, the output:

```
[[-1000]
 [    0]
 [ 4000]]
```

Using `numpy`'s `linalg` module gives me a simple way to find the displacements:

```py
U = np.linalg.solve(S, F)

print(U)
```

And the displacements are:

```
[[ 3.]
 [ 7.]
 [11.]]
```

As a review, here's the entire script:

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

S = K_1 + K_2 + K_3

print(S, end="\n\n")

free = [1, 2, 3]
S = S[np.ix_(free, free)]

print(S, end="\n\n")

F = np.matrix(
    [
        [0],
        [-1000],
        [0],
        [4000],
    ]
)[np.ix_(free)]

print(F, end="\n\n")

U = np.linalg.solve(S, F)

print(U)
```

And the results are:

$$
\boxed{\delta_2 = 3 \text{in}}
$$

$$
\boxed{\delta_3 = 7 \text{in}}
$$

$$
\boxed{\delta_4 = 11 \text{in}}
$$

## 2.

![](https://i.imgur.com/G7Hpk4B.png)

I will just be forking my code from before as I have already explained everything. I will also be reducing the intermediate prints as it's unnecessary:

```py
import numpy as np

k_1 = 20
k_2 = 20
k_3 = 20
k_4 = 20

free = [1, 2, 3]

F = np.matrix(
    [
        [0],
        [0],
        [5],
        [0],
        [0],
    ]
)

base = np.matrix(
    [
        [1, -1],
        [-1, 1],
    ]
)

K_1 = k_1 * base
K_2 = k_2 * base
K_3 = k_3 * base

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

S = K_1 + K_2 + K_3
S = S[np.ix_(free, free)]

F = F[np.ix_(free)]
U = np.linalg.solve(S, F)

print(U)
```

Output:

```
[[0.25]
 [0.5 ]
 [0.5 ]]
```

Interpretation:

$$
\boxed{\delta_2 = 0.25 \text{in}}
$$

$$
\boxed{\delta_3 = 0.5 \text{in}}
$$

$$
\boxed{\delta_4 = 0.5 \text{in}}
$$

## 3.

![](https://i.imgur.com/b3yX3EL.png)

Because there are unknowns both in $U$ and $F$, I will have to do this symbolically. Here are the knowns (everything in Newtons and millimeters):

$$
\delta_1 = 0
$$

$$
\delta_3 = 20mm
$$

$$
k_1 = k_2 = 2000 \frac{N}{m} \frac{1m}{1000mm} = 2 \frac{N}{mm}
$$

$$
S = \begin{bmatrix}
  k_1 & -k_1 & 0 \\
  -k_1 & k_1 + k_2 & -k_2 \\
  0 & -k_2 & k_2
\end{bmatrix} = \begin{bmatrix}
  2 & -2 & 0 \\
  -2 & 4 & -2 \\
  0 & -2 & 2
\end{bmatrix}
$$

Trimming $S$:

$$
S' = \begin{bmatrix}
  4 & -2 \\
  -2 & 2
\end{bmatrix}
$$

The trimmed force vector:

$$
F' = \begin{bmatrix}
  0 \\
  F_3
\end{bmatrix}
$$

The trimmed displacement vector:

$$
U' = \begin{bmatrix}
  \delta_2 \\
  \delta_3 = \delta = 20mm
\end{bmatrix}
$$

The formula:

$$
S' U' = F'
$$

$$
\begin{bmatrix}
  4 & -2 \\
  -2 & 2
\end{bmatrix} \begin{bmatrix}
  \delta_2 \\
  20
\end{bmatrix} = \begin{bmatrix}
  0 \\
  F_3
\end{bmatrix}
$$

Expanding to equations:

$$
4 \delta_2 - 2 * 20 = 0 \Rightarrow 4 \delta_2 - 40 = 0 \Rightarrow \delta_2 = 10
$$

$$
-2 \delta_2 + 2 * 20 = F_3 \Rightarrow -2 * 10 + 40 = F_3 \Rightarrow F_3 = 20
$$

Thus:

$$
\boxed{\delta_2 = 10mm}
$$

$$
\boxed{F_3 = 20N}
$$
