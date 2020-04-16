import pybullet as p
import pybullet_data as pd
import os

import glob, copy

p.connect(p.DIRECT)

obj_files = glob.glob('*.obj')

for obj_file in obj_files:
    name_out = copy.copy(obj_file)
    name_out = name_out.replace('.obj', '_vhacd.obj')
    name_log = "log.txt"
    p.vhacd(obj_file, name_out, name_log, alpha=0.04,resolution=50000 )
