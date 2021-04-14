from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Xtranews import views
from Xtranews import getnews
from Xtranews import getFullDesciption
from Xtranews import AddData

urlpatterns = [
    
    path('load/', AddData.main , name='loadnews'),

    path('', views.redirectToHome),
    path('home/',views.homepage , name='home'),
    path('home/post/<str:title>',views.homepage , name='getspecificnews'),  
    path('api/getnews/home/', getnews.gethomenews , name='getnews') ,
    path('api/getnews/home/post/'r'<str:titleIn>', getnews.getSpecificHomeNews , name='getspecificHomenews') ,  
    path('api/getnews/home/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificHomenews') ,

    path('sports/', views.sports , name='sports'),
    path('sports/post/<str:title>',views.sports , name='getspecificnews'),  
    path('api/getnews/sports/', getnews.getsportsnews , name='getnews') ,
    path('api/getnews/sports/post/'r'<str:titleIn>', getnews.getSpecificSportsNews , name='getspecificSportsnews') ,  
    path('api/getnews/sports/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificSportsnews') ,

    path('technology/', views.tech , name='technology'),
    path('technology/post/<str:title>',views.tech , name='getspecificnews'),  
    path('api/getnews/technology/', getnews.getTechnews , name='getnews') ,
    path('api/getnews/technology/post/'r'<str:titleIn>', getnews.getSpecificTechNews , name='getspecificTechnews') ,  
    path('api/getnews/technology/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificTechnews') ,

    path('health/', views.health , name='health'),
    path('health/post/<str:title>',views.health , name='getspecificnews'),  
    path('api/getnews/health/', getnews.getHealthnews , name='getnews') ,
    path('api/getnews/health/post/'r'<str:titleIn>', getnews.getSpecificHealthNews , name='getspecificHealthnews') ,  
    path('api/getnews/health/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificHealthnews') ,

    path('science/', views.science , name='science'),
    path('science/post/<str:title>',views.science , name='getspecificnews'),  
    path('api/getnews/science/', getnews.getSciencenews , name='getnews') ,
    path('api/getnews/science/post/'r'<str:titleIn>', getnews.getSpecificScienceNews , name='getspecificSciencenews') ,  
    path('api/getnews/science/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificSciencenews') ,

    path('bussiness', views.bussiness , name='business'),
    path('bussiness/post/<str:title>',views.bussiness , name='getspecificnews'),  
    path('api/getnews/bussiness/', getnews.getBussinessnews , name='getnews') ,
    path('api/getnews/bussiness/post/'r'<str:titleIn>', getnews.getSpecificBussinessNews , name='getspecificBussinessnews') ,  
    path('api/getnews/bussiness/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificBussinessnews') ,

    path('entertainment', views.entertainment , name='entertainment'),
    path('entertainment/post/<str:title>',views.entertainment , name='getspecificnews'),  
    path('api/getnews/entertainment/', getnews.getEntertainmentnews , name='getnews') ,
    path('api/getnews/entertainment/post/'r'<str:titleIn>', getnews.getSpecificEntertainmentNews , name='getspecificentErtainmentnews') ,  
    path('api/getnews/entertainment/post/detail/'r'<str:articleUrl>', getFullDesciption.getDescription , name='getspecificEntertainmentnews') ,


]