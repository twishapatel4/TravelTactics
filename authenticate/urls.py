from .views import IntroView
from django.urls import path
from .views import  CusLoginView , RegPage
from django.contrib.auth.views import  LogoutView

urlpatterns=[
    path('', IntroView.as_view(), name='intro'),
    path('login/',CusLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegPage.as_view(),name='register'),
    ]