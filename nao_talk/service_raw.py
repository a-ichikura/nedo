#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Talk(object):
    
    def wrapping(self):
        print("いらっしゃいませ")
        print("お預かりします")

        word = raw_input("こちらご自宅用ですか:")
        if self.yes_no(word) == 0:
            #通常レジ作業
            return 0
        else :
            #プレゼント
            word = raw_input("ラッピングいたしますか:")
            if self.yes_no(word) == 1:
                #通常レジ作業
                return 0
            else :
                word = raw_input("どの袋にされますか:")
                #袋を選ぶ関数
                word = raw_input("包み方はどれにされますか:")
                #包み方を選ぶ関数
                word = raw_input("シールをお選びください:")
                #シールを選ぶ関数
                word = raw_input("どこにお貼りしますか:")
                print("おまたせいたしました")
                print("お会計にご案内します")
            pass

    def small_talk(self):
        list = [
            '今日はどちらへお出かけですか:',
            '今日も良いお天気ですね:',
            'このあとのご予定は:',
            '今日のお召し物はとても素敵ですね:',
            'いつもご利用いただきありがとうございます:',
            ]
        e = random.randrange(len(list))
        word = raw_input(list[e])
        #聞いた内容に対するメッセージ
        

    def yes_no(self,word):
        word = str(word)
        if word == "はい":
            return 0
        if word == "いいえ":
            return 1

   

if __name__ == '__main__':
    word = str(raw_input("ラッピングorメッセージ:"))
    if word == "ラッピング":
	p = Talk()
        p.wrapping()
    else:
        p = Talk()
        p.small_talk()
