from django.shortcuts import render, redirect
from django.http import HttpResponse

def index_view(request):
    return render(request,'blog/index.html')

def main_view(request):
    return render(request,'blog/main.html')

def signup_view(request):
    return render(request,'blog/signup.html')

def recommend_view(request):
    return render(request,'blog/recommend.html')

def signup(request):
    if request.method == 'POST':
        # 여기에서 POST 요청으로 받은 회원가입 데이터 처리
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # 비밀번호 확인 (간단한 체크)
        if password != confirm_password:
            return HttpResponse("비밀번호가 일치하지 않습니다.", status=400)

        # 회원가입 처리 로직 추가 (예: 사용자 모델 생성 등)
        # 예시: User.objects.create(nickname=nickname, email=email, password=password)
        
        return redirect('login')  # 회원가입 후 로그인 페이지로 리디렉션

    return render(request, 'signup.html')