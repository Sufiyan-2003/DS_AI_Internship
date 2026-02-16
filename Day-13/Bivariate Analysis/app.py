import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Day-13/Bivariate Analysis/housing (1).csv")

plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("SquareFootage vs Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="City", y="Price", data=df)
plt.xticks(rotation=45)
plt.title("City vs Price")
plt.show()

print("Observation: As SquareFootage increases, Price tends to increase.")
