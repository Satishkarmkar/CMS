"""project21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app21 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showcommon, name = 'home'),
    path('studentlogin/', views.studentLogin, name = 'studentLogin'),
    path('stu_registration/', views.studentRegistration, name= 'stu_registration'),
    path('registration_student/',views.registrationStudent, name = 'registration_student'),
    path('login_check/', views.logincheck, name = 'login_check'),


    path('stu_home/', views.studentHome, name = 'stu_home'),
    path('stu_profile', views.studentProfile, name= 'stu_profile'),
    path('stu_update/',views.updateStudent,name= 'stu_update'),
    path('stu_updated/',views.updated_student,name='stu_updated'),
    # path('stu_logout/', views.stu_logout,name='home')


]
