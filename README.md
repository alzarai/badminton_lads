This is my first project. Its an attempt to learn skills for data handling, analysis and machine learning along with developing my skills to work with git and Github.

The prupose of this project is to predict the outcome of a badminton match between two players given distinct unique features of these players. 

These predictions will be based on training a model on match data of players that have their own unique values for the same set of feature. 

The purpose of this task will be to see if the model can generalise well enough that it has "learned" what the underlying formula is that decides who wins a game given feature values of two new players. 

This task will be divided into two sections.

(1) Creation of training data. 
A list of 260 players A1 - Z10 (26 Groups with 10 players in each) is created with each having unique values for their features (Height, Weight, Age, Experience, Dominant_hand, Gender). Some of these features will impact performance more than others, while other features will have no impact on the performance. Each player will be matched against each other player to simulate a game. The result of the game is determined by the formula;

    win_probability = (h1 - h2) + (w1 - w2) + (age1 - age2) + (exp1 - exp2) + (hand1 - hand2) + (gender1 - gender2) + f(noise)

where each feature from one player is compared to the feature of their opponent and scaled by the importance of that feature to a potential win. Ie the gender of a player will not matter hence this value will be multiplied by 0 to eliminate it. Within each run, a noise variable will be randomly generated and compared to a predefined threshold for noise (e=0.8). If the noise variable is larger than the threshold, the result of the match will be reversed.  This will introduce potential "upsets" where there is a non-zero chance that a player who is supposed to win may lose a match. Each player will play each other player 5 times to allow for a total of 336,700 matches (260*259*10) or training examples, with the labels being a probability that the first player beats the second player.

It goes without saying that values close to 0.5 indicate a draw, values > 0.5 indicate more liklihood of a win and values < 0.5 indicate a probable loss.


(2) Training and Prediction. 

A model will be created and trained on the existing data. This is where best practices of creating and evaluating different model architectures, hyperparameters and other practices will be implemented. Once a model has been trained that performs well against training, cross validation and test data - it will be put to the test. Two totaly new players will be manually created and the function above will be applied to calcualte a win probability. The model will then be fed these same features and be tested against how well it is able to generate the exact same win probability. 


Questions to refine project:
(1) Data Simulation
1. Should noise probability (e=0.8) be independent of the pairing? (i.e Should matchups with much larger differences in opponents be less susceptible to upsets, compared to matchups with smaller differences in opponents)