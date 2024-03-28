import geopandas
import folium
import get_info as gi
def create(latitude, logitude):
    map = folium.Map(location=[ latitude,  logitude], zoom_start=5, control_scale=True)
    return map

date = gi.recup_date()

mag = gi.recup_mag()

user = '&starttime='+date[0]+'&endtime='+date[1]+'&minmagnitude='+mag

seismes = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"+user,
    driver="GeoJSON",
)
