import random
from playsound import playsound
import time
hack = False
op = True
# Define card suits and ranks
casinoemojies=['⚫🔴🃏🎰💲💳💰🕒🎲⏩🕹️💵👑 🏆🎰📱💳🎲⚡️,\
               🤞🎲🎰🍀🥠🔮🎱🧧☘🌠8️⃣7️⃣6️⃣🐞🌈🦋🙏 🧿,\
               ','🍀𝑼 𝑨𝑹𝑬 𝑳𝑼𝑪𝑲𝒀 𝑱𝑼𝑺𝑻 𝑩𝑬𝑳𝑰𝑽𝑬🍀',' 🎡✨']
suits = ['♢','♧','♡','♤']#🅰 ❤ 👑
ranks = ["🅰", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "👑"]
#balance= 1000
#bet = int(input('Bet:'))
def sound(file):
    pt =  playsound('C:\\Users\\Dell\\Desktop\\test\\pic\\'+file)
    return pt 
fruits = ['🍒', '🍊', '🍇', '🍉', '🍋', '🍓', '🥝', '🍎','🍆','🍍','🍐' ]
def moneyanimation(times,sec):
    for i in range (times):
        print('💰',end= '',flush=True)
        time.sleep(sec)
    print('\n')
wheel = [
    {"number": "0", "color": "🟩"},
    {"number": "00", "color": "🟩"},
    {"number": "1", "color": "🟥"},
    {"number": "2", "color": "⬛"},
    {"number": "3", "color": "🟥"},
    {"number": "4", "color": "⬛"},
    {"number": "5", "color": "🟥"},
    {"number": "6", "color": "⬛"},
    {"number": "7", "color": "🟥"},
    {"number": "8", "color": "⬛"},
    {"number": "9", "color": "🟥"},
    {"number": "10", "color": "⬛"},
    {"number": "11", "color": "⬛"},
    {"number": "12", "color": "🟥"},
    {"number": "13", "color": "⬛"},
    {"number": "14", "color": "🟥"},
    {"number": "15", "color": "⬛"},
    {"number": "16", "color": "🟥"},
    {"number": "17", "color": "⬛"},
    {"number": "18", "color": "🟥"},
    {"number": "19", "color": "🟥"},
    {"number": "20", "color": "⬛"},
    {"number": "21", "color": "🟥"},
    {"number": "22", "color": "⬛"},
    {"number": "23", "color": "🟥"},
    {"number": "24", "color": "⬛"},
    {"number": "25", "color": "🟥"},
    {"number": "26", "color": "⬛"},
    {"number": "27", "color": "🟥"},
    {"number": "28", "color": "⬛"},
    {"number": "29", "color": "⬛"},
    {"number": "30", "color": "🟥"},
    {"number": "31", "color": "⬛"},
    {"number": "32", "color": "🟥"},
    {"number": "33", "color": "⬛"},
    {"number": "34", "color": "🟥"},
    {"number": "35", "color": "⬛"},
    {"number": "36", "color": "🟥"},
]
animation = [
    {"number": "0", "color": "🟩"},
    {"number": "00", "color": "🟩"},
    {"number": "1", "color": "🟥"},
    {"number": "2", "color": "⬛"},
    {"number": "3", "color": "🟥"},
    {"number": "4", "color": "⬛"},
    {"number": "5", "color": "🟥"},
    {"number": "6", "color": "⬛"},
    {"number": "7", "color": "🟥"},
    {"number": "8", "color": "⬛"},
    {"number": "9", "color": "🟥"},
    {"number": "10", "color": "⬛"},
    {"number": "11", "color": "⬛"},
    {"number": "12", "color": "🟥"},
    {"number": "13", "color": "⬛"},
    {"number": "14", "color": "🟥"},
    {"number": "15", "color": "⬛"},
    {"number": "16", "color": "🟥"},
    {"number": "17", "color": "⬛"},
    {"number": "18", "color": "🟥"},
    {"number": "19", "color": "🟥"},
    {"number": "20", "color": "⬛"},
    {"number": "21", "color": "🟥"},
    {"number": "22", "color": "⬛"},
    {"number": "23", "color": "🟥"},
    {"number": "24", "color": "⬛"},
    {"number": "25", "color": "🟥"},
    {"number": "26", "color": "⬛"},
    {"number": "27", "color": "🟥"},
    {"number": "28", "color": "⬛"},
    {"number": "29", "color": "⬛"},
    {"number": "30", "color": "🟥"},
    {"number": "31", "color": "⬛"},
    {"number": "32", "color": "🟥"},
    {"number": "33", "color": "⬛"},
    {"number": "34", "color": "🟥"},
    {"number": "35", "color": "⬛"},
    {"number": "36", "color": "🟥"},
]
payouts = {"number": 35, "color": 1}


# Generate 5 random cards
class Moves:
    def dice(self):
        dice_op = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣",]
        self.deiceview = random.choice(dice_op)
        dice_move ={"1️⃣":1,"2️⃣":2,"3️⃣":3,"4️⃣":4,"5️⃣":5,"6️⃣":6,}
        self._move = dice_move[self.deiceview]
        return self._move,self.deiceview
    
    
class Games:
    def game_poker(self):
        cards = []
        
        for i in range(5):
            suit = random.choice(suits)
            rank = random.choice(ranks)
            card = {"suit": suit, "rank": rank}
            if card not in cards:
                cards.append(card)
            else:
                suit = random.choice(suits)
                rank = random.choice(ranks)
                card = {"suit": suit, "rank": rank}
                #cards.append(card)
                if card not in cards:
                     cards.append(card)
                else:
                    suit = random.choice(suits)
                    rank = random.choice(ranks)
                    card = {"suit": suit, "rank": rank}
                    cards.append(card)
        # Print the cards
        print("🃏Your cards are:🃏")
        for card in cards:
            
            print(card["rank"], card["suit"],' ',end='',flush=True)
            time.sleep(0.5)
            
            
        # Check for poker combinations
        rank_count = {}
        for card in cards:
            rank = card["rank"]
            if rank not in rank_count:
                rank_count[rank] = 1
            else:
                rank_count[rank] += 1
        if len(rank_count) == 2:
            if max(rank_count.values()) == 4:
                print("💰 Four of a kind!💰")
                print(" 💰Full house!💰")
                print('💥MEGA-GIGA WIN💥',end = '')
                for i in range (30):
                    print('💰',end= '',flush=True)
                    time.sleep(0.2)
                print('\n')
                return 150
            else:
                print(" 💰Full house!💰")
                print('💥MEGA-GIGA WIN💥',end = '')
                for i in range (30):
                    print('💰',end= '',flush=True)
                    time.sleep(0.2)
                print('\n')
                return 150
        elif len(rank_count) == 3:
            if max(rank_count.values()) == 3:
                print(" 💰Three of a kind!💰")
                print('💥EXTRA WIN💥',end = '')
                for i in range (10):
                    print('💰',end= '',flush=True)
                    time.sleep(0.4)
                print('\n') 
                return 25
            else:
                print("💰 Two pairs!💰")
                print('💥SUPER WIN💥',end = '')
                for i in range (6):
                    print('💰',end= '',flush=True)
                    time.sleep(0.5)
                print('\n') 
                return 10

        
        else:
            sorted_ranks = sorted(ranks.index(card["rank"]) for card in cards)
            if len(set(card["suit"] for card in cards)) == 1 and sorted_ranks == [0, 9, 10, 11, 12] or all(sorted_ranks[i] == sorted_ranks[i+1]-1 for i in range(4)) or hack:
                print(" 💰Straight Flush!💰")
                moneyanimation(30,0.2)
                return 1000
            
            elif sorted_ranks == [0, 9, 10, 11, 12] or all(sorted_ranks[i] == sorted_ranks[i+1]-1 for i in range(4)):
                print(" 💰Straight!💰")
                print('💥MEGA-GIGA WIN💥',end = '')
                for i in range (30):
                    print('💰',end= '',flush=True)
                    time.sleep(0.2)
                print('\n')
                return 150
            elif len(set(card["suit"] for card in cards)) == 1:
                print(" 💰Flush!💰")
                return 150
            else:
                for i in cards:
                    times = 0
                    if i["rank"] == '👑':
                            times+=1
                            if times == 2:
                                print(" 👑👑👑")
                                print("👑KING WIN👑",end = '')
                                moneyanimation(6,0.4)
                                return 6
                    if op:            
                        for i in cards:
                            if i["rank"] == '👑':
                                print(" 👑DOUBLE!👑")
                                print('👑KING WIN👑',end = '')
                                for i in range (2):
                                    print('💰',end= '',flush=True)
                                    time.sleep(1)
                                print('\n')
                                return 2
                                                        
                    elif i["rank"] == '🅰':
                        times+=1
                        if times == 2:
                            print('🅰🅰🅰')
                            moneyanimation(6,0.4)
                            return 4
                if len(rank_count) == 4:
                    moneyanimation(1,0.9) 
                    return 1
                    #elif i["rank"] == '🅰':
                    #    print('🅰🅰🅰')
                    #   return 2 
                else:
                    print(" High card.")
                    return 0

 

# Define a function to get the player's bet
    def game_roulette(self,balance):
        
        bet_amount = 0
        def get_bet():
            while True:
                bet_type = input("❓Do you want to bet on a number or a color? (number(n)/color(c)):❓ ")
                if bet_type not in ["n", "c"]:
                    print("❗Invalid bet type. Please choose 'number' or 'color'.❗")
                    continue
                bet = input("💳❓What do you want to bet on 🟥(r) ,⬛(b) or🟩(g)? ")
                if bet == 'r':
                    bet = '🟥'
                elif bet == 'b':
                    bet = '⬛'
                elif bet == 'g':
                    bet = '🟩'
                if bet_type == "n" and not bet.isdigit():
                    print("❗Invalid number. Please enter a number between 0 and 36.❗")
                    continue
                elif bet_type == "c" and bet.lower() not in ["🟥", "⬛","🟩"]:
                    print("❗Invalid color. Please enter 🟥(r) , ⬛(b) or 🟩(g).❗")
                    continue
                else:
                    return {"type": bet_type, "bet": bet}

        # Define a function to spin the wheel and determine the result
        def spin_wheel():
            if hack:
                randomchoise = {"number": "0", "color": "🟩"}
            else:
                randomchoise=random.choice(wheel)
            winning_number = randomchoise
            animation.append(winning_number)
            for i in animation:
                print(i['number'],i['color'],'', flush=True)
                time.sleep(0.05)
            print(f"The winning number is ⚡️{winning_number['number']}⚡️ ({winning_number['color']}).")
            animation.remove(winning_number)
            return winning_number
            
        
        #Define a function to calculate the payout
        def calculate_payout(bet, result,betamount):
            if bet["type"] == "n" and bet["bet"] == result["number"]:
                result_ =payouts["number"] * bet_amount
                return result_
            elif bet["type"] == "c" and bet["bet"].lower() == result["color"] and bet["bet"].lower()=='🟩':
                result_ =payouts["number"] * bet_amount
                return result_   
            elif bet["type"] == "c" and bet["bet"].lower() == result["color"]:               
                result_ =payouts["color"] * betamount
                return result_
            else:
                betamount = -betamount
                return betamount

        #Define the main game loop
        
        
            
        while int(balance) > 0:
            print(f"Your current balance is 💲{balance}.")
         

            try:
                bet_amount_ = int(input("💳How much do you want to bet?💳"))
             

                bet_amount = bet_amount + bet_amount_
                balance = int(balance)
                if bet_amount > balance:
                    print("❗You don't have enough money to make that bet.❗")
                    continue
                elif bet_amount <= 0:
                    print("❗Invalid bet amount. Please enter a positive number.❗")
                    continue
            except ValueError:
                print("❗Invalid bet. Please enter a positive number.❗")
                continue
            bet = get_bet()
            print(f"You bet 💲{bet_amount} on {bet['bet']} ({bet['type']}).")
            result = spin_wheel()
            payout = calculate_payout(bet, result,bet_amount)
            return payout
           #balance += payout * bet_amount
            #print(f"You {'won' if payout > 0 else 'lost'} ${payout * bet_amount}.")
           #break
           
            #print("You're out of money! Thanks for playing!")
            #play_again = input("Do you want to play again? (y/n): ")
            #if play_again.lower() == "n":
            #    break



    def game_slot(self):
        fruits = ['🍒', '🍊', '🍇', '🍉', '🍋', '🍓', '🥝', '🍎','🍆','🍍','🍐' ]

        
        # Randomly select a fruit from the list for each row
        row1 = [random.choice(fruits) for _ in range(3)]
        row2 = [random.choice(fruits) for _ in range(3)]
        row3 = [random.choice(fruits) for _ in range(3)]
        luck = random.randint(1, 100)
        
        luck2 = random.randint(1, 1000)
        if  luck2<= 25:
            row1 = ['🍀','🍀', random.choice(fruits)]
            row2 = [random.choice(fruits), '🍀','🍀']
            row3 = ['🍀', random.choice(fruits),'🍀']
        elif luck2 >= 950:
            row1 = ['🍀', '🍀','🍀']
            row2 = [random.choice(fruits), '👑', random.choice(fruits)]
            row3 = ['🍀', '🍀','🍀']
        elif luck2 == 777 or hack:
            row1 = ['🍀', '🍀','🍀']
            row2 = ['🍀', '🍀','🍀']
            row3 = ['🍀', '🍀','🍀']
        if luck  <= 3:
            row1 = [random.choice(fruits), random.choice(fruits), random.choice(fruits)]
            row2 = [random.choice(fruits), '👑', random.choice(fruits)]
            row3 = ['👑', '👑', '👑']
        elif  5>luck<= 8:
            row1 = ['👑', random.choice(fruits), '👑']
            row2 = [random.choice(fruits), '👑', random.choice(fruits)]
            row3 = [ '👑',random.choice(fruits), '👑']
        elif 12>luck <= 15:
            row1 = [ '👑','👑','👑']
            row2 = [random.choice(fruits),'👑' , random.choice(fruits)]
            row3 = [random.choice(fruits), random.choice(fruits), random.choice(fruits)]
        def slotanimation(timetoslow):
            #sleep = time.sleep(timetoslow)
            for i in [row1,row2,row3]:
                print('\n')
                for item in i:
                    print(item,'|',flush=True,end='')
                    time.sleep(timetoslow)

        slotanimation(0.5)       
        # Check for 4 of the same kind on all the rows combined
        all_rows = row1 + row2 + row3
        for fruit in fruits:
            if all_rows.count(fruit) == 4:
                
                print(f"\n🎉  SUPER WIN!  🎉\n")
                moneyanimation(10,0.2)
                return 10
        if len(set(all_rows))== 3:
            print(f"\n🎉  SUPER WIN!  🎉\n")
            moneyanimation(15,0.2)
            return 35
        elif  len(set(all_rows))== 2:
            print(f"\n🎉  SUPER WIN!  🎉\n")
            moneyanimation(30,0.2)
            return 100
        elif  len(set(all_rows))== 4 or len(set(all_rows))== 5 :
            print(f"\n🎉  SUPER WIN!  🎉\n")
            moneyanimation(5,0.3)
            return 5


        # Check for 3 of the same kind on each row
        if len(set(row1)) == 1 and len(set(row2)) == 1 and len(set(row3)) == 1:
            print(f"\n🎉 OMEGA WIN!  🎉")
            moneyanimation(100,0.1)
            return 10000
        
        # Check for 2 of the same kind on each row
        if len(set(row1)) <= 2 and len(set(row2)) <= 2 and len(set(row3)) <= 2:
            print(f"\n🎉  MEGA WIN!  🎉")
            moneyanimation(30,0.2)
            return 100       
        
        else:
            print(f"\n🙁  Better luck next time!  🙁")
            return 0    
        spin()
    # Example usage
if __name__ =='__main__':
    gm = Games()
   # print(gm.game_roulette(1000))
    print(gm.game_slot())
