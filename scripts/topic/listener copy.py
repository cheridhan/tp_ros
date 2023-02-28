#!/usr/bin/env python

import rospy

from std_msgs.msg import String

from tp_ros.msg import Num


def callback(data):
    # print(data.num)
    rospy.loginfo(data.num)
    rospy.loginfo(data.name)


def listener():
    rospy.init_node('listener')

    rospy.Subscriber('chatter', Num, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
