from django.urls import path
from  index import views

urlpatterns = [
    path('index', views.index),
    path('nav', views.nav),
    path('contactus', views.contactus),
    path('about', views.about),
    path('newsinformation', views.newsInformation),
    path('goodstype', views.goodstype),
    path('goods', views.goods)
]
