import pandas as pd

df = pd.read_csv("Day-10/The Integrity Audit/customer_orders.csv")

print("Shape before cleaning:", df.shape)

print("\nMissing values report:")
print(df.isna().sum())

df = df.fillna(df.median(numeric_only=True))

df = df.drop_duplicates()

print("\nShape after cleaning:", df.shape)
