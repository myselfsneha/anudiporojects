import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

# Step 1: Load your dataset (make sure the file path is correct)
data = pd.read_csv(r"C:\Users\SNEHA SINGH\updated_wedding_data.csv")

# Step 2: Print the first few rows to verify data loading
print("Dataset preview:")
print(data.head())

# Step 3: Initialize geolocator
geolocator = Nominatim(user_agent="wedding_analysis")

# Step 4: Geocode locations (create a function to get latitude and longitude from a location)
def geocode_location(location):
    try:
        location_data = geolocator.geocode(location)
        if location_data:
            return location_data.latitude, location_data.longitude
        else:
            return None, None
    except:
        return None, None

# Step 5: Create latitude and longitude columns
data['Latitude'], data['Longitude'] = zip(*data['Location'].apply(geocode_location))

# Step 6: Check for missing coordinates
missing_locations = data[data['Latitude'].isnull() | data['Longitude'].isnull()]
print("Locations with missing coordinates:")
print(missing_locations[['Location']])

# Step 7: Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))

# Step 8: Load a map of the world (or a specific region)
world = gpd.read_file(r"C:\Users\SNEHA SINGH\Downloads\110m_cultural.zip", layer='ne_110m_admin_0_countries')

# Step 9: Plot the world map with wedding locations
fig, ax = plt.subplots(figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
gdf.plot(ax=ax, color='orange', markersize=5, alpha=0.6, label='Wedding Locations')

# Step 10: Customize the plot
plt.title('Geographic Distribution of Weddings')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()
