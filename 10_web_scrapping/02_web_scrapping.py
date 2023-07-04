import requests
import bs4


# getting request from given link
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# feed text to bs4.soup

soup = bs4.BeautifulSoup(res.text,"lxml")
print(len(soup))
# grab all class toctext


# # Syntax to pass to the .select() method    Match Results
# soup.select('div')                          All elements with the <div> tag
# soup.select('#some_id')                     The HTML element containing the id attribute of some_id
# soup.select('.notice')                      All the HTML elements with the CSS class named notice
# soup.select('div span')                     Any elements named <span> that are within an element named <div>
# soup.select('div > span')                   Any elements named <span> that are directly within an element named <div>, with no other element in between

# iterate all item and getting all text in between tags
for item in soup.select(".toctext"):
    print(item.text)
