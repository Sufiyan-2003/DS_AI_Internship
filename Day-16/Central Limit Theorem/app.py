import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

population = np.random.exponential(scale=2, size=10000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (CLT)")
plt.show()
