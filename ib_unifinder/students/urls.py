from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('recommend_university/', views.recommend_university,
         name='recommend_university'),
    path('selection/', views.selection, name='selection'),
    path('api/', views.get_data, name='api'),
    path('subjects/', views.subjects, name='subjects'),
    path('final/', views.final, name='final')
]
