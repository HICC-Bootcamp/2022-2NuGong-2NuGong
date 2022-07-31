from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, nickname, password=None, favorites=None, subscribe = None):
        if not nickname:
            raise ValueError("nickname required")
        #아래줄의 리스트에서 0번째 인덱스는 tag번호와 인덱스를 일치시키기 위헤 존재함. 즉, 사용하지 않음.
        user = self.model(
            nickname = nickname, 
            favorites = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            subscribe = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 유저 생성
    def create_superuser(self, nickname, password=None):
        user = self.create_user(
            nickname = nickname,
            password = password
        )

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField()
    views = models.PositiveIntegerField()
    tag = models.IntegerField()
    department = models.IntegerField()
    contents = models.TextField()
    url = models.URLField(max_length=500, null=True)

    def __str___(self):
        return self.title


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=20, unique=True)
    department = models.IntegerField(null=True)
    favorites = ArrayField(models.IntegerField(), null=True) #태그 별 조회수 저장, 추후 컬럼명 favorites -> tagviews으로 변경 필요
    subscribe = ArrayField(models.IntegerField(), null=True) #관심 태그 저장
    bookmarks = models.ManyToManyField(Notice, related_name="users")
    # User 모델의 필수 field
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # username field는 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수 작성 field
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nickname