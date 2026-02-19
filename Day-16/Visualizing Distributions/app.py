import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

heights = np.random.normal(170, 10, 1000)          
income = np.random.exponential(50000, 1000)       
scores = 100 - np.random.exponential(15, 1000)    

datasets = {
    "Heights (Normal)": heights,
    "Income (Right-Skewed)": income,
    "Scores (Left-Skewed)": scores
}

for name, data in datasets.items():
    mean = np.mean(data)
    median = np.median(data)

    plt.figure()
    sns.histplot(data, kde=True)
    plt.axvline(mean, color='red', linestyle='--', label="Mean")
    plt.axvline(median, color='green', linestyle='-', label="Median")
    plt.title(name)
    plt.legend()
    plt.show()

    print(name)
    print("Mean:", mean)
    print("Median:", median)
    print()
