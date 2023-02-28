#! /usr/bin/env python

import rospy

import actionlib
import tp_ros.msg

class FibonacciAction(object):
    #create messages that are used to publish
    _feedback=tp_ros.msg.FibonnacciFeedback()
    _result=tp_ros.msg.FibonnacciResult()

    def __init__(self, name):
        self._action_name=name
        self._as=actionlib.SimpleActionServer(self._action_name, tp_ros.msg.FibonnacciAction,execute_cb=self.execute_cb,auto_start=False)
        self._as.start()

    def execute_cb(self,goal):
        #helper variables
        r=rospy.Rate(1)
        success=True

        # append the seeds for the fibonacci sequence
        self._feedback.partial_sequence=[]
        self._feedback.partial_sequence.append(0)
        self._feedback.partial_sequence.append(1)

        # publish info to the console for the user
        # rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i'%(self._action_name, goal.order, self._feedback.partial_sequence[0], self._feedback.partial_sequence[0],self._feedback.partial_sequence[1]))

        # start executing the action
        for i in range(1, goal.order):
            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted'% self._action_name)
                self._as.set_preempted()
                success=False
                break
            self._feedback.partial_sequence.append(self._feedback.partial_sequence[i]+self._feedback.partial_sequence[i-1])


            # publish the feedback
            self._as.publish_feedback(self._feedback)

            r.sleep()

        if success:
            self._result.sequence=self._feedback.partial_sequence
            rospy.loginfo('%s: Succeeded'% self._action_name)
            self._as.set_succeeded(self._result)


if __name__=='__main__':
    rospy.init_node('fibonacci_node')
    server= FibonacciAction(rospy.get_name())
    rospy.spin()
