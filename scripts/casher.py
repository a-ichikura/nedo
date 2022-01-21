#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TalkChaplus(object):

    def __init__(self):
        self.headers = {'content-type':'text/json'}
        self.url = 'https://www.chaplus.jp/v1/chat?apikey=6098e31511276'

    def talk(self):
        word = raw_input("")
        word = str(word)
        payload = {'utterance':word,
                   'agentState':{'agentName':'pippo','age':'23','tone':'nonmal'}
                   'addition':{}}
        res = requests.post(url=self.url,headers=self.headers,data=json.dumps(payload))
        best_res = res.json()['bestResponse']['utterance']
        print(type(best_res))
        print(best_res.encode('utf-8'))

if __name__ == '__main__':
    word = "いらっしゃいませ"
    print(word)
    word = "お預かりします"
    while True:
        p = TalkChaplus()
        p_say = p.talk()    
