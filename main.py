from data_operations import *

# 2 labels - 2 powers
# Read data
rawData=Data()
rawData.get_file_names("/All_data")
rawData.read_data("All_data/")
rawData.calculate_RMS(rawData.raw_data)

plt.figure(1, figsize=(10, 10))
rawData.plot_RMS(rawData.rms_data)

plt.figure(2, figsize=(10, 10))
draw_1D(rawData)

plt.figure(3, figsize=(10, 10))
draw_2D(rawData)

# Feature extraction
rawData.window(rawData.raw_data, 60, 1)
rawData.calculate_RMS(rawData.window_data)

# Plot extracted data
plt.figure(4, figsize=(10, 10))
rawData.plot_RMS(rawData.rms_data)

plt.figure(5, figsize=(10, 10))
draw_1D(rawData)

plt.figure(6, figsize=(10, 10))
draw_2D(rawData)

# SVM implememntation

svclassifier, X_train, X_test, y_train, y_test=classify_data(rawData.rms_data, 'linear', drop_Z_rms=True)

plt.figure(7)
plot_classifier_2D(X_train,y_train,svclassifier)
plt.figure(8)
plot_classifier_2D(X_test,y_test,svclassifier)

fig = plt.figure(9)
#plot_classifier_3D(rawData.rms_data,svclassifier)

