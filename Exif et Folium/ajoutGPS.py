from exif import Image
image = Image("photo4.jpg")


image.gps_latitude = (63.0, 24.0, 52.3249)
image.gps_latitude_ref = "N"
image.gps_longitude = (19.0, 0.0, 38.05946)
image.gps_longitude_ref = "W"
image.gps_altitude = 0  # in meters

with open('photo4.jpg', 'wb') as new_image_file:
    new_image_file.write(image.get_file())

#63.414534695192984, -19.010572072271515