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



class Talk(object):
     def __init__(self):
          self.NAO_IP = "192.168.10.105"
          self.PORT = 9559

          #nao_proxy
          self.speechproxy = ALProxy("ALTextToSpeech",self.NAO_IP,self.PORT)
          try:
               self.motionproxy = ALProxy("ALMotion",self.NAO_IP,self.PORT)
          except Exception, e:
               print "Error when creating face detection proxy:"
               print str(e)
               exit(1)
          try:
               self.faceproxy = ALProxy("ALFaceDetection",self.NAO_IP,self.PORT)
          except Exception, e:
               print "Error when creating face detection proxy:"
               print str(e)
               exit(1)
          try:
               self.postureproxy = ALProxy("ALRobotPosture",self.NAO_IP,self.PORT)
          except Exception, e:
               print "Error when creating face detection proxy:"
               print str(e)
               exit(1)
          rospy.init_node("talk",anonymous=True)
          self.pNames = "Body"
          self.pStiffnessLists = 1.0
          self.pTimeLists = 1.0
          self.rate = 10

          self.pFractionMaxSpeed = 0.4

          self.JointNames = ["LShoulerPitch","LshoulderRoll","LElbowYaw","LElbowRoll","LWristYaw","RShoulerPitch","RshoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
          self.JointNames1 = ["LShoulerPitch","LshoulderRoll","LElbowYaw","LElbowRoll","LWristYaw","RShoulerPitch","RshoulderRoll","RElbowYaw","RElbowRoll","RWristYaw","HeadPitch"]
          self.Arm1 = [81.2, 8.52, -46.0, -60.8, 7.6, 78, -21.7, 111, 58.4, 0.87]
          self.Arm2 = [81.7, 16, -78.5, -57, 0.61, 68, -32, 119, 78.3, 2.6]
          self.Arm3 = [86.8, 1.66, -53.9, -58.1, 0.44, 81.5, -3.34, 46.1, 51, -0.18,19.5]

          self.postureproxy.goToPosture("Crouch", 0.5)
     #words = recognition results
     def topic_cb(self, msg):
          result = msg.transcript[0]
          word = re.findall('\s(.*?)\|', result)
          words = "".join(word)
          if words == "":
               words=result[4:]
               print(words)
          return words

     #detect_face
     def detect_person(self):
          time_start = time.time()
          period = 500
          self.faceproxy.subscribe("Test_Face",period,0.0)
          memValue = "FaceDetected"
          try:
               memoryproxy = ALProxy("ALMemory", self.NAO_IP, self.PORT)
          except Exception, e:
               print "Error when creating memory proxy:"
               print str(e)
               exit(1)
               #search
          tim = 0
          pose = 0
          while True:
               val = memoryproxy.getData(memValue)
               if val:
                    print "face detected"
                    self.motionproxy.stopWalk()
                    time.sleep(2.0)
                    tim = 50
                    self.faceproxy.unsubscribe("Test_Face")
                    face_detected = 0
                    face_tracking = True
                    self.face_tracking(face_tracking)
                    break
               else:
                    self.walk_around(pose)    
                    print("walk_around")
                    time_end = time.time()
                    tim = time_end - time_start
                    pose = 1
                    if tim >= 15:
                         self.motionproxy.stopWalk()
                         face_detected = 1
                         break
          self.postureproxy.goToPosture("Crouch",1.0)
          return face_detected

     def face_tracking(self,face_tracking):
          self.faceproxy.enableTracking(face_tracking)
          print(self.faceproxy.isTrackingEnabled())
          
                    
                
     def walk_around(self,pose):
          pose = pose
          if pose == 0:
               self.motionproxy.stiffnessInterpolation(self.pNames,self.pStiffnessLists,self.pTimeLists)
               self.postureproxy.goToPosture("StandInit", 0.5)
               self.motionproxy.setWalkArmsEnabled(True, True)
               self.motionproxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
          else:
               X = 0.8
               Y = 0.0
               Theta = 0.0
               Frequency =0.2 # max speed = 1.0
               self.motionproxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
               time.sleep(4.0)
               
               X = 0.0
               Y = 0.0
               Theta = 0.6
               Frequency = 0.2
        
               self.motionproxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
               time.sleep(2.0)

    
     def greet(self):
          list = [
               'サイズをお探ししましょうか:',
               '商品をお探ししましょうか:',
               '何かお困りですか:',
               'こちらご試着されますか:',
               ]
          #e = random.randrange(len(list))
          #self.speechproxy.post.say(list[e])

          self.face_tracking(True) #face tracking on
                    
          self.speechproxy.post.say("こちらご試着されますか")
          Arm_move = [ x * motion.TO_RAD for x in self.Arm1]
          self.motionproxy.angleInterpolationWithSpeed(self.JointNames,Arm_move,self.pFractionMaxSpeed)
          time.sleep(7)
          print("say words")
          m = rospy.wait_for_message("/Tablet/voice",SpeechRecognitionCandidates,timeout=None)
          words = self.topic_cb(m)
          
          if words == "お願いします":
               self.speechproxy.post.say("かしこまりました")
               time.sleep(2)
               self.face_tracking(False) #face tacking off
               self.postureproxy.goToPosture("StandInit", 0.5)
               time.sleep(3)
               Arm_move = [ x * motion.TO_RAD for x in self.Arm2]
               self.motionproxy.angleInterpolationWithSpeed(self.JointNames,Arm_move,self.pFractionMaxSpeed)
               self.speechproxy.post.say("こちらへどうぞ")
               time.sleep(3)
               return 0
          
          if words == "いいえ":
               self.speechproxy.post.say("またお声がけください")
               return 1

     def fitting(self):
          #最初
          list_0 =[
               '鏡をお持ちしますね',
               '歩いてみてください']
          e_0 = random.randrange(len(list_0))
          self.speechproxy.post.say(list_0[e_0])
          time.sleep(10)

          self.face_tracking(True)
          #お客さんの反応を待つ
          list_1 = [
               "汚れやすいので防水スプレーをご利用ください:",
               "他にもご試着されますか:"
          ]
          list_2 = [
               "もう少し大きいサイズをお持ちしましょうか:",
               "中敷きをお入れしますか:",
               "こちらの商品は如何ですか:"
          ]
          #e_1 = random.randrange(len(list_1))
          #e_2 = random.randrange(len(list_2))
          
          self.speechproxy.post.say("いかがですか")
          time.sleep(5)
          print("say words")
          m = rospy.wait_for_message("/Tablet/voice",SpeechRecognitionCandidates,timeout=None)
          words = self.topic_cb(m)
          if words == "とてもいいです":
               #満足そうだった時
               self.speechproxy.post.say("お似合いですね")
               
          elif words == "少しきついです":
               #気に入っていなさそうだった時
               self.speechproxy.post.say(list_2[0])
          elif words == "少し大きいです":
               self.speechproxy.post.say(list_2[1])
          elif words == "違うものはありますか":
               self.speechproxy.post.say(list_2[2])
               
          self.speechproxy.post.say("こちらでお決まりですか:")
          time.sleep(3)
          self.face_tracking(False)
          self.speechproxy.post.say("ありがとうございます")
          time.sleep(3)
          Arm_move = [ x * motion.TO_RAD for x in self.Arm3]
          self.motionproxy.angleInterpolationWithSpeed(self.JointNames1,Arm_move,self.pFractionMaxSpeed)
          time.sleep(2)
          self.motionproxy.angleInterpolationWithSpeed("HeadPitch",0,self.pFractionMaxSpeed)
          time.sleep(2)
          self.speechproxy.post.say("レジへどうぞ")
          time.sleep(1)
          self.postureproxy.goToPosture("Crouch", 0.5)
          self.motionproxy.rest()
          
     def talked_to(self):
          rospy.wait_for_message("/Tablet/voice",SpeechRecognitionCandidates,timeout=None)
          self.face_tracking(True)
          self.postureproxy.goToPosture("StandInit", 0.5)
	  time.sleep(2)
          
          #商品の在庫を聞かれた時
          list_1 = [
               "こちらの商品をお持ちします:",
               "裏からお持ちしますね:",
               "パソコンでお調べします:",
          ]
          list_2 = [
               "お取り寄せをお調べしますか:",
               "こちらの商品は如何ですか:",
          ]
          e_1 = random.randrange(len(list_1))
          e_2 = random.randrange(len(list_2))

          e = 0
          if e == 0:
               #在庫があったとき
               self.speechproxy.post.say(list_1[e_1])
               time.sleep(3)
               return 0
          elif e == 1:
               #在庫がなかったとき
               print("申し訳ございません、こちらのサイズは売り切れです")
               word = raw_input(list_2[e_2])
               if self.yes_no(word) == 0:
                    print("ご試着されますか")
                    return 0
            #他の手段を使う
               else :
                    return 1



if __name__ == '__main__':
    p = Talk()
    e = p.detect_person()
    if e == 0:
        y = p.greet()
        y
        if y == 0:
            p.fitting()
        else:
            p.motionproxy.rest()
    else:
        print "いつでもはなしかけてください"
        y = p.talked_to()
        y
        if y == 0:
            p.fitting()
        else:
            p.motionproxy.rest()

