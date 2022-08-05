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

######## First Approach ########

# Using Inter-Quartile Range

for i in range(len(df) - 1):

    if np.quantile(df["lat"], .25) < df["lat"][i] <= np.quantile(df["lat"], .25):

        pass
    
    else:
        print("yess")
        print(df["lat"][i])

# # Interquartile range (IQR)
# print("arr : ", df["lat"]) 
# print("Q2 quantile of arr : ", np.quantile(df["lat"], .50))
# print("Q1 quantile of arr : ", np.quantile(df["lat"], .25))
# print("Q3 quantile of arr : ", np.quantile(df["lat"], .75))
# print("100th quantile of arr : ", np.quantile(df["lat"], .1)) 

for i in range(len(df) - 1):

    if df["lat"][i] - df["lat"][i + 1] > 0.05:

        # print(f"{df["lat"][i]}, {df["lat"][i + 1]}, index, {i}")
        # print("YES")
        # print(f"Index, {i}")
        # print(df["lat"][i])
        # print(df["lat"][i + 1])
        print(df["lat"][i + 1], "is an Outlier")


        # df["lat"][i + 1] = 0
        # print(df["lat"][i + 1])

    if df["lng"][i + 1] - df["lng"][i] > 0.05:

    #     # print(f"{df["lat"][i]}, {df["lat"][i + 1]}, index, {i}")
        # print("YES")
        # print(f"Index, {i}")
        # print(df["lng"][i])
        # print(df["lat"][i])
        # print(df["lng"][i + 1])
        print(df["long"][i + 1], "is an Outlier")

    # pass

# import scipy.stats as stats

# stats.zscore(df)

# print(stats.zscore(df))

# df["z_score_lat"] = stats.zscore(df["lat"])
# df["z_score_lng"] = stats.zscore(df["lng"])

# print(df)

# df.to_csv("abc.csv")

# for i in df["z_score_lat"]:

#     # print("Yes")
#     if i > 3:
#         print("Yes")