import pandas as pd

usernames = pd.Series([" Alice ", "BOB", "Charlie_Data ", "daisy"])

cleaned_usernames = usernames.str.strip().str.lower()

contains_a = cleaned_usernames.str.contains("a")

print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nContains letter 'a':")
print(contains_a)
