
import map_creation as mp
import get_info as gi
import draw_circle as dc
import folium.plugins


map = mp.create(48.1333,  -1.9667)

seismes = mp.seismes

info = gi.recup_info(seismes)

magnitude = info[0]
latitude = info[1]
longitude = info[2]

dc.circle(magnitude,latitude,longitude,map)

map.add_child(folium.plugins.MeasureControl())

map.save("map.html")

