#Aim of the code is to generate individual player data and save it to a folder, that will then be used as  the basis to create the training data for the main project

#Importing required libs
import pandas as pd
from os import path
import string
import random
#Defining the seed for random generator
random.seed(42)

#Defining global features such total number of features, and the order they will appear in the data/file
feature_options = ["Name","Height", "Weight", "Age", "Experience", "Dominant_hand", "Gender", "Historic Win Ratio", "Reaction Time",
                   "Play Frequency", "Athleticism", "Serve Speed","Court Coverage", "Vision"]
#Defining the list of uppercase letters hat will be used to make player names
uppercase_letters = list(string.ascii_uppercase)#Defining the possible options or boundaries for a feature 
height_options = [140, 190]
weight_options = [50,95]
age_options = [18,37]
experience_options = [0,20]
dominant_hand_options = ["left","right"]
gender_options = ["male","female"]


win_ratio_options = [0,1]
reaction_time = [100,700]
play_frequency_options = [0,1]
athleticism_options = [1,7]
serve_speed_options = [110,130]
court_coverage_options = [10,30]
vision_options = ["20/20","20/40","20/60","20/80"]

#Defining a function that will create an array of features for a player
def players_creator(number_of_players):
    
    #Creating the array that will hold all player data, that will eventually be read into the CSV
    player_array = []
    #Creating a loop that creates an array which stores individual player data thats created

    for iterator1 in range(len(uppercase_letters)):
        player_group = uppercase_letters[iterator1]

        for iterator2 in range(number_of_players):
            #Defining the attributes of a player based on the ootions available
            player_name = player_group + str(iterator2)
            player_height = random.randint(height_options[0],height_options[-1])
            player_weight = random.randint(weight_options[0],weight_options[-1])
            player_age = random.randint(age_options[0],age_options[-1])
            player_experience = random.randint(experience_options[0],experience_options[-1])
            #These two values have to be either or - we will keep them as labeled data and not numerical classifications (we will leave that part for the training)
            player_dominant_hand = random.choice(dominant_hand_options)
            player_gender = random.choice(gender_options)
            #Continuing with the remaining attributes
            player_win_ratio = random.uniform(win_ratio_options[0],win_ratio_options[-1])
            player_reaction_time = random.uniform(reaction_time[0],reaction_time[-1])
            player_play_frequency = random.uniform(play_frequency_options[0],play_frequency_options[-1])
            player_athleticism = random.randint(athleticism_options[0],athleticism_options[-1])
            player_serve_speed = random.uniform(serve_speed_options[0],serve_speed_options[-1])
            player_court_coverage = random.uniform(court_coverage_options[0],court_coverage_options[-1])
            player_vision = random.choice(vision_options)

            #Defining the overall features of the player
            player_stats = [player_name,player_height,player_weight,player_age,player_experience,player_dominant_hand,player_gender,
                            player_win_ratio,player_reaction_time,player_play_frequency,player_athleticism,player_serve_speed,player_court_coverage,
                            player_vision]
            
            player_array.append(player_stats)
    return(player_array)

#Defining the number of players in each class (i.e. A0 - A9, B1-B9, etc)
number_of_players = 10
player_data_for_file = players_creator(number_of_players)

#Creating a DataFrame to store this data into a file
df = pd.DataFrame(player_data_for_file, columns=feature_options)
#Naming the file to save total player data
DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
file_path = path.join(DIR,'player_data.csv')

df.to_csv(file_path,index="False")
