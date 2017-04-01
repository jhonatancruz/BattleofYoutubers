# from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# page = Request("https://www.youtube.com/")

# soup = BeautifulSoup(html_doc, 'html.parser')
import urllib.request

req = urllib.request.Request('https://www.youtube.com/')
with urllib.request.urlopen(req) as response:
   the_page = response.read()

soup = BeautifulSoup(the_page, "lxml")
print(soup.title)
