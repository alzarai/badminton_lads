#This is the python script to work on the project on a more reduced level.
#Aim is to read player data from a csv, apply a formula for winning/losing, and then saving this data into a file

#Importing required libs
import pandas as pd
from os import path
import numpy as np
import random
#Defining the seed for random generator
random.seed(42)

DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'

#getting player data
player_data = pd.read_csv(path.join(DIR,'player_data.csv'))

#Defining total number of features, and the order they will appear in
feature_options = ["Player","Height", "Weight", "Age", "Experience", "Dominant_hand", "Gender"]
#Defining the possible options or boundaries for a feature 
height_options = [140, 190]
weight_options = [50,95]
age_options = [18,37]
experience_options = [0,20]
dominant_hand_options = ["left","right"]
gender_options = ["male","female"]

#Defining a function that will create an array of features for a player
def player_creator():
    player_height = random.randint(height_options[0],height_options[-1])
    