import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop rows with missing city or rating data
df = df.dropna(subset=["City", "Aggregate rating"])

# 1. City with highest number of restaurants
city_counts = df["City"].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

print(f"\n🔹 City with Most Restaurants: {top_city} ({top_city_count} restaurants)")

# 2. Average rating per city
avg_rating_per_city = df.groupby("City")["Aggregate rating"].mean().round(2)
print("\n🔹 Average Rating per City (Top 10 shown):")
print(avg_rating_per_city.sort_values(ascending=False).head(10))

# 3. City with highest average rating
highest_avg_city = avg_rating_per_city.idxmax()
highest_avg_rating = avg_rating_per_city.max()
print(f"\n🔹 City with Highest Avg Rating: {highest_avg_city} ({highest_avg_rating})")

# Plot: Top 10 cities by number of restaurants with different colors
top_10_cities = city_counts.head(10)
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1',
          '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC']

plt.figure(figsize=(10, 6))
top_10_cities.plot(kind='bar', color=colors)
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Restaurant Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Outputs/Level_1_outputs/02_city_restaurant_count.png")
plt.show()
