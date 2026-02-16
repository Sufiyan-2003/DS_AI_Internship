import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Day-13/Correlation & Outliers/housing_correlation.csv")

correlation = df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

for col in correlation.columns:
    for row in correlation.index:
        if col != row and abs(correlation.loc[row, col]) > 0.8:
            print(f"High correlation between {row} and {col}: {correlation.loc[row, col]}")

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price (Outlier Detection)")
plt.show()
