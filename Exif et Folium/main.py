#Martin Couture
#Vidéo explicative:
import exif, folium, os

def dmsTodd(coord, coorfRef):
    dd = coord[0] + coord[1]/60 + coord[2]/3600
    if coorfRef == 'S' or coorfRef == 'W':
        dd *= -1
    return dd

def lectureDonneesPhoto(pathPhoto):
    with open(pathPhoto, 'rb') as fichierPhoto:
        dataPhoto = exif.Image(fichierPhoto)
        #Extraction des données
        titre = dataPhoto.image_description
        coordLat = dmsTodd(dataPhoto.gps_latitude, dataPhoto.gps_latitude_ref)
        coordLong = dmsTodd(dataPhoto.gps_longitude, dataPhoto.gps_longitude_ref)
    return titre, coordLat, coordLong



# Démarrage de folium
m = folium.Map()
listePhoto = os.listdir(os.curdir)
for photo in listePhoto:
    if photo.endswith(".jpg"):
       titre,coordLat,coordLong = lectureDonneesPhoto(photo)
       folium.Marker(location=(coordLat, coordLong),popup='<a href="'+ photo + '" target="_blank">'+titre+'</a>',icon=folium.Icon(color='green')).add_to(m)
m.save("index.html")


