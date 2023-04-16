import rospy

from geometry_msgs.msg import PoseStamped

import yaml


def listener():
    rospy.init_node('goal_listener')
    rospy.Subscriber('move_base_simple/goal', PoseStamped, goals)


def goals(data):
    rospy.loginfo(data)

    rospy.set_param('charging_stations/station_1/position/x',
                    data.pose.position.x)
    
    input_data = {
        'station_1':{
            'position':{
                'x': data.pose.position.x,
                'y': data.pose.position.y,
                'z': data.pose.position.z,
            }
        }
    }


    path='/home/lissassi/catkin_ws/src/tp_ros/config/charging_station'

    with open(f'{path}.yaml','w') as f:
        yaml.dump(input_data,f,sort_keys=False)
    
    print('Written to file successfully')


def setPosition():
    pass


if __name__ == '__main__':

    listener()
    rospy.spin()
