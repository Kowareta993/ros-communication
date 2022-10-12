#!/usr/bin/env python

from conversation.srv import service
import rospy

responses = {"Hey 2! How are you?": "Fine, I am busy with the homework.", "Ah! Same here.": "What's the news?", "This latest assignment is very time-consuming!": "So you should get to it ASAP!"}
i = 0
pub = None
finished = False

def handle(req):
    global finished
    if req.req == "end":
        finished = True
        return "OK"
    rospy.loginfo(f"Agent 1: {req.req}")
    return responses[req.req]

def server():
    rospy.init_node('Agent2')
    s = rospy.Service('server', service, handle)
    r = rospy.Rate(10)
    while not rospy.is_shutdown() and not finished:
        r.sleep()

if __name__ == "__main__":
    server()

