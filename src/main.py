import map_creation as mp
import get_info as gi
import draw_circle as dc
import folium.plugins


map = mp.create(48.1333,  -1.9667) # creation de la carte et définition de la position de départ (près de Rennes)

seismes = mp.seismes # récupération des caractéristiques des séismes

info = gi.recup_info(seismes) # récupération de la magnitude, longitude et latitude des séismes 

magnitude = info[0]
latitude = info[1]
longitude = info[2]

dc.circle(magnitude,latitude,longitude,map) # tracé des cercles sur la carte 

map.add_child(folium.plugins.MeasureControl()) # ajout d'un plugin folium permettant de calculer une distance sur la carte 

map.save("map.html") # sauvegarde de la carte folium sur le fichier map.html

