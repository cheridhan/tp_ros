#!/bin/bash

# Update the package list
echo "Updating the package list ..."
sudo apt-get update

# Install nano text editor
echo "Installing nano editor..."
sudo apt-get install nano -y nano

# Installing Turtlebot3 ROS package
echo "Installing Turtlebot3 ROS package..."
sudo apt-get install ros-noetic-turtlebot3

# Installing Turtlebot3 simulation package
echo "Installing Turtlebot3 simulation package..."
sudo apt-get install ros-noetic-turtlebot3-simulations

# Setting up TURTLEBOT3_MODEL environment variable
sudo echo "export TURTLEBOT3_MODEL=burger">>.bashrc
source ~/.bashrc

# Installing map server
echo "Installing Map Server"
sudo apt-get install ros-noetic-map-server

cd ~/catkin_ws/src
echo "Installing tp_ros package"
git clone -b workout_communication https://github.com/cheridhan/tp_ros

echo "Install Turtlebot3 teleop package"
sudo apt-get install ros-noetic-turtlebot3-teleop

cd ~/catkin_ws
catkin_make

echo "Installation and Setup complete successfully"
