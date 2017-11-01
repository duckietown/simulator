# Duckietown Simulator

## 1 Installation

You will need to pull two separate github repos. 
Please ignore the instructions in the respective repos. 
This installation guide will walk you 
through the installation of both.

Pull the simulator client (doesn't matter where you put it):

    cd ~/dev/ # for example, or cd ~/Documents
    git pull git@github.com:duckietown/gym-duckietown.git 

Install the simulator client globally on your PC:

    cd gym-duckietown
    sudo pip2 install -e .

Pull the simulator server into your duckietown catkin workspace:

    cd ~/duckietown/catkin_ws/src
    git pull git@github.com:duckietown/duckietown-sim-server.git
    
Install dependencies for the sim-server

    #TODO - do the students need any other deps?
    
If you've never evr run `catkin_make` after installing
duckietown, you should do this now.

    #TODO instructions on how to run catkin_make in duckietown
    
Test your Gazebo installation

    cd duckietown/
    source environment.sh
    gazebo
    
This last command should start Gazebo and after some 10 seconds or so
you should see an empty Gazebo simulator 3D environment.

    #TODO add image

If you don't see this image or if Gazebo only loads with a black screen,
you might have to compile Gazebo from source

    #TODO add link to instructions
    
-----

## 2 Running Experiments

For running an RL experiment you need 3 shells:

 - **running the Gazebo simulator** - starting the Duckietown
 world and loading the Duckiebot car 
 - **running the Gym server** - for receiving actions from the RL
  agent and executing them via ROS in the Gazebo simulator
 - **running the Gym client** - for training the RL agent
  

### 2.1 Starting the Server

Start the duckietown environment:

    cd duckietown/
    source environment.sh
    
Then load the additional Gazebo parameters:

    cd catkin_ws/src/duckietown-sim-server/
    cd duckietown_gazebo && source env_gazebo.sh && cd -
    
Start the Gazebo simulator:

    ./run_gazebo.sh
    
You should wait for a few seconds to see Gazebo load the duckietown model.
 
Open a new shell and repeat the environment steps to get your ROS environment:

    cd duckietown/
    source environment.sh
    cd catkin_ws/src/duckietown-sim-server/
    
Launch the Python server

    python2 ./gym-gazebo-server.py

Now you have the Python server running in its own process,
you can start clients. 
      
### 2.2 Running a Gym client

We provided a little interactive client within the `gym-duckietown` repo
that lets you control the robot with the keyboard
and stream the image from the robot's camera.

In order to run this demo (and see how the gym works),
please (open a new shell,) change into the gym directory, and 
run the demo:

    cd ~/dev/gym-duckietown # or wherever you installed the gym repo
    python2 standalone.py

This opens a new window with the streaming camera image.
If you click on the camera image, you can use the **arrow
keys** to navigate with your Duckiebot. Each keypress
executes a single step in the simulation.

-----

## 3 Goals:
- Provide a Docker container with a simulation that users can easily deploy
  -  Should be able to connect to one or more simulation machine (ie: clusters)
  - Docker container will contain ROS, Gazebo, and a Gym server (ROS bridge)
- Easy to use Python library for interacting with the simulation
  - Compatible with OpenAI gym
- First version will use a fixed Duckietown map layout

[2017-10-25 Meeting notes](https://docs.google.com/document/d/1TL7UA9BhEvJCniv5VI4grfxC2hKiDUztNttiu7o18co/edit)

[2017-10-18 Meeting notes](https://docs.google.com/document/d/1ht5vmjObMQHqdZVo86coZaMxk0uCPw6SBI5OHzZKR30/edit)

[2017-10-11 Meeting notes](https://docs.google.com/document/d/1q2-KIFl0sBp39PCQfJB-0MNN-UxoQTrf57uf72-D8Hk/edit)
