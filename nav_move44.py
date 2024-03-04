#! /usr/bin/env python

import actionlib
import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom'
goal.target_pose.header.stamp = rospy.Time.now() 
goal.target_pose.pose.position.x = -1.5
goal.target_pose.pose.position.y = -0.5
goal.target_pose.pose.orientation.z = 0.0
goal.target_pose.pose.orientation.w = 1.0
client.send_goal(goal)
client.wait_for_result()
     
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom'
goal.target_pose.header.stamp = rospy.Time.now() 
goal.target_pose.pose.position.x = 0.0
goal.target_pose.pose.position.y = -0.5
goal.target_pose.pose.orientation.z = 0.0
goal.target_pose.pose.orientation.w = 1.0
client.send_goal(goal)
client.wait_for_result()
   
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom'
goal.target_pose.header.stamp = rospy.Time.now() 
goal.target_pose.pose.position.x = 1.5
goal.target_pose.pose.position.y = -0.5
goal.target_pose.pose.orientation.z = 0.0
goal.target_pose.pose.orientation.w = 1.0
client.send_goal(goal)
client.wait_for_result()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom'
goal.target_pose.header.stamp = rospy.Time.now() 
goal.target_pose.pose.position.x = 2.0
goal.target_pose.pose.position.y = 0.0
goal.target_pose.pose.orientation.z = 0.5
goal.target_pose.pose.orientation.w = 1.9
client.send_goal(goal)
client.wait_for_result()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom'
goal.target_pose.header.stamp = rospy.Time.now() 
goal.target_pose.pose.position.x = 1.5
goal.target_pose.pose.position.y = 0.5
goal.target_pose.pose.orientation.z = 0.9
goal.target_pose.pose.orientation.w = 0.5
client.send_goal(goal)
client.wait_for_result()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = 0.0
goal.target_pose.pose.position.y = 0.5
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.0
client.send_goal(goal)
client.wait_for_result()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = -1.5
goal.target_pose.pose.position.y = 0.5
goal.target_pose.pose.orientation.z = 1.0
goal.target_pose.pose.orientation.w = 0.0
client.send_goal(goal)
client.wait_for_result()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = -2.0
goal.target_pose.pose.position.y = 0.0
goal.target_pose.pose.orientation.z = 0.9
goal.target_pose.pose.orientation.w = -0.5
client.send_goal(goal)
client.wait_for_result()
 
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.pose.position.x = -2.0
goal.target_pose.pose.position.y = -0.5
goal.target_pose.pose.orientation.z = 0.707
goal.target_pose.pose.orientation.w = -0.707
 
print('Goal succeeded!')
 
client.send_goal(goal)
client.wait_for_result()
