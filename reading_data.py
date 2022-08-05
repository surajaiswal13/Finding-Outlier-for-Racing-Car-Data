import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

url = "C:\\Users\\User\\Downloads\\Geolocation - Trip with a jump.csv"
df = pd.read_csv(url, usecols=["lat", "lng"])

######## Plotting the Graph ########

# df.boxplot(column=["lat", "lng"])
df.plot(kind = 'scatter', x = 'lat', y = 'lng')

plt.show()

######## 1nd Approach ########

# Assuming a Distancefrom which the value cannot be greater 

for i in range(len(df) - 1):

    if df["lat"][i] - df["lat"][i + 1] > 0.05:

        print(df["lat"][i + 1], "is an Outlier")

    if df["lng"][i + 1] - df["lng"][i] > 0.05:

        print(df["long"][i + 1], "is an Outlier")

######## 2nd Approach ######## [ Not Applicable ]

# Using Inter-Quartile Range

# f_quantile = np.quantile(df["lat"], .25)
# t_quantile = np.quantile(df["lat"], .75)
# print("f_quantile", f_quantile)
# print("t_quantile", t_quantile)

# for i in range(len(df) - 1):

#     if df["lat"][i] < f_quantile or df["lat"][i] > t_quantile:
#         print("Yess")
#         print(df["lat"][i])
    
    # else:
        # print("yess")
        # print(df["lat"][i])

  
# Interquartile range (IQR)
# print("arr : ", df["lat"]) 
# print("Q2 quantile of arr : ", np.quantile(df["lat"], .50))
# print("Q1 quantile of arr : ", np.quantile(df["lat"], .25))
# print("Q3 quantile of arr : ", np.quantile(df["lat"], .75))
# print("100th quantile of arr : ", np.quantile(df["lat"], .1)) 