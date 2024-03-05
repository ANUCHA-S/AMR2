#! /usr/bin/env python

import actionlib
import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

print('Select 0 for goto Bedroom')
print('Select 1 for goto Living Room')
print('Select 2 for goto Kitchen')
print('Select 3 for goto Home')

waypoint = input("Location: ")

while not rospy.is_shutdown():    
	if waypoint == 0:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 0
            goal.target_pose.pose.position.y = 0.5
            goal.target_pose.pose.orientation.w = 0
            goal.target_pose.pose.orientation.z = 1.0
            rospy.loginfo('Sending to Bedroom succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    exit()

        if waypoint == 1:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 2
            goal.target_pose.pose.position.y = 0.0
            goal.target_pose.pose.orientation.w = 0
            goal.target_pose.pose.orientation.z = 1.0
            rospy.loginfo('Sending to Living Room succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    exit()

        if waypoint == 2:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 0
            goal.target_pose.pose.position.y = -1.5
            goal.target_pose.pose.orientation.w = 0
            goal.target_pose.pose.orientation.z = 1.0
            rospy.loginfo('Sending to Kitchen succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    exit()

        if waypoint == 3:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = -2
            goal.target_pose.pose.position.y = -0.5
            goal.target_pose.pose.orientation.w = 0
            goal.target_pose.pose.orientation.z = 1.0
            rospy.loginfo('Sending to Home succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
            exit()


