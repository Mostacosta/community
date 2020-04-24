from .models import groups,posts,comments
from rest_framework import serializers
from users.serializer import user_serializer

class groups_serializer (serializers.ModelSerializer):
    class Meta :
        model = groups
        fields = '__all__'
        extra_kwargs = {'longtude': {'write_only': True}, 'latitude': {'write_only': True},"name":{"read_only":True}}

class posts_serializer (serializers.ModelSerializer):
    group = groups_serializer(read_only=True)
    user = user_serializer(read_only=True)
    class Meta :
        model = posts
        fields = ['post','group','user']

class comments_serializer (serializers.ModelSerializer):
    post = posts_serializer(read_only=True)
    user = user_serializer(read_only=True)
    class Meta :
        model = comments
        fields = ['comment','post','user']
