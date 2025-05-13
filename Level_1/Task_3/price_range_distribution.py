import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop missing price range values (if any)
df = df.dropna(subset=["Price range"])

# Count how many restaurants in each price range
price_counts = df["Price range"].value_counts().sort_index()

# Calculate percentage
total = len(df)
percentages = (price_counts / total * 100).round(2)

print("\n🔹 Price Range Distribution (% of Total Restaurants):\n")
for price, pct in percentages.items():
    print(f"Price Range {price}: {pct}%")

# Plot with distinct colors
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9']
plt.figure(figsize=(6, 4))
price_counts.plot(kind='bar', color=colors)
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Outputs/Level_1_outputs/03_price_range_distribution.png")
plt.show()
