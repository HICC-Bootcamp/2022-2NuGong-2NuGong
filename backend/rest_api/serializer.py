from rest_framework import serializers, validators
from .models import Bookmark, Notice, User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('nickname', 'password')

        extra_kwargs = {
            "nickname": {
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(),
                        "이미 존재하는 유저명입니다."
                    )
                ]
            },
            "password": {"write_only":True} #write_only를 통해 GET요청 시 접근을 차단
        }

    def create(self, validated_data):
        print(validated_data)
        print(2222)
        nickname = validated_data['nickname']
        password = validated_data['password']

        user = User.objects.create_user(
            nickname=nickname,
            password=password,
        )
        return user


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__' #모든 필드로 지정함

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
    
    def create(self, validated_data):
        user_id=validated_data['user_id']
        notice_id=validated_data['notice_id']
        bookmark = Bookmark.objects.create(user_id=user_id, notice_id=notice_id)
        return bookmark