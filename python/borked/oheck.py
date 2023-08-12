from random import shuffle
import json

class Card:
    def __init__(self, suit: int, value: int):
        self.suit = suit
        self.value = value
    def __str__(self):
        match self.value:
            case 0:
                key = "A"
            case 10:
                key = "J"
            case 11:
                key = "Q"
            case 12:
                key = "K"
            case _:
                key = str(self.value)
        match self.suit:
            case 0:
                color = "\033[37m"
                suit = "♠️"
            case 1:
                color = "\033[91m"
                suit = "♥️"
            case 2:
                color = "\033[91m"
                suit = "♦️"
            case 3:
                color = "\033[37m"
                suit = "♣️"
        return f"{color}{key}{suit}\033[0m"
    def __eq__(self, other):
        if other is None:
            return False
        return [self.suit, self.value] == [other.suit, other.value]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for value in range(13):
                self.cards.append(Card(suit, value))
    def shuffle(self):
        shuffle(self.cards)
    def __str__(self):
        return str(self.cards)

class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0
        self.hand = []
        self.latestBid = 0
        self.tricks = 0
    def addCard(self, card):
        self.hand.append(card)
        cardTracker.update(card, self.id)
    def bid(self, bid):
        self.latestBid = bid
    def clearHand(self):
        for card in self.hand:
            cardTracker.update(card, -1)
        self.hand = []
    def playCard(self, index, pot):
        assert index < len(self.hand)
        card = self.hand.pop(index)
        cardTracker.update(card, -2)
        pot.update(self.id, card)
    def leadCard(self, index):
        assert index < len(self.hand)
        card = self.hand.pop(index)
        cardTracker.update(card, -2)
        pot.clear() #pot is cleared when a new trick is started
        pot.update(self.id, card)
        pot.update("lead", card)
    def prettyHand(self) -> str:
        out = ""
        for i in self.hand:
            out += str(i) + " "
        return out
    def __str__(self) -> str:
        return "Player " + str(self.id) + \
            ":\n    Hand: " + self.prettyHand() + \
            "\n    Score: " + str(self.score) + \
            "\n" + "    Latest Bid: " + str(self.latestBid) + "\n"

#for keeping track of card locations
#key:
#  -1: in deck
# 0+: in player's hand
# -2: played
class CardTracker:
    def __init__(self):
        self.cards = {}
        for i in Deck().cards:
            self.cards[str(i)] = -1
    def __str__(self):
        out = ""
        for i in self.cards:
            out += str(i) + ": " + str(self.cards[i]) + "\n"
        return out
    def update(self, card, location):
        self.cards[str(card)] = location
    def getCardLocation(self, card):
        return self.cards[str(card)]
    def selfCheck(self):
        assert len(self.cards) == 52
        for i in self.cards:
            assert self.cards[i] >= -2
        return True

class Pot:
    def __init__(self):
        self.pot = {}
        self.pot["lead"] = None
    def __str__(self):
        out = ""
        for i in pot.pot.keys():
            if i == "lead":
                continue
            out += str(pot.pot[i]) + " "
        return out + "\n"
    def update(self, player: Player, card: Card):
        self.pot[player] = card
    def getPot(self):
        return self.pot
    def clear(self):
        self.pot = {}
        self.pot["lead"] = None
    def selfCheck(self):
        assert len(self.pot) <= 52
        return True

def dealCards(cards, players, deck):
    assert cards * len(players) <= 52
    offset = 0
    for i in range(len(players)):
        for j in range(cards):
            players[i].addCard(deck[offset])
            offset += 1

def trickWinner(pot: Pot) -> Player:
    """Returns the id of the player who won the trick"""
    leadSuit = pot.pot["lead"].suit
    #if spades were played, treat them as the lead suit
    if any([i.suit == 0 for i in pot.pot.values()]):
        leadSuit = 0
    #the highest card of the lead suit wins
    highestCard = None
    for i in pot.pot.values():
        if i.suit == leadSuit:
            if highestCard is None or i.value > highestCard.value:
                highestCard = i
    #return the player who played the highest card
    for i in pot.pot.keys():
        if pot.pot[i] == highestCard:
            for j in players:
                if j.id == i:
                    return j

def reorderPlayers(players: list, index: int):
    """Reorders the players list so that the specified index is first, and the rest are in order"""
    return players[index:] + players[:index]

def printScores(players: list):
    """Prints the scores of all players"""
    out = ""
    for i in players:
        out += "Player " + str(i.id) + ": " + str(i.score) + "\n"
    return out



cardTracker = CardTracker()
players = []
pot = Pot()
deck = Deck()
deck.shuffle()
leadPlayer = None
for i in range(4):
    players.append(Player(i))

#main game loop
roundNumber = 0
while len(players)-roundNumber > 0:
    assert len(deck.cards) == 52
    assert cardTracker.selfCheck()
    assert pot.selfCheck()
    players = reorderPlayers(players, roundNumber % len(players))
    dealCards(len(players)-roundNumber, players, deck.cards)
    #bid phase
    for i in players:
        print(i.prettyHand())
        #first player to bid cycles each round
        i.bid(int(input("Player " + str(i.id) + " bid: ")))

    print("\n\n")
    #play phase
    for j in range(len(players[0].hand)):
        #lead subphase
        if j == 0:
            #on the first trick, player 1 leads
            leadPlayer = players[roundNumber % len(players)]
        else:
            #lead goes to winner of previous trick
            leadPlayer = trickWinner(pot)

        print("\nHand: " + leadPlayer.prettyHand())
        leadPlayer.leadCard(int(input("Player " + str(leadPlayer.id) + " lead: ")))
        print(cardTracker)


        #follow subphase
        for i in players:
            if i == leadPlayer:
                continue #lead player already played
            #first player to play cycles each round
            print("\nHand: " + i.prettyHand())
            print("Pot: " + str(pot))
            while True:
                index = int(input("Player " + str(i.id) + " play: "))
                if pot.pot["lead"].suit != i.hand[index].suit and any([k.suit == pot.pot["lead"].suit for k in i.hand]):
                    # raise Exception("You must follow suit")
                    print("You must follow suit")
                    continue
                break
            i.playCard(index, pot)
            print(cardTracker)

        trickWinner(pot).tricks += 1
        print("Trick winner: " + str(trickWinner(pot).id))

    #scoring phase
    for i in players:
        if i.latestBid == i.tricks:
            i.score += 10 + i.latestBid
        else:
            i.score += i.tricks
    print(printScores(players))


    #cleanup phase
    for i in players:
        print(i)
        i.clearHand()
        i.tricks = 0
    roundNumber += 1
