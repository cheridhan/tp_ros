#!/usr/bin/env python

import rospy

from std_msgs.msg import String

import sys


def talker(name):
    rospy.init_node('talker')

    pub=rospy.Publisher('chatter', String, queue_size=10)
    
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        data = "My name is " + name
        rospy.loginfo(data)
        pub.publish(name)
        rate.sleep()




if __name__=='__main__':
    try: 
        name  = " "

        if len(sys.argv) == 2:
             name = sys.argv[1]

        talker(name)

    except rospy.ROSInterruptException:
        pass