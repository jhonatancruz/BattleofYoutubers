from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("popup.html")

@app.route('/url', methods=['GET', 'POST'])
def evaluateUrl():
    global url
    url= request.form['URL']
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()

    global soup
    soup = BeautifulSoup(the_page, "lxml")
    webTitle= soup.title

    # urlRemove=[]
    # for x in webTitle:
    #     if x !='[':
    #         urlRemove.append(x)
    #     else:
    #         print("dont enter ")

    urlRemove= webTitle.text

    driver= webdriver.PhantomJS()
    driver.set_window_size(1124, 850) # set browser size.
    driver.get(url)

    time.sleep(2)
    moreButton =driver.find_element_by_xpath("//*[@id='action-panel-overflow-button']/span").click()
    # moreButton =driver.find_element_by_xpath("//*[@id='action-panel-overflow-button']/span").click()

    transcriptButton= driver.find_element_by_xpath("//*[@id='action-panel-overflow-menu']/li[2]/button/span").click()
    time.sleep(1)

    #may have to use javacript after this
    firstLine=soup.find("div", {"id":"watch-description-text"})

    cleanLine= firstLine.text



    return render_template("urlEval.html", urlRemove=urlRemove, cleanLine = cleanLine)


if __name__=="__main__":
    app.run(debug=True)
