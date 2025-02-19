from django.urls import path
from blog.views import home_view, main_view, signup_view, ko_food, signup, login,de_food,ko_food,ja_food,ch_food,we_food
from blog.views import recommend, result, get_gpt_response, result_by_type
from blog.views import get_gpt_response ,recipe_detail , guest_login  #mypage
from . import views
from blog.views import user_list_view, delete_selected_recipes, delete_all_recipes

urlpatterns = [
    path('',home_view ,name='home'),
    path('main/',main_view, name='main'),
    path('signup_re/',signup, name='signup_re'),
    path('signup/',signup_view, name='signup'),
    path('login/',login, name='login'),
    path('guest_login/', guest_login, name='guest_login'),
    path('result/',result, name='result'),
    # path('mypage/',mypage, name='mypage'),
    path('get_gpt_response/', get_gpt_response, name='get_gpt_response'),


    # path('korean-food/', korean_food_list, name='korean_food_list'),

    path('recommend',recommend ,name='recommend'),
    path("ko_food/<str:category>/", ko_food, name="ko_food"),
    # path("ko_food/", ko_food, {'category': 'Korean'}, name="ko_food_default"),  # 기본 경로 추가
    # path('ko_food',ko_food ,name='ko_food'),
    path('ja_food',ja_food ,name='ja_food'),
    path('ch_food',ch_food ,name='ch_food'),
    path('we_food',we_food ,name='we_food'),
    path('de_food',de_food ,name='de_food'),

    path('chat/', get_gpt_response, name='chat_gpt'),

    path('result_by_type/',result_by_type,name="result_by_type"),
    path('recipe_detail/<int:rec_id>/', recipe_detail, name='recipe_detail'),
    path('user_list/', user_list_view, name='user_list'),
    path('delete_selected/', delete_selected_recipes, name='delete_selected_recipes'),
    path('delete_all/', delete_all_recipes, name='delete_all_recipes'),
]
