#import random module
import random

#list of input for the game
play = ['Rock', 'Paper', 'Scissors']

playerScore = 0
computerScore = 0
game = True

#the main game
while game == True:
    print('Player: Enter R-Rock, P-Paper or S-Scissors\n')
    
    x = True
    playerValue = ''
    #request and process player input
    while x == True:
        value = input()
        if(value not in ['r', 'R', 'p', 'P', 's', 'S']):
            print("Invalid input")
        else:
            if(value == 'r' or value == 'R'):
                playerValue = 'Rock'
            if(value == 'p' or value == 'P'):
                playerValue = 'Paper'
            if(value == 's' or value == 'P'):
                playerValue = 'Scissors'
            x = False
    
    #AI value using random.choice        
    computerValue = random.choice(play)
    
    set = True
    #To check if the values are not equal
    if(playerValue == computerValue):
        set = False
    
    #check for the winner per point    
    if(set == True):
        if(playerValue == 'Rock' and computerValue == 'Scissors'):
            playerScore += 1
        elif(playerValue == 'Paper' and computerValue == 'Rock'):
            playerScore += 1
        elif(playerValue == 'Scissors' and computerValue == 'Paper'):
            playerScore += 1
        elif(computerValue == 'Rock' and playerValue == 'Scissors'):
            computerScore += 1
        elif(computerValue == 'Paper' and playerValue == 'Rock'):
            computerScore += 1
        elif(computerValue == 'Scissors' and playerValue == 'Paper'):
            computerScore += 1
    
    print('Score: \n Player: ', playerScore, ' AI: ', computerScore)
    if(playerScore > 1 or computerScore > 1):
        game = False
        
    #print game result
    if(playerScore > 1):
        print('Player wins!\n Play again')
    elif(computerScore > 1):
        print('AI wins!\n Play again')
    