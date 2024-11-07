#Aim is to read player data from a csv, apply a formula for winning/losing, and then saving this data into a new file
#We will start with very crude relational data before moving on to more redined possible outcomes

#Importing required libs
import pandas as pd
from os import path
import numpy as np
from scipy.stats import norm


'''import numpy as np
def score_weight(weight, center=80, sigma=5):
    return np.exp(-((weight - center) ** 2) / (2 * sigma ** 2))'''

#Defining the function that will calculate the influence height has on the overall score
def height_influence(pl1_h,pl2_h):
    #The influence via height will be calculated by assuming there is an ideal height, and heights on either side of that tail off via a normal distribution
    #Defining the centralised height that I believe represents the ideal height of a player for this game (i.e. 190 cm)
    height_centre = 190
    height_sigma = 0.5
    #Creation of a normal distribution# Create the normal distribution
    height_distribution = norm(loc=height_centre, scale=height_sigma)
    #Defining the "normalised" value of a given height in terms of this distribution
    pl1_h_norm = height_distribution.pdf(pl1_h)
    pl2_h_norm = height_distribution.pdf(pl2_h)
    return([pl1_h_norm,pl2_h_norm])


#Function that decides the probability that a certain player will beat their opponent, given the features of two players
def match_win_probability(pl1,pl2):


    #Creating a comparison between the features, along with how important that feature is to the overall score
    
    #For height, the taller a player is the more likely to win.
    height_factor = pl1[1] - pl2[1]
    #Height impacts the likelihood of winning pretty highly positive so we will make this difference 10x
    height_weight = 10
    
    #For weight, the heavier a player is the less likely to win.
    weight_factor = pl1[2] - pl2[2]
    #Height impacts the likelihood of winning pretty highly negatively, but not as much as height, so we will make this 6x
    weight_weight = 6
   
    #For age, the older the player is the less likely to win, since all players are between 18 and 37
    age_factor = pl1[3] - pl2[3]
    #Age isn't as important as all players are at age of competition
    age_weight = 2

    #For experience, undoubtedly the more experience you have the better you are
    experience_factor = pl1[4] - pl2[4]
    #Experience really matters, so lets make it a 10x
    experience_weight = 10

    #Neither dominant hand nor gender influence a win so they wont be counted
    
    #Defining the final formula to decide a win or not
    win_probability = (height_factor*height_weight) + (weight_factor*weight_weight) + (age_factor*age_weight) + (experience_factor*experience_weight)
    #Defining the data that will be stored in the match data file
    match_data_for_file = [[pl1[0],pl2[0],win_probability]]

    #Creating a DataFrame to store this data into a file
    df = pd.DataFrame(match_data_for_file, columns=['Player 1','Player 2','Probability of Win for Player 1'])
    #Naming the file to save total player data
    DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
    file_path = path.join(DIR,'match_data.csv')
    #Writing the data to the file
    df.to_csv(file_path,index="False")

pl1 = ['A0', 191, 100, 18, 8, 'left', 'male']
pl2 = ['D0', 141, 55, 35, 13, 'left', 'female']
#match_win_probability(pl1,pl2)
height_influence(pl1[1],pl2[1])


