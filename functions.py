import random
from itertools import combinations



def create_deck():
    ranks = ['2','3','4','5','6','7','8','9','10','A','J',"Q",'K',]
    suits = ['Spades','Clubs','Diamonds','Hearts']
    deck = [{'rank':rank, 'suit':suit}for rank in ranks for suit in suits ] 
    random.shuffle(deck)
    return deck

def strait(hand):
    value_mapping = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    values = [value_mapping[card['rank']] for card in hand]
    values.sort()
    for i in range(len(values) - 1):
        if values[i] + 1 != values[i + 1]:
            return False
    return True


def royalFlush(hand):
    royalFlushEx = {'10', 'J', 'Q', 'K', 'A'}
    for fiveCards in combinations(hand, 5):
        suits = {card['suit'] for card in hand}
        ranks = {card['rank']for card in fiveCards}
        if ranks == royalFlushEx and len(suits) == 1:
            return True

    return False

def straitFlush(hand):
    suit_count = {}
    for card in hand:
        suit=card['suit']
        if suit in suit_count:
            suit_count[suit] += 1
        else:
            suit_count[suit] = 1
    if any(count >= 5 for count in suit_count.values()):
        return strait(hand)
    return False

def fourOfKind(hand):
    rank_count = {}
    for card in hand:
        rank = card['rank']
        if rank in rank_count:
            rank_count[rank]+=1
        else:
            rank_count[rank] = 1
    return any(count ==4 for count in rank_count.values())
def fullHouse(hand):
    for card in hand:
        if hand.count(card['rank'])==3:
            for other_card in hand:
                if other_card['rank'] != card['rank'] and hand.count(other_card['rank'])==2: 
                    return True
    return False
def flush(hand):
    suit_set = {}
    for card in hand:
        suit = card['suit']
        if suit in suit_set:
            suit_set[suit] += 1
        else: 
            suit_set[suit] =1  
    return any(count >= 5 for count in suit_set.values())

def threeKind(hand):
    ranks = {}
    for card in hand:
        rank = card['rank']
        if rank in ranks:
            ranks[rank]+= 1
        else:
            ranks[rank]=1
    return any(count==3 for count in ranks.values())


def twoPair(hand):
    rank_check = {}
    for card in hand:
        rank = card['rank']
        if rank in rank_check:
            rank_check[rank]+=1
        else:
            rank_check[rank]=1
    amountOfPair = sum(count==2 for count in rank_check.values())
    return amountOfPair == 2

def onePair(hand):
    rank_check = {}
    for card in hand:
        rank = card['rank']
        if rank in rank_check:
            rank_check[rank]+=1
        else:
            rank_check[rank]=1
    return any(count==2 for count in rank_check.values())
def highCard(player):
    value_mapping = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    values = [value_mapping[card['rank']] for card in player.hand]
    values.sort()
    return values


def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def wrapper(x):
    return f'''
------------------------------------------
    {x}
------------------------------------------ 
    '''

def checkPlayers(players, foldedPlayers):
    if len(players) == 1 or len(foldedPlayers) == len(players)-1:
        return True
    for player in players:
        if player.money == 0:
            players.remove(player)
            continue
    return False



class Player:
    def __init__(self,num, hand, money, name):
        self.hand = hand
        self.money = money
        self.num = num
        self.name = name
    def showPlayerWon(self):
        print(wrapper(f"player {self.name} won "))

    def showHand(self):
        print(f"Player {self.num} Hand: \n")
        for card in self.hand:
            print(f" {card['rank']} of {card['suit']}\n")
        
    def showMoney(self):
        print(f"player {self.num} money : ${self.money}")
    
def check(player):
    print(wrapper(f"player {player.num} check"))

def raiseBet(player, amount, pot):
    pot += amount
    player.money -= amount
    return pot

def PlayerCheck(players):
    return len(players) >= 1


