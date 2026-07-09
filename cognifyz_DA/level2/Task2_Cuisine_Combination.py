import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")

print("LEVEL 2 - TASK 2 : CUISINE COMBINATION")
print("=" * 50)

df = df.dropna(subset=["Cuisines"])

top_combinations = df["Cuisines"].value_counts().head(10)

print("\nTop 10 Cuisine Combinations:\n")
print(top_combinations)

os.makedirs("graph", exist_ok=True)

plt.figure(figsize=(10,5))

plt.bar(top_combinations.index, top_combinations.values)

plt.title("Top 10 Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=60)

plt.tight_layout()

plt.savefig("graph/Level2_Task2_Cuisine_Combination.png")

plt.show()

print("\nTask Completed Successfully!")