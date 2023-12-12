#!/usr/bin/env python

import rospy
import sys

from std_msgs.msg import String
from tp_ros.msg import Num

def talker():
    rospy.init_node('talker')

    pub=rospy.Publisher('chatter', Num, queue_size=10)
    
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        data=Num()

        data.num=20
        data.name="kokou"
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()


def test():
    print('\n'.join(sys.path))


if __name__=='__main__':
    try: 
        talker()
        # test()
    except rospy.ROSInterruptException:
        pass