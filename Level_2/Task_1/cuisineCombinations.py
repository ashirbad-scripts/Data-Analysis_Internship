import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop missing cuisine or rating entries
df = df.dropna(subset=["Cuisines", "Aggregate rating"])

# Filter only multi-cuisine entries (i.e., with commas)
multi_df = df[df["Cuisines"].str.contains(",")].copy()

# Count most common cuisine combinations (as-is, raw string)
combo_counts = multi_df["Cuisines"].value_counts().head(10)

print("\n🔹 Top 10 Most Common Cuisine Combinations:\n")
print(combo_counts)

# Get average rating for top 10 combinations
combo_ratings = {}
for combo in combo_counts.index:
    avg_rating = multi_df[multi_df["Cuisines"] == combo]["Aggregate rating"].mean().round(2)
    combo_ratings[combo] = avg_rating

# Print combination + avg rating
print("\n🔹 Average Rating of Top Combinations:\n")
for combo, rating in combo_ratings.items():
    print(f"{combo}: {rating}")

# Plot
plt.figure(figsize=(10, 6))
plt.barh(list(combo_ratings.keys()), list(combo_ratings.values()), color="#6B5B95")
plt.xlabel("Average Rating")
plt.title("Top 10 Cuisine Combinations by Avg Rating")
plt.tight_layout()
plt.savefig("Outputs/Level_2_Output/01_cuisine_combinations_rating.png")
plt.show()
