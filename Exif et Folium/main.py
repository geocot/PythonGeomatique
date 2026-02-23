#Martin Couture
#Vidéo explicative:
import exif, folium

def dmsTodd(coord, coorfRef):
    dd = coord[0] + coord[1]/60 + coord[2]/3600

    if coorfRef == 'S' or coorfRef == 'W':
        dd *= -1

    return dd

with open('photo.jpg', 'rb') as fichierPhoto:
    dataPhoto = exif.Image(fichierPhoto)

coordLat = dmsTodd(dataPhoto.gps_latitude, dataPhoto.gps_latitude_ref)
coordLong = dmsTodd(dataPhoto.gps_longitude, dataPhoto.gps_longitude_ref)

print(coordLong, coordLat)

#Partie avec Folium
m = folium.Map(location=(coordLat, coordLong))
folium.Marker(
    location=(coordLat, coordLong),
    tooltip='<b>Photo</b>',
    popup='<a href="photo.jpg" target="_blank">Lien</a>',
    icon=folium.Icon(color='green')
).add_to(m)
m.save("index.html")

#63.414316634831685, -19.01012966016265