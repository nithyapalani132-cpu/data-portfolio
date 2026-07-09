import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

print("Restaurant Ratings Analysis")

print("\nAverage Rating:")
print(df["Aggregate rating"].mean())

print("\nHighest Rating:")
print(df["Aggregate rating"].max())

print("\nLowest Rating:")
print(df["Aggregate rating"].min())

plt.hist(df["Aggregate rating"])
plt.title("Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.show()