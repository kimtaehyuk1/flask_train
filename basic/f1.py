# 홈페이지 작성, 디버깅 모드, 포트 5000번, 홈페이지는 화면에 "Helloworld"만 출력

# 땡기기
from flask import Flask, render_template, jsonify, request, redirect, url_for
# app만들기
app = Flask(__name__)
# 라우트
@app.route('/')
def home():
    return "helloworld"
# 서버가동
if __name__=="__main__":
    # 웹상에 기본 포트: http => 80 => 생략가능 나중에 80을 5000으로 바꿔줘야함
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True, host="0.0.0.0", port=5000)
