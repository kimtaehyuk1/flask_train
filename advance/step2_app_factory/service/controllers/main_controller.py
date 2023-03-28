'''
MVC 패턴 중에 C임.
    메인 서비스를 구축하는 컨트롤러
        - 라우트 : URL과 이를 처리할 함수 연계
        - 비즈니스 로직: 사용자가 요청하는 주 내용을 처리하는 곳
'''
from flask import render_template, request, redirect, url_for
from service.controllers import bp_main as main # controllers 패키지의 init이니까, blueprint객체 들고오기
from service.forms import FormQuestion

# ~/main
@main.route('/') # 등록한 bluepritn도 라우팅할수 있다.
def home():
    return render_template('index.html')

@main.route('/question', methods=['GET','POST']) # 등록한 bluepritn도 라우팅할수 있다.
def question():
    form = FormQuestion()  #폼 유효성 검사통과하고
    if request.method == 'POST' and form.validate_on_submit():
        return redirect( url_for('main_bp.home') ) # ~/main
    return render_template('question.html', wtf=form)