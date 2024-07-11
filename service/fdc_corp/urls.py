from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.news.as_view()),
    path('menu/', views.mainMenu.as_view()),
    path('fmenu/', views.footerMenu.as_view()),
    path('pages/', views.pages.as_view()),
    path('lang/', views.lang.as_view()),
    path('slider/', views.slider.as_view()),
]