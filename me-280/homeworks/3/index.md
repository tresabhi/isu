# ME 280 Homework 3

## 1.

The bag for this question is under `rosbag2_2025_11_03-21_53_21` in `bags.zip`, uploaded to Canvas and also available on [GitHub](https://github.com/tresabhi/isu/tree/main/me-280/homeworks/3/bags/rosbag2_2025_11_03-21_53_21/). My turtle's path:

![](https://i.imgur.com/ZZe76wE.png)

RQT Graph:

![](https://i.imgur.com/iv5ONlK.png)

PlotJuggler:

![](https://i.imgur.com/XfPi9gi.png)

## 2.

> Why does the turtle move randomly in part 2? Supply a narrative about what source of code does this, where it is in the code base, etc.

It moves randomly because that's what `VelPublisher` in `publish_velocity.py` makes it do. More specifically, in the `timer_callback` method, using the `random.uniform` function from the Python `random` library, the message is assigned random values:

```py
        vel_msg = Twist()
        vel_msg.linear.x = np.random.uniform(low=-1, high=1)
        vel_msg.angular.z = np.random.uniform(low=-1, high=1)
```

And after `vel_msg` is constructed, it's published immediately:

```py
        self.publisher_.publish(vel_msg)
```
