import rospy

import actionlib

from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

client = actionlib.SimpleActionClient('move_base', MoveBaseAction)


def callback(goal):

    ## Write your code here 

    ### .....
    pass



def move_base_to(goal_):
    # client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    client.wait_for_server()

    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = 'map'

    goal.target_pose.pose = goal_.pose

    client.send_goal(goal)

    client.wait_for_result()
    
    print(client.get_goal_status_text())
    
    return True if client.get_goal_status_text() == 'Goal reached.' else False

    # return client.get_result()


def listener():
    rospy.init_node('goal_listener')
    rospy.Subscriber('ko/move_base_simple/goal', PoseStamped, callback)


if __name__ == '__main__':

    listener()
    rospy.spin()