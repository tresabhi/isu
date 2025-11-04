# ME 280 Homework 3

## 1.

The bag for this question is under `rosbag2_2025_11_03-21_53_21` in `bags.zip`, uploaded to Canvas and also available on [GitHub](https://github.com/tresabhi/isu/tree/main/me-280/homeworks/3/bags/rosbag2_2025_11_03-21_53_21/). My turtle's path:

![](https://i.imgur.com/ZZe76wE.png)

RQT Graph:

![](https://i.imgur.com/iv5ONlK.png)

PlotJuggler:

![](https://i.imgur.com/XfPi9gi.png)

## 2.1

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

## 2.2

> Modify the code such that the turtle moves around in a circle. (this may require a re-build and sourcing again) Describe or even paste the code in your narrative.

In `publish_velocity.py`, I simply made the angular velocity a constant and gave linear velocity in the x direction since that's relative to the current rotation of the turtle:

```
vel_msg.linear.x = 1.0
vel_msg.angular.z = 1.0
```

This made the turtle spin a circle offset from the origin:

![](https://i.imgur.com/6o7SWEw.png)

## 2.3

> Include a screenshot of the launch file running (and the various outputs being spit out in the terminal).

![](https://i.imgur.com/ykGBqGz.png)

## 2.4

> Describe, in your own words, what the launch file is doing.

The launch file upon inspection is surprisingly just Python. I was expecting a Bash script that runs all the required commands, but Python here's doing something similar, but with just a lot more boilerplate.

Working backwards, you can see the script appending nodes as actions to an instance of `ld = LaunchDescription()` which is then returned:

```py
ld.add_action(sim_node)
ld.add_action(pub_node)
ld.add_action(sub_node)

return ld
```

And nodes seem to contain the package name and the other command parameters used by the relevant package:

```py
sim_node = Node(
    package='turtlesim',
    executable='turtlesim_node',
)
```

## 2.5

> Start a rosbag recording and run the launch file, and submit this rosbag as a separate file in your zip.

Please see `rosbag2_2025_11_04-01_50_38` in `bags.zip` on Canvas or [on GitHub](https://github.com/tresabhi/isu/tree/main/me-280/homeworks/3/bags/rosbag2_2025_11_04-01_50_38/).

## 2.6

> Visualize the trajectory of the turtlesim using rqt_graph and rqt_plot (or plotjuggler) and include screenshots in the narrative.

The graph checks out since we see the `x` increase first since the angle initially is 0 so all the speed's going into `x`:

![](https://i.imgur.com/jKnD69X.png)

## 3.1

> First, run the turtlesim with the launch file you created, then run the owner and renter files in two separate new tabs. Include screen grabs of the terminal output, and update the code such that it outputs your name and age instead of the stock answer given.

Here's the terminal output for the owner:

![](https://i.imgur.com/knBY7M9.png)

And the renter:

![](https://i.imgur.com/ne9uYhQ.png)

My modified owner:
