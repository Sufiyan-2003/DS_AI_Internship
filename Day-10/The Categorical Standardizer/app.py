import pandas as pd

df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "New York"]
})

df["Location"] = df["Location"].str.strip().str.title()

print("Unique locations after cleaning:")
print(df["Location"].unique())
