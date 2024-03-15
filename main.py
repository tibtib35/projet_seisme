import map_creation as mp
import get_info as gi
import draw_circle as dc
import geopandas
from folium.plugins import Search

map = mp.create(48.1333,  -1.9667)
date = ('2014-01-01','2014-01-02')
user = '&starttime='+date[0]+'&endtime='+date[1]
seismes = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"+user,
    driver="GeoJSON",
)

info = gi.recup_info(seismes)

magnitude = info[0]
latitude = info[1]
longitude = info[2]

dc.circle(magnitude,latitude,longitude,map)

geo = folium.GeoJson(
    country,
    name="Country",
    style_function=style_function,
).add_to(m)

countrysearch = Search(
    layer=geo,
    geom_type="Polygon",
    placeholder="Search for a countrye",
    collapsed=False,
    search_label="name",
    weight=3,
).add_to(m)

map.save("map.html")

