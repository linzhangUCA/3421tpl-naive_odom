"""
Run this script with Micropython (on Pico).
"""

from diff_drive_controller import DiffDriveController
from time import sleep
from math import sin, pi


# SETUP
# Instantiate wheel
bot = DiffDriveController(left_ids=((2, 3, 4), (20, 21)), right_ids=((6, 7, 8), (10, 11)))

ref_vels = ((0.5, 0.), (0.75, pi / 8), (0.35, -pi / 4), (0., 0.), (-0.35, -pi / 4), (-0.75, pi / 8), (-0.5, 0.))
# Variables
err = 0.0
err_sum = 0.0
err_diff = 0.0
prev_err = 0.0
target_vel = 0.0
data = []

# LOOP
for i in range(280):  # 20Hz controller, 14 seconds
    if not (i + 1) % 40:
        targ_vel = ref_vels[int((i + 1) / 40) - 1]
        print(targ_vel)
        bot.set_vel(*targ_vel)
    sleep(0.05)

bot.set_vel(0., 0.)
### UNCOMMENT FOLLOWING 3 LINES WHEN SATISFIED WITH PID GAINS ###
# with open(f'data{target_vel}.csv', 'w') as file:
#     for item in data:
#         file.write(f'{item[0]},{item[1]}\n')
