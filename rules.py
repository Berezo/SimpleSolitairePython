import os

def haveWon(game):
    '''
	    Check if you have won, return true if you have, false otherwise
	'''
    return (game.sendSpade == 13 and game.sendClub == 13 and game.sendDiamond == 13 and game.sendHeart == 13)
    
def isDifferent(cardA, cardB):
    '''
        Check if cardA and cardB are different colors, return true if different, false if same
    '''
    if cardA[0] == '♠️' or cardA[0] == '♣️':
        return(cardB[0] == '♥️' or cardB[0] == '♦️')
    else:
        return(cardB[0] == '♠️' or cardB[0] == '♣️')
    
def isOneLarger(cardA, cardB):
    '''
        Check if cardA is larger than cardB by one
    '''
    return(cardA[-1] - cardB[-1] == 1)

def isConnectable(cardA, cardB):
    '''
    Check if the cardB can be connected to the cardA (different color and cardA one larger)
    '''
    return ((len(cardA) == 0) or (isDifferent(cardA, cardB) and isOneLarger(cardA, cardB)))

def getInstruction():
    print('f: flip the top deck\nb: bring the card down from the top deck\nm: move cards between rows\ns: send a card to the finishing slot')
    ans = input('Press a key and Enter: ')
    while ans not in ['f','b','m','s']:
        print('\033[A                                                 \033[A\n\033[A                                                 \033[A\n\033[A                                                 \033[A\n\033[A                                                 \033[A\n\033[A                                                 \033[A')
        print('f: flip the top deck\nb: bring the card down from the top deck\nm: move cards between rows\ns: send a card to the finishing slot')
        ans = input('Wrong key! Press a key and Enter: ')
    return ans  

def doInstruction(ans, game):
    if ans == 'f':
        os.system('cls')
        game.flip()
    elif ans == 'b':
        rowIndex = input('Which row do you want to bring the card to? corresponding row 1-7: ')
        while rowIndex not in ['1','2','3','4', '5', '6', '7']:
            print('\033[A                                                                                          \033[A')
            rowIndex = input('Wrong key! Which row do you want to bring the card to? corresponding row 1-7: ')
        os.system('cls')
        game.bring(int(rowIndex))
    elif ans == 'm':
        rowFrom = input('Which row do you want to move from? corresponding row 1-7: ')
        while rowFrom not in ['1','2','3','4', '5', '6', '7']:
            print('\033[A                                                                                          \033[A')
            rowFrom = input('Wrong key! Which row do you want to move from? corresponding row 1-7: ')
        try:
            cardNum = int(input('How many cards do you want to move? A number: '))
            if cardNum >= 1 and cardNum <= (len(game.rows[int(rowFrom)][0]) - game.rows[int(rowFrom)][1]):
                rowTo = input('Which row do you want move the cards to? corresponding row 1-7: ')
                while rowTo not in ['1','2','3','4', '5', '6', '7']:
                    print('\033[A                                                                                          \033[A')
                    rowTo = input('Wrong key! Which row do you want move the cards to? corresponding row 1-7: ')
                os.system('cls')
                game.move(int(rowFrom), cardNum, int(rowTo))
            else:
                os.system('cls')
                print('There are only ' + str(len(game.rows[int(rowFrom)][0]) - game.rows[int(rowFrom)][1]) + ' moveable cards.')
        except:
            os.system('cls')
            print('Wrong key! How many cards do you want to move?')
    elif ans == 's':
        rowIndex = input('Which row do you want to send from? 0: top deck; 1-7 corresponding row: ')
        while rowIndex not in ['0','1', '2', '3', '4', '5', '6', '7']:
            print('\033[A                                                                                          \033[A')
            rowIndex = input('Wrong key! Which row do you want to send from? 0: top deck; 1-7 corresponding row: ')
        os.system('cls')
        game.send(int(rowIndex))