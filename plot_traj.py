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
    vel_data = tuple(reader)
real_vels = []
for vd in vel_data:
    real_vels.append((float(vd[0]), float(vd[1])))
# Create target velocities
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
targ_vels = []
for i in range(len(real_vels)):
    targ_vels.append(ref_vels[int(i / 40)])
print(len(targ_vels))


x, y, th = [0], [0], [0]
x_hat, y_hat, th_hat = [0], [0], [0]
dt = 0.05  # seconds
for i in range(len(targ_vels)):
    # Compute ideal trajectory
    dx = targ_vels[i][0] * cos(th[-1]) * dt
    dy = targ_vels[i][0] * sin(th[-1]) * dt
    dth = targ_vels[i][1] * dt
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)
    th.append(th[-1] + dth)
    # Compute actual trajectory
    dx_hat = real_vels[i][0] * cos(th_hat[-1]) * dt
    dy_hat = real_vels[i][0] * sin(th_hat[-1]) * dt
    dth_hat = real_vels[i][1] * dt
    x_hat.append(x_hat[-1] + dx_hat)
    y_hat.append(y_hat[-1] + dy_hat)
    th_hat.append(th_hat[-1] + dth_hat)

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
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x, y)
ax.scatter(x_hat, y_hat)
# ax[0].plot(ts, targ_v, "#7C878E", linewidth=2)
# ax[0].plot(ts, real_v, "#582C83", linewidth=1.5)
# ax[0].set_ylabel("Velocity (m/s)")
# ax[0].set_xlim([0, 20.5])
# ax[0].set_ylim([-0.95, 0.95])
# ax[0].set_xticks(xticks)
# ax[0].set_yticks(yticks)
# ax[0].grid()
ax.legend(["target", "actual"])
# ax[1].plot(ts, err, "r")
# ax[1].set_xlabel("Time Stamps (s)")
# ax[1].set_ylabel("Error (m/s)")
# ax[1].set_ylim([-0.4, 0.4])
# plt.grid()
plt.show()
### UNCOMMENT FOLLOWING LINE WHEN SATISFIED WITH PID GAINS AND MSE VALUE ###
# plt.savefig('pid_eval.png'))
