import folium
import math

m = folium.Map(location=[ 48.1333,  -1.9667], zoom_start=5)
def circle(magnitude,latitude, longitude,map):
    for i in range(len(magnitude)):
        radius = (math.exp(magnitude[i]/1.01-0.13))*1000
        folium.Circle(
            location=[latitude[i],  longitude [i]],
            radius=radius,
            color="black",
            weight=1,
            fill_opacity=0.6,
            opacity=1,
            fill_color="red",
            fill=False,  # gets overridden by fill_color
            popup="magnitude de {}".format(magnitude[i]),
            tooltip="I am in meters",
        ).add_to(map)
