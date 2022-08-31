from . import views
from django.urls import path
#from django.contrib import admin


urlpatterns = [
        path('', views.PostList.as_view(), name='home'),
        path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]


