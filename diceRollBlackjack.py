# dice roll 21
import random, sys
name = input('Enter Name: ')
cpu_dice = [1, 2, 3, 4, 5, 6]
user_dice = cpu_dice
def roll_game():
    c = ''
    print("""
The Object Is Of The Game Is To Be The First One To 21
However, If You Or The CPU Score Is Over 21 After Their Roll,
Then That Player Losses. If You Choose To Fold, The CPU Gets Another Roll.
If The CPU Score Is Greater Than Yours Without A Bust, Then You Lose.
Winner Gets The Pot. Pot Starts At 5 And You Start Off With $100.
Good Luck.
""")
    uTotal = 0
    cTotal = 0
    pot = 5
    money = 100
    cMoney = money
    while uTotal <= 21 and cTotal <= 21:
        print('Press Enter To Roll. "Fold" To Fold Turn.')
        uN = random.randint(0,5)
        user_roll = user_dice[uN]
        cN = random.randint(0,5)
        cpu_roll = cpu_dice[cN]
        INPUT = input()
        if INPUT == '':
            print('If You Run Out Of Money, You Will Be In Debt If You Continue To Wager.')
            bet = int(input('Place Wager (No Floats i.e 1.00):$ '))
            cB = random.randint(1,100)
            cBet = cB
            pot += cBet
            print('CPU Bet Has Been Added To The Pot:','$',cBet)
            pot += bet
            money -= bet
            cMoney -= cBet
            uTotal += user_roll
            cTotal += cpu_roll
            print('Game Pot[',pot,']','Money Left[',money,']')
            print('User Rolled:',user_roll)
            print('User Score:',uTotal)
            continue
        elif INPUT == 'Fold' or 'fold':
            cTotal += cpu_roll
            print('User Score:',uTotal,'CPU Score:',cTotal)
            break
        
    if uTotal > 21:
        print(name,'-- Bust. CPU Wins!')
        print(name,'-- Money Lost:',pot)
    elif cTotal > 21:
        print('CPU Bust.',name,'Wins!')
        print(name,'-- Money Won:',pot)
    elif uTotal == 21:
        print(name,'Scored 21.',name,'Wins!')
        print(name,'-- Money Won:',pot)
    elif cTotal == 21:
        print('CPU Has Reached 21. CPU Wins!')
        print(name,'-- Money Lost:',pot)
    elif uTotal > cTotal:
        print(name,'Wins!')
        print(name,'-- Money Won!:',pot)
    elif uTotal < cTotal:
        print('CPU Wins!')
        print(name,'-- Money Lost:',pot)
    else:
        print("It's A Tie!")
        print('Total Pot Will Be Split By The Players')
     
roll_game()
c = input('Press Enter To End The Game: ')
if c == '':
    print('Have A Good Day.')
    sys.exit()
else:
    print('Not A Valid Input.')
    

    
    
    

        


    



