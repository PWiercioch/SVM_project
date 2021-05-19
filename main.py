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

rawData.plot_RMS(rawData.rms_data)

# rawData.create_time(rawData.data, 10)

# rawData.raw_data_plots(rawData.data)

# rawData.calculate_RMS(rawData.data)

# rawData.plot_RMS(rawData.data)
