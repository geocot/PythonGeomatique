#Martin Couture
#Vidéo explicative: https://youtu.be/-FxLmck7uRw
import exif, webbrowser

def dmsTodd(coord, coorfRef):
    dd = coord[0] + coord[1]/60 + coord[2]/3600

    if coorfRef == 'S' or coorfRef == 'W':
        dd *= -1

    return dd

with open('photo.jpg', 'rb') as fichierPhoto:
    dataPhoto = exif.Image(fichierPhoto)

print(dmsTodd(dataPhoto.gps_latitude, dataPhoto.gps_latitude_ref))
print(dmsTodd(dataPhoto.gps_longitude, dataPhoto.gps_longitude_ref))

url = f"https://www.google.com/maps?q={dmsTodd(dataPhoto.gps_latitude, dataPhoto.gps_latitude_ref)},{dmsTodd(dataPhoto.gps_longitude, dataPhoto.gps_longitude_ref)}"
webbrowser.open(url)