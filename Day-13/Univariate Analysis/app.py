import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

df = pd.read_csv("Day-13/Univariate Analysis/housing.csv")

plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

print("Skewness:", skew(df["Price"]))
print("Kurtosis:", kurtosis(df["Price"]))

plt.figure(figsize=(8,5))
sns.countplot(x="City", data=df)
plt.title("Count of Houses by City")
plt.xticks(rotation=45)
plt.show()
