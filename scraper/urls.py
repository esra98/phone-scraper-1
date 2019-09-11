from django.urls import path
from . import views


urlpatterns = [
   path('', views.home_page, name="home-page"),
   path('search/', views.search, name="result-page"),
   path('sent/', views.mail_the_products, name="post-mail"),


]