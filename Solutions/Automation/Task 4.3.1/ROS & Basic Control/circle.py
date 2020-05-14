#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist

def move():

	#Start a new node
	rospy.init_node('circle', anonymous = True)
	move_circle = rospy.Publisher('/cmd_vel' , Twist , queue_size = 10)

	vel_msg = Twist()

	#Give the linear and angular velocities necessary to move the robot in circle

	vel_msg.linear.x = 0.7
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0.7

	#Set the publishing frequency

	rate = rospy.Rate(10)

	#Publishing the velocity

	while True:
		move_circle.publish(vel_msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException: pass




