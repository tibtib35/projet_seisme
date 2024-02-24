import map_creation as mp
import get_info as gi
import test as dc
import geopandas

map = mp.create(48.1333,  -1.9667)

seismes = geopandas.read_file(
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02",
    driver="GeoJSON",
)

info = gi.recup_info(seismes)

magnitude = info[0]
latitude = info[1]
longitude = info[2]

dc.circle(magnitude,latitude,longitude,map)

map.save("map.html")

