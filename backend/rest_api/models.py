from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, nickname, password=None):
        if not nickname:
            raise ValueError("nickname required")
        
        user = self.model(nickname = nickname)

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


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=10, unique=True)
    department = models.IntegerField(null=True)
    favorites = ArrayField(models.IntegerField(), null=True)

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


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    create_at = models.DateTimeField()
    views = models.PositiveIntegerField()
    tag = models.IntegerField()
    department = models.IntegerField()
    contents = models.TextField()

    def __str___(self):
        return self.title


class Bookmark(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, db_column="user_id")
    notice_id = models.ForeignKey("Notice", on_delete=models.CASCADE, db_column="notice_id")

    def __str__(self):
        return self.id