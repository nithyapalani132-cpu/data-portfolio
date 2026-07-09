import pandas as pd
import matplotlib.pyplot as plt
import os

# Read dataset from the project root
df = pd.read_csv("Dataset.csv")

print("=" * 60)
print("LEVEL 1 - TASK 1 : TOP CUISINES")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values in Cuisines:")
print(df["Cuisines"].isnull().sum())

# Remove missing values
df = df.dropna(subset=["Cuisines"])

# Split multiple cuisines into separate rows
cuisines = (
    df["Cuisines"]
    .str.split(",")
    .explode()
    .str.strip()
)

# Count cuisines
cuisine_count = cuisines.value_counts()

# Top 3 cuisines
top3 = cuisine_count.head(3)

print("\nTop 3 Most Common Cuisines:")
print(top3)

print("\nPercentage of Restaurants Serving Top 3 Cuisines:")

total_restaurants = len(df)

for cuisine, count in top3.items():
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine} : {percentage:.2f}%")

# Create graph folder if it doesn't exist
os.makedirs("graph", exist_ok=True)

# Plot graph
plt.figure(figsize=(8, 5))
plt.bar(top3.index, top3.values)

plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save graph
plt.savefig("graph/Task1_Top_Cuisines.png")

plt.show()

print("\nTask 1 Completed Successfully!")
print("Graph saved in 'graph' folder.")