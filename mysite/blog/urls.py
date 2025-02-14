from django.urls import path
from blog.views import home_view, main_view, signup_view, koreanfood, korean_food_list, signup, login,de_food,ko_food,ja_food,ch_food,we_food
from blog.views import recommend, result, get_gpt_response, mypage, guest_login
from blog.views import get_gpt_response
urlpatterns = [
    path('',home_view ,name='home'),
    path('main/',main_view, name='main'),
    path('signup_re/',signup, name='signup_re'),
    path('signup/',signup_view, name='signup'),
    path('login/',login, name='login'),
    path('guest_login/',guest_login, name='guest_login'),
    path('result/',result, name='result'),
    path('mypage/',mypage,name="mypage"),

    path('get_gpt_response/', get_gpt_response, name='get_gpt_response'),

    path('koreanfood/',koreanfood, name='koreanfood'),
    path('korean-food/', korean_food_list, name='korean_food_list'),

    path('recommend',recommend ,name='recommend'),

    path('ko_food',ko_food ,name='ko_food'),
    path('ja_food',ja_food ,name='ja_food'),
    path('ch_food',ch_food ,name='ch_food'),
    path('we_food',we_food ,name='we_food'),
    path('de_food',de_food ,name='de_food'),

    path('chat/', get_gpt_response, name='chat_gpt'),
]
