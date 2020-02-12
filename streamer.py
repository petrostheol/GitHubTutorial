#!/usr/bin/env python

import rospy #as r    this will replace rospy with r. instead of rospy, you press r.
import random
from std_msgs.msg import Int16

def streamer():                                                             # DEFINE FUNCTION
    pub = rospy.Publisher('/task1/numbers', Int16, queue_size = 10)         # DECLARES WHAT AND WHERE YOUR NODE WILL PUBLISH
    rospy.init_node('streamer', anonymous = True)                           # INITIALIZES YOUR NODE (YOU SEE 'streamer' BUT THE anonoymous = True CREATES A UNIQUE NAME FOR THE MASTER TO USE)
    rate = rospy.Rate(1)                                                    # FREQUENCY OF MESSAGE STREAM = 1Hz

    while not rospy.is_shutdown():                                          # WHILE THE NODE IS RUNNING
        rand_value = random.randint(1,10) #% rospy.get_time()               # PRODUCE A random_value BETWEEN 1 & 10 (%rospy.get_time() for more randomness)
        rospy.loginfo(rand_value)                                           # SHOW THE RANDAOM NUMBER WITH ITS LOGINFO
        pub.publish(rand_value)                                             # PUBLISH THE RANDOM NUMBER TO /task1/numbers
        rate.sleep()                                                        # SLEEP ENOUGH BETWEEN MSGS TO MANTAIN 1Hz

if __name__ == '__main__':                                                  # MAIN
    try:
        streamer()
    except rospy.ROSInterruptException:                                     # STANDARD PROCEDURE
        pass
