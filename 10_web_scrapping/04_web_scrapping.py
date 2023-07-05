# scrapping website multiple pages in https://books.toscrape.com/ website
import requests
import bs4 
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format('1'))
# getting books.toscrape.com pages one

soup = bs4.BeautifulSoup(res.text,"lxml")

# grapping all tag with class = product_pod inside of it
products = soup.select(".product_pod")

example = products[0] # get one tag

list(example.children)
# getting class rating 
if [] == example.select('.star-rating.Three'):
    print("there is not a 3 star rating")
if [] == example.select('.star-rating.Two'):
    print("there is not a 2  star rating")

# getting title of the book if star ratting are 3 / etc
print(example.select('a'))
print(example.select('a')[1])
print(example.select('a')[1]['title'])

# packing all codes to loop each pages
# looping to all pages
two_star_titles = []
# since we kwow how much pages an items in it
for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    # get request to pages-n

    # convert it to soup
    soup = bs4.BeautifulSoup(res.text,"lxml")
    # looks to class = product_pod
    books = soup.select(".product_pod")
    
    # iterate all books
    for book in books:
        # check is there class name = star-rating Two?
        if len(book.select('.star-rating.Two')) != 0:
            # founded append to global list 
            two_star_titles.append(book.select('a')[1]['title'])

print(f"this is books title with 2 star :\n{two_star_titles}")
