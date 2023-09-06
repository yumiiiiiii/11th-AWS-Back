from rest_framework import serializers
from .models import Post
from accounts.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source = 'user.name')

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content']