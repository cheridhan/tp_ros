#! /usr/bin/env python


from __future__ import print_function

import rospy
import sys

# brings in the SimpleActionClient
import actionlib

import tp_ros.msg

def fibonacci_client():
    # creates the SimpleActionClient, passing the type of the action
    client = actionlib.SimpleActionClient('', tp_ros.msg.FibonnacciAction)


    # waits until the action server has started up and started
    # listening for goals
    client.wait_for_server()

    # creates a goal to send to the action server
    goal = tp_ros.msg.FibonnacciGoal(order=4)



    # Sends the goal to the action server
    client.send_goal(goal,feedback_cb=feedback)

    # waits for the server to finish performing the action
    client.wait_for_result()

    # prints out the result of executing the action
    return client.get_result()

def feedback(data):
    print(data)


if __name__=='__main__':
    try:
        # initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS

        rospy.init_node('fibonacci_client')

        result=fibonacci_client()

        print('Result:', ','.join([str(n) for n in result.sequence]))

    except rospy.ROSInterruptException:
        print(' program interrupted before completion', file=sys.stderr)