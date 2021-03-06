#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Talk(object):
    
    def greet(self):
        list = [
            'サイズをお探ししましょうか:',
            '商品をお探ししましょうか:',
            '何かお困りですか:',
            'こちらご試着されますか:',
            ]
        e = random.randrange(len(list))
        word = raw_input(list[e])
        if self.yes_no(word) == 0:
            return 0
        if self.yes_no(word) ==1:
            return 1

    def fitting(self):
        #最初
        list_0 =[
            '鏡をお持ちしますね',
            '歩いてみてください']
        e_0 = random.randrange(len(list_0))
        print(list_0[e_0])


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
        e_1 = random.randrange(len(list_1))
        e_2 = random.randrange(len(list_2))

        word = raw_input("いかがですか:")
        if self.yes_no(word) == 0:
            #満足そうだった時
            print("とてもお似合いですね")
            raw_input(list_1[e_1])
        else:
            #気に入っていなさそうだった時
            raw_input(list_2[e_2])
            
        raw_input("こちらでお決まりですか:")

    def talked_to(self):
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

        e = random.randrange(2)
        if e == 0:
            #在庫があったとき
            raw_input(list_1[e_1])
            print("こちらご試着されますか:")
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

    def yes_no(self,word):
        word = str(word)
        if word == "はい":
            return 0
        if word == "いいえ":
            return 1


if __name__ == '__main__':
    e = random.randrange(2)
    p = Talk()
    if e == 0:
        y = p.greet()
        y
        if y == 0:
            p.fitting()
        else:
            pass
    else:
        raw_input("何か話しかけてください:")
        y = p.talked_to()
        y
        if y == 0:
            p.fitting()
        else:
            pass
