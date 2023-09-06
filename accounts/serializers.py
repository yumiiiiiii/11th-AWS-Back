from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserSignupSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=['id', 'username','password','name', 'part', 'created_at', 'updated_at']

    part_list = (
        ('프론트엔드', '프론트엔드'),
        ('백엔드', '백엔드')
    )


    username = serializers.CharField(max_length=32) # 아이디
    password = serializers.CharField(max_length=32)
    name = serializers.CharField(max_length=8) # 이름
    part = serializers.ChoiceField(
        choices=part_list
    )

    def create(self, validated_data):

        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError('username 존재')


        else:
            user = User.objects.create(
                username=validated_data['username'],
                name=validated_data['name'],
                part=validated_data['part'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class UserLoginSerializer(serializers.Serializer):

    class Meta:
        model=User
        fields=['id', 'username','password','name', 'part', 'created_at', 'updated_at']

    part_list = (
        ('기획디자인','기획디자인'),
        ('프론트엔드', '프론트엔드'),
        ('백엔드', '백엔드')
    )

    username = serializers.CharField(max_length=32)  # 아이디
    password = serializers.CharField(max_length=32, write_only=True)
    name = serializers.CharField(max_length=8)  # 이름
    part = serializers.ChoiceField(
        choices=part_list
    )


    def validate(self, data):
        username=data.get("username", None)
        password=data.get("password", None)

        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)

            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호')
        else:
            raise serializers.ValidationError("존재하지 않는 유저")


        data = {
            'id': user.id,
            'username':user.username,
            'name' : user.name,
            'part' : user.part,
        }
        return data