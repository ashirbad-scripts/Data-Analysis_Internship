import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("Dataset.csv")
df = df.dropna(subset=["Restaurant Name", "Aggregate rating", "Votes"])

# Get top 10 by votes
top_voted = df.sort_values(by="Votes", ascending=False).head(10)

# Extract info
names = top_voted["Restaurant Name"]
votes = top_voted["Votes"]
ratings = top_voted["Aggregate rating"]

# Normalize ratings to match vote scale for bar comparison
rating_scaled = ratings * (votes.max() / 5)

# Bar positions
x = np.arange(len(names))
width = 0.4

# Plot
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, votes, width=width, color='#6B5B95', label='Votes')
plt.bar(x + width/2, rating_scaled, width=width, color='#88B04B', label='Rating (Scaled)')

plt.xticks(ticks=x, labels=names, rotation=45, ha='right')
plt.ylabel("Votes / Scaled Rating")
plt.title("Top 10 Most Popular Restaurants: Popularity vs Rating")
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig("Outputs/Level_2_Output/04_restaurant_rating_popularity.png")
plt.show()

