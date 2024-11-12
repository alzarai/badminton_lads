from os import path
import numpy as np
import csv 
import tensorflow
from tensorflow import keras


#from tensorflow.keras import Sequential

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
        next(reader)
        reader = list(reader)
    for i in range(len(reader)):
        for j in range(len(reader)):  # Pair with all rows from i to the last row
            #First data point is 
            row_1 = reader[i][2:]
            #We also know that the last value is always going to be the eyesight, so let us evaluate what that gives us in float form
            row_1[-1]=eval(row_1[-1])
            #Second data point is
            row_2 = reader[j][2:]
            #We also know that the last value is always going to be the eyesight, so let us evaluate what that gives us in float form
            row_2[-1]=eval(row_2[-1])
            #The combined rows that will be used as the total first training example
            combined_row = row_1+row_2 
            x_data.append(combined_row)
    x_data = np.array(x_data) 
    #We know that all the data in the 5th column is dominant hand and 6th column is gender and we we want to replace these with binary values instead, so we create targets and replacements
    target_values = ['left','right','male','female']
    replacement_values = [-1,1,-1,1]
    for target,replacement in zip(target_values,replacement_values):
        x_data[x_data == target] = replacement

    #converting all training values to float to be fed into the neural network
    x_data = x_data.astype(float)
    #return(x_data)
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
    return(y_data)


#Defining the function that will build the neural network
def predictor():
    #Getting training data and labels
    x_data = np.array(define_training_data())
    y_data = np.array(define_training_list())
    #Creating the NN
    model = keras.Sequential([
        keras.layers.Input(shape=(len(x_data),)),
        keras.layers.Dense(25,activation='relu'),
        keras.layers.Dense(15,activation='relu'),
        keras.layers.Dense(1,activation='linear')
    ])
    model.compile(optimizer='adam',loss='mse')
    model.fit(x_data,y_data,epochs=100)

predictor()


#Defining the function that will determine the accuracy of our model, by comparing its evaluation against a new set of player data that will be created using the original formula
#def accuracy_determinator():
