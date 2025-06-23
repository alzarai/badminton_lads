#Aim is to read player data from a csv, apply a formula for winning/losing, and then saving this data into a new file
#We will start with very crude relational data before moving on to more redined possible outcomes

#Importing required libs
import pandas as pd
from os import path
import csv
import numpy as np
from scipy.stats import norm

#Defining the function that will calculate the influence height has on the overall score
def height_influence(pl1_h,pl2_h):
    #The influence via height will be calculated by assuming there is an ideal height, and heights on either side of that tail off via a normal distribution
    #Defining the centralised height that I believe represents the ideal height of a player for this game (i.e. 190 cm)
    height_centre = 190
    height_sigma = 1
    #Creation of a normal distribution# Create the normal distribution
    height_distribution = norm(loc=height_centre, scale=height_sigma)
    #Defining the "normalised" value of a given height in terms of this distribution
    pl1_h_norm = height_distribution.pdf(pl1_h)
    pl2_h_norm = height_distribution.pdf(pl2_h)
    heght_factor = pl1_h_norm - pl2_h_norm
    return(heght_factor)

#Defining the function that will calculate the influence weight has on the overall score
def weight_influence(pl1_w,pl2_w):
    #The influence via weight will be calculated by assuming there is an ideal weight, and weights on either side of that tail off via a normal distribution
    #Defining the centralised height that I believe represents the ideal height of a player for this game (i.e. 85 kg)
    weight_centre = 85
    weight_sigma = 1
    #Creation of a normal distribution
    height_distribution = norm(loc=weight_centre, scale=weight_sigma)
    #Defining the "normalised" value of a given height in terms of this distribution
    pl1_w_norm = height_distribution.pdf(int(pl1_w))
    pl2_w_norm = height_distribution.pdf(int(pl2_w))
    weight_factor = pl1_w_norm - pl2_w_norm
    return(weight_factor)

#Defining the function that will calculate the influence age has on the overall score
def age_influence(pl1_age,pl2_age):
    #The influence via age will be calculated by assuming there is an ideal age, and weights on either side of that tail off via a normal distribution
    #Defining the centralised height that I believe represents the ideal height of a player for this game (i.e. 26 years old)
    age_centre = 26
    age_sigma = 1
    #Creation of a normal distribution
    age_distribution = norm(loc=age_centre, scale=age_sigma)
    #Defining the "normalised" value of a given height in terms of this distribution
    pl1_age_norm = age_distribution.pdf(int(pl1_age))
    pl2_age_norm = age_distribution.pdf(int(pl2_age))
    age_factor = pl1_age_norm - pl2_age_norm
    return(age_factor)

#Defining the function that will calculate the influence experience has on the overall score
def experience_influence(pl1_experience,pl2_experience):
    #The influence via age will be calculated by taking the log of values and then finding their difference (finding log of division)
    #This is mostly just to introduce more relations for the model to play with than sums or products
    experience_factor = np.log(float(pl1_experience)/float(pl2_experience))
    return(experience_factor)

#Defining the function that will calculate the influence historic wins has on the overall score
def historic_wins_influence(pl1_historic_wins,pl2_historic_wins):
    #The influence via historic wins will be calculated by taking the log of values and then finding their difference (finding log of division)
    #This is mostly just to introduce more relations for the model to play with than sums or products
    historic_wins_factor = np.log10(float(pl1_historic_wins)/float(pl2_historic_wins))
    return(historic_wins_factor)

#Defining the function that will calculate the influence historic wins has on the overall score
def reaction_time_influence(pl1_reaction_time,pl2_reaction_time):
    #The influence via historic wins will be calculated by taking the log of values and then finding their difference (finding log of division)
    #This is mostly just to introduce more relations for the model to play with than sums or products
    reaction_time_factor = (float(pl1_reaction_time) - float(pl2_reaction_time))/1000
    return(reaction_time_factor)

#Defining the function that will calculate the influence play_frequency wins has on the overall score
def play_freq_influence(pl1_play_freq,pl2_play_freq):
    #Random formula just to kep making this example interesting. Can be be refined later
    reaction_time_factor = np.power(float(pl1_play_freq), (float(pl1_play_freq) + 1 - float(pl2_play_freq)))
    return(reaction_time_factor)

#Defining the function that will calculate the influence athleticism  has on the overall score
def athleticism_influence(pl1_athleticism,pl2_athleticism):
    #Random formula just to kep making this example interesting. Can be be refined later
    athleticism_factor = np.power(0.9,(1/(int(pl1_athleticism)/int(pl2_athleticism))))
    return(athleticism_factor)

#Defining the function that will calculate the influence serve speed has on the overall score
def serve_speed_influence(pl1_serve_speed,pl2_serve_speed):
    #The influence that serve speed has on wins. Just copied the reaction time formula
    serve_speed_factor = (float(pl1_serve_speed) - float(pl2_serve_speed))/1000
    return(serve_speed_factor)

#Defining the function that will calculate the influence court coverage has on the overall score
def court_coverage_influence(pl1_court_coverage,pl2_court_coverage):
    #This time, the greater the value the worse off a player is; so we can use inverses.
    court_coverage_factor = (1/float(pl1_court_coverage)) -  (1/float(pl2_court_coverage))
    return(court_coverage_factor)

#Function that decides the probability that a certain player will beat their opponent, given the features of two players
def match_win_probability(pl1,pl2):
    #Creating a comparison between the features, along with how important that feature is to the overall score

    #Computing the influence the height will have on player 1's win using the dedicated function for it
    height_factor = height_influence(int(pl1[1]),int(pl2[1]))
    #Height impacts the likelihood of winning pretty highly positive so we will make this difference 0.75x
    height_weight = 0.75
    height_impact = (height_factor*height_weight)

    #Computing the influence the height will have on player 1's win using the dedicated function for it
    weight_factor = weight_influence(pl1[2],pl2[2])
    #Height impacts the likelihood of winning pretty highly positive so we will make this difference 0.4x
    weight_weight = 0.4
    weight_impact = (weight_factor*weight_weight)

    #Computing the influence the age will have on player 1's win using the dedicated function for it
    age_factor = age_influence(pl1[3],pl2[3])
    #Age impacts the likelihood of winning pretty mid because players have been chosen to have healthy age ranges hence we'll make it 0.15x
    age_weight = 0.15
    age_impact = (age_factor*age_weight)

    #Computing the influence the experience will have on player 1's win using the dedicated function for it
    experience_factor = experience_influence(pl1[4],pl2[4])
    #Experience impacts the likelihood of winning pretty highly so we will multiply it by 1x
    experience_weight = 1
    experience_impact = experience_factor * experience_weight

    #Dominant Hand and Gender are irrelevant to the probability that someone wins so these wont even be factored in

    #Computing the influence the historic win ratio will have on player 1's win using the dedicated function for it
    historic_wins_factor = historic_wins_influence(pl1[7],pl2[7])
    #Historic wins is a strong indicator of a current win so lets make it 0.85
    historic_wins_weight = 0.85
    historic_wins_impact = historic_wins_factor * historic_wins_weight

    #Computing the influence the reaction time will have on player 1's win using the dedicated function for it
    reaction_time_factor = reaction_time_influence(pl1[8],pl2[8])
    #Historic wins is a mid level influence so lets give it 0.60
    reaction_time_weight = 0.60
    reaction_time_impact = reaction_time_factor * reaction_time_weight

    #Computing the influence play frequency has on player 1's win using the dedicated function for it
    play_freq_factor = play_freq_influence(pl1[9],pl2[9])
    #Historic wins is a mid level influence so lets give it 0.60
    play_freq_weight = 0.60
    play_freq_impact = play_freq_factor * play_freq_weight

    #Computing the influence athleticism has on player 1's win using the dedicated function for it
    athleticism_factor = athleticism_influence(pl1[10],pl2[10])
    #Historic wins is a mid level influence so lets give it 0.93
    athleticism_weight = 0.93
    athleticism_impact = athleticism_factor * athleticism_weight

    #Computing the influence the serve speed will have on player 1's win using the dedicated function for it
    serv_speed_factor = serve_speed_influence(pl1[11],pl2[11])
    #Historic wins is a mid level influence so lets give it 0.22
    serve_speed_weight = 0.22
    serve_speed_impact = serv_speed_factor * serve_speed_weight

    #Computing the influence the serve speed will have on player 1's win using the dedicated function for it
    court_coverage_factor = court_coverage_influence(pl1[12],pl2[12])
    #Historic wins is a mid level influence so lets give it 0.45
    court_coverage_weight = 0.45
    serve_speed_impact = court_coverage_factor * court_coverage_weight

    #Lets keep eye-sight redundant because we can assume that all players will play with corrected vision




    #Defining the final formula to decide a win or not
    win_probability_array = [height_impact,weight_impact,age_impact,experience_impact,historic_wins_impact,reaction_time_impact, play_freq_impact, athleticism_impact,
                             serve_speed_impact,serve_speed_impact]
    #Defining the win as a sigmoid so we can get values between 0 and 1
    win_probability = 1 / (1 + np.exp(-np.sum(win_probability_array)))

    #Defining the data that will be stored in the match data file
    match_data_for_regression_file = win_probability
    return(match_data_for_regression_file)


#Function to compute the match data results from all current players
def generate_data():
    match_data_for_regression = []
    match_data_for_classification = []

    #Defining the file to read all data from
    #Naming the file to save total player data
    DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads/Data Files (CSV)'
    file_path = path.join(DIR,'player_data.csv')
    #Writing the information from file to array
    generated_player_information = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            generated_player_information.append(row[1:])
    
    #Doing match calcs for all player combos
    for player1 in range(len(generated_player_information)):
        pl1_generate = generated_player_information[player1]
        for player2 in range((len(generated_player_information))):
            pl2_generate = generated_player_information[player2]
            match_win_probss = match_win_probability(pl1_generate,pl2_generate)
            if(pl1_generate[0]==pl2_generate[0]):
                pass
            else:
                match_data_for_regression.append([pl1_generate[0],pl2_generate[0],match_win_probss])
                if(match_win_probability(pl1_generate,pl2_generate)) > match_win_probability(pl2_generate,pl1_generate):
                    prob_1_wins = 1
                else:
                    prob_1_wins = 0
                match_data_for_classification.append([pl1_generate[0],pl2_generate[0],prob_1_wins])

    #Creating a DataFrame to store the regression data into a file
    df_regression = pd.DataFrame(match_data_for_regression, columns=['Player 1','Player 2','Probability of Win for Player 1'])
    #Naming the file to save total player data
    DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads/Data Files (CSV)'
    file_path = path.join(DIR,'match_data_regression.csv')
    #Writing the data to the file
    df_regression.to_csv(file_path, index=False)
        
    #Creating a DataFrame to store the classification data into a file
    df_classification = pd.DataFrame(match_data_for_classification, columns=['Player 1','Player 2','Win/Loss for Player 1'])
    #Naming the file to save total player data
    DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads/Data Files (CSV)'
    file_path = path.join(DIR,'match_data_classification.csv')
    #Writing the data to the file
    df_classification.to_csv(file_path, index=False)

generate_data()