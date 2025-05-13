import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop rows with missing cuisine values
df = df.dropna(subset=["Cuisines"])

# Split multiple cuisines per restaurant into separate entries
all_cuisines = df["Cuisines"].str.split(", ").explode()

# Get top 3 cuisines
top_3 = all_cuisines.value_counts().head(3)

print("\n🔹 Top 3 Most Common Cuisines:\n")
print(top_3)

# Calculate percentage of restaurants offering each of the top cuisines
total_restaurants = len(df)
for cuisine in top_3.index:
    count = df["Cuisines"].str.contains(cuisine, case=False).sum()
    percentage = round((count / total_restaurants) * 100, 2)
    print(f"{cuisine}: {percentage}% of restaurants")

# Plot with distinct colors
colors = ['#FF6F61', '#6B5B95', '#88B04B']  # Red, Purple, Green
plt.figure(figsize=(6, 4))
top_3.plot(kind="bar", color=colors)
plt.title("Top 3 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.tight_layout()

# Storing Outputs in a folder
plt.savefig("Outputs/Level_1_outputs/01_top_cuisines.png")
plt.show()
