import json
import math
import os
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Data:

    data={}

    def create_DataFrame(self):
        self.df=pd.DataFrame(self.data)

    def welcome(self): # test function
        print("Hello wolrd!")

    def read_json(self, path): # read data from json file
        file=open(path)
        return json.load(file)

    def RMS(self, data): # calculate rms from data
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

    def get_file_names(self, directory): # as an argument pass directory within working directory
        dir=str(pathlib.Path().absolute())
        self.file_names=os.listdir(dir+directory) # adds data path to working directory


    def read_data(self, dir):# reads data from all files in a directory
        data={}
        for file in self.file_names:
            if file.endswith(".json"):
                current_f = self.read_json(dir+file)
                self.data[file[:-5]] = {"accX":np.array(current_f['payload']['values'])[:, 0], # first key - file name, extension excluded
                                    "accY": np.array(current_f['payload']['values'])[:, 1],
                                    "accZ": np.array(current_f['payload']['values'])[:, 2]}
        # nested dictionaries

    def create_time(self, data, end_time): # creates time vector with start 0, end at end_time and number of steps based on provided data
       self.raw_time = np.linspace(0, end_time, len(data[list(data.keys())[0]]["accX"]))  # gets accX data from first file (keys function requires conversion to list)

    def calculate_RMS(self, data):
        for keys in data:
            data[keys]["RMS_X"] = self.RMS(data[keys]["accX"])
            data[keys]["RMS_Y"] = self.RMS(data[keys]["accY"])
            data[keys]["RMS_Z"] = self.RMS(data[keys]["accZ"])

    def raw_data_plots(self, data):  # plots raw data
        n = 0
        for keys in data:
            plt.figure(n)
            plt.subplot(3, 1, 1)
            plt.title(keys)
            plt.plot(self.raw_time, data[keys]["accX"])
            plt.xlabel("Time [s]")
            plt.ylabel("AccX [m/s^-2]")
            plt.subplot(3, 1, 2)
            plt.plot(self.raw_time, data[keys]["accY"])
            plt.xlabel("Time [s]")
            plt.ylabel("AccY [m/s^-2]")
            plt.subplot(3, 1, 3)
            plt.plot(self.raw_time, data[keys]["accY"])
            plt.xlabel("Time [s]")
            plt.ylabel("AccZ [m/s^-2]")
            n += 1

    def get_RMS(self, data, label):  # creates numpy arrays from dictionary data
        RMS_X = []
        RMS_Y = []
        RMS_Z = []

        for keys in data:
            if keys[:3] == label:
                RMS_X.append(data[keys]["RMS_X"])
                RMS_Y.append(data[keys]["RMS_Y"])
                RMS_Z.append(data[keys]["RMS_Z"])
        RMS = {"X": RMS_X, "Y": RMS_Y, "Z": RMS_Z}
        return RMS

    def plot_RMS(self, data):
        RMS_110 = self.get_RMS(data, "110")
        RMS_60 = self.get_RMS(data, "60_")
        RMS_OFF = self.get_RMS(data, "OFF")
        # Creating figure
        fig = plt.figure(figsize=(10, 7))
        ax = plt.axes(projection="3d")

        # Creating plot
        ax.scatter3D(RMS_110["X"], RMS_110["Y"], RMS_110["Z"], s=300, color="green")
        ax.scatter3D(RMS_60["X"], RMS_60["Y"], RMS_60["Z"], s=300, color="red")
        ax.scatter3D(RMS_OFF["X"], RMS_OFF["Y"], RMS_OFF["Z"], s=300, color="blue")
        plt.title("Feature extraction")
        plt.xlabel("X_RMS")
        plt.ylabel("Y_RMS")
        ax.set_zlabel("Z_RMS")
        ax.legend(["110 watts", "60 watts", "off"])

        # show plot
        plt.show()
