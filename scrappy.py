from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import urllib.request

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("popup.html")

@app.route('/url', methods=['GET', 'POST'])
def evaluateUrl():
    url= request.form['URL']
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()

    soup = BeautifulSoup(the_page, "lxml")
    webTitle= soup.title

    urlRemove=[]
    for x in webTitle:
        if x !='[':
            urlRemove.append(x)
        else:
            print("dont enter ")

    return render_template("urlEval.html", urlRemove=urlRemove)

if __name__=="__main__":
    app.run(debug=True)
