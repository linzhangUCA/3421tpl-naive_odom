# Naive Odometry

## Objetives

- Practice building a bare minimal odometry system.
- Get familiar with [HomeR](https://github.com/linzhangUCA/homer)'s control system.
- Compare the robot's actual trajectory to its ideal trajectory.

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

#### Install Matplotlib

```console
# Run following line in terminal
pip install matplotlib --break-system-packages
```

#### Understand Mean Squared Error

- [Article](https://www.geeksforgeeks.org/mean-squared-error/)
- [Video](https://youtu.be/beIgcdf0YDE?si=HzSU4BpFaquhJd5t)

## AI Policies

Please acknowledge AI's contributions follow the policies in the syllabus.
