import folium

m = folium.Map(location=[ 48.1333,  -1.9667], zoom_start=5)
magnitude = 9
radius = magnitude*5000
folium.Circle(
    location=[48.1333,  -1.9667],
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="green",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="I am in meters",
).add_to(m)

m.save("map.html")
