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
print("Welcome to Human Behavior Prediction by Prof. Manoel Gadi")

select_difficulty = int(input("Choose the type of game (1: Easy; 2: Difficult): "))

moves = int(input("Enter the number of moves: "))

MS = 0
PS = 0
xi = 1234

if select_difficulty == 1:
    for turn in range(moves):
        #print(turn)
        player_move = int(input("Choose your move number %s (0 or 1):" % (turn+1)))
        computer_move,xi = linear_congruence(xi)
        if player_move == computer_move:
            MS = MS + 1
            print("player = 0 machine = 0 - Machine wins!")
            print("You: %d Computer: %d" % (PS, MS))
        else:
            PS = PS + 1
            print("player = 0 machine = 0 - Machine wins!")
            print("You: %d Computer: %d" % (PS, MS))
            
        print('PLAYER: ' + '*'*PS)
        print('MACHINE: ' + '*'*MS)
            
# Open:
# create overall for loop that only ends when the play decides to quit the game
# implement difficulty 2
                
