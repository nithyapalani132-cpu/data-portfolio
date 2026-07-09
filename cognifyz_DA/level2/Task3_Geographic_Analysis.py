import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")

print("LEVEL 2 - TASK 3 : GEOGRAPHIC ANALYSIS")
print("=" * 50)

print("\nTotal Restaurants:")
print(len(df))

print("\nTop 10 Cities with Restaurants:\n")

city = df["City"].value_counts().head(10)

print(city)

os.makedirs("graph", exist_ok=True)

plt.figure(figsize=(10,5))

plt.bar(city.index, city.values)

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("graph/Level2_Task3_Geographic_Analysis.png")

plt.show()

print("\nTask Completed Successfully!")