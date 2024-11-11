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
            combined_row = reader[i][2:] + reader[j][2:]  # Skip the first column of each row
            x_data.append(combined_row)
    x_data = np.array(x_data)   
    return(x_data)

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
    x_data = define_training_data()
    y_data = define_training_list()
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
