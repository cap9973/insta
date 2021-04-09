from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email=self.normalize_email(email)
        username=self.model.normalize_username(username)
        user=self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username='d', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)


    def create_superuser(self, email, username='d', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, username, password, **extra_fields)



class User(AbstractUser):
    username = models.CharField(_('사용자이름'), max_length=20)
    email = models.EmailField(
        _('이메일'),
        max_length=60,
        unique=True,
        help_text=_(
            '사용자 이메일입니다.'
        ),
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'  # email 로 로그인
    REQUIRED_FIELDS = []  # 필수로 받고 싶은 필드를 넣기 위해 소스 코드엔 email필드가 들어가지만


    def __str__(self):
        return "<%d %s>" % (self.pk, self.email)


    class Meta:
        db_table = 'users_to_do'
        verbose_name = _('사용자')
        verbose_name_plural = _('사용자들')

