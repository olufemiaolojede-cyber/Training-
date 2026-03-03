from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
# we are to get data from website
url = "https://fakestoreapi.com/products"
feedback = requests.get(url)
productdatas = feedback.json()
feeds = []
for productdata in productdatas:
    title = productdata['title']
    price = productdata['price']
    description = productdata['description']
    rating = productdata['rating']
    category = productdata['category']
    image = productdata['image']
    feeds.append({
        "title":title,
        "price":price,
        "description":description,
        "image":image,
        "category":category
    })

# df = pd.DataFrame(feeds)

writer = open("web.json", "w")
writer.write(f"""{feeds}""")


