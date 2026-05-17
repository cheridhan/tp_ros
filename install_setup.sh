#!/bin/bash

# Update the package list
echo "Updating the package list ..."
sudo apt-get update

# Install nano text editor
echo "Installing nano editor..."
sudo apt-get install nano -y nano

# Setting up TURTLEBOT3_MODEL environment variable
sudo echo "export TURTLEBOT3_MODEL=burger">>.bashrc

# Installing map server
echo "Installing Map Server"
sudo apt-get install ros-noetic-map-server -y

git clone -b noetic https://github.com/ROBOTIS-GIT/turtlebot3.git catkin_ws/src/turtlebot3

git clone -b noetic https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git catkin_ws/src/turtlebot3_msg

git clone -b noetic https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git catkin_ws/src/turtlebot3_simulations

cd ~/catkin_ws
catkin_make


source /home/user/.bashrc
source /home/user/catkin_ws/devel/setup.bash
echo "Installation and Setup complete successfully"
