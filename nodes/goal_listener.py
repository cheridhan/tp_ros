import rospy

import actionlib

from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

import yaml


client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

waypoints = []

def listener():
    rospy.init_node('goal_listener')
    rospy.Subscriber('ko/move_base_simple/goal', PoseStamped, callback)


def callback_(goal):
    # rospy.loginfo(goal)
    print(move_base_(goal))

def callback(goal):

    waypoints.append(goal)

    if len(waypoints) == 3:
        continue_ = True
        while continue_ and len(waypoints) > 0:
            continue_ = move_base_(waypoints.pop(0))



def move_base_(goal_):
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


def save_goal(goal):
    pass

    rospy.set_param('charging_stations/station_1/position/x',
                    goal.pose.position.x)

    input_data = {
        'station_1': {
            'position': {
                'x': goal.pose.position.x,
                'y': goal.pose.position.y,
                'z': goal.pose.position.z,
            }
        }
    }

    path = '/home/lissassi/catkin_ws/src/tp_ros/config/charging_station'

    with open(f'{path}.yaml', 'w') as f:
        yaml.dump(input_data, f, sort_keys=False)

    print('Written to file successfully')


if __name__ == '__main__':

    listener()
    rospy.spin()
