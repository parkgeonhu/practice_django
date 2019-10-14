import uuid
import datetime
from pytz import timezone

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
)
from django.db import models


def now_korea() -> datetime.datetime:
    return datetime.datetime.now(timezone('Asia/Seoul'))


def clean_phone(phone: str) -> str:
    return phone.replace('-', '')



class ModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)

    class Meta:
        abstract = True



class UserManager(BaseUserManager):
    def _create_user(self, phone, nickname, password=None,
                     is_staff=False, is_superuser=False, **extra_fields):
        now = now_korea()
        if not phone:
            raise ValueError('The given phone must be set')
        is_active = extra_fields.pop("is_active", True)
        phone = clean_phone(phone)
        user = self.model(phone=phone, nickname=nickname, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          created_at=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, nickname, password=None, **extra_fields):
        return self._create_user(phone, nickname, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        return self._create_user(phone, f'admin-{phone}', password, True, True, **extra_fields)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=255, unique=True, db_index=True, help_text='전화번호 (id로 쓰임)')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, help_text='회원 탈퇴 플래그')

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone

    def first_name(self):
        return self.phone

    def last_name(self):
        return self.phone
