import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Dataset.csv")

print("=" * 60)
print("LEVEL 1 - TASK 4 : ONLINE DELIVERY ANALYSIS")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values in Online Delivery Column:")
print(df["Has Online delivery"].isnull().sum())

delivery_count = df["Has Online delivery"].value_counts()

print("\nOnline Delivery Availability:\n")
print(delivery_count)

total = delivery_count.sum()

print("\nPercentage of Restaurants:\n")

for status, count in delivery_count.items():
    percentage = (count / total) * 100
    print(f"{status} : {percentage:.2f}%")

rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()

print("\nAverage Rating Based on Online Delivery:\n")
print(rating)

os.makedirs("graph", exist_ok=True)

plt.figure(figsize=(6,5))

plt.pie(
    delivery_count.values,
    labels=delivery_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Restaurants Offering Online Delivery")

plt.savefig("graph/Task4_Online_Delivery.png")

plt.show()

print("\nGraph Saved Successfully!")
print("Task 4 Completed Successfully!")