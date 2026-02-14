import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Home"]
sales = [300, 450, 200]

months = [1, 2, 3, 4, 5]
revenue = [2000, 3500, 4000, 6000, 7500]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()
