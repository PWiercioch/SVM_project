from data_operations import *
from visualization import *

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

rawData.window(rawData.raw_data, 30, 1)
