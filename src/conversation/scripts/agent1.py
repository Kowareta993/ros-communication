#!/usr/bin/env python

import rospy
from conversation.srv import service

msgs = ["Hey 2! How are you?", "Ah! Same here.", "This latest assignment is very time-consuming!"]
i = 0
pub = None

def client():
    rospy.init_node('Agent1')
    rospy.wait_for_service('server')
    f = rospy.ServiceProxy('server', service)
    for msg in msgs:
        rospy.loginfo(f"Agent 2: {f(msg).res}")
    f("end")
    


if __name__ == "__main__":
   client()
