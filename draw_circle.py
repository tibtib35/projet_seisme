import folium
import math

def circle(magnitude,latitude, longitude,map):
    '''
    Prend en paramètre les magnitudes, latitudes et longitudes des séismes et 'dessine' des cercles sur la carte selon ces paramètres. 
    '''
    for i in range(len(magnitude)):
        if magnitude[i] >= 0:
            radius = magnitude[i]*100000*math.cos(longitude[i]/180*math.pi) # création du rayon proportionnel à la magnitude
            folium.Circle(
                location=[longitude[i],  latitude [i]], # place le séisme sur la carte selon ses coordonnées 
                radius=radius,
                weight=1,
                color='black',
                fill_opacity=0.8,
                opacity=1,
                fill_color="#FF5F5D" if magnitude[i] > 7 else "#ED8B16" if magnitude[i] > 5  else "#FFEC5C" if magnitude[i] > 4.50 else "#146152", # défini la couleur de remplissage du cercle selon un dégradé qui a un rapport à la magnitude (de vert = séismes les plus faibles au rouge = séismes les plus forts)
                fill=False,  # Pas prioritaire par rapport à 'fill_color'
                popup="magnitude de {}".format(magnitude[i]), # ajoute un texte indiquant la magnitude
            ).add_to(map) # ajoute le cercle à la carte 

