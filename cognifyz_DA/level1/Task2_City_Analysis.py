import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")

print("=" * 60)
print("LEVEL 1 - TASK 2 : CITY ANALYSIS")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nChecking Missing Values in City:")
print(df["City"].isnull().sum())

city_count = df["City"].value_counts()

print("\nTop 10 Cities with Maximum Restaurants:\n")
print(city_count.head(10))

top_city = city_count.idxmax()
top_count = city_count.max()

print("\nCity with Maximum Restaurants:")
print(top_city)

print("\nNumber of Restaurants:")
print(top_count)

city_rating = (
    df.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 Cities Based on Average Rating:\n")
print(city_rating.head(10))

os.makedirs("graph", exist_ok=True)

plt.figure(figsize=(10,6))

city_count.head(10).plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graph/Task2_City_Analysis.png")

plt.show()

print("\nGraph Saved Successfully!")

print("\nTask 2 Completed Successfully!")