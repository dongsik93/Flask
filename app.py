from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/greeting")
def greeting():
    return """
    <h1>hihihi~</h1>
    <ul>
        <li>중식</li>
        <li>한식</li>
        <li>양식</li>
        <li>분식</li>
    </ul>
    """
    
@app.route("/index")
def index():
    # html코드를 리턴
    return render_template("index.html")
    
    
@app.route("/lunch")
def lunch():
    menus = ["짜장면", "투움바 파스타", "김치찜", "굴국밥", "만두라면"]
    pick = random.choice(menus)
    
    return render_template("lunch.html", one_pick=pick)
    
@app.route("/lotto")
def lotto():
    number = sorted(random.sample(range(1,46),5))
    
    return render_template("lotto.html", lotto_pick = number)
    
    
@app.route("/student/<string:name>")
# name이라는 변수에 받음 
def student(name):
    return render_template("student.html", name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    num1 = num**3
    return render_template("cube.html", num1 = num1, num=num)
    
@app.route("/naver")
def naver():
    return render_template("naver.html")
    
    
@app.route("/google")
def google():
    return render_template("google.html")
    
@app.route("/flex")
def flex():
    return render_template("flex.html")
    
    
@app.route("/grid")
def grid():
    return render_template("grid.html")
        
        
@app.route("/opgg")
def opgg():
    return render_template('opgg.html')
    
@app.route("/summoner")
def summoner():
    # 사용자가 검색하려고 하는 소환사 이름
    username = request.args.get("summoner")
    # 실제 op.gg사이트에서 검색 요청 url
    url = "http://www.op.gg/summoner/userName="
    res = requests.get(url+username).text
    soup = BeautifulSoup(res, "html.parser")
    
    win = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
    lose = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses").text
 
    
    f = open("output.csv", 'a+', encoding="utf-8", newline="")
    csv_f = csv.writer(f)
    csv_f.writerow([username, win, lose, datetime.datetime.now()])
    f.close()

    return render_template("summoner.html", win=win, lose=lose)
    
@app.route("/rank")
def rank():
    f = open('output.csv', 'r', encoding="utf-8")
    csv_r = csv.reader(f)
    
    return render_template("rank.html", csv_r = csv_r)



# 이 문장은 맨 마지막에 들어가야 함

if(__name__ == "__main__"): # 모듈로 불렀는지, 파이썬 파일(main으로)로 실행했는지
    app.run(debug=True,host="0.0.0.0",port=8080) # app은 Flask객체 / debug모드로 호스트, 포트를 설정
    
