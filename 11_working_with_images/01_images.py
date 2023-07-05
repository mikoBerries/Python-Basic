# pillow liblary -> PIL

from PIL import Image

# grapping iamges
img = Image.open("example.jpg")

# image attribute
print(img.size)         # (width, height)
print(img.filename)
print(img.format_description)


img.show()
# cropping iamges
halfway = 1993/2
x = halfway - 200
w = halfway + 200

y = 800
h = 1257

cropped_img = img.crop((x,y,w,h)) # x,y started coordinate w,h width,length from given x,y coordinate 
cropped_img.show()

# copying images in iamges
# pasteing cropped_img in coordinate 0,0
img.paste(im=cropped_img,box=(0,0))
img.show()

# this operation not writed in actual pict but only in memory

# rezize image and rotate iamge
img= img.resize((3000,400))
img =img.rotate(90)
img.show()