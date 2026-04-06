import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("results.csv")

data_types = data["DataType"].unique()

for dtype in data_types:
    subset = data[data["DataType"] == dtype]
    
    algorithms = subset["Algorithm"].unique()
    
    for algo in algorithms:
        temp = subset[subset["Algorithm"] == algo]
        plt.plot(temp["Size"], temp["Time"], label=algo)

    plt.title(dtype + " Data Performance Comparison")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time")
    plt.legend()
    plt.show()