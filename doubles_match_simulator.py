#This is the python file for the simulator of badminton doubles data
#importing the necessary libraries
import numpy as np
from itertools import combinations
import random as rand
from match_results import win_lose_function

##One method of linking string to attributes is with a 2-d list
jon = ['jon',[[7,5,0.95]]]

#Another method of linking string to attributes is to make a class that stores both
class Player:
    def __init__(self,name,attributes):
        self.name = name
        self.attributes = attributes  


#Defiing all the players as objects
jon = Player('John',[7,5,0.95])
nish = Player('Nishant',[9,7,1])
jun = Player('Junior',[2,5,0.96])
mo = Player('Mohamed',[10,10,0.98])


#Player data - defining an array that contains all players
players = [jon, nish, mo, jun]

'''#Defining all player attributes in an array
jon = np.array([7,5,0.95])
nish = np.array([9,7,1])
jun = np.array([2,5,0.96])
mo = np.array([10,10,0.98])'''

#Defining the matrix that will hold the values of the chemistry rating for all pairs

#Defining the value of the weights for the traits, to be used in the match determiniation formula
trait_weights = np.array([0.4,0.2,0.1])

#Defining a function that returns the inverse of an input (0s -> 1s and vice versa)
def inv_function(value):
    if (value == 0):
        new_value = 1
    else:
        new_value = 0
    return(new_value)

#Creating a list of valid combinations of teams from the amount of players registered 
two_pair_combo = list(combinations(players,2))


#Defining the win formula
#THIS FUNCTION NEEDS TO BE REFINED SO THAT YOU CAN PASS A LIST OF PAIRS INSTEAD OF INDIVIDUAL NAMES
    

final_win = win_lose_function(two_pair_combo[0][0].attributes,
                  two_pair_combo[0][1].attributes,
                  two_pair_combo[1][0].attributes,
                  two_pair_combo[1][1].attributes,trait_weights) 

print(final_win)
print(two_pair_combo[0][0].name,
                  two_pair_combo[0][1].name,
                  two_pair_combo[1][0].name,
                  two_pair_combo[1][1].name)
##Testing that the probabilities and outcomes are as expected
##print("The probability that (Jon,Nish) beat (Mo, Jun) is %f" %win_lose_function(jon,nish,mo,jun,trait_weights))



