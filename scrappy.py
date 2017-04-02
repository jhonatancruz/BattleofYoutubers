from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


def Algo_You(views,day,subscriber_count,Likes,Dislikes):
	points = (views/day)/subscriber_count * (views/(Likes - Dislikes))
	return points


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

@app.route('/testvid', methods=["POST", "GET"])
def testvid():
    firstYoutuber=request.form['y1']
    secYoutuber= request.form['y2']

    driver= webdriver.Chrome()
    driver.set_window_size(1124, 850) # set browser size.
    url1= "https://www.youtube.com/user/"+firstYoutuber+"/videos"
    url2= "https://www.youtube.com/user/"+secYoutuber+"/videos"

    # driver.get(url1)
    # driver.get(url2)

    driver.get(url1)
    recentVid =driver.find_element_by_xpath("//*[@id='channels-browse-content-grid']/li[1]/div/div[1]/div[2]/h3/a").click()
    time.sleep(2)
    likesDriver= driver.find_element_by_xpath("//*[@id='watch8-sentiment-actions']/span/span[1]/button/span")
    time.sleep(1)
    dislikesDriver= driver.find_element_by_xpath("//*[@id='watch8-sentiment-actions']/span/span[3]/button/span")
    nameVidDriver1= driver.find_element_by_xpath("//*[@id='eow-title']")
    datePostedDriver1= driver.find_element_by_xpath("//*[@id='watch-uploader-info']/strong")
    viewsDriver1= driver.find_element_by_xpath("//*[@id='watch7-views-info']/div[1]")
    subsDriver1= driver.find_element_by_xpath("//*[@id='watch7-subscription-container']/span/span[1]")
    img1= driver.find_element_by_xpath("//*[@id='watch7-user-header']/a/span/span/span/img")
    likes= likesDriver.text
    dislikes= dislikesDriver.text
    nameVid= nameVidDriver1.text
    datePosted= datePostedDriver1.text #this is the date
    views1= viewsDriver1.text
    subs1=subsDriver1.text
    src1= img1.get_attribute('src')


    #start date algo under here


    Months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Nov" : 10, "Oct" :11, "Dec" : 12}

    datePosted = datePosted[13:]

    datePosted = datePosted.replace(",", "")
    Dateposted = datePosted.split(" ")
    Dateposted[0] = Months[Dateposted[0]]
    j = 0
    for i in Dateposted:
    	Dateposted[j] = int(i)
    	j = j + 1
    now = datetime.datetime.now();
    DatePosted = datetime.datetime(Dateposted[2], Dateposted[0], Dateposted[1])
    D3 = now - DatePosted
    datePosted = D3.days
    Views = views1[:-6]
    Views = Views.replace(",", "")
    Views = int(Views)
    subs = subs1.replace(",", "")
    subs = int(subs)
    Likes = likes.replace(",", "")
    Likes = int(Likes)
    Dislikes = dislikes.replace(",", "")
    Dislikes = int(Dislikes)
    points1 = Algo_You(Views,datePosted,subs,Likes,Dislikes)
    print (points1)


    driver.get(url2)
    recentVid =driver.find_element_by_xpath("//*[@id='channels-browse-content-grid']/li[1]/div/div[1]/div[2]/h3/a").click()
    time.sleep(2)
    likesDriver= driver.find_element_by_xpath("//*[@id='watch8-sentiment-actions']/span/span[1]/button/span")
    time.sleep(1)
    dislikesDriver= driver.find_element_by_xpath("//*[@id='watch8-sentiment-actions']/span/span[3]/button/span")
    nameVidDriver= driver.find_element_by_xpath("//*[@id='eow-title']")
    datePostedDriver2= driver.find_element_by_xpath("//*[@id='watch-uploader-info']/strong")
    viewsDriver2= driver.find_element_by_xpath("//*[@id='watch7-views-info']/div[1]")
    subsDriver2= driver.find_element_by_xpath("//*[@id='watch7-subscription-container']/span/span[1]")
    img2= driver.find_element_by_xpath("//*[@id='watch7-user-header']/a/span/span/span/img")
    likes2= likesDriver.text
    dislikes2= dislikesDriver.text
    nameVid2= nameVidDriver.text
    datePosted2= datePostedDriver2.text
    views2= viewsDriver2.text
    subs2= subsDriver2.text
    src2= img2.get_attribute('src')

    datePosted2 = datePosted2[13:]
    datePosted2 = datePosted2.replace(",", "")
    Dateposted2 = datePosted2.split(" ")
    Dateposted2[0] = Months[Dateposted2[0]]
    j = 0
    for i in Dateposted2:
    	Dateposted2[j] = int(i)
    	j = j + 1
    now = datetime.datetime.now();
    DatePosted2 = datetime.datetime(Dateposted2[2], Dateposted2[0], Dateposted2[1])
    D3 = now - DatePosted2
    datePosted2 = D3.days
    Views = views2[:-6]
    Views = Views.replace(",", "")
    Views = int(Views)
    subs = subs2.replace(",", "")
    subs = int(subs)
    Likes = likes2.replace(",", "")
    Likes = int(Likes)
    Dislikes = dislikes2.replace(",", "")
    Dislikes = int(Dislikes)
    points2 = Algo_You(Views,datePosted,subs,Likes,Dislikes)
    print(points2)

    return render_template('showResult.html', firstYoutuber=firstYoutuber,secYoutuber=secYoutuber, likes=likes, dislikes=dislikes,
    likes2=likes2, dislikes2=dislikes2, nameVid2=nameVid2, nameVid=nameVid, datePosted=datePosted, datePosted2=datePosted2,
    views1=views1, views2=views2, subs1=subs1, subs2=subs2, src2=src2, src1=src1)

if __name__=="__main__":
    app.run(debug=True)
