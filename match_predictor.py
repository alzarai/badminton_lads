from os import path
import numpy as np
import csv 

#The code that will be used to build and train a NN to see if we can we predict the outcome of matches
#We will assume we are given the files that have been created as they are - hence we will need to combine into one master file and extract relevant data to be fed into model



#Defining the function that will generate the training data list form the files
#For simplicity we will assume that the order of the training data is the same as the label data
def define_training_data():
    x_data = []
    #Reading from the file
    DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
    file_path = path.join(DIR,'player_data.csv')
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        reader = list(reader)
        for row in range(1, len(reader), 1):  # Step by 2 for pairs
            if row + 1 < len(reader):  # Ensure there’s a next row
                #The 2 here ensures we are omitting the player name, as we dont want this to have an influence on training data
                x_data.append(reader[row][1:] + reader[row + 1][1:])
    x_data = np.array(x_data)   
    print(len(x_data))
    print(x_data)
define_training_data()


#Defining the function that will generate the training labels list form the files
def define_training_list():
    y_data=[]
    #Reading from the file
    DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
    file_path = path.join(DIR,'match_data.csv')
    with open(file_path, mode='r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            y_row = float(row[2:][0])
            y_data.append(y_row)
        print(len(y_data)) 
define_training_list()

#Defining the function that will build the neural network
#def predictor():

#Defining the function that will determine the accuracy of our model, by comparing its evaluation against a new set of player data that will be created using the original formula
#def accuracy_determinator():
