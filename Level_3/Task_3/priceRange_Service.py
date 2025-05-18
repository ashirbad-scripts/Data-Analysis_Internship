import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop missing relevant data
df = df.dropna(subset=["Price range", "Has Online delivery", "Has Table booking"])

# Normalize to lowercase
df["Has Online delivery"] = df["Has Online delivery"].str.lower()
df["Has Table booking"] = df["Has Table booking"].str.lower()

# Define service category
def service_type(row):
    if row["Has Online delivery"] == "yes" and row["Has Table booking"] == "yes":
        return "Both"
    elif row["Has Online delivery"] == "yes":
        return "Delivery Only"
    elif row["Has Table booking"] == "yes":
        return "Booking Only"
    else:
        return "None"

df["Service Combo"] = df.apply(service_type, axis=1)

# Count by price range and service combo
combo_stats = df.groupby(["Price range", "Service Combo"]).size().unstack(fill_value=0)

# Convert to percentage
combo_pct = combo_stats.div(combo_stats.sum(axis=1), axis=0) * 100
combo_pct = combo_pct.round(2)

print("\n🔹 Combined Service Distribution by Price Range (%):\n")
print(combo_pct)

# Plot
combo_pct.plot(kind="bar", stacked=True, figsize=(10, 6),
               color=["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9"])

plt.title("Combined Service Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.legend(title="Service Offered", loc="upper right")
plt.tight_layout()
plt.savefig("Outputs/Level_3_Outputs/03_combined_service_analysis.png")
plt.show()
