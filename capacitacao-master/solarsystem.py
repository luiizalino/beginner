#!/usr/bin/env python 


import rospy
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg
import math


rospy.init_node("publisher", anonymous=True)
broadcaster = tf2_ros.TransformBroadcaster()
rate = rospy.Rate(10)

class Planet():
	def __init__(self,name, orbit_radius, header="Sun"):
		
		self.name = name
		#self.header = header
		self.orbit_radius = orbit_radius
		self.trans = geometry_msgs.msg.TransformStamped()
		self.trans.header.frame_id = header
		self.trans.child_frame_id = self.name
		self.trans.header.stamp = rospy.Time.now() 

		self.trans.transform.translation.x = 1
		self.trans.transform.translation.y = 2
		self.trans.transform.translation.z = 0

		self.trans.transform.rotation.x = 0
		self.trans.transform.rotation.y = 0
		self.trans.transform.rotation.z = 0
		self.trans.transform.rotation.w = 1




	def translation(self):
		x = 2 * rospy.Time.now().to_sec() * math.pi / (self.orbit_radius ** (3/2) * 60)
		self.trans.transform.translation.x = self.orbit_radius*math.sin(x)
		self.trans.transform.translation.y = self.orbit_radius*math.cos(x)
		self.trans.transform.translation.z = 0.0
		self.trans.header.stamp=rospy.Time.now()
		return self.trans



Earth = Planet("earth",1)
Moon = Planet("moon",0.8,"earth")

while not rospy.is_shutdown():
	Earth.translation()
	Moon.translation()
	broadcaster.sendTransform(Earth.trans)
	broadcaster.sendTransform(Moon.trans)
	rate.sleep()

rospy.spin()
   
