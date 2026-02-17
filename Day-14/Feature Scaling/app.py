import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [25, 30, 35, 40, 45],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

standard_scaler = StandardScaler()
df_standard = standard_scaler.fit_transform(df)

minmax_scaler = MinMaxScaler()
df_minmax = minmax_scaler.fit_transform(df)

df_standard = pd.DataFrame(df_standard, columns=df.columns)
df_minmax = pd.DataFrame(df_minmax, columns=df.columns)

print("Standardized Data:")
print(df_standard)

print("\nNormalized Data:")
print(df_minmax)

plt.hist(df["Salary"], alpha=0.5, label="Original")
plt.hist(df_standard["Salary"], alpha=0.5, label="Standardized")
plt.hist(df_minmax["Salary"], alpha=0.5, label="Normalized")
plt.legend()
plt.title("Salary Before and After Scaling")
plt.show()
