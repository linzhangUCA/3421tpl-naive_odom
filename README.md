# Naive Odometry

## Objetives

- Practice building a bare minimal odometry system.
- Get familiar with [HomeR](https://github.com/linzhangUCA/homer)'s control system.
- Compare the robot's actual trajectory to its ideal trajectory.

## Requirements

### 1. (40%) Collect Velocity Data (Pico MicroPython)

Run [vel_data_collect.py](vel_data_collect.py) to drive your robot.
Uncomment the last 3 lines, store the target and actual velocity data on your Pico.

- (40%) Upload the saved data to [data](/data/) directory in this repository.

### 2. (60%) Plot Trajectories

Complete the provided python scripts.
Code the sections wrapped by the following comments.

```python
### START CODING HERE ###

### END CODING HERE ###
```

Mean squared error (MSE) is a metric used to measure the average squared difference between two variables.
We can employ such a metric to measure the difference between the wheel's target velocity and actual velocity.
And such a metric can serve as an indicator of the PID controller's performance.

- During the data collection process, $T$ measurements are taken to probe/sample the wheel's actual velocity.
- Each measurement is taken at a certain moment $t_i$, where $i \in {0, 1, 2, \dots, T}$.
- Let velocity of the wheel at moment $t_i$ be $v_i$ and the actual velocity at the same moment to be $\hat{v}_i$.

The MSE between the target and the actual wheel velocity in this control process can be written as,

$$e_{MSE} = \frac{1}{T} \sum_{i=0}^T (v_i - \hat{v}_i)^2$$

Complete the code in [evaluation.py](evaluation.py) for the following requests.

1. (10%) Visualize target vs. actual velocity data. Uncomment last line to plot the velocity comparison graph. Upload the figure to this repository.
2. (40%) Compute the MSE using the data collected in the first section. You'll need to figure out the correct values for $T$, $v_i$, and $\hat{v}_i$
3. (10%) Your MSE is below **0.003**

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
