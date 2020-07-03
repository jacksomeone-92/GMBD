# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:01:04 2020

@author: Nicolas G
"""

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
#throw00 = countofthenumberoftimesthehumanplayerchose0giventhatinthepreviousbidhis/herbidwas0
#throw01 = countofthenumberoftimesthehumanplayerchose0giveninthebidprevioushis/herbidwas1,
#throw10 = countofthenumberoftimesthehumanplayerchose1giventhathis/herpreviousbidwas0,
#throw11 = countofthenumberoftimesthehumanplayerchose1givenhis/herpreviousbidwas1.


if select_difficulty == 1:
    for turn in range(moves):
        #print(turn)
        player_move = int(input("Choose your move number %s (0 or 1):" % (turn+1)))
        computer_move,xi = linear_congruence(xi)
        if player_move == computer_move:
            MS = MS + 1
            print("player = %d machine = %d - Machine wins!" % (player_move, computer_move))
            print("You: %d Computer: %d" % (PS, MS))
        else:
            PS = PS + 1
            print("player = %d machine = %d - Player wins!" % (player_move, computer_move))
            print("You: %d Computer: %d" % (PS, MS))
            
        print('PLAYER: ' + '*'*PS)
        print('MACHINE: ' + '*'*MS)

    if turn == moves and PS > MS:
        print("The game has ended, you win!")
    elif PS == MS:
        print("The game has ended, it is a draw!")
    else:
        print("the game has ended, the machine wins!")

#loop if player selects "difficult" as game setting
if select_difficulty == 2:
    for turn in range(moves):
        #print(turn)
        player_move = int(input("Choose your move number %s (0 or 1):" % (turn+1)))
        #define the previous move of the player
        player_previous_move = (player_move-1)
        
        #define computer behavior depening on previous player move
        computer_move,xi = linear_congruence(xi)
        if player_previous_move == 0:
            computer_move,xi = linear_congruence(xi)  
            #1.Ifthrow10>throw00:thenthecomputerchooses1
            #2.Ifthrow10<throw00:thenthecomputerchooses0
            #3.Ifthrow10=throw00:thenthecomputerchoosesrandomly0or1.     
        elif player_previous_move == 1:
            computer_move,xi = linear_congruence(xi)  
            #4.Ifthrow11>throw01:thenthecomputerchooses1
            #5.Ifthrow11<throw01:thenthecomputerchooses0
            #6.Ifthrow11=throw01:thenthecomputerchoosesrandomly0or1.
        else:
            computer_move,xi = linear_congruence(xi)            
        
        if player_move == computer_move:
            MS = MS + 1
            print("player = 0 machine = 0 - Machine wins!")
            print("You: %d Computer: %d" % (PS, MS))
        else:
            PS = PS + 1
            print("player = 0 machine = 0 - Player wins!")
            print("You: %d Computer: %d" % (PS, MS))
            
        print('PLAYER: ' + '*'*PS)
        print('MACHINE: ' + '*'*MS)
        
    if turn == moves and PS > MS:
        print("The game has ended, you win!")
    elif PS == MS:
        print("The game has ended, it is a draw!")
    else:
        print("the game has ended, the machine wins!")
            
# Open:
#comment your code
# create overall for loop that only ends when the play decides to quit the game

                
