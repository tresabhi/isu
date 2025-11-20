# ME 280 Homework 4

## 1.

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
    kp_dist_parm: 3.0
    ki_dist_parm: 4.0
    kd_dist_parm: 3.0
    # controller gains (now in terms of angle/heading)
    kp_ang_parm: 2.0
    ki_ang_parm: 4.0
    kd_ang_parm: 6.0
    # parameters for determining when the robot has hit its goal
    eps_dist_tol: 0.1
    eps_ang_tol: 0.08
goto_pose_client:
  ros__parameters:
    # (x,y) goal positions
    x_goal_value: 2.
    y_goal_value: 2.
```

This results in a decent path that a turtle might survive:

![](https://i.imgur.com/CB1bKyWm.png)

I made the gain on the angular displacement very aggressive since without such extreme values, it always ended up leaving the bounds of the simulation because it couldn't turn fast enough in contrast to the `dist_param`s.

Now it's time to try different positions. Since we live in a relative universe, changing the starting position is equivalent to changing its target position, which is why I only changed the `goal_value`s and not the starting positions. Here's the turtle going to $(7, 9)$:

![](https://i.imgur.com/dVjQUq3m.png)

The corresponding bag can be found in the `rosbag2_2025_11_16-22_17_19` folder within `bags.zip`, `Section_1.bag.zip` as requested explicitly by the question in the Canvas submission, or on [GitHub](https://github.com/tresabhi/isu/tree/main/me-280/homeworks/4/bags/rosbag2_2025_11_16-22_17_19/).

Here's what I observed changing the values of `K` did:

- `K_p`: this buffed the pull towards the target, or the aggressiveness of its correction, relative to the target which is why overshoots kep happening back when I was tinkering with all values of the same magnitude.
- `K_d`: this was the dampening factor which makes sense since the dampening factor is usually a coefficient of the first derivative which helped smooth out the motion and kill the oscillations over time.
- `K_i`: this acted like the memory, or the wisdom of the system where it helped eliminate cases where the turtle was just ever so slightly away from the target, delaying convergence.

## 2.

The `time_to_goal_*` files were polluting my workspace directory so I modified Dr. Fleming's code to write to the `times/` directory by modifying `turtlebot3_PID_controller.py`:

```py
fname = (
    "times/"
    + str(total_seconds)
    + "sec"
    + "_kpl"
    + str(self.get_parameter("kp_dist_parm").value)
    + "_kil"
    + str(self.get_parameter("ki_dist_parm").value)
    + "_kdl"
    + str(self.get_parameter("kd_dist_parm").value)
    + "_kpa"
    + str(self.get_parameter("kp_ang_parm").value)
    + "_kia"
    + str(self.get_parameter("ki_ang_parm").value)
    + "_kda"
    + str(self.get_parameter("kd_ang_parm").value)
    + ".txt"
)
```

To get a basic understanding of how the bot performs, I set all values to `1.0`:

```yaml
turtlebot3_controller:
  ros__parameters:
    # controller gains (in terms of linear distance first)
    kp_dist_parm: 1.0
    ki_dist_parm: 1.0
    kd_dist_parm: 1.0
    # controller gains (now in terms of angle/heading)
    kp_ang_parm: 1.0
    ki_ang_parm: 1.0
    kd_ang_parm: 1.0
    # parameters for determining when the robot has hit its goal
    eps_dist_tol: 0.01
    eps_ang_tol: 0.01
goto_pose_client:
  ros__parameters:
    # (x,y) goal positions
    x_goal_value: 2.
    y_goal_value: 2.
```

Which resulted in the file `1553.1sec_kpl1.0_kil1.0_kdl1.0_kpa1.0_kia1.0_kda1.0.txt` being generated:

```
Total time to goal: 1553.10 seconds
Location of goal, (x,y)=(2.0,2.0)
Linear gains: Kp=1.0, Ki=1.0, Kd=1.0
Angular gains: Kp=1.0, Ki=1.0, Kd=1.0
```

This is nice, but I would have to use REGEX to extract data from this later, so I stripped the part of the code that wrote the data to just this:

```py
f = open(fname, "w")
f.write(f"|{total_seconds:.2f}|")
f.write(f"{self.desired_x},{self.desired_y}|")
f.write(f"{self.get_parameter('kp_dist_parm').value}|")
f.write(f"{self.get_parameter('ki_dist_parm').value}|")
f.write(f"{self.get_parameter('kd_dist_parm').value}|")
f.write(f"{self.get_parameter('kp_ang_parm').value}|")
f.write(f"{self.get_parameter('ki_ang_parm').value}|")
f.write(f"{self.get_parameter('kd_ang_parm').value}|")
f.close()
```

Rerunning now resulted in a far easier file to parse `2025.4sec_kpl1.0_kil1.0_kdl1.0_kpa1.0_kia1.0_kda1.0`:

```txt
|2025.40|2.0,2.0|1.0|1.0|1.0|1.0|1.0|1.0|
```

It's formatted so that I can just pase the above into a Markdown file lie this one and get a table:

| Time    | x,y     | K_p_dist | K_i_dist | K_d_dist | K_p_ang | K_i_ang | K_d_ang |
| ------- | ------- | -------- | -------- | -------- | ------- | ------- | ------- |
| 2025.40 | 2.0,2.0 | 1.0      | 1.0      | 1.0      | 1.0     | 1.0     | 1.0     |

To simplify rerunning the script, I came up with this Bash command to launch the simulation perfectly every single time:

```bash
clear && killgazebo && export TURTLEBOT3_MODEL=waffle_pi && ros2 launch pid_turtlebot3 launch_sim_and_control.launch
```

To start off with the simulation, I set both proportionals to 0.01 (with others at 0) but that was unbelievably slow so I bumped both up to 0.1. This was better but it was create the angular proportional gain needed to be more aggressive as the position would outdistance the progress of the angular correction. Thus, I settled on ths following starting values and relaxed tolerances:

```yaml
kp_dist_parm: 0.1
ki_dist_parm: 0.0
kd_dist_parm: 0.0

kp_ang_parm: 0.5
ki_ang_parm: 0.0
kd_ang_parm: 0.0

eps_dist_tol: 0.1
eps_ang_tol: 0.05
```

This resulted in a run that lasted nearly a minute long! Following my experiences tuning PID systems from the robotics club, I started bumping the proportional gains until I saw oscillations by 0.1. Eventually, I settled on the following (still keeping everything else 0):

```yaml
kp_dist_parm: 0.2
ki_dist_parm: 0.0
kd_dist_parm: 0.0

kp_ang_parm: 0.5
ki_ang_parm: 0.0
kd_ang_parm: 0.0
```

Then I incremented the integral gains by 0.002 until the steady state errors were gone and went back a few steps when it started oscillating again:

```yaml
kp_dist_parm: 0.2
ki_dist_parm: 0.05
kd_dist_parm: 0.0

kp_ang_parm: 0.5
ki_ang_parm: 0.05
kd_ang_parm: 0.0
```

But there was a lot of overshoot in the angles, so I started incrementing the derivative by 0.1 until the oscillations were gone:

```yaml
kp_dist_parm: 0.2
ki_dist_parm: 0.05
kd_dist_parm: 0.0

kp_ang_parm: 0.5
ki_ang_parm: 0.05
kd_ang_parm: 0.5
```

At this point, it was painfully obvious the bot could go a little faster at the very end as it kept slowing down immensely as it neared the goal. This means, it needs to keep some of its velocity instead of discarding it since its closer. This involved buffing the proportional to speed up the bot and the derivative to stop it from overshooting:

```yaml
kp_dist_parm: 0.3
ki_dist_parm: 2.0
kd_dist_parm: 0.125

kp_ang_parm: 0.5
ki_ang_parm: 0.05
kd_ang_parm: 0.5
```

I realized the angles were being a little too aggressive so I tuned down the proportional angular gain but buffed the integral and derivative:

```yaml
kp_dist_parm: 0.3
ki_dist_parm: 2.0
kd_dist_parm: 0.125

kp_ang_parm: 0.25
ki_ang_parm: 1.5
kd_ang_parm: 10.0
```

Now there was room to buff the aggression of the displacement (with a buff to the angular derivative to handle the increased oscillation):

```yaml
kp_dist_parm: 0.6
ki_dist_parm: 2.0
kd_dist_parm: 0.125

kp_ang_parm: 0.25
ki_ang_parm: 1.5
kd_ang_parm: 11.0
```

This is the limit of what I have been able to make the bot converge with. Any other solution involves the bot gunning for the target and overshooting it, but the script counts that as a "goal reached" which I think is dishonest. Anyway, here's the full data:

| Time  | x,y     | K_p_dist | K_i_dist | K_d_dist | K_p_ang | K_i_ang | K_d_ang |
| ----- | ------- | -------- | -------- | -------- | ------- | ------- | ------- |
| 11.80 | 2.0,2.0 | 0.3      | 1.0      | 0.02     | 1.0     | 1.0     | 3.0     |
| 11.90 | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 4.5     | 1.0     |
| 12.10 | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 0.5     | 1.0     |
| 12.10 | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.0     | 1.0     |
| 12.20 | 2.0,2.0 | 0.3      | 0.08     | 0.02     | 1.0     | 1.0     | 3.0     |
| 12.20 | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.0     | 1.0     |
| 14.00 | 2.0,2.0 | 0.3      | 0.08     | 0.02     | 1.0     | 1.0     | 0.25    |
| 14.70 | 2.0,2.0 | 0.3      | 0.1      | 0.1      | 0.5     | 0.05    | 0.5     |
| 14.90 | 2.0,2.0 | 0.25     | 0.25     | 0.15     | 0.5     | 0.05    | 0.5     |
| 14.90 | 2.0,2.0 | 0.2      | 0.2      | 0.2      | 0.5     | 0.05    | 0.5     |
| 16.30 | 2.0,2.0 | 0.3      | 0.08     | 0.02     | 1.0     | 0.0     | 0.0     |
| 19.50 | 2.0,2.0 | 0.2      | 0.05     | 0.0      | 0.5     | 0.05    | 0.5     |
| 19.50 | 2.0,2.0 | 0.2      | 0.1      | 0.0      | 0.5     | 0.05    | 0.5     |
| 20.70 | 2.0,2.0 | 0.3      | 0.0      | 0.0      | 0.7     | 0.0     | 0.0     |
| 21.70 | 2.0,2.0 | 0.2      | 0.05     | 0.0      | 0.5     | 0.05    | 0.0     |
| 21.90 | 2.0,2.0 | 0.2      | 0.025    | 0.0      | 0.5     | 0.025   | 0.0     |
| 40.90 | 2.0,2.0 | 0.1      | 0.0      | 0.0      | 0.5     | 0.0     | 0.0     |
| 47.80 | 2.0,2.0 | 0.1      | 0.0      | 0.0      | 0.2     | 0.0     | 0.0     |
| 5.60  | 2.0,2.0 | 0.6      | 2.0      | 0.125    | 0.25    | 1.5     | 11.0    |
| 6.00  | 2.0,2.0 | 0.6      | 2.0      | 0.125    | 0.25    | 1.5     | 10.0    |
| 6.20  | 2.0,2.0 | 0.6      | 2.0      | 0.125    | 0.25    | 1.5     | 10.0    |
| 7.30  | 2.0,2.0 | 0.6      | 2.0      | 0.125    | 0.25    | 1.5     | 5.0     |
| 7.70  | 2.0,2.0 | 0.3      | 1.0      | 0.5      | 1.0     | 1.0     | 3.0     |
| 8.90  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.5     | 10.0    |
| 9.00  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.5     | 10.0    |
| 9.30  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.5     | 10.0    |
| 9.30  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 1.0     | 1.0     | 3.0     |
| 9.40  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.5     | 2.0     |
| 9.40  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 1.0     | 1.0     | 3.0     |
| 9.60  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.0     | 3.0     |
| 9.70  | 2.0,2.0 | 0.3      | 2.0      | 0.125    | 0.25    | 1.0     | 3.0     |

Here's the same thing, but in Google Sheets with the best row highlighted: https://docs.google.com/spreadsheets/d/1MblvIsPUXqbpznzQ592WdRYqOzhaqPRqr91uXXEJd0k/edit?usp=sharing

Here's the full `params.yaml` file:

```yaml
turtlebot3_controller:
  ros__parameters:
    kp_dist_parm: 0.6
    ki_dist_parm: 2.0
    kd_dist_parm: 0.125

    kp_ang_parm: 0.25
    ki_ang_parm: 1.5
    kd_ang_parm: 11.0

    eps_dist_tol: 0.1
    eps_ang_tol: 0.05

goto_pose_client:
  ros__parameters:
    x_goal_value: 2.0
    y_goal_value: 2.0
```

### Deliverables

You can find the corresponding bag for the best run under the `rosbag2_2025_11_19-20_02_06` folder in `bags.zip` submitted to Canvas, directly in `Section_2.bag.zip` or on [GitHub](https://github.com/tresabhi/isu/tree/main/me-280/homeworks/4/bags/rosbag2_2025_11_19-20_02_06/).

Rebuilding the environment using `colcon build --symlink-install` changes nothing. Sure, the convergence time is off by less than 0.2s but that's to be expected as that seems to happen between runs anyway.

For the dist parameters, $K_p = 0.6$, $K_i = 2.0$, and $K_d = 0.125$. For the ang parameters, $K_p = 0.25$, $K_i = 1.5$, and $K_d = 11.0$.

Increasing $K_p$ made the bot more aggressive at the beginning since it was the furthest away at that point than it would've been when it got closer. But if this is too low, you end up with the bot barely creeping forwards near the end as it slowed time the closer it got. And increase it too much, you start getting oscillations which is an indicator of you needing to back up a little.

The introduction of $K_i$ gives the bot some memory, or as I like it call it, wisdom. In other words, it reduces persistent errors that may accumulate. But this must be used sparingly as if this is too high, you get oscillations again. $K_d$ simply dampens the oscillations at the expense of amplifying noise if too high.

## 3.

For this section, I came up with a similar Bash command to launch correctly every single time:

```bash
clear && killgazebo && export TURTLEBOT3_MODEL=waffle_pi && ros2 launch pid_turtlebot3 launch_sim_and_coll_avoidance.launch
```

After much experimentation, this is the implementation I came up with. The numbers are very much pulled out of thin air to make it work:

```py
    # Callback to process turtle's laser scan and compute control commands
    def timer_callback(self, msg):  #: LaserScan):
        import math

        # Function to get the range for a specific angle
        def get_range_for_angle(scan, angle_deg):
            n = len(scan)

            # Shouldn't ever happen
            if n == 0:
                return float("inf")

            # MATLAB-like extraction pattern
            idx = int(round(angle_deg)) % n

            # This can fail sometimes so assume we're out of range
            try:
                r = scan[idx]
            except Exception:
                return float("inf")

            if r == 0.0 or r is None or math.isinf(r) or math.isnan(r):
                return float("inf")

            return float(r)

        front = get_range_for_angle(msg.ranges, 0)
        front_15 = get_range_for_angle(msg.ranges, 15)
        left = get_range_for_angle(msg.ranges, 90)
        right = get_range_for_angle(msg.ranges, 270)
        front_345 = get_range_for_angle(msg.ranges, 345)

        print("Front-direction laser scan:", front)
        print("15 deg laser scan:", front_15)
        print("Left-direction laser scan:", left)
        print("Right-direction laser scan:", right)
        print("345 deg laser scan:", front_345)

        SAFE_DIST = 0.8
        CAUTION_DIST = 0.5
        TOO_CLOSE = 0.35

        l_v = 0.0
        a_v = 0.0

        # Completely clear ahead and around: go forward
        if front > SAFE_DIST and front_15 > SAFE_DIST and front_345 > SAFE_DIST:
            l_v = 0.20  # forward speed (m/s) - small safe value
            a_v = 0.0

        # Immediate danger anywhere in front arc: stop and turn away
        elif front < TOO_CLOSE or front_15 < TOO_CLOSE or front_345 < TOO_CLOSE:
            l_v = 0.0
            left_space = min(left, 10.0)
            right_space = min(right, 10.0)

            # Turn in place
            if left_space > right_space:
                a_v = 0.8
            else:
                a_v = -0.8

        # Something is approaching but not dangerously close: slow and steer around it
        else:
            if front <= CAUTION_DIST:
                l_v = 0.05
            else:
                l_v = 0.12

            # Simple steering command using front-left vs front-right
            left_feel = min(front_15, 10.0)
            right_feel = min(front_345, 10.0)
            diff = left_feel - right_feel

            K_ang = 0.8
            a_v = K_ang * math.tanh(2 * diff)  # I love hyperbolic tangent :)

            if front < SAFE_DIST:
                if front_15 < front_345:
                    a_v = -abs(a_v) - 0.2
                else:
                    a_v = abs(a_v) + 0.2

        self.my_velocity_cont(l_v, a_v)
```

The produced bag files are in the order of Gigabytes for `turtlebot3_world` and `turtlebot3_house`. Thus, they will be available only on Canvas as `turtlebot3_house.bag.zip` and `turtlebot3_world.bag.zip`.

Furthermore, I modified `turtlebot3_house.launch.py` in the `turtlebot3_simulations` submodule to spawn the robot inside for the purposes of the second simulation under `turtlebot3_world` because that's more interesting/useful than it spawning outside and exploring the great vast void:

```py
x_pose = LaunchConfiguration("x_pose", default="-2.0")
y_pose = LaunchConfiguration("y_pose", default="3")
```
