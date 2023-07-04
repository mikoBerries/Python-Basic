import requests
import bs4
import lxml

# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter 
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("http://www.example.com")
print(type(res))
print(res.text)

# amking raw docttyp become read able using bs4
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup)

# getting given tag from soup object
title = soup.select('title')
print(title)
# getting text in beetwen tags
print(title[0].text)