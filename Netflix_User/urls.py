from Netflix_User import views
from django.urls import path, include

urlpatterns = [
    path('', views.NetflixView, name='in'),
    path('index/', views.IndexView, name='index'),
    path('signin/', views.SigninViews, name='signin'),
    path('signup/', views.SignupViews, name='signup'),
    path('NetflixViews/', views.NetflixViews, name='NetflixViews'),
]
