'''
MVC 패턴 중에 C임.
    메인 서비스를 구축하는 컨트롤러
        - 라우트 : URL과 이를 처리할 함수 연계
        - 비즈니스 로직: 사용자가 요청하는 주 내용을 처리하는 곳
'''
from flask import render_template, request
from service.controllers import bp_main as main # controllers 패키지의 init이니까, blueprint객체 들고오기


# ~/main
@main.route('/') # 등록한 bluepritn도 라우팅할수 있다.
def home():
    return render_template('index.html')