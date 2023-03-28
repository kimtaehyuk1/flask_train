'''
MVC 패턴 중에 C임.
    메인 서비스를 구축하는 컨트롤러
        - 라우트 : URL과 이를 처리할 함수 연계
        - 비즈니스 로직: 사용자가 요청하는 주 내용을 처리하는 곳
'''
from flask import render_template, request, url_for
from service.controllers import bp_auth as auth # 블루프린트 땡겨오기

# ~/auth/
@auth.route('/') # 등록한 bluepritn도 라우팅할수 있다.
def home():
    # url_for(별칭.함수명) => url이 리턴된다.
    print(url_for('auth_bp.login'))
    return "auth 홈1"


@auth.route('/login') # 등록한 bluepritn도 라우팅할수 있다.
def login():
    return "auth login"

@auth.route('/logout') # 등록한 bluepritn도 라우팅할수 있다.
def logout():
    return "auth logout"

@auth.route('/signup') # 등록한 bluepritn도 라우팅할수 있다.
def signup():
    return "auth signup"

@auth.route('/delete') # 등록한 bluepritn도 라우팅할수 있다.
def delete():
    return "auth delete"