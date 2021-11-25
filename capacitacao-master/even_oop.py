#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def callback(data):
	if data.data%2 != 0:
		rospy.loginfo(data.data)

if __name__ == '__main__':
	rospy.init_node('talker', anonymous=True)
	pub = rospy.Publisher('chatter', Int64, queue_size=10)
	sub = rospy.Subscriber('chatter', Int64, callback)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		for i in range(0,11):
			if i%2 != 0:
				pub.publish(i)
			rate.sleep()
