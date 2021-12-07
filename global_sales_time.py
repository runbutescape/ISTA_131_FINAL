# numpy is needed for x-tick label positions
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import sys

def annual_sales(df, region):
    annual_sale = {}
    for i in df["Year"]:
        if i not in annual_sale:
            annual_sale[i] = 0
        else:
            annual_sale[i] += df.loc[df.Year == i, region].values[0]
    return annual_sale

def main():
    region_sales = ['NA_Sales', 'EU_Sales', 'JP_Sales']
    ### This is a local path for my computer, change if vgsales.csv is located elsewhere
    data = pd.read_csv("C:\\Users\\LANBox\\Desktop\\ISTA_131\\vgsales.csv")
    ###
    df = pd.DataFrame(data)
    df.sort_values(by=["Year"], inplace=True, ascending=True)

    na_sales = annual_sales(df, 'NA_Sales')
    plt.plot(na_sales.keys(), na_sales.values(), color = 'r', label = "NA Sales")

    eu_sales = annual_sales(df, 'EU_Sales')
    plt.plot(eu_sales.keys(), eu_sales.values(), color = 'g', label = "EU Sales")

    jp_sales = annual_sales(df, 'JP_Sales')
    plt.plot(jp_sales.keys(), jp_sales.values(), color = 'b', label = "JP Sales")

    plt.title("Top Selling Video Game Sales Over Time")
    plt.xlabel("Year")
    plt.ylabel("Sales per year (millions)")
    plt.legend(loc = 'upper left')

    plt.show()

main()