#!/usr/bin/env python                                                           
# -*- coding: utf-8 -*-                                                         

import random
import rospy
from std_msgs.msg import String
from speech_recognition_msgs.msg import SpeechRecognitionCandidates
import requests
import json
from naoqi import ALProxy
import time
import re
import motion

#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use rasta Method"""

import qi
import argparse
import sys


def main(session):
    """
    This example uses the rasta method.
    """
    # Get the service ALLeds.

    leds_service = session.service("ALLeds")

    # Example showing a one second rasta animation
    duration = 10
    #leds_service.rotateEyes(0x0000FA9A,1,10)
    #leds_service.randomEyes(5)
    #leds_service.fadeRGB("FaceLed7",0x00FF00FF,5)
    #leds_service.fadeRGB("FaceLed7","cyan",5)
    #leds_service.off("FaceLeds")
    #leds_service.fade("FaceLeds",1.0,1)
    #leds_service.reset("AllLeds")

    black_group = ["FaceLed0","FaceLed4","FaceLed1","FaceLed3","FaceLed5","FaceLed7"]
    white_group = ["FaceLed2", "FaceLed6"]
    leds_service.createGroup("black_group",black_group)
    leds_service.createGroup("white_group",white_group)
    rDuration = 0.08
    leds_service.fadeRGB( "black_group", 0x000000, rDuration )
    leds_service.fadeRGB( "white_group", 0xffffff, rDuration )
    time.sleep( 0.1 )

    leds_service.reset("AllLeds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.10.105",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
