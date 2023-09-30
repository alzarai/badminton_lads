This is my first project. Its an attempt to learn skills for data handling, analysis and machine learning (?) along with developing my skills to work with git and Github.

The prupose of this project is to predict, given n badminton players (first trial n=4, with further expansion to n=6 to ensure project is robust), the winner in a doubles game of randomly matched players. To make the project more complex and interesting, a model will be designed to make a prediction on a matching that has not been played before previously. This will be done by giving the model match data on various pairings and using this info to analyze the strongest/weakest matchups, their probability of winning - and then using this data to make informed decision on winners of matches that have not been played.

As this is a problem randomly thought out for practice purposes, no match data exists. To make things more interesting, the project is divided into two parts; (1) Data Simulation and (2) Training and Prediction. 

For (1) Data Simulation, 4 players (Jon, Jr, Mo and Nish) are defined with 3 individually unique traits (skill, athleticism, height) along with 1 trait that depends on their pairing for a game (chemistry). The effectivness of a pairing is calculated (SEE FORMULA BELOW) and compared against the effectivness of their opponent to generate the outcome of a winner. Each match is simulated 100 times but to replicate real world scenarios, noise is introduced. For each match, there is a chance of an upset where the "favourites" lose and this is taken into account in the overall probability of a win. At the end of the data simulation, the outcome should be the probability of the outcome (win/lose) for all possible combination of matches.

Given a match of [(A,B) vs (C,D)] we will calculate the effective winner by taking into account the unique traits of individuals in a pairing, along with the chemistry of the pairing and comparing with opponent. It was decided that the different traits have different impact on the result of a game (skill(0.4) > chemistry(0.3) > athleticism(0.2) > height(0.1)) and were weighted accordingly. When it comes to individual traits, the average in a pair is calculated and then compared (subtracted) to their opponent before being multiplied by the weight and added to the chemistry rating. As height differences can (numerically) be relatively quite large, heights are normalized where the tallest player is given a rating of 1 and other players are assigned a relative value. The match winning formula will be used to generate a win value for [(A,B) vs (C,D)] which will be run 100 times. Within each run, a noise variable will be randomly generated and compared to a predefined threshold for noise (e=0.8). If the noise variable is larger than the threshold, the result of the match will be reversed. In this way, a list of probable wins and losses for this match will be generated and a conclusive probability for an (A,B) win vs (C,D) will be determined. 



For (2) Training and Prediction, a model will be asked to calculate the winner of a specific match. The model will be fed all available match data *except* any matches where the combination in question is played. From said data, the model will calculate the match outcome and this expected outcome will be compared to true data (from (1)) to validate the accuracy of the prediciton. 



Questions to refine project:
(1) Data Simulation
1. Should noise probability (e=0.8) be independent of the pairing? (i.e Should matchups with much larger differences in opponents be less susceptible to upsets, compared to matchups with smaller differences in opponents)
2. Should the final outcome be of data simulation be a matrix of total win probabilities (including noise) or include every single iteration of a match for each pairing. 
3. Why do weights have to add up to 1?
4. Make an excel file with the players, their attributes and the chemistry between them and import + manipulate to generate the rest of the data - which will then be saved to (another?) excel file that will be used by the predictor 
5. The "true value of the probability" just tends towards the threshold we've set as we increase the number of simulations