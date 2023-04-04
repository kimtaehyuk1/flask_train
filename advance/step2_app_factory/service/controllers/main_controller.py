'''
MVC 패턴 중에 C임.
    메인 서비스를 구축하는 컨트롤러
        - 라우트 : URL과 이를 처리할 함수 연계
        - 비즈니스 로직: 사용자가 요청하는 주 내용을 처리하는 곳
'''
from flask import render_template, request, redirect, url_for, Response
from service.controllers import bp_main as main # controllers 패키지의 init이니까, blueprint객체 들고오기
from service.forms import FormQuestion
# 환경변수의 시크릿 키 획득을 위해서 Flask 객체 획득
from flask import current_app
# jwt
import jwt
# 시간 관련
import time
from datetime import datetime


# ~/main
@main.route('/') # 등록한 bluepritn도 라우팅할수 있다.
def home():
    # 1. 쿠키중에 토큰 획득 -> 실패 -> 401
    token = request.cookies.get('token')
    SECRET_KEY = current_app.config['SECRET_KEY']
    print(token,SECRET_KEY)
    if not token or not SECRET_KEY:
        return Response(status=401)
    try:
        # 2. 디코딩 -> 실패하면 -> 401
        payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
        # 3. 유효 날짜 추출, 현재 시간 기준보다 과거인지 체크 => 과거라면:만료 -> 401
        if payload['exp'] < time.mktime( datetime.utcnow().timetuple() ): # 현재시간보다는 과거
            return Response(status=401)
        # 4. 정상
        return render_template('index.html')
    except jwt.InvalidTokenError:
        return Response(status=401)
    except jwt.ExpiredSignatureError:
        return Response(status=401)
    except jwt.exceptions.DecodeError:
        return Response(status=401)
    

@main.route('/question', methods=['GET','POST']) # 등록한 bluepritn도 라우팅할수 있다.
def question():
    form = FormQuestion()  #폼 유효성 검사통과하고
    if request.method == 'POST' and form.validate_on_submit():
        return redirect( url_for('main_bp.home') ) # ~/main
    return render_template('question.html', wtf=form)