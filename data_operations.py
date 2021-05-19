import json
import math
import os
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

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

    def read_data(self, dir):
        raw_data_x_temp={}
        raw_data_y_temp = {}
        raw_data_z_temp = {}

        for file in self.file_names:
            if file.endswith(".json"):
                current_f = self.read_json(dir+file)
                raw_data_x_temp[re.sub(".json","",file)]=np.array(current_f["payload"]["values"])[:, 0]
                raw_data_y_temp[re.sub(".json", "", file)] = np.array(current_f["payload"]["values"])[:, 1]
                raw_data_z_temp[re.sub(".json", "", file)] = np.array(current_f["payload"]["values"])[:, 2]

        raw_data_x=pd.DataFrame(raw_data_x_temp)
        raw_data_y = pd.DataFrame(raw_data_y_temp)
        raw_data_z = pd.DataFrame(raw_data_z_temp)

        self.raw_data={"X":raw_data_x, "Y":raw_data_y, "Z":raw_data_z,}

    def create_time(self, data, end_time): # creates time vector with start 0, end at end_time and number of steps based on provided data
       self.raw_time = np.linspace(0, end_time, len(data[list(data.keys())[0]]["accX"]))  # gets accX data from first file (keys function requires conversion to list)

    def calculate_RMS(self, data):
        self.rms_data=pd.DataFrame()
        for dataset in data["X"]:
            row=pd.DataFrame({"X RMS":[self.RMS(data["X"][dataset].values)],
                 "Y RMS":[self.RMS(data["Y"][dataset].values)],
                "Z RMS":[self.RMS(data["Z"][dataset].values)],
                "Label":dataset[:3],
                 "Dataset":dataset})
            self.rms_data=self.rms_data.append(row, ignore_index=True)

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

    def plot_RMS(self, data):
        # Creating figure
        fig = plt.figure(figsize=(10, 7))
        ax = plt.axes(projection="3d")

        for label in data["Label"].unique():
            plot_data=data[data["Label"]==label]
            ax.scatter3D(plot_data["X RMS"], plot_data["Y RMS"], plot_data["Z RMS"], s=300)

        plt.title("Feature extraction")
        plt.xlabel("X_RMS")
        plt.ylabel("Y_RMS")
        ax.set_zlabel("Z_RMS")
        ax.legend(data["Label"].unique())
