# ME 280 Homework 3

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

The corresponding bag can be found in the `rosbag2_2025_11_16-22_17_19` folder within `bags.zip`, `Section_1.bag.zip` as requested explicitly by the question in the Canvas submission, or (https://github.com/tresabhi/isu/tree/main/me-280/homeworks/4/bags/rosbag2_2025_11_16-22_17_19/).

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

```
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

With this done, I went to town trying out combinations from the following pool:

$$
[0.1, 0.5, 1.0, 5.0, 10.0]
$$

To automate this process, I wrote the following Bash script. Note line 2 where I delete the `waffle_pi` entity. I ran into an issue where simultaneous simulations kept running at once, letting the bot reach speeds exceeding the sound barrier, disallowing convergence.

```bash
clear
ros2 service call /delete_entity gazebo_msgs/srv/DeleteEntity "{name: 'waffle_pi'}"
ros2 launch pid_turtlebot3 launch_sim_and_control.launch
```

And then I realized I don't actually know how to write Bash beyond just batching commands together, so I wrote the following Python script instead. Note that there's a peculiar `ANG_FACTOR` variable in there, allow me to explain.

The original idea was I would go through all possible combinations of $[0.1, 0.5, 1.0, 5.0, 10.0]$. That's a lot of combinations and I plan to finish this assignment before I graduate so I tried setting both angular and linear gains equally but that has an inherit flaw: angles are radians, displacements is a distance. So I approximated the playground to be around 8 by 8 units large and then scaled the dist gain by $8 / 2\pi$ to get the angular gains. This is either really clever, or really really naive and I am betting on the latter.

```py
import itertools
import yaml
import subprocess
import time
import os
from math import pi
import psutil

PARAMS_FILE = "src/me2800_hw4/pid_turtlebot3/config/params.yaml"
ROS_LAUNCH_CMD = ["ros2", "launch", "pid_turtlebot3", "launch_sim_and_control.launch"]
DELETE_CMD = [
    "ros2",
    "service",
    "call",
    "/delete_entity",
    "gazebo_msgs/srv/DeleteEntity",
    "{name: 'waffle_pi'}",
]
TIMES_DIR = "times"

gain_values = [0.1, 0.5, 1.0, 5.0, 10.0]
dist_keys = ["kp_dist_parm", "ki_dist_parm", "kd_dist_parm"]
ang_keys = ["kp_ang_parm", "ki_ang_parm", "kd_ang_parm"]

ANG_FACTOR = 8 / (2 * pi)


def snapshot_times():
    return set(os.listdir(TIMES_DIR)) if os.path.exists(TIMES_DIR) else set()


def kill_process_tree(pid):
    try:
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()
    except psutil.NoSuchProcess:
        pass


for combo in itertools.product(gain_values, repeat=len(dist_keys)):
    with open(PARAMS_FILE, "r") as f:
        data = yaml.safe_load(f)

    for key, value in zip(dist_keys, combo):
        data["turtlebot3_controller"]["ros__parameters"][key] = value

    for key, value in zip(ang_keys, combo):
        data["turtlebot3_controller"]["ros__parameters"][key] = value * ANG_FACTOR

    with open(PARAMS_FILE, "w") as f:
        yaml.dump(data, f)

    before_files = snapshot_times()

    subprocess.run(DELETE_CMD, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    proc = subprocess.Popen(ROS_LAUNCH_CMD)

    start_time = time.time()
    new_file_found = False
    while time.time() - start_time < 10:
        time.sleep(0.1)
        after_files = snapshot_times()
        new_files = after_files - before_files
        if new_files:
            new_file_found = True
            break

    kill_process_tree(proc.pid)

    print(f"Combo {combo} -> New file found: {new_file_found}")

print("All combinations completed")
```
