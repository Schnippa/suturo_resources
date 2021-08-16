#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

if __name__ == u'__main__':
    rospy.init_node(u'init_joint_positions')
    position_publisher = {
        u'head_tilt_joint':
            {"publisher": rospy.Publisher('/hsrb/head_tilt_joint_position_controller/command', Float64, queue_size=10),
             "position": 0.0},
        u'head_pan_joint':
            {"publisher": rospy.Publisher('/hsrb/head_pan_joint_position_controller/command', Float64, queue_size=10),
             "position": 0.0},
        u'arm_lift_joint':
            {"publisher": rospy.Publisher('/hsrb/arm_lift_joint_position_controller/command', Float64, queue_size=10),
             "position": 0.05},
        u'arm_flex_joint':
            {"publisher": rospy.Publisher('/hsrb/arm_flex_joint_position_controller/command', Float64, queue_size=10),
             "position": 0.0},
        u'arm_roll_joint':
            {"publisher": rospy.Publisher('/hsrb/arm_roll_joint_position_controller/command', Float64, queue_size=10),
             "position": -1.57},
        u'wrist_flex_joint':
            {"publisher": rospy.Publisher('/hsrb/wrist_flex_joint_position_controller/command', Float64, queue_size=10),
             "position": -1.57},
        u'wrist_roll_joint':
            {"publisher": rospy.Publisher('/hsrb/wrist_roll_joint_position_controller/command', Float64, queue_size=10),
             "position": 0.0}}

    for p in position_publisher.values():
        rospy.sleep(rospy.Duration(1))
        p["publisher"].publish(Float64(data=p["position"]))

