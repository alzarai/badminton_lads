#Aim of the code is to generate individual player data and save it to a folder, that will then be used as  the basis to create the training data for the main project

#Importing required libs
import pandas as pd
from os import path
import string
import random
#Defining the seed for random generator
random.seed(42)

#Defining global features such total number of features, and the order they will appear in the data/file
feature_options = ["Name","Height", "Weight", "Age", "Experience", "Dominant_hand", "Gender"]
#Defining the list of uppercase letters hat will be used to make player names
uppercase_letters = list(string.ascii_uppercase)#Defining the possible options or boundaries for a feature 
height_options = [140, 190]
weight_options = [50,95]
age_options = [18,37]
experience_options = [0,20]
dominant_hand_options = ["left","right"]
gender_options = ["male","female"]

#Defining a function that will create an array of features for a player
def players_creator(number_of_players):
    
    #Creating the array that will hold all player data, that will eventually be read into the CSV
    player_array = []
    #Creating a loop that creates an array which stores individual player data thats created

    for iterator1 in range(len(uppercase_letters)):
        player_group = uppercase_letters[iterator1]

        for iterator2 in range(number_of_players):
            player_name = player_group + str(iterator2)
            player_height = random.randint(height_options[0],height_options[-1])
            player_weight = random.randint(weight_options[0],weight_options[-1])
            player_age = random.randint(age_options[0],age_options[-1])
            player_experience = random.randint(experience_options[0],experience_options[-1])
            #These two values have to be either or - we will keep them as labeled data and not numerical classifications (we will leave that part for the training)
            player_dominant_hand = random.choice(dominant_hand_options)
            player_gender = random.choice(gender_options)

            player_stats = [player_name,player_height,player_weight,player_age,player_experience,player_dominant_hand,player_gender]
            player_array.append(player_stats)
    
    print(player_array)
    return(player_array)

#Defining the number of players in each class (i.e. A0 - A9, B1-B9, etc)
number_of_players = 1
player_data_for_file = players_creator(number_of_players)

#Creating a DataFrame to store this data into a file
df = pd.DataFrame(player_data_for_file, columns=feature_options)
#Naming the file to save total player data
DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
file_path = path.join(DIR,'player_data.csv')

df.to_csv(file_path,index="False")
