import geopandas
import folium
import get_info as gi
def create(latitude, logitude):
    map = folium.Map(location=[ latitude,  logitude], zoom_start=5, control_scale=True) # cration de la carte, définition de la position de départ, définition d'un zoom fois 5 au départ et ajout d'une échelle de distance sur la carte
    return map

date = gi.recup_date() # récupération des dates de début et de fin demandées par l'utilisateur

mag = gi.recup_mag() # récupération de la magnitude minimum demandée par l'utilisateur

user = '&starttime='+date[0]+'&endtime='+date[1]+'&minmagnitude='+mag

seismes = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"+user, # appel à l'API
    driver="GeoJSON",
)
