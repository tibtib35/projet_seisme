import folium
import math
import get_info as gi

m = folium.Map(location=[ 48.1333,  -1.9667], zoom_start=5)
def circle(magnitude,latitude, longitude,map):
    for i in range(len(magnitude)):
        if magnitude[i] >= 0:
            radius = magnitude[i]*100000*math.cos(longitude[i]/180*math.pi)
            folium.Circle(
                location=[longitude[i],  latitude [i]],
                radius=radius,
                weight=1,
                color='black',
                fill_opacity=0.8,
                opacity=1,
                fill_color="#FF5F5D" if magnitude[i] > 7 else "#ED8B16" if magnitude[i] > 5  else "#FFEC5C" if magnitude[i] > 4.50 else "#146152",
                fill=False,  # gets overridden by fill_color
                popup="magnitude de {}".format(magnitude[i]),
            ).add_to(map)
