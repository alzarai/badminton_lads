#This is the python script to work on the project on a more reduced level.
#Aim is to read player data from a csv, apply a formula for winning/losing, and then saving this data into a file

#Importing required libs
import pandas as pd
from os import path
import numpy as np
DIR = '/Users/mohamed.alzarai/Desktop/Git/badminton_lads'
#getting player data
player_data = pd.read_csv(path.join(DIR,'player_data.csv'))

#YOU NEED TO SEE IF YOU CAN (1) TAKE A COL/ROW AND MANIPULATE IT AS AN ARRAY (2) SAVE AN ARRAY AS A SERIES BACK INTO A DATAFRA [ANSWER = .toDataFrame()]
#TRYING (1) - Creating an extra COL that is( the cumulative frequency of the chemistry.

#ANSWER = .to_numpy() methid
chemistry_array = player_data['Chemistry'].to_numpy()
name_array = player_data['Player'].to_dict
print(chemistry_array)
print(name_array)

#Defining the maths that needs to be done with the specific numpy array
def cum_chem(chem_data):
    iterator = 0
    array_size = len(chem_data)
    #defining new array
    cum_array = np.empty(array_size,dtype=int)
    while (iterator < array_size):
        cum_array[iterator] = sum(chem_data[:iterator+1])
        iterator+=1
    return(cum_array)

'''cum_array = cum_chem(chemistry_array)
#Writing this array back to a df
player_data['cumulative chemistry'] = cum_array
print(player_data)
print(type(cum_array))
print(type(player_data['cumulative chemistry']))'''