import numpy as np
import pandas as pd

data = np.random.normal(50, 10, 100)
data = np.append(data, [120, 130])  

df = pd.DataFrame(data, columns=["Values"])

mean = df["Values"].mean()
std = df["Values"].std()

df["Z_Score"] = (df["Values"] - mean) / std

outliers = df[np.abs(df["Z_Score"]) > 3]

print("Mean:", mean)
print("Standard Deviation:", std)
print("Outliers:")
print(outliers)
