from django.urls import path
from . import views


# define the url endpoints when, this will activate a function in views.py when the url is visited
urlpatterns = [
    path('', views.loginPage, name='login'), # when user first visits the website, they will be redirected to the login page
    path('register/', views.register, name='register'), # when user visits the register page, they will be redirected to the register page
    path('login/', views.loginPage, name='login'), # when user visits the login page, they will be redirected to the login page
    path('logout/', views.logoutUser, name='logout'), # when user visits the logout page, they will be redirected to the login page which is handled by the logoutUser function in views.py
    path('subjects/', views.subjects, name='subjects'), # when user visits the home page, they will be redirected to the home page
    path('recommend_university/', views.recommend_university, 
         name='recommend_university'),
    path('final/', views.final, name='final'),
    
]
