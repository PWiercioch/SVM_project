import json
import math
import os
import pathlib
import numpy as np

def welcome(): # test function
    print("Hello wolrd!")

def read_json(path): # read data from json file
    file=open(path)
    return json.load(file)

def RMS(data): # calculate rms from data
    n = len(data)
    sqr = 0.0
    root = 0.0
    mean = 0.0

    # calculating Squre
    for i in range(0, n):
        sqr += (data[i] ** 2)
    # Calculating Mean
    mean = (sqr / (float)(n))
    # Calculating Root
    root = math.sqrt(mean)
    return root

def get_file_names(directory): # as an argument pass directory within working directory
    dir=str(pathlib.Path().absolute())
    return(os.listdir(dir+directory)) # adds data path to working directory


def read_data(dir,files):# reads data from all files in a directory
    data={}
    for file in files:
        if file.endswith(".json"):
            current_f = read_json(dir+file)
            data[file[:-5]] = {"accX":np.array(current_f['payload']['values'])[:, 0], # first key - file name, extension excluded
                                "accY": np.array(current_f['payload']['values'])[:, 1],
                                "accZ": np.array(current_f['payload']['values'])[:, 2]}
    return data  # nested dictionaries

def create_time(data, end_time): # creates time vector with start 0, end at end_time and number of steps based on provided data
   return np.linspace(0, end_time, len(data[list(data.keys())[0]]["accX"]))  # gets accX data from first file (keys function requires conversion to list)

def calculate_RMS(data):
    for keys in data:
        data[keys]["RMS_X"] = RMS(data[keys]["accX"])
        data[keys]["RMS_Y"] = RMS(data[keys]["accY"])
        data[keys]["RMS_Z"] = RMS(data[keys]["accZ"])
