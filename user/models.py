from tkinter import CASCADE
from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
  def create_user(self, username, password=None):
    if not username:
        raise ValueError('유저는 username이 필수입니다.')
    user = self.model(
        username=username,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, password):
    user = self.create_user(
      username=username,
      password=password
    )
    user.is_admin = True
    user.save(using=self.db)
    return user


class User(AbstractBaseUser):
  username = models.CharField('사용자 계정', max_length=20, unique=True)
  email = models.EmailField('이메일 주소', max_length=100)
  password = models.CharField('비밀번호', max_length=200)
  fullname = models.CharField('이름', max_length=20)
  join_date = models.DateTimeField('가입일', auto_now_add=True)

  # is_active = False: 계정 비활성화
  is_active = models.BooleanField(default=True)
  
  # is_staff에서 사용
  is_admin = models.BooleanField(default=False)

  # id로 사용할 필드 지정
  # 로그인 시 USERNAME_FIELD에 설정된 필드와 password 사용됨.
  USERNAME_FIELD = 'username'

  # user를 생성할 때 입력받은 필드 지정
  REQUIRED_FIELDS = []

  objects = UserManager() # custom user 생성하려면 필수

  def __str__(self):
      return self.username

  # 로그인 사용자의 특정 테이블 crud 권한 설정 / admin=True, (is_active=False)=False
  def has_perm(self, perm, obj=None):
        return True

  # 로그인 사용자의 특정 app 접근 가능여부 설정. app_laber = app 이름
  # admin=True, (is_active=False)=False
  def has_module_perms(self, app_label):
      return True

  # admin 권한 설정
  @property
  def is_staff(self):
      return self.is_admin
      
          
class UserProfile(models.Model):
  user = models.OneToOneField(to='User', verbose_name='사용자', on_delete=models.CASCADE)
  introduction = models.TextField('소개')
  birthday = models.DateField('생일')
  age = models.IntegerField('나이')
  
  def __str__(self):
    return self.user