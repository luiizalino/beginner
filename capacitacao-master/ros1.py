#!/usr/bin/env python

import rospy
from std_msgs.msg import String
#!/usr/bin/env python

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
	for talk in range (1,11):
        	rospy.loginfo(talk)
        	pub.publish(str(talk))
        	rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


