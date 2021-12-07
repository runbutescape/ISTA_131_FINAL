# numpy is needed for x-tick label positions
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import sys

def main():

    ### This is a local path for my computer, change if vgsales.csv is located elsewhere
    data = pd.read_csv("C:\\Users\\LANBox\\Desktop\\ISTA_131\\vgsales.csv")
    ###
    df = pd.DataFrame(data)
    df.sort_values(by=["Year"], inplace=True, ascending=False)

    result = pd.DataFrame(data = df['NA_Sales'], index = df["Year"])
    plt.plot(result.index, result['NA_Sales'], color = 'r', label = "NA Sales")

    result = pd.DataFrame(data = df['EU_Sales'], index = df["Year"])
    plt.plot(result.index, result['EU_Sales'], color = 'g', label = "EU Sales")

    result = pd.DataFrame(data = df['JP_Sales'], index = df["Year"])
    plt.plot(result.index, result['JP_Sales'], color = 'b', label = "JP Sales")

    plt.title("Regional Video Game Sales Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Sales (millions)")
    plt.legend(loc = 'upper left')

    plt.show()

main()