import pandas as pd
import folium

# Load dataset
df = pd.read_csv("Dataset.csv")

# Drop missing coordinates
df = df.dropna(subset=["Latitude", "Longitude"])

# Center map on mean lat/lon
map_center = [df["Latitude"].mean(), df["Longitude"].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=4)

# Add restaurant markers (limit to 500 for performance)
for _, row in df.head(500).iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=2,
        color="crimson",
        fill=True,
        fill_opacity=0.6,
    ).add_to(restaurant_map)

# Save map to HTML
restaurant_map.save("Outputs/Level_2_Output/02_restaurant_geolocation_map.html")

print("\n🔹 Map created: Outputs/Level_2_Output/restaurant_geolocation_map.html")
print("✅ Open the HTML file in your browser to view the plotted restaurant locations.")
