#Importing Image sub module from exif module
from exif import Image

img_path = "IMGI_20220512_132319.jpeg"

with open(img_path, "rb") as src:  #reading image path in binary.
    img = Image(src)


def decimal_coords(coords, ref):
    #Decimal degrees = Degrees + Minutes/60 + Seconds/3600
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    #since we coordinates are in 2d.
    #we have put negative in south and west for accuracy
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def image_coordinates(image_path):
    with open(image_path, 'rb') as src:
        img = Image(src)
    #checking if image has exif data or not
    if img.has_exif:
        try:
            img.gps_longitude
            # calling decimal_coords function and storing into variable coords
            coords = (decimal_coords(img.gps_latitude,
                                     img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                                     img.gps_longitude_ref))
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    # printing image source name,software, coordinates
    print(f"=============================\nImage {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
    print(f"has coordinates:{coords}\n=============================")

# taking user input 
def main():
    
    a = int(
        input("=============================\n:: Welcome to our project ::\n=============================\n1.Find Location\n2.Original Date and Time\n3.System Model\n4.Others\n0.Exit\n=============================\n"))

    
    if (a == 1):
        image_coordinates(img_path)
    elif (a == 2):
        print(f"=============================\nDate and time : {img.datetime_original}\n=============================")
    elif (a == 3):
        print(f"=============================\nSystem model: {img.model}\n=============================")
    elif (a == 4):
        print('\n'.join(img.list_all()))
        b = str(input("=============================\nEnter the exif data name:"))
        print(b, f":{img.get(b)}\n=============================")
    #terminating program by exit function
    elif(a == 0):
        print("=============================\nThank You\n=============================")
        exit()
    else:
        raise Exception("Enter correct input")
    #recursively calling main funtion
    
    main()
#calling main function
if __name__ == "__main__":
    main()