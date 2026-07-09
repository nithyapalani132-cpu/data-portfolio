import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")

print("=" * 60)
print("LEVEL 1 - TASK 3 : PRICE RANGE DISTRIBUTION")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values in Price Range:")
print(df["Price range"].isnull().sum())

price_count = df["Price range"].value_counts().sort_index()

print("\nNumber of Restaurants in Each Price Range:\n")
print(price_count)

total = price_count.sum()

print("\nPercentage of Restaurants in Each Price Range:\n")

for price, count in price_count.items():
    percentage = (count / total) * 100
    print(f"Price Range {price} : {percentage:.2f}%")

os.makedirs("graph", exist_ok=True)

plt.figure(figsize=(8,5))

plt.bar(
    price_count.index.astype(str),
    price_count.values,
    color="orange",
    edgecolor="black"
)

plt.title("Restaurant Distribution by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graph/Task3_Price_Range_Distribution.png")

plt.show()

print("\nGraph Saved Successfully!")
print("Task 3 Completed Successfully!")