from data_operations import *
from visualization import *
'''
file_names=get_file_names("/Test_data")

data=read_data("Test_data/",file_names)

time=create_time(data,10)

# raw_data_plots(time, data)

calculate_RMS(data)

plot_RMS(data)
'''
rawData=Data()
rawData.get_file_names("/Test_data")
rawData.read_data("Test_data/")

rawData.calculate_RMS(rawData.raw_data)

plt.figure(1, figsize=(10, 10))
rawData.plot_RMS(rawData.rms_data)

plt.figure(2, figsize=(10, 10))
plt.subplot(3,1,1)
rawData.plot_1D(rawData.rms_data,"X RMS")
plt.title("X RMS")
plt.subplot(3,1,2)
rawData.plot_1D(rawData.rms_data,"Y RMS")
plt.title("Y RMS")
plt.subplot(3,1,3)
rawData.plot_1D(rawData.rms_data,"Z RMS")
plt.title("Z RMS")

plt.figure(3, figsize=(10, 10))
plt.subplot(3,1,1,)
rawData.plot_2D(rawData.rms_data,"X RMS", "Y RMS")
plt.title("X RMS")
plt.subplot(3,1,2)
rawData.plot_2D(rawData.rms_data,"X RMS", "Z RMS")
plt.title("Y RMS")
plt.subplot(3,1,3)
rawData.plot_2D(rawData.rms_data,"Y RMS", "Z RMS")
plt.title("Z RMS")

# rawData.create_time(rawData.data, 10)

# rawData.raw_data_plots(rawData.data)

# rawData.calculate_RMS(rawData.data)

# rawData.plot_RMS(rawData.data)
