from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "Index"),
    path('signup/',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout, name="logout"),
    path('profile/<str:pk>',views.profile, name="profile"),
    path('profile/<str:pk>/addblog',views.addblog, name="addblog"),
]
