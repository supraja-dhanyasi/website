from django.contrib import admin
from django.urls import path
from website_app import views

urlpatterns = [
    path('home/',views.firstpage,name="home"),
    path('home1/',views.home),
    path('contact/',views.contact,name="contact"),
    path('courses/',views.courses,name="course"),
    path('search/',views.search,name="search"),

    path('read/',views.read,name="read"),
    path('view/',views.view,name="view"),
    path('readmore/',views.readmore,name="readmore"),
    path('register/',views.register,name='register'),


]
