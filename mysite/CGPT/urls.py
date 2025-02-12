from django.contrib import admin
from django.urls import path
from CGPT.views import chat_gpt

urlpatterns = [
	path('chat/', chat_gpt, name='chat_gpt'),

]