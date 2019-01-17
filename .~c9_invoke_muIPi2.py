from flask import Flask, render_template
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
    
    
    
    
# 이 문장은 맨 마지막에 들어가야 함

# if(__name__ == "__main__"): # 모듈로 불렀는지, 파이썬 파일(main으로)로 실행했는지
#     app.run(debug=True,host="0.0.0.0",port=8080) # app은 Flask객체 / debug모드로 호스트, 포트를 설정
    
