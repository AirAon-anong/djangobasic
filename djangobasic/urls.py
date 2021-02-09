"""djangobasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs import views
#from tweets import views
from tweets.views import home_view, tweet_detail_view1,tweet_detail_view2,tweet_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #tweets app
    path('homepage/',home_view),
    path('tweets/',tweet_list_view),
    path('tweets/patone/<int:tweet_id>',tweet_detail_view1),
    path('tweets/pattwo/<int:tweet_id>',tweet_detail_view2),
    path('tweet_list_view_path',tweet_list_view), #POST ไม่ต้องมี / ตามหลัง URL
    



    #blogs app
    path('',views.hello),
    path('medium/',views.mediumArea),
    path('createdForm/',views.registered),
    path('addform',views.addform), #POST ไม่ต้องมี / ตามหลัง URL
    path('tableData/',views.tableData),
    path('register/',views.register),
    path('addUser',views.addUser), #POST ไม่ต้องมี / ตามหลัง URL
    path('loginForm/',views.loginForm),
    path('login',views.login),
    path('logout',views.logout)
]
