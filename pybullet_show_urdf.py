import pybullet as p
import time
import math
from datetime import datetime
from time import sleep

p.connect(p.GUI)

robot_id = p.loadURDF("nvidia_hand.urdf", useFixedBase=True)

p.setGravity(0, -9.81, 0)

while True:

    p.stepSimulation()
