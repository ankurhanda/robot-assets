This repository contains various robot arm and object URDFs. The URDF models have been obtained from various publicly available resources and we have made sure that the links to the appropriate repositories where we got the models from are also provided. The purpose of this repository to put together many well known and often used models in one place. 

## URDFs

### Robots 


| Robot Name      | Source                                                                   |
|-----------------|--------------------------------------------------------------------------|
| Franka Panda    | https://github.com/dic-iit/gym-ignition-models                           |
| UR5/UR10/Kinova | https://github.com/Gepetto/example-robot-data.git                        |
| KUKA iiwa       | https://github.com/kuka-isir/iiwa_description                            |
| Fetch Robot     | https://github.com/openai/roboschool/tree/master/roboschool/models_robot |
| YUMI            | https://github.com/OrebroUniversity/yumi                                 |
| Ginger          | https://github.com/Rayckey/GingerURDF                                    |
| Anymal          | https://github.com/ANYbotics/anymal_b_simple_description                 |
| Halodi          | https://github.com/Halodi/halodi-robot-models                            |
| R2 and Val      | https://github.com/gkjohnson/nasa-urdf-robots                            |
| Robotiq Gripper | https://github.com/a-price/robotiq_arg85_description                     |
| Barrett Hand    | https://github.com/jhu-lcsr-attic/bhand_model                            |
| AR4             | https://github.com/ycheng517/ar4_ros_driver/tree/main/annin_ar4_description |
| LeRobot SO100   | https://github.com/TheRobotStudio/SO-ARM100/tree/main/Simulation/SO100   |


### Object Assets 

Kitchen asset is from https://github.com/code-iai/robot_scenarios_sim/tree/master/models_pkg/models/kitchen

## Conversion from xacro to URDF

The repo also contains the code to convert xacro to urdf (obtained from https://github.com/doctorsrn/xacro2urdf). 

Run `python xacro.py -o ./target.urdf urdf/origin.xacro` to start convertion. For example, `python xacro.py -o ./test_abb_4600.urdf urdf/irb4600_60_205.xacro` in `abb_irb4600_support` folder. If convert successfully, the `test_abb_4600.urdf` will be generated. Make sure to keep `xacro.py` to the same directory as `urdf` folder.
