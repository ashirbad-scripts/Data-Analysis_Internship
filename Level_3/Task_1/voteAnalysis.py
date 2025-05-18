import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Load dataset
df = pd.read_csv("Dataset.csv")

# Clean and validate data
df = df.dropna(subset=["Restaurant Name", "Aggregate rating", "Votes"])
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")
df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors="coerce")
df = df[(df["Votes"] > 0) & (df["Aggregate rating"].between(0, 5))]

# Filter to remove extreme outliers
filtered_df = df[df["Votes"] <= 5000].copy()
filtered_df["log_votes"] = np.log10(filtered_df["Votes"])

# Top and Bottom 5
print("\n🔹 Top 5 Restaurants with Highest Votes:\n")
print(df.sort_values("Votes", ascending=False).head(5)[["Restaurant Name", "Votes", "Aggregate rating"]])

print("\n🔹 Bottom 5 Restaurants with Lowest (Non-Zero) Votes:\n")
print(df.sort_values("Votes").head(5)[["Restaurant Name", "Votes", "Aggregate rating"]])

# Correlation
correlation = df["Votes"].corr(df["Aggregate rating"])
print(f"\n🔹 Correlation between Votes and Rating: {correlation:.3f}")

# Ensure output directory
os.makedirs("Outputs", exist_ok=True)

# Plot
plt.figure(figsize=(8, 5))
sns.regplot(
    x="log_votes", y="Aggregate rating",
    data=filtered_df,
    scatter_kws={"alpha": 0.4, "s": 10},
    line_kws={"color": "red"}
)
plt.title("Votes vs Aggregate Rating (Log10 Scale)")
plt.xlabel("Votes (log10)")
plt.ylabel("Aggregate Rating")
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("Outputs/Level_3_outputs/01_votes_vs_rating.png")
plt.show()
