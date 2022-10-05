import random
import rules

class Game:
    deck = [('♠️', 1), ('♠️', 2), ('♠️', 3), ('♠️', 4), ('♠️', 5), ('♠️', 6), ('♠️', 7), ('♠️', 8), ('♠️', 9), ('♠️', 10), ('♠️', 11), ('♠️', 12), ('♠️', 13),
    ('♣️', 1), ('♣️', 2), ('♣️', 3), ('♣️', 4), ('♣️', 5), ('♣️', 6), ('♣️', 7), ('♣️', 8), ('♣️', 9), ('♣️', 10), ('♣️', 11), ('♣️', 12), ('♣️', 13),
    ('♥️', 1), ('♥️', 2), ('♥️', 3), ('♥️', 4), ('♥️', 5), ('♥️', 6), ('♥️', 7), ('♥️', 8), ('♥️', 9), ('♥️', 10), ('♥️', 11), ('♥️', 12), ('♥️', 13),
    ('♦️', 1), ('♦️', 2), ('♦️', 3), ('♦️', 4), ('♦️', 5), ('♦️', 6), ('♦️', 7), ('♦️', 8), ('♦️', 9), ('♦️', 10), ('♦️', 11), ('♦️', 12), ('♦️', 13)]

    upDeck = [('♠️', 1), ('♠️', 2), ('♠️', 3), ('♠️', 4), ('♠️', 5), ('♠️', 6)]
    upDeckReveal = len(upDeck) - 2

    rows = {1: [[('♥️', 7)], 6], 2: [[], 5], 3: [[], 4], 4: [[], 3], 5: [[], 2], 6: [[], 1], 7: [[], 0]}

    sendSpade = 0
    sendClub = 0
    sendHeart = 0
    sendDiamond = 0


    def __init__(self):
        random.shuffle(self.deck)
        self.rows[1][0] = self.deck[0:7]
        self.rows[2][0] = self.deck[7:13]
        self.rows[3][0] = self.deck[13:18]
        self.rows[4][0] = self.deck[18:22]
        self.rows[5][0] = self.deck[22:25]
        self.rows[6][0] = self.deck[25:27]
        self.rows[7][0] = self.deck[27:28]
        self.upDeck = self.deck[28:]
        self.upDeckReveal = len(self.upDeck)
    
    def flip(self):
        if self.upDeckReveal == 0:
            self.upDeckReveal = len(self.upDeck)
        else:
            self.upDeckReveal -= 1
    
    def bring(self, rowIndex):
        '''
            Check condition, if true, take the element and append to the corresponding row, If false, print invalid move
        '''
        if self.upDeckReveal < len(self.upDeck):
            if len(self.rows[rowIndex][0]) == 0 or rules.isConnectable(self.rows[rowIndex][0][-1], self.upDeck[self.upDeckReveal]):
                self.rows[rowIndex][0].append(self.upDeck.pop(self.upDeckReveal))
            else:
                print('Invalid move.')
        else:
            print('There is nothing on the upDeck.')
    
    def move(self, moveFrom, moveLen, moveTo):
        '''
        Check condition, if true, take part of the list that is moveLen long from the end of the row moveFrom. Move the segment to the end of the row moveTo. After that, if no card revealed in the original row, reveal the last card of the row.
        If false, print invalid move
        '''

        if len(self.rows[moveTo][0]) == 0 or rules.isConnectable(self.rows[moveTo][0][-1], self.rows[moveFrom][0][-moveLen]):
            self.rows[moveTo][0] += self.rows[moveFrom][0][-moveLen:]
            self.rows[moveFrom][0] = self.rows[moveFrom][0][:-moveLen]
            if len(self.rows[moveFrom][0]) <= self.rows[moveFrom][1]:
                self.rows[moveFrom][1] = len(self.rows[moveFrom][0]) - 1
        else:
            print('Invalid move.')

    def send(self, rowIndex):
        '''
        Send the last card of the row up if applicable. If the input is 0, send the card from updeck Otherwise print invalid move
        '''
        if rowIndex == 0:
            if self.upDeck[self.upDeckReveal][0] == '♠️':
                if self.upDeck[self.upDeckReveal][1] - 1 == self.sendSpade:
                    self.upDeck.pop(self.upDeckReveal)
                    self.sendSpade += 1
                else:
                    print('Invalid move')
            elif self.upDeck[self.upDeckReveal][0] == '♣️':
                if self.upDeck[self.upDeckReveal][1] - 1 == self.sendClub:
                    self.upDeck.pop(self.upDeckReveal)
                    self.sendClub += 1
                else:
                    print('Invalid move')
            elif self.upDeck[self.upDeckReveal][0] == '♥️':
                if self.upDeck[self.upDeckReveal][1] - 1 == self.sendHeart:
                    self.upDeck.pop(self.upDeckReveal)
                    self.sendHeart += 1
                else:
                    print('Invalid move')
            elif self.upDeck[self.upDeckReveal][0] == '♦️':
                if self.upDeck[self.upDeckReveal][1] - 1 == self.sendDiamond:
                    self.upDeck.pop(self.upDeckReveal)
                    self.sendDiamond += 1
                else:
                    print('Invalid move')
        elif rowIndex <= 7:
            if self.rows[rowIndex][0][-1][0] == '♠️':
                if self.rows[rowIndex][0][-1][1] - 1 == self.sendSpade:
                    self.rows[rowIndex][0].pop(len(self.rows[rowIndex][0]) - 1)
                    self.sendSpade += 1
                else:
                    print('Invalid move')
            elif self.rows[rowIndex][0][-1][0] == '♣️':
                if self.rows[rowIndex][0][-1][1] - 1 == self.sendClub:
                    self.rows[rowIndex][0].pop(len(self.rows[rowIndex][0]) - 1)
                    self.sendClub += 1
                else:
                    print('Invalid move')
            elif self.rows[rowIndex][0][-1][0] == '♥️':
                if self.rows[rowIndex][0][-1][1] - 1 == self.sendHeart:
                    self.rows[rowIndex][0].pop(len(self.rows[rowIndex][0]) - 1)
                    self.sendHeart += 1
                else:
                    print('Invalid move')
            elif self.rows[rowIndex][0][-1][0] == '♦️':
                if self.rows[rowIndex][0][-1][1] - 1 == self.sendDiamond:
                    self.rows[rowIndex][0].pop(len(self.rows[rowIndex][0]) - 1)
                    self.sendDiamond += 1
                else:
                    print('Invalid move')
        else:
            print('Invalid move.')

    def getCard(self, cardDeck):
        '''
	        Turn card in deck into graphics
	    '''
        if cardDeck[1] == 1:
            return (cardDeck[0] + "A")
        elif cardDeck[1] == 11:
            return (cardDeck[0] + "J")
        elif cardDeck[1] == 12:
            return (cardDeck[0] + "Q")
        elif cardDeck[1] == 13:
            return (cardDeck[0] + "K")
        else:
            return (cardDeck[0] + str(cardDeck[1]))

    def getRow(self, rowIndex):
        '''
            Turn row of the deck into graphics
        '''
        print(str(rowIndex) + '  ', end="")
        if len(self.rows[rowIndex][0]) == 0:
            print('O')
        else:
            while self.rows[rowIndex][1] >= len(self.rows[rowIndex][0]):
                self.rows[rowIndex][1] -= 1
            while self.rows[rowIndex][1] < 0:
                self.rows[rowIndex][1] += 1
            for i in range(self.rows[rowIndex][1]):
                print('[] ', end="")
            for card in self.rows[rowIndex][0][self.rows[rowIndex][1]:]:
                print(self.getCard(card) + ' ', end="")
        print()
    
    def getBoard(self):
        '''
            Turn rows of the deck into board graphics
        '''
        print('♠️: ' + str(self.sendSpade) + '    ', end = '')
        print('♣️: ' + str(self.sendClub) + '    ', end = '')
        print('♥️: ' + str(self.sendHeart) + '    ', end = '')
        print('♦️: ' + str(self.sendDiamond))
        print()
        if self.upDeckReveal == 0:
            print('O  ', end = "")
        else:
            print('[]  ', end = "")
        if self.upDeckReveal == len(self.upDeck):
            print('')
        else:
            print(self.getCard(self.upDeck[self.upDeckReveal]))
        self.getRow(1)
        self.getRow(2)
        self.getRow(3)
        self.getRow(4)
        self.getRow(5)
        self.getRow(6)
        self.getRow(7)
      