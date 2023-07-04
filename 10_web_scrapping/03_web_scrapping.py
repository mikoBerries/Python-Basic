# srwapping image from website (wikipedia)
import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')

# Getting all tag within class=thumbiamge
image_info = soup.select('.thumbimage')

computer = image_info[0] #get one soup object

# computer['src'] get link in 

# to scrapping image make a request to images it shelf
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# it'll returning base64 and just write it in file to became iamges
f = open('my_new_file_name.jpg','wb')
f.write(image_link.content)
f.close()