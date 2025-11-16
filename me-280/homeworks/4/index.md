# ME 280 Homework 3

## 1.1

I set and scaled all values by the same number, which revealed all that really did was dictate the speed. In other words, if you simply scale the coefficients all together the same, all that changes is the simulation speed. And since the goal is the get the shorted time possible, I tried high values.

Above about `45.0`, the system diverges:

![](https://i.imgur.com/awbIUTdm.png)

And set it too low like `1.0` and you get a slow, but converging simulation:

![](https://i.imgur.com/g8yofjPm.png)

So higher values are the best, right? Nope. `40.0` results in a very fast convergence:

![](https://i.imgur.com/kpn18kem.png)

But notice the zig zag. That's a function of the algorithm being too aggressive. Still sticking to all matching coefficients, lowering it to `30.0` results in the faster, 2-stepped convergence:

![](https://i.imgur.com/kbjIInAm.png)

But this is probably not the intention of the assignment so I went with these decent values to converge fairly fast, without giving the turtle a concussion from pure acceleration:

```yaml
turtle_controller:
  ros__parameters:
    # controller gains (in terms of linear distance first)
    kp_dist_parm: 7.0
    ki_dist_parm: 6.0
    kd_dist_parm: 5.0
    # controller gains (now in terms of angle/heading)
    kp_ang_parm: 20.0
    ki_ang_parm: 49.0
    kd_ang_parm: 20.0
```

This results in a decent path that a turtle might survive:

![](https://i.imgur.com/pDzIyKBm.png)

I made the gain on the angular displacement very aggressive since without such extreme values, it always ended up leaving the bounds of the simulation because it couldn't turn fast enough in contrast to the `dist_param`s.
