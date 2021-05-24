import json
import math
import os
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

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

    def window(self, data, items, overlap):
        window_data_x_temp = {}
        window_data_y_temp = {}
        window_data_z_temp = {}
        for dataset in data["X"]:
            n=1
            while n * items <= len(data["X"][dataset].index.values):
                # make two sets of bools and then add them
                if n > 1:
                    bool1 = data["X"][dataset].index.values < n * items - overlap
                else:
                    bool1 = data["X"][dataset].index.values < n * items
                bool2 = data["X"][dataset].index.values >= (n - 1) * items - overlap
                x_temp = data["X"][dataset][np.logical_and(bool1, bool2)]
                y_temp = data["Y"][dataset][np.logical_and(bool1, bool2)]
                z_temp = data["Z"][dataset][np.logical_and(bool1, bool2)]

                window_data_x_temp[dataset + "_set_" + str(n)] = x_temp.values
                window_data_y_temp[dataset + "_set_" + str(n)] = y_temp.values
                window_data_z_temp[dataset + "_set_" + str(n)] = z_temp.values

                n += 1

            window_data_x = pd.DataFrame(window_data_x_temp)
            window_data_y = pd.DataFrame(window_data_y_temp)
            window_data_z = pd.DataFrame(window_data_z_temp)

            self.window_data={"X":window_data_x, "Y":window_data_y, "Z":window_data_z}

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
        # fig = plt.figure(figsize=(10, 7))
        ax = plt.axes(projection="3d")

        for label in data["Label"].unique():
            plot_data=data[data["Label"]==label]
            ax.scatter3D(plot_data["X RMS"], plot_data["Y RMS"], plot_data["Z RMS"], s=300)

        plt.title("Feature extraction")
        plt.xlabel("X_RMS")
        plt.ylabel("Y_RMS")
        ax.set_zlabel("Z_RMS")
        ax.legend(data["Label"].unique())

    def plot_1D(self, data, axis):
        for label in data["Label"].unique():
            plot_data = data[data["Label"] == label]
            plt.scatter(plot_data[axis], np.zeros(len(plot_data[axis])), s=300)
            plt.legend(data["Label"].unique())

    def plot_2D(self, data, x_axis, y_axis):
        for label in data["Label"].unique():
            plot_data = data[data["Label"] == label]
            plt.scatter(plot_data[x_axis], plot_data[y_axis], s=30)
            plt.legend(data["Label"].unique())

def draw_1D(data):
    plt.subplot(3, 1, 1)
    data.plot_1D(data.rms_data, "X RMS")
    plt.title("X RMS")
    plt.subplot(3, 1, 2)
    data.plot_1D(data.rms_data, "Y RMS")
    plt.title("Y RMS")
    plt.subplot(3, 1, 3)
    data.plot_1D(data.rms_data, "Z RMS")
    plt.title("Z RMS")

def draw_2D(data):
    plt.subplot(3, 1, 1)
    data.plot_2D(data.rms_data, "X RMS", "Y RMS")
    plt.xlabel("X RMS")
    plt.ylabel("Y RMS")
    plt.subplot(3, 1, 2)
    data.plot_2D(data.rms_data, "X RMS", "Z RMS")
    plt.xlabel("X RMS")
    plt.ylabel("Z RMS")
    plt.subplot(3, 1, 3)
    data.plot_2D(data.rms_data, "Y RMS", "Z RMS")
    plt.xlabel("Y RMS")
    plt.ylabel("Z RMS")

def classify_data(data, kernel, degree=2, drop_Z_rms=False):
    # SVM implememntation

    # Data preparation - delete columns: Label, Dataset
    if drop_Z_rms == False:
        X = data.drop(["Label", "Dataset"], axis=1)
    else:
        X = data.drop(["Label", "Dataset", "Z RMS"], axis=1)
    Y = data["Label"]

    # Split data intot training and test
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

    # Classifier setup
    if kernel=="poly":
        svclassifier = SVC(kernel=kernel,degree=degree)
    else:
        svclassifier = SVC(kernel=kernel)

    svclassifier.fit(X_train, y_train)

    # Classify data
    y_pred = svclassifier.predict(X_test)

    # Confusion matrix
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    return svclassifier, X_train, X_test, y_train, y_test

def plot_classifier_2D(X_data, y_data,svclassifier):
    # Plot classifier
    x1 = np.linspace(0.4, 1.4)
    y1 = np.linspace(0.4, 1.4)

    y1 = np.array((-svclassifier.intercept_[0] - svclassifier.coef_[0][0] * x1) / svclassifier.coef_[0][
        1])  # Zrozumiec ta funkcje
    y2 = np.array((-svclassifier.intercept_[1] - svclassifier.coef_[1][0] * x1) / svclassifier.coef_[1][1])
    y3 = np.array((-svclassifier.intercept_[2] - svclassifier.coef_[2][0] * x1) / svclassifier.coef_[2][1])

    X_data["Label"] = y_data

     # dziala gdy wylaczone z rms
    plot_data = X_data[X_data["Label"] == "110"]
    plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30, c="#1f77b4")
    plot_data = X_data[X_data["Label"] == "60_"]
    plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30, c="#ff7f0e")
    plot_data = X_data[X_data["Label"] == "OFF"]
    plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30, c="#2ca02c")
    plt.plot(x1, y1 + 0.0025, c="#ff7f0e", linewidth=3)
    plt.plot(x1, y1 - 0.0025, c="#1f77b4", linewidth=3)
    plt.plot(x1, y2 - 0.0045, c="#2ca02c", linewidth=3)
    plt.plot(x1, y2 + 0.0045, c="#1f77b4", linewidth=3)
    plt.plot(x1, y3 + 0.0025, c="#ff7f0e", linewidth=3)
    plt.plot(x1, y3 - 0.0025, c="#2ca02c", linewidth=3)
    plt.ylim([1.5, 2.5])
    plt.title("Train data")
    plt.xlabel("X RMS")
    plt.ylabel("Y RMS")
    plt.legend(X_data["Label"].unique())

def plot_classifier_3D(data, svclassifier):
    x1 = np.linspace(0.4, 1.4)
    y1 = np.linspace(1.4, 2.1)
    x2, y2 = np.meshgrid(x1, y1)
    z = lambda x1, y1: ((-svclassifier.intercept_[0] - svclassifier.coef_[0][0] * x1 - svclassifier.coef_[0][1] * y1) /
                        svclassifier.coef_[0][2])

    ax = fig.add_subplot(111, projection='3d')
    for label in data["Label"].unique():
        plot_data = data[data["Label"] == label]
        ax.scatter3D(plot_data["X RMS"], plot_data["Y RMS"], plot_data["Z RMS"], s=50)
    ax.plot_surface(x2, y2, z(x2, y2), color="k", shade=0.5)
    plt.xlabel("X_RMS")
    plt.ylabel("Y_RMS")
    ax.set_zlabel("Z_RMS")
