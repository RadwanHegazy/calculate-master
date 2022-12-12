from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView as l_out

urlpatterns = [
    path('',views.index,name='index'),
    
    # Authenticate
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',l_out.as_view(),name='logout'),
    
    # user profile
    path('profile/',views.profile,name='profile'),

    # Exam 
    path('exam/<str:examType>/',views.exam,name='exam'),
    path('congrats/',views.congrats,name='congrats'),

    # Leaderboard api
    path('leaders/',views.leaderboard,name='leader'),
]