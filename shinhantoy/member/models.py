from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    tel = models.CharField(max_length=32, null=True, blank=True, verbose_name='전화번호')
    status = models.CharField(max_length=16, default='일반',
        choices=(
            ('일반','일반'),
            ('탈퇴','탈퇴'),
            ('휴면','휴면'),
        )
    )

    class Meta:
        db_table = 'shinhan_member'
        verbose_name = '회원'
        verbose_name_plural = '회원'