
#! /usr/bin/env python                                                                               
# -*- encoding: UTF-8 -*-

import random
import requests
import json
from naoqi import ALProxy
import time
import re
import motion
import qi
import argparse
import sys


class LED(object):
    def __init__(self):
        self.NAO_IP = "192.168.10.105"
        self.PORT = 9559
        try:
            self.ledproxy = ALProxy("ALLeds",self.NAO_IP,self.PORT)
        except Exception, e:
            print "Error:"
            print str(e)
            exit(1)

    def fade(self,name,color,duration):
        name = name
        color = color
        duration = duration
        self.ledproxy.fadeRGB(name,color,2.0)
        self.ledproxy.reset(name)

            
def main(session):
    """
    This example uses the rasta method.
    """
    # Get the service ALLeds.

    leds_service = session.service("ALLeds")

    # Example showing a one second rasta animation
    duration = 10
    leds_service.rotateEyes(0x0000FA9A,1,10)
    #leds_service.randomEyes(5)
    leds_service.fadeRGB("FaceLed7",0x00FF00FF,5)
    leds_service.fadeRGB("FaceLed7","cyan",5)
    leds_service.off("FaceLeds")
    leds_service.fade("FaceLeds",1.0,1)
    leds_service.reset("AllLeds")

    #Choregraphe_blink
    black_group = ["FaceLed0","FaceLed4","FaceLed1","FaceLed3","FaceLed5","FaceLed7"]
    white_group = ["FaceLed2", "FaceLed6"]
    leds_service.createGroup("black_group",black_group)
    leds_service.createGroup("white_group",white_group)
    rDuration = 0.1
    leds_service.fadeRGB( "black_group", 0x000000, rDuration )
    leds_service.fadeRGB( "white_group", 0x00ffffff, rDuration )
    time.sleep( 0.1 )

    #Choregraphe_randomeyes
    for i in range(10):
        rRandTime = random.uniform(0.0,2.0)
        leds_service.fadeRGB("FaceLeds", 256*random.randint(0,255) + 256*256*random.randint(0,255) + random.randint(0,255), rRandTime)
        time.sleep(random.uniform(0.0,3.0))

    leds_service.reset("AllLeds")

