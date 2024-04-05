#!/usr/bin/env python3
Framework: ROS
Technology Stack: C++, Python

# Author: Automatic Addison
# Date: July 20, 2021
# ROS Version: ROS 1 - Noetic
# Website: https://automaticaddison.com
# This ROS node sends the robot goals to move to a particular location on 
# a map.

# 1 = House 1
# 2 = House 2
# 3 = House 3
# 4 = Post Office (Default)

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib.simple_action_client import SimpleActionClient
import sys

user_choice = 4

# Action specification for move_base
MoveBaseClient = SimpleActionClient('move_base', MoveBaseAction)

def main():
    # Connect to ROS
    rospy.init_node('simple_navigation_goals')

    # Tell the action client that we want to spin a thread by default
    ac = MoveBaseClient

    # Wait for the action server to come up so that we can begin processing goals.
    while not ac.wait_for_server(rospy.Duration(5.0)):
        rospy.loginfo("Waiting for the move_base action server to come up")

    # Ask the user where he wants the robot to go
    print("\nWhere do you want the robot to go?")
    print("\n1 = House 1")
    print("2 = House 2")
    print("3 = House 3")
    print("4 = Post Office")
    user_choice = int(input("\nEnter a number: "))

    # Create a new goal to send to move_base
    goal = MoveBaseGoal()

    # Send a goal to the robot
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Use map_server to load the map of the environment on the /map topic.
    # Launch RViz and click the Publish Point button in RViz to
    # display the coordinates to the /clicked_point topic.
    if user_choice == 1:
        print("\nGoal Location: House 1\n")
        goal.target_pose.pose.position.x = -15.04
        goal.target_pose.pose.position.y = -7.42
        goal.target_pose.pose.orientation.w = 1.0
    elif user_choice == 2:
        print("\nGoal Location: House 2\n")
        goal.target_pose.pose.position.x = -14.25
        goal.target_pose.pose.position.y = 20.02
        goal.target_pose.pose.orientation.w = 1.0
    elif user_choice == 3:
        print("\nGoal Location: House 3\n")
        goal.target_pose.pose.position.x = 7.35
        goal.target_pose.pose.position.y = 20.17
        goal.target_pose.pose.orientation.w = 1.0
    else:
        print("\nGoal Location: Post Office\n")
        goal.target_pose.pose.position.x = 12.12
        goal.target_pose.pose.position.y = -8.41
        goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal")

    # Set a timeout in seconds
    ac.send_goal_and_wait(goal, rospy.Duration(180.0, 0), rospy.Duration(180.0, 0))

    if ac.get_state() == actionlib.SimpleClientGoalState.SUCCEEDED:
        rospy.loginfo("The robot has arrived at the goal location")
    else:
        rospy.loginfo("The robot may have failed to reach the goal location")

if __name__ == "__main__":
    main()
'''