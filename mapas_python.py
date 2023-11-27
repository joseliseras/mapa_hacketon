import folium

mapa =  folium.Map().add_child(
    folium.ClickForMarker()
)

mapa.save("mapita2.html")
'''
mapa = folium.Map(location=(-57.663668877686553, -25.293682223999554))

mapa.save("mapita.html")
'''