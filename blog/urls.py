#
#urls.py
#ウェブページの遷移を管理する
#
#Djangoのコンポーネントを改変
#Updated by Tetsuyoshi Mogami on 2022/02/20
#

from django.urls import path
from . import views


#画面遷移するためにURLを設定する
urlpatterns = [
    path('',views.login,name='login'),
    path('login', views.choice, name='choice'),
    path('login/choice', views.output, name='output'),
    ]
