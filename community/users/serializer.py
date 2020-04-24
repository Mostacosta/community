from django.contrib.auth.models import User
from rest_framework import serializers
from .models import contacts,user_profile

class user_serializer (serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['username','password','email']
        extra_kwargs = {'password': {'write_only': True}}

class contacts_serializer (serializers.ModelSerializer):
    user = user_serializer()
    class Meta :
        model = contacts
        fields = ['user','date']

class profile_serializer (serializers.ModelSerializer):
    user = user_serializer()
    contact = contacts_serializer(many=True)
    class Meta :
        model = user_profile
        fields = ['user','contact']

