from rest_framework import serializers, validators
from .models import Notice, User

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