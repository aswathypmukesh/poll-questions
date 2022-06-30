from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name="login" ),
    path('home/', views.home,name="home" ),
    path('like/<int:pk>/', views.like,name="like" ),
    path('dislike/<int:pk>/', views.dislike,name="dislike" ),
    path('votenow/<int:pk>/', views.votenow,name="votenow" ),
    path('results/<int:pk>/', views.results,name="results" ),
    path('logout/', views.logout,name="logout" )
]