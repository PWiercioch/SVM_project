import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create data
mice=pd.DataFrame({"Weight":[2, 4, 3, 5, 10, 20, 18, 16], "Obese":["no", "no", "no", "no", "no", "yes", "yes", "yes"]})

# select obese mice
mice_obese=mice[mice["Obese"]=="yes"]
mice_not_obese=mice[mice["Obese"]=="no"]

# draw data
plt.figure(1)
plt.scatter(mice_obese["Weight"],np.ones(len(mice_obese["Weight"])), s=200, c="r") # plot weight at constant y=1
plt.scatter(mice_not_obese["Weight"],np.ones(len(mice_not_obese["Weight"])), s=200, c="g")
plt.grid()
plt.xlabel("Weight")
plt.legend(["Obese","Not obese"])

# Margin classifier