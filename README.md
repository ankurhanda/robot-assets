This repository contains various robot arm and object URDFs.

## URDFs

Franka Panda is obtained from https://github.com/dic-iit/gym-ignition-models

Robotiq Gripper is obtained from https://github.com/a-price/robotiq_arg85_description

UR5/UR10/Kinova are obtained from https://github.com/Gepetto/example-robot-data.git

KUKA iiwa is obtained from pybullet data.

Fetch Robot is obtained from https://github.com/openai/roboschool/tree/master/roboschool/models_robot

YUMI is obtained from https://github.com/OrebroUniversity/yumi

Ginger is from https://github.com/Rayckey/GingerURDF

Barrett Hand is from https://github.com/jhu-lcsr-attic/bhand_model

Anymal is from https://github.com/ANYbotics/anymal_b_simple_description

## Conversion from xacro to URDF

The repo also contains the code to convert xacro to urdf (obtained from https://github.com/doctorsrn/xacro2urdf). 

Run `python xacro.py -o ./target.urdf urdf/origin.xacro` to start convertion. For example, `python xacro.py -o ./test_abb_4600.urdf urdf/irb4600_60_205.xacro` in `abb_irb4600_support` folder. If convert successfully, the `test_abb_4600.urdf` will be generated. Make sure to keep `xacro.py` to the same directory as `urdf` folder.
