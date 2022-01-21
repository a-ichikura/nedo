
#!/usr/bin/env python                                                             # -*- coding: utf-8 -*-

class Talk(object):
    
    def talk(self):
        print("いらっしゃいませ")
        print("お預かりします")

        word = raw_input("箱は持って帰られますか:")
        if self.yes_no(word) == 0:
            pass
        else :
            pass #箱から出す

        word = raw_input("こちらXXXcmでお間違いないですか:")
        if self.yes_no(word) == 0:
            pass
        else :
            pass #サイズを交換する
        #バーコードをスキャンする関数

        word = raw_input("袋はおつけしますか:")
        if self.yes_no(word) == 0:
            word = raw_input("ビニールと紙どちらにされますか:")
            if self.bag(word) == 0:
                pass #紙の時
            else :
                pass #ビニールの時
        else :
            print("紙でお包みしますね")
            pass #袋はつけない
        print("お会計はXXXになります")

        word = raw_input("ポイントカードはお持ちですか:")
        if self.yes_no(word)==0:
            print("カードをお預かりします")
            #ポイントカードをスキャンする関数
            word = raw_input("ポイントはお貯めしたままでよろしいですか")
            if self.yes_no(word)==0:
                print("ポイントをお貯めします")
                pass
            else:
                #ポイントを使う関数
                pass
        else:
            pass
        
        word = raw_input("お支払い方法はいかがされますか:")
        if self.cash(word)==0:
            #現金で操作する関数
            pass
        elif self.cash(word)==1:
            #カードで操作する関数
            pass
        elif self.cash(word)==2:
            #電子マネーで操作する関数
            pass

        print("お品物をお渡し致します")
        #袋を渡す関数
        print("ありがとうございました")
        #お辞儀の関数

    def yes_no(self,word):
        word = str(word)
        if word == "はい":
            return 0
        if word == "いいえ":
            return 1

    def bag(self,word):
        word = str(word)
        #袋代を足す関数
        if word == "紙":
            return 0
        if word == "ビニール":
            return 1

    def cash(self,word):
        word = str(word)
        if word =="現金":
            print("先にポイントカードをお返しします")
            print("XXX円のお返しです")
            return 0
        if word =="クレジットカード":
            print("カードをこちらに差し込んでください")
            print("カードをお返しします")
            return 1
        if word =="電子マネー":
            print("こちらにタッチお願いします")
            return 2
   

if __name__ == '__main__':
    while True:
	p = Talk()
        p_say = p.talk()
