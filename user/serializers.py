from dataclasses import field
from rest_framework import serializers
from .models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
  # 외래키 관계로 이어져 있는 필드는 Serializer를 바로 호출 가능
  class Meta:
    model = UserProfile
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  # one-to-one 관계에서는 fk처럼 사용가능
  userprofile = UserProfileSerializer()
  class Meta:
    model = User
    fields = '__all__'