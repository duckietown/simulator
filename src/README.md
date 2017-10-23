# Duckietown Environment and Duckiebot in gazebo

With this folder, you can run duckietown environment and control robot with gazebo.


##Build and run duckietown environment with a duckiebot

```
cd simulator
catkin build
source devel/setup.bash
cd simulator/src/duckietown_gazebo
source env_gazebo.sh
cd ..
./run_gazebo.sh
'''
You will see a Duckiebot in Duckietown now. You can also control robot through publish messege to topic with command ```rostopic pub /cmd_vel geometry_msgs/Twist "linear:
  x: 0.2
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.1"``` or ```./run_cmd```
**NOTE:  To build successfully, maybe you need to install a lot ros packages. Based on the error message, use ```sudo apt-get install ros-kinetic-packagename **






