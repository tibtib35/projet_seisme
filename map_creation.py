import geopandas
import folium
import get_info as gi
def create(latitude, logitude):
    map = folium.Map(location=[ latitude,  logitude], zoom_start=5)
    return map

date = gi.recup_date()
user = '&starttime='+date[0]+'&endtime='+date[1]

seismes = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"+user,
    driver="GeoJSON",
)
