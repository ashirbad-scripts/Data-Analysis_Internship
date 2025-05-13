import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop rows with missing delivery info or rating
df = df.dropna(subset=["Has Online delivery", "Aggregate rating"])

# Convert delivery column to lowercase for consistency
df["Has Online delivery"] = df["Has Online delivery"].str.lower()

# Count how many offer delivery
delivery_counts = df["Has Online delivery"].value_counts()

# Percentage calculation
total = len(df)
delivery_yes = delivery_counts.get("yes", 0)
delivery_pct = round((delivery_yes / total) * 100, 2)
print(f"\n🔹 {delivery_pct}% of restaurants offer online delivery.")

# Compare average ratings
avg_rating_delivery = df[df["Has Online delivery"] == "yes"]["Aggregate rating"].mean().round(2)
avg_rating_no_delivery = df[df["Has Online delivery"] == "no"]["Aggregate rating"].mean().round(2)

print(f"\n🔹 Average Rating (Online Delivery): {avg_rating_delivery}")
print(f"🔹 Average Rating (No Online Delivery): {avg_rating_no_delivery}")

# Plot average ratings comparison
labels = ["Online Delivery", "No Delivery"]
ratings = [avg_rating_delivery, avg_rating_no_delivery]
colors = ['#45B8AC', '#DD4124']

plt.figure(figsize=(5, 4))
plt.bar(labels, ratings, color=colors)
plt.title("Avg Rating: Delivery vs No Delivery")
plt.ylabel("Aggregate Rating")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("Outputs/Level_1_outputs/04_online_delivery_rating_comparison.png")
plt.show()
