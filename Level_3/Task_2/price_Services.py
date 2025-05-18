import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop missing relevant columns
df = df.dropna(subset=["Price range", "Has Online delivery", "Has Table booking"])

# Normalize values
df["Has Online delivery"] = df["Has Online delivery"].str.lower()
df["Has Table booking"] = df["Has Table booking"].str.lower()

# Group by price range and calculate service percentages
service_stats = df.groupby("Price range").agg({
    "Has Online delivery": lambda x: (x == "yes").sum() / len(x) * 100,
    "Has Table booking": lambda x: (x == "yes").sum() / len(x) * 100
}).rename(columns={
    "Has Online delivery": "Online Delivery (%)",
    "Has Table booking": "Table Booking (%)"
}).round(2)

print("\n🔹 Service Availability by Price Range:\n")
print(service_stats)

# Plotting
price_ranges = service_stats.index.astype(str)
delivery = service_stats["Online Delivery (%)"]
booking = service_stats["Table Booking (%)"]

bar_width = 0.35
x = range(len(price_ranges))

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x], delivery, width=bar_width, color="#FF6F61", label="Online Delivery")
plt.bar([i + bar_width/2 for i in x], booking, width=bar_width, color="#6B5B95", label="Table Booking")

plt.xticks(x, price_ranges)
plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.title("Service Availability by Price Range")
plt.legend()
plt.tight_layout()
plt.savefig("Outputs/Level_3_Outputs/02_price_vs_services.png")
plt.show()
