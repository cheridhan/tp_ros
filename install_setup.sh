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

cd ~/catkin_ws
catkin_make


source .bashrc
echo "Installation and Setup complete successfully"
