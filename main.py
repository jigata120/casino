import random 
import csv
import pandas as pd
from main import Games 
 
avatars  = {1:"👨",2:"👩",3:"👧",4:"👦",5:"👳‍♂️",6:"🎅",\
                7:"🧔",8:"👲"}
list = []
L =[]
name = None
avatar = None
balance = 1000

#balance = int(input("balance:"))
 
 
class Exceptions:
    def invalid(self,name):
        if not name :
            raise ValueError("Not name givven!")
        elif len(str(name)) <1:
            raise ValueError("Too short Name")
 
 
class Data(Exceptions):
    def set_data(self,name,avatar,balance):
        with open("data.csv","a") as file:
            self.writer = csv.DictWriter(file, fieldnames=["name","avatar","balance"])
            self.writer.writerow({"name":name,"avatar":avatar,"balance":balance})
 
    def accs(self): 
        with open("data.csv","r") as file:
            self.reader =  csv.DictReader(file)  
            for row in self.reader:
                self.list = list.append({"name":row["name"] ,"avatar":row["avatar"],"balance":row["balance"]})
            print("All your avatars are:")
            super().invalid(list)
            for info in list :
                avatar_n = int(info["avatar"])
                avatar = avatars[avatar_n]
                print(f" {info['name']} {avatar}{info['balance']}")
 
    def join_acc(self, acctojoin): 
        for info in list:
            if info["name"] == acctojoin:
                name = info["name"]
                avatar_n = int(info["avatar"])
                avatar = avatars[avatar_n]
                balance = info["balance"]
                print(f"Wellcome {name} {avatar} ✅ balance:💲{balance} !")
                return name , avatar,balance
  
class Update:
    
    def index(self):
        index=0
        for i in list:
            index += 1
            if i["name"]==name:
                
                return index -1
    def update(self,n,balance):

        df = pd.read_csv("data.csv",delimiter=",")
        df.loc[n, "balance"] = balance
        df.to_csv("data.csv", index=False)
       # print(df)
   # update(index,int(balance))
class Avatar(Exceptions):
    def __init__(self,name):
        self.name= name
 
    def choiseof_avatar(self):
 
        for i in avatars:
            print (str(i)+avatars[int(i)])
        #super().invalid()
    def get_avatar(self,name):
 
            super().invalid(name)
            #try:
            self._avatar_choise = avatars[name]
            #except KeyError:
             #   raise KeyError("invalid input(must be 1-8)")
            Data.set_data(self,self._name,name,balance)
            print("Seccessfully registerd "+self._avatar_choise+" " +self._name, "✅")
 
 
    @property
    def name(self):
        return self._name
    @name.setter
    def name (self,name):
        super().invalid(name)
        self._name = name
 
 
class Balance(Exceptions):

    def  win(self,win):
           global balance                    
           win1 = win
           while True:
                color  = random.choice(['⚫','🔴'])
                if input(f"WIN!💲 {win1} 💰2️❌💰(y)") == "y":
                    while True:
                        suit = input("Guess the SUIT ⚫🃏🔴 (b)(r)")
                        if suit not in ["b","r"]:
                            continue
                        if suit == "b":
                            suit ='⚫'
                        elif suit == "r":
                            suit ='🔴'
                        if suit == color:
                            win1 = win1 *2
                            break
                        else:
                            return f"LOSS! 😢0 Balance:{balance}"
                    continue
                balance = int(win1) + int(balance)
                return f"WIN!💲 {win1} 💲 Balance:{balance}"
    def loss(self,lost):
           global balance
         # super().invalid(balance)
           #lost = int(input("lost:"))
           if lost<0:
               lost = lost * -1
           balance =  int(balance)-int(lost) 
           return f"LOSS! 😢{lost} Balance:",balance


def register():
    nickname = Avatar(name = input("❓What to be your name?❓").upper())
    nickname.choiseof_avatar()
    nickname.get_avatar(name = int(input("❓Choose a avatar (number 1-8).❓")))
    #data = Data(self._name,self._avatar_choise)
 
def join():
    global name,avatar,balance
    #print(name,avatar,balance)
    data = Data()
    data.accs()
    #print(name,avatar,balance)
    name,avatar,balance =data.join_acc(input("❓acc to join:❓ ").upper())
    #bl = Balance()
   # bl.win()
    #bl.lost()
def play():
    up = Update()
    bl = Balance()
    gm = Games()
    print(list)
    print("\n🍀𝑼 𝑨𝑹𝑬 𝑳𝑼𝑪𝑲𝒀 𝑱𝑼𝑺𝑻 𝑩𝑬𝑳𝑰𝑽𝑬🍀")
    print("\n(1)  🎡ROULETTE🎡\n(2)  🃏KING'S👑 POKER🃏\n(3) 🎰 SHINNING CROWNS👑🎰")
    choise  = str(input("(1),(2),(3):"))
    if choise =="1":
        print("\nWelcome to 🎡Roulette🎡!\n")
        while True:
            bet_result=int(gm.game_roulette(balance))
            #print(bet_result)
            if bet_result>0:
                result = bl.win(bet_result)
            else:
                result = bl.loss(bet_result)
            print(result)
            up.update(up.index(),int(balance))
            play_again = input("❓Do you want to play again? (Enter/Lobby(l)): ")
            if play_again.lower() == "l":
                    break              
    elif choise=="2":
        print("\nWelcome to 🃏KING'S👑 POKER🃏!\n")
        while True:
            try:
                bet = int(input("💳How much do you want to bet?"))
               # balance = int(balance)
                if bet > balance:
                    print("❗You don't have enough money to make that bet.❗")
                    continue
                elif bet <= 0:
                    print("❗Invalid bet amount. Please enter a positive number.❗")
                    continue
            except ValueError:
                print("❗Invalid bet. Please enter a positive number.❗")
                continue 
            bl.loss(bet)
            gamereturn = gm.game_poker()
            betresult = int(bet*gamereturn)
            if betresult>=bet:
                result = bl.win(betresult)
            else:
                result = bl.loss(betresult)
            print (result)
            up.update(up.index(),int(balance))
            play_again = input("❓Do you want to play again? (Enter/Lobby(l)): ")
            if play_again.lower() == "l":
                    break
    elif choise == "x":
        quit()
        
    else:
        print("\nWelcome to 🎰 SHINNING CROWNS👑🎰\n")
        while True:
            try:
                bet = int(input("💳How much do you want to bet?"))
               # balance = int(balance)
                if bet > balance:
                    print("❗You don't have enough money to make that bet.❗")
                    continue
                elif bet <= 0:
                    print("❗Invalid bet amount. Please enter a positive number.❗")
                    continue
            except ValueError:
                print("❗Invalid bet. Please enter a positive number.❗")
                continue
            bl.loss(bet)
            gamereturn = gm.game_slot()
            betresult = int(bet*gamereturn)
            if betresult>=bet:
                result = bl.win(betresult)
            else:
                result = bl.loss(betresult)
            print (result)
            up.update(up.index(),int(balance))
            play_again = input("❓Do you want to play again? (Enter/Lobby(l)): ")
            if play_again.lower() == "l":
                    break
            
    play()
def main():
    global balance
    #bl = Balance()
   # bl.win()
    #bl.lost()
   #register() 
   #move = Moves()j

    bl = Balance()
    up = Update()
    if input("❓REGISTER(r) or JOIN(j): ")=="j":
        join()
        #for i in range(5):
        balance = int(balance)
        play()
        
        up.update(up.index(),int(balance))
    else:
        register()
        join()
        balance = int(balance)
        play()
        up.update(up.index(),int(balance))
    print(f"Your name is :{name}, your avatar is:{avatar} and your balance is: 💲{balance}")
    
   #print(move.dice())
 
 
if __name__=="__main__":
    main()
#up = Update()
#up.update(name,balance)

'''
list=[]
with open("data.csv","r") as file:
                    reader =  csv.DictReader(file)
                    for row in reader:
                        list.append({"name":row["name"] ,"avatar":row["avatar"],"balance":row["balance"]})

class Update:
    def update(self,name,value) :
        list.append({"name": "name", "avatar": "avatar", "balance": "balance"}	)
        with open("data.csv","r") as file:
                    reader =  csv.DictReader(file)  
                    for row in reader:
                        list.append({"name":row["name"] ,"avatar":row["avatar"],"balance":row["balance"]})
        for row in list:
            if row["name"]== name:
                row ["balance"]= value
            L.append(row)
        with open("data.csv","a") as file:
            file.write(f"name")
            file.write(f",")
            file.write(f"avatar")
            file.write(f",")
            file.write(f"balance\n")
        with open("data.csv","w") as file:
            writer = csv.DictWriter(file, fieldnames=["name","avatar","balance"])
            for row in L:    
                writer.writerow({"name":row["name"],"avatar":row["avatar"],"balance":row["balance"]})
    with open("data.csv","r") as file:
        reader =  csv.DictReader(file)
        for row in reader:
                print (row)
'''  
