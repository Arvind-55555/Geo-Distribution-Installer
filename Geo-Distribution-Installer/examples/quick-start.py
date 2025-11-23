"""
Quick start examples for Geo Distribution
"""

import geopandas as gpd
import rasterio
import folium
import geopy
from geopy.geocoders import Nominatim

def demo_geopandas():
    """Demo GeoPandas functionality"""
    print("🌍 GeoPandas Demo")
    # Create sample geodataframe
    from shapely.geometry import Point
    gdf = gpd.GeoDataFrame({
        'city': ['Paris', 'London', 'New York'],
        'geometry': [Point(2.3522, 48.8566), Point(-0.1276, 51.5074), Point(-74.0060, 40.7128)]
    })
    gdf.crs = "EPSG:4326"
    print(gdf)
    return gdf

def demo_folium():
    """Demo Folium web mapping"""
    print("\n🗺️ Folium Demo")
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
    folium.Marker([40.7128, -74.0060], popup='New York').add_to(m)
    m.save('map.html')
    print("✓ Map saved as 'map.html'")
    return m

def demo_geocoding():
    """Demo geocoding with geopy"""
    print("\n📍 Geocoding Demo")
    geolocator = Nominatim(user_agent="geo_distro_demo")
    location = geolocator.geocode("Eiffel Tower, Paris")
    if location:
        print(f"✓ Eiffel Tower coordinates: {location.latitude}, {location.longitude}")
    return location

if __name__ == "__main__":
    print("🚀 Geo Distribution Quick Start Examples")
    print("=" * 50)
    
    gdf = demo_geopandas()
    folium_map = demo_folium()
    location = demo_geocoding()
    
    print("\n🎉 All demos completed successfully!")