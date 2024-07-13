from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from .models import Course
from .models import Enrollment
from .models import LearningModule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_pic', 'location', 'birth_date']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class Enrollment(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class LearningModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningModule
        fields = '__all__'


