import folium
import geopandas

m = folium.Map(location=[ 48.1333,  -1.9667], zoom_start=5)
seisme = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02&limit=5",
    driver="GeoJSON",
)

magnitude = seisme["mag"]
print(magnitude[1])

m.save("map.html")
