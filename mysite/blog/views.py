from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
import pymysql
from flask_wtf.csrf import CSRFProtect
from blog import query_sql as q
from .models import Recipe
from django.contrib.auth.hashers import check_password

# DB 연결 함수
def mysql_rdb_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="RECIPE",
        port=3306
    )

def index_view(request):
    return render(request,'blog/index.html')

def main_view(request):
    return render(request,'blog/main.html')

def signup_view(request):
    return render(request,'blog/signup.html')

def koreanfood(request):
    return render(request,'blog/koreanfood.html')

def korean_food_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/koreanfood.html', {'recipes': recipes})

def signup(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        try:
            with mysql_rdb_conn() as conn:
                with conn.cursor() as curs:
                    # 닉네임 중복 체크
                    curs.execute(q.select_nickname_from_users(), (nickname,))
                    if curs.fetchone():
                        messages.error(request, "이미 사용 중인 닉네임입니다.")
                        return redirect('signup')  # Django에서는 URL명을 사용

                    # 이메일 유효성 체크
                    if "@" not in email:
                        messages.error(request, "올바른 이메일 형식을 입력해주세요.")
                        return redirect('signup')

                    # 비밀번호 일치 체크
                    if password != confirm_password:
                        messages.error(request, "비밀번호가 일치하지 않습니다.")
                        return redirect('signup')

                    # 회원가입 정보 DB 삽입
                    user_id = nickname
                    regi_data = (user_id, nickname, email, password)
                    query_1 = q.mem_register()
                    curs.execute(query_1, regi_data)
                    conn.commit()

                    messages.success(request, "회원가입이 완료되었습니다!")
                    return redirect('index')  # 홈 페이지로 리다이렉트

        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
            return redirect('signup')

    return render(request, 'blog/signup.html')

def login(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        password = request.POST['password']

        # 닉네임 입력 확인
        if not nickname:
            messages.error(request, "닉네임을 입력하세요.")
            return redirect('index')

        # 비밀번호 입력 확인
        if not password:
            messages.error(request, "비밀번호를 입력하세요.")
            return redirect('index')

        try:
            with mysql_rdb_conn() as conn:
                with conn.cursor() as curs:

                    # 닉네임있나 체크
                    nickname_chk = q.select_nickname_from_users()
                    curs.execute(nickname_chk, (nickname,))
                    if curs.fetchone() is None:
                        messages.error(request, "아이디가 없습니다.")
                        return redirect('index')

                    # 비밀번호 맞나 체크
                    password_chk = q.select_password_from_users()
                    curs.execute(password_chk, (nickname,))
                    row = curs.fetchone()

                    db_password = row[0] if row else None  # DB에서 가져온 비밀번호

                    # 평문 비밀번호 비교
                    if db_password is None or password != db_password:
                        messages.error(request, "비밀번호가 틀립니다.")
                        return redirect('index')

                    messages.success(request, "로그인이 완료되었습니다!")
                    return redirect('main')  # 로그인 성공하면 메인 페이지로

        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
            return redirect('index')
    return render(request, 'index')
