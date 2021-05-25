from data_operations import *

# Read data for all labels
all_labels=Data()
all_labels.get_file_names("/All_data")
all_labels.read_data("All_data/")
all_labels.calculate_RMS(all_labels.raw_data)

# Read data for 2 Labels
two_labels=Data()
two_labels.get_file_names("/2_Labels")
two_labels.read_data("2_Labels/")
two_labels.calculate_RMS(two_labels.raw_data)

# Plot non-split data for all labels
plt.figure(1, figsize=(10, 10))
all_labels.plot_RMS(all_labels.rms_data)
plt.title("Non-split data for all labels")
plt.figure(2, figsize=(10, 10))
draw_1D(all_labels)
plt.suptitle("1D representation for non-split all labels")
plt.figure(3, figsize=(10, 10))
draw_2D(all_labels)
plt.suptitle("2D representation for non-split all labels")

# Plot non-split data for 2 labels
plt.figure(4, figsize=(10, 10))
two_labels.plot_RMS(two_labels.rms_data)
plt.title("Non-split data for 2 labels")
plt.figure(5, figsize=(10, 10))
draw_1D(two_labels)
plt.suptitle("1D representation for non-split 2 labels")
plt.figure(6, figsize=(10, 10))
draw_2D(two_labels)
plt.suptitle("2D representation for non-split 2 labels")

# Split data by moving window for all labels
all_labels.window(all_labels.raw_data, 60, 10)
all_labels.calculate_RMS(all_labels.window_data)

# Split data by moving window for 2 labels
two_labels.window(two_labels.raw_data, 60, 10)
two_labels.calculate_RMS(two_labels.window_data)

# Plot split data for all labels
plt.figure(7, figsize=(10, 10))
all_labels.plot_RMS(all_labels.rms_data)
plt.title("Split data for all labels")
plt.figure(8, figsize=(10, 10))
draw_1D(all_labels)
plt.suptitle("1D representation for split all labels")
plt.figure(9, figsize=(10, 10))
draw_2D(all_labels)
plt.suptitle("2D representation for split all labels")

# Plot split data for 2 labels
plt.figure(10, figsize=(10, 10))
all_labels.plot_RMS(two_labels.rms_data)
plt.title("Split data for all labels")
plt.figure(11, figsize=(10, 10))
draw_1D(two_labels)
plt.suptitle("1D representation for split 2 labels")
plt.figure(12, figsize=(10, 10))
draw_2D(two_labels)
plt.suptitle("2D representation for split 2 labels")

# SVM implememntation

# all labels, 2 dimnsions
print("Classification \n All labels \n 2 dimensions \n linear classifier")
svclassifier, X_train, X_test, y_train, y_test=classify_data(all_labels.rms_data, 'linear', drop_Z_rms=True)
plt.figure(13)
plot_classifier_2D(X_train,y_train,svclassifier)
plt.title("All labels \n 2 dimensons: X RMS, Y RMS \n Train set")
plt.figure(14)
plot_classifier_2D(X_test,y_test,svclassifier)
plt.title("All labels \n 2 dimensons: X RMS, Y RMS \n Test set")

# all labels, 3 dimnsions
print("Classification \n All labels \n 3 dimensions \n linear classifier")
svclassifier, X_train, X_test, y_train, y_test=classify_data(all_labels.rms_data, 'linear', drop_Z_rms=False)

# 2 labels, 2 dimnsions
print("Classification \n 2 labels \n 2 dimensions \n linear classifier")
svclassifier, X_train, X_test, y_train, y_test=classify_data(two_labels.rms_data, 'linear', drop_Z_rms=True)
plt.figure(15)
plot_classifier_2D(X_train,y_train,svclassifier)
plt.title("2 labels \n 2 dimensons: X RMS, Y RMS \n Train set")
plt.figure(16)
plot_classifier_2D(X_test,y_test,svclassifier)
plt.title("2 labels \n 2 dimensons: X RMS, Y RMS \n Test set")

# 2 labels, 3 dimnsions
print("Classification \n 2 labels \n 3 dimensions \n linear classifier")
svclassifier, X_train, X_test, y_train, y_test=classify_data(two_labels.rms_data, 'linear', drop_Z_rms=False)
fig = plt.figure(17)
plot_classifier_3D(X_train,y_train,svclassifier,fig)
plt.title("2 labels \n 3 dimensons: X RMS, Y RMS, Z RMS \n Train set")
fig = plt.figure(18)
plot_classifier_3D(X_test,y_test,svclassifier,fig)
plt.title("2 labels \n 3 dimensons: X RMS, Y RMS, Z RMS \n Test set")

print("Classification \n 2 labels \n 3 dimensions \n 5 degree polynomial classifier")
svclassifier, X_train, X_test, y_train, y_test=classify_data(all_labels.rms_data, 'poly', 5, drop_Z_rms=False)
