'''
    데이터 베이스 접속후 쿼리 수행
'''
import pymysql as my

def select_login(uid,upw):  # 함수화 하기
    '''
        아이디, 비밀번호를 넣어서 회원여부를 체크하는 함수
        parameter
            - uid : 아이디
            - upw : 비밀번호
        returns
            - 회원인경우 
                - {'name': '게스트', 'uid': 'guest', 'regdate': datetime.datetime(2023, 3, 24, 13, 2, 31)}
            - 비회원인경우, 디비측 오류
                - None
    '''
    connection = None
    row = None # 로그인 쿼리 수행 결과를 담는 변수
    try:    
        connection = my.connect(host        ='localhost',
                                #port        = 3306,     
                                user        ='root',     
                                password    ='12341234', 
                                database    ='ml_db',    
                                # 조회 결과는 [ {}, {}, {},...  ] 이런 형태로 추출된다                            
                                cursorclass =my.cursors.DictCursor
                                )
        with connection.cursor() as cursor:
            # 파라미터는 %s표시로 순서대로 세팅된다 '값' => ''는 자동으로 세팅된다
            sql = '''
                SELECT 
                    `name`, uid, regdate 
                FROM 
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
            '''
            # execute() 함수의 2번 인자가 파라미터 전달하는 자리, 튜플로 표현
            cursor.execute( sql,(uid,upw) )
            row = cursor.fetchone() # 결과셋중 한개만 가져온다 => 단수(리스트가 아닌 단독타입:딕셔너리)
            #print( row['name'] )
            pass
    except Exception as e:
        print('접속 오류', e)
    else:
        print('접속시 문제 없었음')
    finally:    # 예외 사항이든 아니든 무조건 수행
        if connection:
            connection.close()
    # 로그인한 결과를 리턴 -> { ... }
    return row

if __name__ == '__main__':  # d4개발자의 테스트 코드, f5개발자는 호출할 수 없음. 만약 이거안하고 f5에서 import하고 수행하게 되면 d4에서 연습수행하려 했던 select_login()이 한번더 수행된다.
    # 정상계정
    print(select_login('guest','1234'))
    # 비정상계정
    print(select_login('guest','12345'))