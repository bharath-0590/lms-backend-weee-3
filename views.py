from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .models import Course 
from .models import Enrollment 
from .models import LearningModule
from .serializers import UserSerializer
from .serializers import ProfileSerializer
from .serializers import CourseSerializer
from .serializers import EnrollmentSerializer
from .serializers import LearningModuleSerializer


# Create your views here.

class UserCreate(generics.CreateAPIView):
    """Create a new user. """
    serializer_class = UserSerializer

class ProfileDetail(generics.RetriveUpdateAPIView):
    """Get and update a user profile. """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentList(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
class LearningModuleList(generics.ListCreateAPIView):
    queryset = LearningModule.objects.all()
    serializer_class = LearningModuleSerializer

class LearningModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningModule.objects.all()
    serializer_class = LearningModuleSerializer
    
    
