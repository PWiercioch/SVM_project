import matplotlib.pyplot as plt


def get_labels(data): # unused! - returns list of labels, potentially to dynamically create variables
    labels=set()
    dict_keys=[]
    for keys in data:
        if keys[:3] not in labels:
            labels.add(keys[:3])
            dict_keys.append([keys[:3]])
    return dict_keys

def get_RMS(data, label): # creates numpy arrays from dictionary data
    RMS_X = []
    RMS_Y = []
    RMS_Z = []

    for keys in data:
        if keys[:3]==label:
            RMS_X.append(data[keys]["RMS_X"])
            RMS_Y.append(data[keys]["RMS_Y"])
            RMS_Z.append(data[keys]["RMS_Z"])
    RMS={"X": RMS_X, "Y": RMS_Y, "Z": RMS_Z}
    return RMS


def raw_data_plots(time, data): # plots raw data
    n=0
    for keys in data:
        plt.figure(n)
        plt.subplot(3, 1, 1)
        plt.title(keys)
        plt.plot(time, data[keys]["accX"])
        plt.xlabel("Time [s]")
        plt.ylabel("AccX [m/s^-2]")
        plt.subplot(3, 1, 2)
        plt.plot(time, data[keys]["accY"])
        plt.xlabel("Time [s]")
        plt.ylabel("AccY [m/s^-2]")
        plt.subplot(3, 1, 3)
        plt.plot(time, data[keys]["accY"])
        plt.xlabel("Time [s]")
        plt.ylabel("AccZ [m/s^-2]")
        n+=1

def plot_RMS(data):
    RMS_110=get_RMS(data, "110")
    RMS_60=get_RMS(data, "60_")
    RMS_OFF=get_RMS(data, "OFF")
    # Creating figure
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes(projection="3d")

    # Creating plot
    ax.scatter3D(RMS_110["X"],RMS_110["Y"],RMS_110["Z"], s=300, color="green")
    ax.scatter3D(RMS_60["X"], RMS_60["Y"], RMS_60["Z"], s=300, color="red")
    ax.scatter3D(RMS_OFF["X"], RMS_OFF["Y"], RMS_OFF["Z"], s=300,  color="blue")
    plt.title("Feature extraction")
    plt.xlabel("X_RMS")
    plt.ylabel("Y_RMS")
    ax.set_zlabel("Z_RMS")
    ax.legend(["110 watts","60 watts","off"])

    # show plot
    plt.show()

