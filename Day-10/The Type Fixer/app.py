import pandas as pd

df = pd.read_csv("Day-10/The Type Fixer/data.csv")

print("Before conversion:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nAfter conversion:")
print(df.dtypes)
