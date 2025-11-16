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

print("All combinations completed.")
