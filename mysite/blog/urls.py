from django.urls import path
from blog.views import home_view, main_view, signup_view, koreanfood, korean_food_list, signup, login

urlpatterns = [
    path('',home_view ,name='home'),
    path('main/',main_view, name='main'),
    path('signup_re/',signup, name='signup_re'),
    path('signup/',signup_view, name='signup'),
    path('login/',login, name='login'),
    path('koreanfood/',koreanfood, name='koreanfood'),
    path('korean-food/', korean_food_list, name='korean_food_list'),
]