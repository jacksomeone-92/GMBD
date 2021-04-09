# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:01:04 2020

@author: Nicolas G
"""

#import exit in order to end main() if the user decides to end the game
#from sys import exit

#define the function for linear congruences
def linear_congruence(xi):
    """ Function to calculate linear congruences value and computer bet """
    a = 22695477
    b = 1
    m = 2**32
    xi_plus_1 = (a * xi + b) % m
    if xi_plus_1 <= 2**31:
        comp_move = 0
    else: 
        comp_move = 1
    return comp_move, xi_plus_1


#1. Create an opening message
      
print("Welcome to Human Behavior Prediction Game inspired by Prof. Manoel Gadi and (partially coded) by Nicolas")

select_difficulty = int(input("Choose the type of game (1: Easy; 2: Difficult): "))

moves = int(input("Enter the number of moves: "))

MS = 0
PS = 0
xi = 1234

throw00 = []
throw01 = []
throw10 = []
throw11 = []


if select_difficulty == 1:
    for turn in range(moves):
        #print(turn)
        player_move = int(input("Choose your move number %s (0 or 1): " % (turn+1)))
        computer_move,xi = linear_congruence(xi)
        if player_move == computer_move:
            MS = MS + 1
            print("player = %d machine = %d - Computer wins!" % (player_move, computer_move))
            print("You: %d Computer: %d" % (PS, MS))
        else:
            PS = PS + 1
            print("player = %d machine = %d - Player wins!" % (player_move, computer_move))
            print("You: %d Computer: %d" % (PS, MS))
            
        print('PLAYER: ' + '*'*PS)
        print('MACHINE: ' + '*'*MS)

    if turn == moves and PS > MS:
        print("Easy game is over, final score: player %d - %d computer - You won!" % (PS, MS))
    elif PS == MS:
        print("Easy game is over, final score: player %d - %d computer - it is a draw!" % (PS, MS))
    else:
        print("Easy game is over, final score: player %d - %d computer - the COMPUTER won!" % (PS, MS))
            
    
#for-loop if player selects "difficult" as game setting
if select_difficulty == 2:
    player_move_dif = [] #create an empty list out of your for-loop
    player_previous_move = None 
        
    
for turn in range(moves): 

    check = 1 #check variable is only to see where the computer "gets" 
    #the move decision, not relevant for the loopt itself
    if turn <= 1: #since turn starts at 0 (at the first move)
            computer_move,xi = linear_congruence(xi)
            check = 'turn smaller than 2'
           
    ############################
    # you just need if and else here, because turn can only be <=1 or >1        
    ####################
            
    else:
        
        if player_previous_move == 0  and len(throw10) > len(throw00):
                computer_move = 1
                check = 'a'
        elif player_previous_move == 0 and len(throw10) < len(throw00):
                computer_move = 0
                check = 'b'
        elif player_previous_move == 1 and len(throw11) > len(throw01):
                computer_move = 1
                check = 'c'
        elif player_previous_move == 1 and len(throw11) < len(throw01):
                computer_move = 0
                check = 'd'
        else:
            computer_move,xi = linear_congruence(xi)
            check = 'else1'
        
    #conditions for player move
        
    #########################
    # changing turn ==0 to turn <=1, you need the first 2 moves by the human for the machine to learn
    ###########################        
        
    if turn <= 1: #first move has no previous one
        player_move_dif.append(input("Choose your move number %s (0 or 1):" % (turn+1)))
        player_move_2 = int(player_move_dif[turn])
        player_previous_move = None #since in the first move there cannot be a previous move from the player
    elif turn > 1:
        player_move_dif.append(input("Choose your move number %s (0 or 1):" % (turn+1)))
        player_move_2 = int(player_move_dif[turn])
        player_previous_move = int(player_move_dif[turn-1])
    else:
        player_move_dif.append(input("Choose your move number %s (0 or 1):" % (turn+1)))
        player_move_2 = int(player_move_dif[turn])
        player_previous_move = int(player_move_dif[turn-1])
    #if statements to append player moves to lists which are used for conditions
    #in computer move loop. Waiting for feedback from the professor what to do with
    #the very first move from the player (since in the firstmove there is no previous move)
    #to decide to which list (eg. throw00 etc.) to append to
    if player_move_2 == 0:
        if player_previous_move == 0:
            throw00.append(player_move_2)
        elif player_previous_move == 1:
            throw01.append(player_move_2)
    elif player_move_2 == 1:
        if player_previous_move == 0:
            throw10.append(player_move_2)
        elif player_previous_move == 1:
            throw11.append(player_move_2)
            
    if player_move_2 == computer_move:
       MS = MS + 1
       print("player = %d machine = %d - Computer wins!" % (int(player_move_2), computer_move)) #pick the last move fr1om play_move_dif
       print("You: %d Computer: %d" % (PS, MS))
    else:
       PS = PS + 1
       print("player = %d machine = %d - Player wins!" % (int(player_move_2), computer_move)) #pick the last move from play_move_dif
       print("You: %d Computer: %d" % (PS, MS))
    
    print('PLAYER: ' + '*'*PS)
    print('COMPUTER: ' + '*'*MS)
    
    if turn == moves and PS > MS:
        print("Difficult game is over, final score: player %d - %d computer - You won!" % (PS, MS))
    elif PS == MS:
        print("Difficult game is over, final score: player %d - %d computer - it is a draw!" % (PS, MS))
    else:
        print("Difficult game is over, final score: player %d - %d computer - the COMPUTER won!" % (PS, MS))
            
    

                
