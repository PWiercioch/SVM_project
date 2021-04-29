from data_operations import *
from visualization import *

file_names=get_file_names("/Test_data")

data=read_data("Test_data/",file_names)

time=create_time(data,10)

# raw_data_plots(time, data)

calculate_RMS(data)

plot_RMS(data)
