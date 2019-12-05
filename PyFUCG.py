import random
import sys

print('This python file is located at: ' + sys.path[0] + '\n\n\nFree Untitled Card Game\n\n\n\n')

class Card:
    def __init__(self,iname,iphysical,itechnical,iemotional,iphysicald,itechnicald,iemotionald,ihealth,iheal):
        self.name = iname
        self.physical = iphysical
        self.technical = itechnical
        self.emotional = iemotional
        self.physicald = iphysicald
        self.technicald = itechnicald
        self.emotionald = iemotionald
        self.health = ihealth
        self.healthmax = ihealth
        self.heal = iheal
        self.alive = True
        self.position = 0

    def __str__(self):
        return self.name

    def stats(self):
        return 'Card ' + str(self.position) + ' is ' + self.name + ' and has ' + str(self.health) + ' health of a maximum of ' + str(self.healthmax) + ' health and can heal for ' + str(self.heal) + ' when inactive.\n   ' + str(self.physical) + ' physical, ' + str(self.technical) + ' technical, and ' + str(self.emotional) + ' emotional attack ratings, ' + str(self.physicald) + ' physical, ' + str(self.technicald) + ' technical, and ' + str(self.emotionald) + ' emotional defense ratings.\n'
    
    def healing(self):
        if (self.health < self.healthmax)  & self.alive:
            self.health += self.heal
            if self.health > self.healthmax:
                healed = self.heal - (self.health - self.healthmax)
                self.health = self.healthmax
                return '   ' + self.name + ' healed for ' + str(healed) + " health, current health is at the maximum of " + str(self.healthmax) + ' health points.'
            return '   ' + self.name + ' healed for ' + str(self.heal) + " health, current health is at " + str(self.health) + ' out of ' + str(self.healthmax) + ' health points.'
        if self.alive:
            return '   ' + self.name + ' is at maximum health of ' + str(self.healthmax) + ' health points.'
        return '   ' + self.name + ' cannot heal as they are already dead.'

    def damage(self, idamage):
        if self.alive:
            self.health -= idamage
            if self.health <= 0:
                self.alive = False
                self.health = 0
                return str(idamage) + ' damage dealt, ' + self.name + ' is now dead.'
            return str(idamage) + ' damage dealt, ' + self.name + ' now has ' + str(self.health) + ' health left.'
        return self.name + ' is already dead you fool.'


class Die:
    def __init__(self,iname,isides):
        self.name = iname
        self.sides = isides
        self.sidevalues = []
        for i in range(1,isides+1):
            self.sidevalues.append(i)
        self.result = self.sidevalues[0]

    def __str__(self):
        return self.name
    
    # Method to set custom values for each side
    def sidevalueset(self,ivalues):
        self.sidevalues = ivalues
        self.sides = len(self.sidevalues)
    
    # Method to set the sides of the die and load default values into sidevalues
    def sideset(self,isides):
        self.sides = isides
        self.sidevalues = []
        for i in range(1,isides+1):
            self.sidevalues.append(i)

    # Method to roll the die, also stores the result
    def roll(self):
        self.result = int(self.sidevalues[random.randint(1,self.sides-1)])
        return self.result


def attack(attacker,defender,type):
    if attacker.alive:
        type(attacker,defender)
    else:
        print(attack.name() + ' is dead, how do you expect them to attack?')

def physical(attacker,defender):
    roll = die[attacker.physical].roll()
    if roll <= defender.physicald:
        result = 0
        print(str(attacker) + ' rolled ' + str(roll) + ' with a ' + str(die[attacker.physical]) + ' and was completely blocked by ' + str(defender))
    else:
        print(str(attacker) + ' rolled ' + str(roll) + ' with a ' + str(die[attacker.physical]) + ' : ' + defender.damage(roll - defender.physicald))

def technical(attacker,defender):
    roll = die[attacker.technical].roll()
    if roll <= defender.technicald:
        result = 0
        print(str(attacker) + ' rolled ' + str(roll) + ' with a ' + str(die[attacker.technical]) + ' and was completely blocked by ' + str(defender))
    else:
        print(str(attacker) + ' rolled ' + str(roll) + ' with a ' + str(die[attacker.technical]) + ' : ' + defender.damage(roll - defender.technicald))

def emotional(attacker,defender):
    roll = die[attacker.emotional].roll()
    if roll <= defender.emotionald:
        result = 0
        print(str(attacker) + ' rolled ' + str(roll) + ' with a ' + str(die[attacker.emotional]) + ' and was completely blocked by ' + str(defender))
    else:
        print(str(attacker) + ' rolled ' + str(roll) + ' with a ' + str(die[attacker.emotional]) + ' : ' + defender.damage(roll - defender.emotionald))

def swap(hand, card1, card2):
    if hand[card1].alive:
        tempcard = hand[card1]
        tempcard.position = hand[card2].position
        hand[card2].position = hand[card1].position
        hand[card1] = hand[card2]
        hand[card2] = tempcard
        print(hand[card2].name + ' has been swapped with ' + hand[card1].name + '.')
    else:
        print("Dead cards cannot be swapped.")

def discard(hand, dcard):
    if len(deck) > 0:
        ncard = random.randint(0,len(deck)-1)
        print(hand[dcard].name + ' has been discarded and replaced with with ' + deck[ncard].name + '.  ' + str(len(deck)-1))
        deck[ncard].position = hand[dcard].position
        hand[dcard] = deck[ncard]
        deck.pop(ncard)
    else:
        print('Deck has already been depleted.')


def compturn():
    print(handcomp[3].healing())
    print(handcomp[4].healing())
    if handcomp[0].alive | handcomp[1].alive | handcomp[2].alive :
        if handcomp[0].alive & handcomp[0].health < 8:
            if handcomp[0].health <  handcomp[3].health & handcomp[4].health <  handcomp[3].health:
                swap(handcomp,0,3)
                return
            if handcomp[0].health <  handcomp[4].health:
                swap(handcomp,0,4)
                return
        if handcomp[1].alive & handcomp[1].health < 8:
            if handcomp[1].health <  handcomp[3].health & handcomp[4].health <  handcomp[3].health:
                swap(handcomp,1,3)
                return
            if handcomp[1].health <  handcomp[4].health:
                swap(handcomp,1,4)
                return
        if handcomp[2].alive & handcomp[2].health < 8:
            if handcomp[2].health <  handcomp[3].health & handcomp[4].health <  handcomp[3].health:
                swap(handcomp,2,3)
                return
            if handcomp[2].health <  handcomp[4].health:
                swap(handcomp,2,4)
                return
        randomc = random.randint(0,2)
        while not handcomp[randomc].alive:
            randomc = random.randint(0,2)
        randomu = random.randint(0,2)
        while not handuser[randomu].alive:
            randomu = random.randint(0,2)
        if handcomp[randomc].physical >= handcomp[randomc].technical & handcomp[randomc].physical >= handcomp[randomc].emotional:
            attack(handcomp[randomc],handuser[randomu],physical)
        elif handcomp[randomc].technical >= handcomp[randomc].emotional:
            attack(handcomp[randomc],handuser[randomu],technical)
        else:
            attack(handcomp[randomc],handuser[randomu],emotional)      



def userturn():
    print(handuser[3].healing())
    print(handuser[4].healing())
    while handuser[0].alive | handuser[1].alive | handuser[2].alive:
        print("")
        for i in range(0,5):
            print(handuser[i].stats())
        action = ''
        print("")
        while action.lower() not in ['attack','swap','discard','pass']:
            action = input("Would you like to attack, swap, discard, or pass?: ")
        acard = dcard = attacktype = ''

        if action.lower() == 'attack':
            while acard not in ['0','1','2']:
                acard = input("Which card do you want to attack with?: ")
            while dcard not in ['0','1','2']:
                dcard = input("Which card do you want to attack?: ")
            while attacktype.lower() not in ['physical','technical','emotional']:
                attacktype = input("Which type of attack do you want to do?: ")
            print("")
            if attacktype.lower() == 'physical':
                attack(handuser[int(acard)],handcomp[int(dcard)],physical)
            if attacktype.lower() == 'technical':
                attack(handuser[int(acard)],handcomp[int(dcard)],technical)
            if attacktype.lower() == 'emotional':
                attack(handuser[int(acard)],handcomp[int(dcard)],emotional)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

        if action.lower() == 'swap':
            while acard not in ['0','1','2']:
                acard = input("Which active card do you want to swap with?: ")
            while dcard not in ['3','4']:
                dcard = input("Which inactive card do you want to swap with?: ")
            print("")
            swap(handuser,int(acard),int(dcard))

        if action.lower() == 'discard':
            while dcard not in ['3','4']:
                dcard = input("Which inactive card do you want to discard?: ")
            print("")
            discard(handuser,int(dcard))
        compturn()
        userturn()


# Game initialization stuff
deck = []
handcomp = []
handuser = []
knowcomp = []
knowuser = []
die = []
for i in range(0,13):
    if i < 2:
        die.append(Die('D' + str(2),2))
    else:
        die.append(Die('D' + str(i),i))

file = open(sys.path[0]+'\\cards.csv')
for aline in file:
    aline = aline.replace('\n','')
    line = aline.split(',')
    deck.append(Card(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8])))

for i in range(0,5):
    icard = random.randint(0,len(deck)-1)
    handuser.append(deck[icard])
    handuser[i].position = i
    deck.pop(icard)
    icard = random.randint(0,len(deck)-1)
    handcomp.append(deck[icard])
    handcomp[i].position = i
    deck.pop(icard)

# Game run
userturn()
if handuser[0].alive | handuser[1].alive | handuser[2].alive:
    print('Congrats, you win!')
else:
    print("Sorry, you lose.")
