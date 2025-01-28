"""
Run this script with Micropython (on Pico).
"""

from diff_drive_controller import DiffDriveController
from time import sleep
from math import pi


# SETUP
# Instantiate wheel
bot = DiffDriveController(
    left_ids=((2, 3, 4), (20, 21)), right_ids=((6, 7, 8), (10, 11))
)

ref_vels = (
    (0.5, 0.0),
    (0.75, pi / 8),
    (0.4, 0.0),
    (0.35, -pi / 4),
    (0.0, -2 * pi / 3),
    (-0.35, -pi / 4),
    (-0.4, 0.0),
    (-0.75, pi / 8),
    (-0.5, 0.0),
    (0.0, 2 * pi / 3),
)
# Variables
targ_vel_data = []
real_vel_data = []

# LOOP
sleep(1)  # get your robot ready!
targ_vel = ref_vels[0]
bot.set_vel(*targ_vel)
for i in range(400):  # 20Hz controller, 20 seconds
    if not (i + 1) % 40:
        if i < 399:
            targ_vel = ref_vels[int((i + 1) / 40)]
        # print(targ_vel)
        bot.set_vel(*targ_vel)
    sleep(0.05)
    # print(bot.lin_vel, bot.ang_vel)
    targ_vel_data.append(targ_vel)
    real_vel_data.append((bot.lin_vel, bot.ang_vel))

bot.set_vel(0.0, 0.0)
### UNCOMMENT FOLLOWING 3 LINES WHEN SATISFIED WITH PID GAINS ###
# with open(f'vel_data.csv', 'w') as file:
#     for i in range(len(targ_vel_data)):
#         file.write(f'{targ_vel_data[i][0]},{targ_vel_data[i][1]},{real_vel_data[i][0]},{real_vel_data[i][1]}\n')
