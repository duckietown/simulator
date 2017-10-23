# Duckietown Simulator

[2017-10-18 Meeting notes](https://docs.google.com/document/d/1ht5vmjObMQHqdZVo86coZaMxk0uCPw6SBI5OHzZKR30/edit)

[2017-10-11 Meeting notes](https://docs.google.com/document/d/1q2-KIFl0sBp39PCQfJB-0MNN-UxoQTrf57uf72-D8Hk/edit)

Goals:
- Provide a Docker container with a simulation that users can easily deploy
  -  Should be able to connect to one or more simulation machine (ie: clusters)
  - Docker container will contain ROS, Gazebo, and a Gym server (ROS bridge)
- Easy to use Python library for interacting with the simulation
  - Ideally compatible with OpenAI gym
- First version will use a fixed Duckietown map layout
