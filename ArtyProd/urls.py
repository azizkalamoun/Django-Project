from django.urls import include, path
from django.contrib import admin, auth
from .views import *
from ArtyProd import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('home/', home, name='home'),
    path('projets/<int:id>/', views.project_details, name='project_details'),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name= "logout"),
    path("login/", views.login_request, name="login"),
    path('submit-message/', submit_message, name='submit_message'),
    path('download-cv/<int:personnel_id>/', views.download_cv, name='download-cv'),
    path('my-projects/', views.my_projects, name='my_projects'),

]
