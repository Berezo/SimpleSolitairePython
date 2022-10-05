import random
import game, rules

def main():
    gameNew = game.Game()
    while not rules.haveWon(gameNew):
        gameNew.getBoard()
        ans = rules.getInstruction()
        rules.doInstruction(ans, gameNew)
    gameNew.getBoard()
    print('Congratulations! You win!')

if __name__ == '__main__':
    main()