import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")

print("LEVEL 2 - TASK 4 : RESTAURANT CHAINS")
print("=" * 50)

chain = df["Restaurant Name"].value_counts()

chains = chain[chain > 1].head(10)

print("\nTop Restaurant Chains:\n")
print(chains)

os.makedirs("graph", exist_ok=True)

plt.figure(figsize=(10,5))

plt.bar(chains.index, chains.values)

plt.title("Top Restaurant Chains")
plt.xlabel("Restaurant Name")
plt.ylabel("Number of Branches")

plt.xticks(rotation=60)

plt.tight_layout()

plt.savefig("graph/Level2_Task4_Restaurant_Chains.png")

plt.show()

print("\nTask Completed Successfully!")