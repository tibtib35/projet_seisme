import folium
def create(latitude, logitude):
    map = folium.Map(location=[ latitude,  logitude], zoom_start=5)
    return map

