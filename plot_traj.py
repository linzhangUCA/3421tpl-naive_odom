"""
Run this script with local Python (on RPi).
"""

import sys
import os
import csv
import matplotlib.pyplot as plt
from math import pi, sin, cos

# Extract data
data_dir = os.path.join(sys.path[0], "data")
### START CODING HERE ### ~ 1 line
data_file = os.path.join(data_dir, "example_data.csv")  # use your own data
### END CODING HERE ###
with open(data_file, newline="") as f:
    reader = csv.reader(f)
    vel_log = tuple(reader)
targ_lin_vels = []
targ_ang_vels = []
real_lin_vels = []
real_ang_vels = []
for vels in vel_log:
    targ_lin_vels.append(float(vels[0]))
    targ_ang_vels.append(float(vels[1]))
    real_lin_vels.append(float(vels[2]))
    real_ang_vels.append(float(vels[3]))

targ_xs, targ_ys, targ_thetas = [0], [0], [0]
real_xs, real_ys, real_thetas = [0], [0], [0]
dt = 0.05  # seconds
for i in range(len(vel_log)):
    # Compute ideal trajectory
    dx_targ = targ_lin_vels[i] * cos(targ_thetas[-1]) * dt
    dy_targ = targ_lin_vels[i] * sin(targ_thetas[-1]) * dt
    dth_targ = targ_ang_vels[i] * dt
    targ_xs.append(targ_xs[-1] + dx_targ)
    targ_ys.append(targ_ys[-1] + dy_targ)
    targ_thetas.append(targ_thetas[-1] + dth_targ)
    # Compute actual trajectory
    dx_real = real_lin_vels[i] * cos(real_thetas[-1]) * dt
    dy_real = real_lin_vels[i] * sin(real_thetas[-1]) * dt
    dth_real = real_ang_vels[i] * dt
    real_xs.append(real_xs[-1] + dx_real)
    real_ys.append(real_ys[-1] + dy_real)
    real_thetas.append(real_thetas[-1] + dth_real)
# targ_v = []
# real_v = []
# err = []
# for item in data:
#     targ_v.append(float(item[0]))
#     real_v.append(float(item[1]))
#     err.append(targ_v[-1] - real_v[-1])

# ### START CODING HERE ### ~ 4 lines
# mse = None
# ### END CODING HERE ###
# print(f"PID Controller's Mean Squared Error: {mse}")

# Plot data
# ts = list(range(len(data)))  # create timestamps for x axis
# for i in range(len(data)):
#     ts[i] = 0.05 * i
# xticks = [0] * 21
# for i in range(21):
#     xticks[i] = i
# yticks = [0] * 20
# for i in range(20):
#     yticks[i] = i * 0.1 - 1


ref_vels = (
    (0.5, 0.0),
    (0.5, pi / 8),
    (0.4, 0.0),
    (0.35, -pi / 4),
    (0.0, -2 * pi / 3),
    (-0.35, -pi / 4),
    (-0.4, 0.0),
    (-0.5, pi / 8),
    (-0.5, 0.0),
    (0.0, 2 * pi / 3),
)

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(targ_xs, targ_ys)
ax.scatter(real_xs, real_ys)
# ax[0].plot(ts, targ_v, "#7C878E", linewidth=2)
# ax[0].plot(ts, real_v, "#582C83", linewidth=1.5)
# ax[0].set_ylabel("Velocity (m/s)")
# ax[0].set_xlim([0, 20.5])
# ax[0].set_ylim([-0.95, 0.95])
# ax[0].set_xticks(xticks)
# ax[0].set_yticks(yticks)
# ax[0].grid()
# ax[0].legend(["target", "actual"])
# ax[1].plot(ts, err, "r")
# ax[1].set_xlabel("Time Stamps (s)")
# ax[1].set_ylabel("Error (m/s)")
# ax[1].set_ylim([-0.4, 0.4])
# plt.grid()
plt.show()
### UNCOMMENT FOLLOWING LINE WHEN SATISFIED WITH PID GAINS AND MSE VALUE ###
# plt.savefig('pid_eval.png'))
