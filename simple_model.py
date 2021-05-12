import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create data
mice=pd.DataFrame({"Weight":[2, 4, 3, 5, 20, 18, 16, 7, 1, 14, 22, 24, 13], "Obese":["no", "no", "no", "no", "yes", "yes", "yes", "no", "no", "no", "yes", "yes", "yes"]})

# select obese mice
mice_obese=mice[mice["Obese"]=="yes"]
mice_not_obese=mice[mice["Obese"]=="no"]

# draw data
plt.figure(1)
plt.scatter(mice_obese["Weight"],np.zeros(len(mice_obese["Weight"])), s=200, c="r") # plot weight at constant y=0
plt.scatter(mice_not_obese["Weight"],np.zeros(len(mice_not_obese["Weight"])), s=200, c="g")
plt.grid()
plt.xlabel("Weight")
plt.title("Data")
plt.legend(["Obese","Not obese"])

# Maximal Margin classifier
lb=max(mice_not_obese["Weight"])
ub=min(mice_obese["Weight"])
max_margin=(lb+ub)/2

plt.figure(2)
plt.plot([max_margin, max_margin],[-1, 1])
plt.scatter(mice_obese["Weight"],np.zeros(len(mice_obese["Weight"])), s=200, c="r") # plot weight at constant y=0
plt.scatter(mice_not_obese["Weight"],np.zeros(len(mice_not_obese["Weight"])), s=200, c="g")
plt.grid()
plt.xlabel("Weight")
plt.title("Maximum margi classifier")
plt.legend(["Classifier", "Obese","Not obese"])

# Support vector classifier
results=pd.DataFrame({"Margin":[],"Accuracy":[], "Support vectors":[]})
i=1
for o in mice_obese["Weight"]:
    for n in mice_not_obese["Weight"]:
        margin=(n+o)/2
        if margin not in results["Margin"].values:
            acc=0
            sv=0
            for mouse in mice.iterrows():
                if mouse[1]["Weight"]<=margin and mouse[1]["Obese"]=="no":
                    acc+=1
                elif mouse[1]["Weight"]>=margin and mouse[1]["Obese"]=="yes":
                    acc+=1

                if abs(mouse[1]["Weight"]-margin)<abs(n-o)/2:
                    sv+=1

            temp=pd.DataFrame({"Margin":[margin],"Accuracy":[acc/len(mice)], "Support vectors":[sv]})

            plt.figure(i)
            plt.plot([margin, margin], [-1, 1])
            plt.scatter(mice_obese["Weight"], np.zeros(len(mice_obese["Weight"])), s=200, c="r")
            plt.scatter(mice_not_obese["Weight"], np.zeros(len(mice_not_obese["Weight"])), s=200, c="g")
            plt.plot([n, n], [-1, 1], c="k")
            plt.plot([o, o], [-1, 1], c="k")
            plt.grid()
            plt.xlabel("Weight")
            plt.title("Soft classifier = "+str(margin))
            plt.legend(["Classifier", "Obese", "Not obese"])
            plt.annotate("Accuracy = "+str(temp["Accuracy"].values[0])+"\nSupport Vectors = "+str(temp["Support vectors"].values[0]),[0,-1])

            i+=1

            results=results.append(temp, ignore_index=False)
