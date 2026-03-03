from bs4 import BeautifulSoup
import requests
import pandas as pd 
url = "https://fakestoreapi.com/products"
feedback = requests.get(url)
contentdata = feedback.content
webcontent = open("contentdata.txt", "w")
webcontent.write(f"""{contentdata}""")
webcontent.close()

