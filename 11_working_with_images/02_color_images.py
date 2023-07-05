# image transparacy
from PIL import Image


red_img     = Image.open('red_color.jpg')
# blue_img    = Image.open('blue_color.png')
# purple_img  = Image.open('purple_color.jpg')

# .putalpha(int) giving opacity in img

red_img.putalpha(128)
red_img.show()
red_img.save('new_red_color.png')

# purple_img.show()