# Naive Odometry

## Objetives

- Build a bare minimal odometry system.
- Compare the robot's actual trajectory to its ideal trajectory.
- Get familiar with [HomeR](https://github.com/linzhangUCA/homer)'s control system.

## Requirements

### 1. (40%) Collect Velocity Data (Pico MicroPython)

Run [vel_data_collect.py](vel_data_collect.py) to drive your robot and collect data.
Uncomment the last 3 lines, store the target and actual velocity data on your Pico.

1. (20%) Lift the wheels and have a no-load test run on desktop. Collect data and upload the saved data to [data](/data/) directory in this repository.
2. (20%) Put the robot down on the ground to test again. Collect data and upload the saved data to [data](/data/) directory in this repository.

### 2. (60%) Calculate Trajectories

Complete [plot_traj.py](plot_traj.py). Code the sections wrapped between the following comments.

```python
### START CODING HERE ###

### END CODING HERE ###
```

Tackle the following requests.

1. (40%) Calculate the ideal and actual robot trajectories using the collected data.
2. (20%) Plot the desktop and ground trajectories and upload to the [images](images/) directory.

#### Frame Setup

![odom_frame](images/odom_frame.png)

There are 2 reference frames involved.

1. Global frame: $\{X, Y\}$ is fixed on the driving plane and will not move along the robot.
2. Body frame: $\{x, y\}$ is attached to the robot and will translate and rotate along the robot's movement.

The body frame's origin is sitting at the geometric center of the robot's base plate. The $x$ axis is always pointing to the head of the robot, and the $y$ axis is perpendicular to the $x$ axis and pointing to the left wheel.

The Global frame will be generated according to the initial pose of the robot. The $\{X, Y\}$ frame will overlap with the initial $\{x, y\}$ frame.

#### Install Matplotlib

```console
# Run following line in terminal
pip install matplotlib --break-system-packages
```

## AI Policies

Please acknowledge AI's contributions follow the policies in the syllabus.
