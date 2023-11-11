import numpy as np
import random as rand

def win_lose_function(a,b,c,d,w):
    #Defining an array that will hold value of all (X = 1,250) outcomes of this simulated pairing
    total_win_loss = np.empty(100000)
    for looper in range(total_win_loss.size):
        trait=0
        #Defining the threshold noise value
        noise_threshold = 0.32
        #Defining the pairing difference for each match
        match_difference = 0 
        #Defining the win/lose value for each iteraton 
        w_l_unique = 0
        #Defining the noise value
        noise_val = 0
        #Generating the noise value for this individual simulation
        noise_val = rand.uniform(-1, 1)
        #Creating a loop to calculate the win or loss for each unique matchup
        while trait < w.size:
            #Getting the average of the trait for the first pair
            first_pair_avg = (a[trait]+b[trait])/2
            #Getting the average of the trait for the second pair
            second_pair_avg = (c[trait]+d[trait])/2
            #Calculating the difference in the trait between the two pairs and assigning the weight to the trait
            weighted_avg = w[trait] * (first_pair_avg - second_pair_avg)
            #Accounting each weighted trait into the match difference for this individual simulation 
            match_difference = match_difference + weighted_avg + noise_val
            #Increasing the trait counter to iterate through all traits
            trait=trait+1
        #If the outcome is positive (meaning AB beat CD), this is a win to be categorised as a "1"
        if(match_difference > 0):
            w_l_unique = 1
        else:
            w_l_unique = 0
        #Testing to see if noise value is larger than the threshold
        """if (noise_val > noise_threshold):
            w_l_unique = inv_function(w_l_unique)"""
        #Appending this new instance of a win or loss to the total ledger of wins and losses
        total_win_loss[looper] = w_l_unique
    #Setting the outcome of the function to being the FINAL average win/loss outcome/probability, even after accounting for noise/upsets
    return(np.average(total_win_loss))