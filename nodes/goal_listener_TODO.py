import rospy

import actionlib

from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

waypoints = [] # array to accumulate the 3 waypoints

def listener():
    rospy.init_node('goal_listener')
    rospy.Subscriber('ko/move_base_simple/goal', PoseStamped, waypointRvizClbk)



# This function is called each time a new goal is set in the Rviz interface.
def waypointRvizClbk(goal): 

    ## TO DO
    ## Complete the following code

    waypoints.append(goal)

    ...

    continue_ = move_base_(waypoints.pop(0))


    ...


 

# This function is responsible of moving the robot from point A to point B.
# It returns True if the robot successfully reach point B and False otherwise.
def move_base_(goal_):

    client.wait_for_server()

    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = 'map'

    goal.target_pose.pose = goal_.pose

    client.send_goal(goal)

    client.wait_for_result()
    
    print(client.get_goal_status_text())
    
    return True if client.get_goal_status_text() == 'Goal reached.' else False

   
if __name__ == '__main__':

    listener()
    rospy.spin()
