import geopandas
import folium
def create(latitude, logitude):
    map = folium.Map(location=[ latitude,  logitude], zoom_start=5)
    return map

date = ('2001-03-10','2001-03-12')
user = '&starttime='+date[0]+'&endtime='+date[1]

seismes = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"+user,
    driver="GeoJSON",
)
