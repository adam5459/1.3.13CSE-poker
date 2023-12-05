from functions import * 
import sys, random,time
game=True
rounds = ['PreGame','PreFlop',"Flop", "Turn", 'River',"Show Down"]
cRound = rounds[0]
firstRun = True
deck = create_deck()
players = []
cPot = 20
tempNameValue = []
foldedPlayers=[]
players_to_remove = []
amountPlayers = 0 

while game:
    random.shuffle(deck)
    roundWinner = None
    blind = 20
    
    showHand,close= True, True

    valueMapp = {'RoyalFlush':10, 'StraightFlush':9,"FourKind":8,"FullHouse":7,"Flsuh":6,"Straight":5,"ThreeKind":4,"TwoPair":3,"OnePair":2}


    while cRound == "PreGame":
        while amountPlayers <= 2:
            amountPlayers = int(input("how many people are playing?>  "))
            if amountPlayers <= 2:
                print('please find more players')
                continue
            
        
        for x in range(amountPlayers):
            hand = deck[:2]
            deck = deck[2:]
            startingMoney = 10000
            while True:
                name = input(f"What is player {x+1} name >   ")
                if name in tempNameValue:
                    print('\nPlease choose a uneque name\n')
                    continue
                break
            tempNameValue.append(name)
            cls()
            player = Player(x+1,hand,startingMoney,name)
            players.append(player)
            print(f"Player {x+1} had been added ")
            while showHand:
                rts = input('press x to see hand >  ')
                if rts.lower() != 'x': continue
                else:
                    cls()
                    player.showHand()
                    print(wrapper(f"\ncurrent money: {player.money}\n"))
                    input('type anything to close   > ')
                    cls()
                    if len(players) == amountPlayers:
                        if not checkPlayers(players, foldedPlayers):
                            cRound = 'PreFlop'  
                        else:
                            players[0].showPlayerWon()
                            game=False 
                            time.sleep(5) 
                            sys.exit()           
                    break
            

    while cRound == 'PreFlop':
        if not checkPlayers(players, foldedPlayers):
            pass 
        else:
            print(wrapper(f"plyer {players[0].name} wins ")) 
            game=False 
            sys.exit()  
        if not firstRun:
            for count,player in enumerate(players):
                while True:
                    print(F"player {player.num} ")
                    rts = input('press x to see hand >  ')
                    if rts.lower() != 'x': continue
                    else:
                        cls()
                        player.showHand()
                        print(wrapper(f"\ncurrent money: {player.money}\n"))
                        input('type anything to close   > ')
                        cls()
                        tempValueOne = False
                        break


        print(wrapper(f'Big Blind is {str(blind)} | raise is double the pot\n        Folding is GAME WIDE not per ROUND '))
        for number,player in enumerate(players[:]):
            while True:
                bhsc = input(f'player {number+1} would you like to raise(r)/fold(f)/hit(h)>  ')
                if bhsc.lower() in ['h','r','f']:
                    break
                else:
                    continue
            if bhsc.lower() == 'f':
                foldedPlayers.append(player)
                players.remove(player)
            if bhsc.lower() == 'r':
                raiseAmount = cPot * 2
                blind = raiseAmount
                cPot = raiseBet(player,raiseAmount,cPot)
            if bhsc.lower() =='h':
                cPot += blind
                player.money -= blind
            if player.money <= 1:
                players_to_remove.append(player)
        players = [player for player in players if player.money > 1]
        firstRun = False

        if not checkPlayers(players, foldedPlayers):
            cRound = 'Flop'  
        else:
            players[0].showPlayerWon()
            game=False
            time.sleep(5)
            sys.exit()              
    



    tempValueOne = True
    while cRound == "Flop":
        while tempValueOne:
            print(wrapper('Flop'))
            tableCards = deck[:3]
            deck = deck[3:]
            for count,player in enumerate(players):
                player.hand.extend(tableCards)
                while True:
                    print(F"player {player.num} ")
                    rts = input('press x to see hand >  ')
                    if rts.lower() != 'x': continue
                    else:
                        cls()
                        player.showHand()
                        print(wrapper(f"\ncurrent money: {player.money}\n"))
                        input('type anything to close   > ')
                        cls()
                        tempValueOne = False
                        break
        print(wrapper(f'current pot is {cPot}'))
        for number,player in enumerate(players):
            while True:
                bhsc = input(f'player {number+1} would you like to raise(r)/fold(f)/hit(h)>  ')
                if bhsc.lower() in ['h','r','f']:
                    break
                else:
                    continue
            if bhsc.lower() == 'f':
                foldedPlayers.append(player)
                players.remove(player)
            if bhsc.lower() == 'r':
                raiseAmount = cPot * 2
                cPot = raiseBet(player,raiseAmount,cPot)
            if bhsc.lower() =='h':
                cPot += blind
            if player.money <= 1:
                players_to_remove.append(player)
        players = [player for player in players if player.money > 1]

                
        if not checkPlayers(players, foldedPlayers):
            cRound = 'Turn'  
        else:
            players[0].showPlayerWon()
            game=False 
            time.sleep(5)
            sys.exit() 




    tempValueOne = True
    while cRound == "Turn":
        while tempValueOne:
            print(wrapper('Turn'))
            tableCards = deck[:1]
            deck = deck[1:]
            for count,player in enumerate(players):
                player.hand.extend(tableCards)
                while True:
                    print(F"player {player.num} ")
                    rts = input('press x to see hand >  ')
                    if rts.lower() != 'x': continue
                    else:
                        cls()
                        print(wrapper(f"\ncurrent money: {player.money}\n"))
                        player.showHand()
                        input('type anything to close   > ')
                        cls()
                        tempValueOne = False
                        break
        print(wrapper(f'current pot is {cPot}'))
        for number,player in enumerate(players):
            while True:
                bhsc = input(f'player {number+1} would you like to raise(r)/fold(f)/hit(h)>  ')
                if bhsc.lower() in ['h','r','f']:
                    break
                else:
                    continue
            if bhsc.lower() == 'f':
                foldedPlayers.append(player)
                players.remove(player)
            if bhsc.lower() == 'r':
                raiseAmount = cPot * 2
                cPot = raiseBet(player,raiseAmount,cPot)
            if bhsc.lower() =='h':
                cPot += blind
            if player.money <= 1:
                players_to_remove.append(player)
        players = [player for player in players if player.money > 1]


        if not checkPlayers(players, foldedPlayers):
            cRound = 'River'  
        else:
            players[0].showPlayerWon()
            game=False 
            time.sleep(5)
            sys.exit() 


    tempValueOne = True
    while cRound == "River":
        while tempValueOne:
            print(wrapper('River'))
            tableCards = deck[:1]
            deck = deck[1:]
            for count,player in enumerate(players):
                player.hand.extend(tableCards)
                while True:
                    print(F"player {player.num} ")
                    rts = input('press x to see hand >  ')
                    if rts.lower() != 'x': continue
                    else:
                        cls()
                        print(wrapper(f"\ncurrent money: {player.money}\n"))
                        player.showHand()
                        input('type anything to close   > ')
                        cls()
                        tempValueOne = False
                        break
        print(wrapper(f'current pot is {cPot}'))
        for number,player in enumerate(players):
            while True:
                bhsc = input(f'player {number+1} would you like to raise(r)/fold(f)/hit(h)>  ')
                if bhsc.lower() in ['h','r','f']:
                    break
                else:
                    continue
            if bhsc.lower() == 'f':
                foldedPlayers.append(player)
                players.remove(player)
            if bhsc.lower() == 'r':
                raiseAmount = cPot * 2
                cPot = raiseBet(player,raiseAmount,cPot)
            if bhsc.lower() =='h':
                cPot += blind
            if player.money <= 1:
                players_to_remove.append(player)
        players = [player for player in players if player.money > 1]

        if not checkPlayers(players, foldedPlayers):
            cRound = 'ShowDown'  
        else:
            print(wrapper(f"plyer {players[0].num} wins "))
            game=False
            time.sleep(5)
            sys.exit() 


    while cRound == "ShowDown" and len(players) > 1:
        playerFinalScore= {}
        HighCardPlayers = {}
        for player in players:
            if royalFlush(player.hand):
                playerFinalScore[player] = 10
            elif straitFlush(player.hand):
                playerFinalScore[player] = 9
            elif fourOfKind(player.hand):
                playerFinalScore[player] = 8
            elif fullHouse(player.hand):
                playerFinalScore[player] = 7
            elif flush(player.hand):
                playerFinalScore[player] = 6
            elif strait(player.hand):
                playerFinalScore[player] = 5
            elif threeKind(player.hand):
                playerFinalScore[player] = 4
            elif twoPair(player.hand):
                playerFinalScore[player] = 3
            elif onePair(player.hand):
                playerFinalScore[player] = 2
            else:
                HighCardPlayer = highCard(player)
                HighCardPlayers[player] = HighCardPlayer
                
        if len(HighCardPlayers) <= 0 or len(HighCardPlayers)<len(playerFinalScore):
            sortedplayers = sorted(playerFinalScore.items(), key=lambda item:item[1], reverse=True)
            roundWinner = sortedplayers[0][0]
            roundWinner.money += cPot
            print(wrapper(f"player {roundWinner.name} won with a pot of {cPot}"))
            cPot = 0
            if not checkPlayers(players, foldedPlayers):
                cRound = 'PreFlop'  
            else:
                players[0].showPlayerWon()
                game=False
            continue
        else:
            sortedplayers = dict(sorted(HighCardPlayers.items(), key=lambda item:item[1], reverse=True))
            roundWinner = list(sortedplayers.keys())[0]
            roundWinner.money += cPot
            print(wrapper(f"player {roundWinner.num} won with a pot of {cPot}"))
            cPot = 0
            if not checkPlayers(players, foldedPlayers):
                cRound = 'PreFlop'  
            else:
                players[0].showPlayerWon() 
                game=False
                time.sleep(5)
                sys.exit() 
            continue
            
        if len(players) >1:
            break
            

  

