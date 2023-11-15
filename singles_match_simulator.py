#This is the python script to work on the project on a more reduced level.
#Aim is to read player data from a csv, apply a formula for winning/losing, and then saving this data into a file

#Importing required libs
import pandas as pd
from os import path
DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
#getting player data
player_data = pd.read_csv(path.join(DIR,'player_data.csv'))
print(player_data)

