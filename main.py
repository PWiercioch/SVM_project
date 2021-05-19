from data_operations import *
from visualization import *
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# 3 labels
'''
# Read data
rawData=Data()
rawData.get_file_names("/All_data")
rawData.read_data("All_data/")
rawData.calculate_RMS(rawData.raw_data)

# Plot raw data
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

# Feature extraction
rawData.window(rawData.raw_data, 60, 1)
rawData.calculate_RMS(rawData.window_data)

# Plot extracted data
plt.figure(4, figsize=(10, 10))
rawData.plot_RMS(rawData.rms_data)

plt.figure(5, figsize=(10, 10))
plt.subplot(3,1,1)
rawData.plot_1D(rawData.rms_data,"X RMS")
plt.title("X RMS")
plt.subplot(3,1,2)
rawData.plot_1D(rawData.rms_data,"Y RMS")
plt.title("Y RMS")
plt.subplot(3,1,3)
rawData.plot_1D(rawData.rms_data,"Z RMS")
plt.title("Z RMS")

plt.figure(6, figsize=(10, 10))
plt.subplot(3,1,1,)
rawData.plot_2D(rawData.rms_data,"X RMS", "Y RMS")
plt.title("X RMS")
plt.subplot(3,1,2)
rawData.plot_2D(rawData.rms_data,"X RMS", "Z RMS")
plt.title("Y RMS")
plt.subplot(3,1,3)
rawData.plot_2D(rawData.rms_data,"Y RMS", "Z RMS")
plt.title("Z RMS")

# SVM implememntation

# Data preparation - delete columns: Label, Dataset
X=rawData.rms_data.drop(["Label","Dataset","X RMS"], axis=1)
Y=rawData.rms_data["Label"]

# Split data intot training and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20)

# Classifier setup
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

# Classify data
y_pred = svclassifier.predict(X_test)

# Confusion matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
'''

# 2 labels - 2 powers
# Read data
rawData=Data()
rawData.get_file_names("/All_data")
rawData.read_data("All_data/")
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
plt.xlabel("X RMS")
plt.ylabel("Y RMS")
plt.subplot(3,1,2)
rawData.plot_2D(rawData.rms_data,"X RMS", "Z RMS")
plt.xlabel("X RMS")
plt.ylabel("Z RMS")
plt.subplot(3,1,3)
rawData.plot_2D(rawData.rms_data,"Y RMS", "Z RMS")
plt.xlabel("Y RMS")
plt.ylabel("Z RMS")

# Feature extraction
rawData.window(rawData.raw_data, 60, 1)
rawData.calculate_RMS(rawData.window_data)

# Plot extracted data
plt.figure(4, figsize=(10, 10))
rawData.plot_RMS(rawData.rms_data)

plt.figure(5, figsize=(10, 10))
plt.subplot(3,1,1)
rawData.plot_1D(rawData.rms_data,"X RMS")
plt.title("X RMS")
plt.subplot(3,1,2)
rawData.plot_1D(rawData.rms_data,"Y RMS")
plt.title("Y RMS")
plt.subplot(3,1,3)
rawData.plot_1D(rawData.rms_data,"Z RMS")
plt.title("Z RMS")

plt.figure(6, figsize=(10, 10))
plt.subplot(3,1,1,)
rawData.plot_2D(rawData.rms_data,"X RMS", "Y RMS")
plt.title("X RMS")
plt.subplot(3,1,2)
rawData.plot_2D(rawData.rms_data,"X RMS", "Z RMS")
plt.title("Y RMS")
plt.subplot(3,1,3)
rawData.plot_2D(rawData.rms_data,"Y RMS", "Z RMS")
plt.title("Z RMS")

# SVM implememntation

# Data preparation - delete columns: Label, Dataset
X=rawData.rms_data.drop(["Label","Dataset"], axis=1)
Y=rawData.rms_data["Label"]

# Split data intot training and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20)

# Classifier setup
svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, y_train)

# Classify data
y_pred = svclassifier.predict(X_test)

# Confusion matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

'''
# Plot classifier
x1=np.linspace(0.4,1.4)
y1=np.linspace(0.4,1.4)

y1=np.array((-svclassifier.intercept_[0]-svclassifier.coef_[0][0]*x1)/svclassifier.coef_[0][1]) # Zrozumiec ta funkcje
y2=np.array((-svclassifier.intercept_[1]-svclassifier.coef_[1][0]*x1)/svclassifier.coef_[1][1])
y3=np.array((-svclassifier.intercept_[2]-svclassifier.coef_[2][0]*x1)/svclassifier.coef_[2][1])

X_train["Label"]=y_train
X_test["Label"]=y_test

plt.figure(7) # dziala gdy wylaczone z rms
plot_data = X_train[X_train["Label"] == "110"]
plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30,c="#1f77b4")
plot_data = X_train[X_train["Label"] == "60_"]
plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30,c="#ff7f0e")
plot_data = X_train[X_train["Label"] == "OFF"]
plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30,c="#2ca02c")
plt.plot(x1,y1+0.0025, c="#ff7f0e", linewidth=3)
plt.plot(x1,y1-0.0025, c="#1f77b4", linewidth=3)
plt.plot(x1,y2-0.0045, c="#2ca02c", linewidth=3)
plt.plot(x1,y2+0.0045, c="#1f77b4", linewidth=3)
plt.plot(x1,y3+0.0025, c="#ff7f0e", linewidth=3)
plt.plot(x1,y3-0.0025, c="#2ca02c", linewidth=3)
plt.ylim([1.5,2.5])
plt.title("Train data")
plt.xlabel("X RMS")
plt.ylabel("Y RMS")
plt.legend(X_train["Label"].unique())


plt.figure(8) # dziala gdy wylaczone z rms
plot_data = X_test[X_test["Label"] == "110"]
plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30,c="#1f77b4")
plot_data = X_test[X_test["Label"] == "60_"]
plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30,c="#ff7f0e")
plot_data = X_test[X_test["Label"] == "OFF"]
plt.scatter(plot_data["X RMS"], plot_data["Y RMS"], s=30,c="#2ca02c")
plt.plot(x1,y1+0.0025, c="#ff7f0e", linewidth=3)
plt.plot(x1,y1-0.0025, c="#1f77b4", linewidth=3)
plt.plot(x1,y2-0.0045, c="#2ca02c", linewidth=3)
plt.plot(x1,y2+0.0045, c="#1f77b4", linewidth=3)
plt.plot(x1,y3+0.0025, c="#ff7f0e", linewidth=3)
plt.plot(x1,y3-0.0025, c="#2ca02c", linewidth=3)
plt.ylim([1.5,2.5])
plt.title("Train data")
plt.xlabel("X RMS")
plt.ylabel("Y RMS")
plt.legend(X_train["Label"].unique())

x1=np.linspace(0.4,1.4)
y1=np.linspace(1.4,2.1)
x2,y2=np.meshgrid(x1,y1)
z=lambda x1,y1:((-svclassifier.intercept_[0]-svclassifier.coef_[0][0]*x1-svclassifier.coef_[0][1]*y1)/svclassifier.coef_[0][2])

fig = plt.figure(9) # dziala gdy wlaczone z rms
ax  = fig.add_subplot(111, projection='3d')
data=rawData.rms_data
for label in data["Label"].unique():
    plot_data = data[data["Label"] == label]
    ax.scatter3D(plot_data["X RMS"], plot_data["Y RMS"], plot_data["Z RMS"], s=50)
ax.plot_surface(x2, y2, z(x2,y2), color="k", shade=0.5)
plt.xlabel("X_RMS")
plt.ylabel("Y_RMS")
ax.set_zlabel("Z_RMS")
'''
