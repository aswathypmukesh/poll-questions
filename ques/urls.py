from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home" ),
    path('votenow/<int:pk>/', views.votenow,name="votenow" ),
    path('results/<int:pk>/', views.results,name="results" ),

]