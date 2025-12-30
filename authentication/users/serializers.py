from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__" 

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True, label="Email")
  password = serializers.CharField(label="Password", write_only=True)
  password2 = serializers.CharField(write_only=True, label="Confirm Password")
  class Meta:
    model = User 
    fields = ['email', 'password', 'password2']

  def validate_email(self, value):
    if User.objects.filter(email=value).exists():
      raise serializers.ValidationError("Email already exists!!")
    return value 
    
  def validate(self, attrs):
    if len(attrs['password']) < 8:
      raise serializers.ValidationError("Password must be at least 8 characters long!!")
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError("Passwords do not match!!")
    return attrs 

  def create(self, validated_data):
    password = validated_data.pop('password')
    validated_data.pop('password2')
    user = User.objects.create_user(password=password, **validated_data)
    user.save()
    return user 
  
class LoginSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=50)
  password = serializers.CharField(max_length=12, write_only=True)

  def validate(self, data):
      user = authenticate(**data)
      if user and user.is_active:
        return user
      raise serializers.ValidationError("Invalid credentials!!") 
      