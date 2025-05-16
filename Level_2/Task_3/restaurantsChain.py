import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop missing restaurant names or ratings
df = df.dropna(subset=["Restaurant Name", "Aggregate rating", "Votes"])

# Group by restaurant name and count occurrences
chain_counts = df["Restaurant Name"].value_counts()

# Filter potential chains (appearing more than once)
chains = chain_counts[chain_counts > 1]
print(f"\n🔹 Total Restaurant Chains Found: {len(chains)}\n")
print("Top 10 Most Frequent Restaurant Chains:\n")
print(chains.head(10))

# Analyze ratings and votes for top 10 chains
top_chains = chains.head(10).index
avg_ratings = []
avg_votes = []

for name in top_chains:
    sub_df = df[df["Restaurant Name"] == name]
    avg_ratings.append(sub_df["Aggregate rating"].mean().round(2))
    avg_votes.append(sub_df["Votes"].mean().round(1))

# Plot ratings
plt.figure(figsize=(10, 5))
plt.bar(top_chains, avg_ratings, color='#88B04B')
plt.title("Avg Ratings of Top 10 Restaurant Chains")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Outputs/Level_2_Output/03_top_chains_avg_ratings.png")
plt.show()

# Plot votes
plt.figure(figsize=(10, 5))
plt.bar(top_chains, avg_votes, color='#F7CAC9')
plt.title("Avg Votes of Top 10 Restaurant Chains")
plt.ylabel("Average Votes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Outputs/Level_2_Output/03_top_chains_avg_votes.png")
plt.show()
