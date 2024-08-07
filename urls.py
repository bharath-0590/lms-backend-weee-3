"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from .views import UserCreate 
from .views import ProfileDetail
from .views import CourseList, CourseDetail
from .views import EnrollmentList, EnrollmentDetail
from .views import LearningModuleList, LearningModuleDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('register/', UserCreate.as_view(), name='user-create'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('enrollments/', EnrollmentList.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', EnrollmentDetail.as_view(), name='enrollment-detail'),
    path('modules/', LearningModuleList.as_view(), name='module-list'),
    path('modules/<int:pk>/', LearningModuleDetail.as_view(), name='module-detail'),
    
    
]
