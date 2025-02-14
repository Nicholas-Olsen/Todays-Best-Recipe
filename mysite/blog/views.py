from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
import pymysql
from blog import query_sql as q
from .models import Recipe
import requests
import os
import json
from dotenv import load_dotenv
import re
from django.db import connection
from django.conf import settings
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

def mypage(request):
    return render(request,'blog/mypage.html')

def home_view(request):
    settings.GLOBAL_NICKNAME = "게스트"
    return render(request,'blog/home.html')

def main_view(request):
    return render(request,'blog/main.html')

def signup_view(request):
    return render(request,'blog/signup.html')

def koreanfood(request):
    return render(request,'blog/koreanfood.html')

def korean_food_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/koreanfood.html', {'recipes': recipes})

# def ko_food(request):
#     return render(request,'blog/koreanfood.html')

def ja_food(request):
    return render(request,'blog/koreanfood.html')

def ch_food(request):
    return render(request,'blog/koreanfood.html')

def de_food(request):
    return render(request,'blog/koreanfood.html')

def we_food(request):
    return render(request,'blog/koreanfood.html')

def recommend(request):
    return render(request,'blog/recommend.html')

def result(request):
    return render(request,'blog/result.html')



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
                    return redirect('home')  # 홈 페이지로 리다이렉트

        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
            return redirect('signup')

    return render(request, 'blog/signup.html')

def login(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        password = request.POST['password']

        settings.GLOBAL_NICKNAME = nickname

        # 닉네임 입력 확인
        if not nickname:
            messages.error(request, "닉네임을 입력하세요.")
            return redirect('home')

        # 비밀번호 입력 확인
        if not password:
            messages.error(request, "비밀번호를 입력하세요.")
            return redirect('home')

        try:
            with mysql_rdb_conn() as conn:
                with conn.cursor() as curs:

                    # 닉네임있나 체크
                    nickname_chk = q.select_nickname_from_users()
                    curs.execute(nickname_chk, (nickname,))
                    if curs.fetchone() is None:
                        messages.error(request, "아이디가 존재하지 않습니다.")  
                        return redirect('home')

                    # 비밀번호 맞나 체크
                    password_chk = q.select_password_from_users()
                    curs.execute(password_chk, (nickname,))
                    row = curs.fetchone()

                    db_password = row[0] if row else None  # DB에서 가져온 비밀번호

                    # 평문 비밀번호 비교
                    if db_password is None or password != db_password:
                        messages.error(request, "비밀번호가 틀립니다.")
                        return redirect('home')

                    messages.success(request, "로그인이 완료되었습니다!")
                    return redirect('main')  # 로그인 성공하면 메인 페이지로

        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
            return redirect('main')
    return render(request, 'home')

def guest_login(request):
    if request.method == 'POST':
        return redirect('main')  # 로그인 성공하면 메인 페이지로
    return render(request,'home')
# GPT 연동

# def get_gpt_response(request):
#     load_dotenv()
#
#     GPT_API_KEY = os.getenv("GPT_API_KEY")
#     GPT_API_URL = os.getenv("GPT_API_URL")
#
#     gpt_response = None
#     ingredientInput = ""
#
#     if request.method == "POST":
#         ingredientInput = request.POST.get("ingredientInput", "").strip()
#
#         prompt = f"""
#         사용자가 입력한 재료를 바탕으로 가장 적절한 요리 종류(한식, 중식, 일식, 양식 등)를 결정하고, 그에 맞는 요리를 추천해줘.
#         그리고 추천된 요리의 레시피를 단계별로 설명해줘.
#
#         입력된 재료: {ingredientInput}
#
#         출력 형식(JSON):
#         {{
#             "요리종류": [한식, 중식, 일식, 양식 중 하나],
#             "추천요리이름": [요리 이름],
#             "레시피": [
#                  [단계 1]
#                  [단계 2]
#                  [단계 3]
#             ]
#         }}
#         """
#
#         if ingredientInput:
#             headers = {
#                 "Authorization": f"Bearer {GPT_API_KEY}",
#                 "Content-Type": "application/json",
#             }
#             data = {
#                 "model": "gpt-3.5-turbo",
#                 "messages": [{"role": "user", "content": prompt}],
#                 "max_tokens": 1000,
#             }
#
#             response = requests.post(GPT_API_URL, headers=headers, json=data)
#             response.raise_for_status()
#
#             # ✅ 응답을 JSON 형태로 변환
#             gpt_response_text = response.json()["choices"][0]["message"]["content"].strip()
#             try:
#                 gpt_response = json.loads(gpt_response_text)  # JSON 변환
#             except json.JSONDecodeError:
#                 gpt_response = {"error": "올바른 형식의 데이터를 반환받지 못했습니다."}
#
#     return render(request, "blog/result.html", {
#         "ingredientInput": ingredientInput,
#         "gpt_response": gpt_response
#     })


def get_gpt_response(request):

    load_dotenv()

    GPT_API_KEY = os.getenv("GPT_API_KEY")
    GPT_API_URL = os.getenv("GPT_API_URL")

    if request.method == 'POST':
        ingredientInput = request.POST['ingredientInput']

    gpt_response = None  # 기본값 설정

    prompt = f"""
    사용자가 입력한 재료를 바탕으로 가장 적절한 요리 종류(한식, 중식, 일식, 양식 등)를 결정하고, 그에 맞는 요리를 추천해줘.
    그리고 추천된 요리의 레시피를 단계별로 출력해줘. 단계 수는 재료와 요리에 따라 달라질 수 있어.

    입력된 재료: {ingredientInput}

    출력 형식:
    {{
        "dish_type": "[한식, 중식, 일식, 양식 중 하나]",
        "dish_name": "[요리 이름]",
        "recipe_steps": [
            "1. 첫번째 단계",
            "2. 두번째 단계",
            "3. 세번째 단계",
            ...
        ]
    }}
    """
    if request.method == "POST":
        headers = {
            "Authorization": f"Bearer {GPT_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300,
        }

        response = requests.post(GPT_API_URL, headers=headers, json=data)
        response.raise_for_status()  # 오류 발생 시 예외 발생

        gpt_response = response.json()["choices"][0]["message"]["content"].strip()

        # 응답을 JSON 형식으로 파싱
        try:
            parsed_response = json.loads(gpt_response)
            dish_type = parsed_response.get("dish_type", "")
            dish_name = parsed_response.get("dish_name", "")
            recipe_steps = parsed_response.get("recipe_steps", [])

            # 숫자 글머리 제거
            recipe_steps = [re.sub(r'^\d+\.\s*', '', step) for step in recipe_steps]
        except json.JSONDecodeError:
            dish_type = dish_name = recipe_steps = []

    return render(request, "blog/result.html", {
        "ingredientInput": ingredientInput,
        "dish_type": dish_type,
        "dish_name": dish_name,
        "recipe_steps": recipe_steps
    })



def ko_food(request):
    with connection.cursor() as cursor:
        sql = q.select_ko_from_recipes()
        cursor.execute(sql)
        results = cursor.fetchall()

    # 데이터 가공 (튜플 데이터를 리스트의 딕셔너리로 변환)
    recipes = [
        {"rec_id": row[0], "rec_name": row[1], "rec_descrip": row[2], "rec_detail": row[3], "rec_img": f"{row[4]}" if row[4] else None}
        for row in results
    ]

    return render(request, "blog/koreanfood.html", {"recipes": recipes})
