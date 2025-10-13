# AERE 351 Homework 5

## 1.

The goal is to reach $E$ from $\theta$ and $e$. I am assuming we're only dealing with elliptical orbits. Thankfully, there's a real neat formula that we derived in class relating the two sets of variables:

$$
\tan \frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E}{2}
$$

$$
\sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} = \tan \frac{E}{2}
$$

$$
E = 2 \arctan \left( \sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} \right)
$$

`true_to_ecc` implementation:

```m
function E = true_to_ecc(e, theta)
    E = 2 * atan(sqrt((1 - e) / (1 + e) * tan(theta / 2)));
end
```
