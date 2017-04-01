from bs4 import BeautifulSoup
from flask import Flask, render_template
import urllib.request

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    req = urllib.request.Request('https://www.youtube.com/')
    with urllib.request.urlopen(req) as response:
       the_page = response.read()

    soup = BeautifulSoup(the_page, "lxml")
    webTitle= soup.title
    # print(soup.title)

    return render_template("popup.html", webTitle= webTitle)

if __name__=="__main__":
    app.run(debug=True)
